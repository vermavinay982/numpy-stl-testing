import numpy as np
from stl import mesh
import trimesh
from icecream import ic 

# Define the 8 vertices of the cube
vertices = np.array([\
    [4,4,0],
    [0,0,0],
    [1,0,0],
    [2,0,0],
    [3,0,0],
    [4,0,0],
    [0,1,0], #6
    [1,1,0],
    [2,1,0],
    [3,1,0],
    [4,1,0], #10
    [0,2,0],
    [1,2,0],
    [3,2,0], #13
    [4,2,0],
    ])
# Define the 12 triangles composing the cube
faces = np.array([\
    [1,2,6],
    [2,7,6],

    [2,7,3],
    [3,8,7],

    [3,4,8],
    [4,8,9],

    [5,9,4],
    [6,7,11],
    ])


cube_mesh = np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype)
# Create the mesh
ic(cube_mesh)

cube = mesh.Mesh(cube_mesh)
for i, f in enumerate(faces):
    for j in range(3):
        vert = vertices[f[j]]
        ic(j, vert)
        cube.vectors[i][j] = vert 
    print()
    # cube.save('test.stl')
    # stl_file_path = "test.stl"
    # mesh = trimesh.load(stl_file_path)
    # mesh.show()
ic(cube_mesh)
# Write the mesh to file "cube.stl"
cube.save('square.stl')


