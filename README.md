# Orginal Code
You can find it [here](https://github.com/Erfaniaa/map-coloring)

# map-coloring

Now you can draw some lines on web. It will fill your picture using four colors.

# Some Basic Stuff to Know

1. [Map coloring](https://en.wikipedia.org/wiki/Map_coloring)
2. [Four color theorem](https://en.wikipedia.org/wiki/Four_color_theorem)

# Algorithm

1. Detecting all non-white regions (eg. provinces or states).
2. Converting the input map to a simple planar graph:
   There will be a node for each region. Two nodes will be adjacent, if and only if their corresponding regions have a common border on the map.
3. Using backtracking for [coloring](https://en.wikipedia.org/wiki/Graph_coloring#Vertex_coloring) that graph (it's a recursive function that produces all valid colorings).
4. Displaying all produced colorings on the given map.

# Dependencies

```
pip install -r requirements.txt
```

# Run

Run app.py and open index.html