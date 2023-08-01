import trimesh

if __name__ == "__main__":
    # Load the STL file
    stl_file_path = "cube_stl.stl"  # Replace with the actual path to your STL file
    mesh = trimesh.load(stl_file_path)

    # View the STL file
    mesh.show()