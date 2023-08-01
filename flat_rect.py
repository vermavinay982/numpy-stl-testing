import numpy as np
from stl import mesh
import trimesh
from icecream import ic 

# Define the 8 vertices of the cube
vertices = np.array([\
    [-1, -1, -1], # 
    [+1, -1, -1], # x
    [+1, +1, -1], # x,y
    [-1, +1, -1], # y
    [+1, -1, -1], # z
    [+2, -1, -1], # x,z
    [+2, +1, -1], # x,y,z
    [+1, +1, -1]  # y,z

    ])
# Define the 12 triangles composing the cube
faces = np.array([\
    [0,3,1],
    [1,3,2],
    # [0,4,7],
    # [0,7,3],

    # [4,5,6],
    [4,6,7],
    
    # [5,1,2],
    # [5,2,6],

    # [2,3,6],
    # [3,7,6],

    # [0,1,5],
    # [0,5,4]
    ])



cube_mesh = np.ones(faces.shape[0])*0
cube_mesh = np.array(cube_mesh,dtype=mesh.Mesh.dtype)
# Create the mesh
ic(cube_mesh)

cube = mesh.Mesh(cube_mesh)
for i, f in enumerate(faces):
    for j in range(3):
        # vert = vertices[f[j],:]
        vert = vertices[f[j]]
        cube.vectors[i][j] = vert 
        ic(j, vert)

    print()
    # cube.save('cube.stl')
    # stl_file_path = "cube.stl"
    # mesh = trimesh.load(stl_file_path)
    # mesh.show()

# Write the mesh to file "cube.stl"
cube.save('flat_rect.stl')


