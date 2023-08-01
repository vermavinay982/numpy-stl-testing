import numpy as np
from stl import mesh
import trimesh
from icecream import ic 

# Define the 8 vertices of the cube
vertices = np.array([\
    [-1, -1, -1],
    [+1, -1, -1],
    [+1, +1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
    [+1, -1, +1],
    [+1, +1, +1],
    [-1, +1, +1]
    ])
# Define the 12 triangles composing the cube
faces = np.array([\
    [0,3,1],
    [1,3,2],

    [0,4,7],
    [0,7,3],

    [4,5,6],
    [4,6,7],
    
    [5,1,2],
    [5,2,6],

    [2,3,6],
    [3,7,6],

    [0,1,5],
    [0,5,4]
    ])



cube_mesh = np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype)
# Create the mesh
ic(cube_mesh)

cube = mesh.Mesh(cube_mesh)
for i, f in enumerate(faces):
    for j in range(3):
        vert = vertices[f[j],:]
        ic(j, vert)

        cube.vectors[i][j] = vert 
    print()
    # cube.save('cube.stl')
    # stl_file_path = "cube.stl"
    # mesh = trimesh.load(stl_file_path)
    # mesh.show()

# Write the mesh to file "cube.stl"
cube.save('cube.stl')


