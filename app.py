from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from PIL import Image
import io
import base64
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    image_data = data['image']
    
    header, encoded = image_data.split(",", 1)
    binary_data = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(binary_data))
    
    image.save('uploaded_image.png')

    subprocess.call(['python', 'map_coloring.py', 'uploaded_image.png'])
    
    processed_image_path = 'processed_image.png'

    return send_file(processed_image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)