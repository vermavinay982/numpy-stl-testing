import numpy as np

def create_sphere(radius, num_latitude=30, num_longitude=30):
    phi = np.linspace(0, np.pi, num_latitude)
    theta = np.linspace(0, 2 * np.pi, num_longitude)

    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return np.array([x, y, z]).T

def save_as_stl(vertices, file_path):
    num_vertices = vertices.shape[0]
    num_faces = (num_vertices - 2) * 2

    faces = np.zeros((num_faces, 3), dtype=np.int32)

    for i in range(num_vertices - 2):
        faces[i * 2] = [0, i + 1, i + 2]
        faces[i * 2 + 1] = [num_vertices - 1, num_vertices - 2 - i, num_vertices - 3 - i]

    # Flatten the 3D array into a 2D array with shape (num_vertices, 3)
    vertices_2d = vertices.reshape(num_vertices, 3)

    with open(file_path, 'wb') as f:
        f.write(np.array(num_faces, dtype=np.uint32).tobytes())
        np.savetxt(f, vertices_2d, fmt='%.6f', header='solid sphere')
        np.savetxt(f, np.column_stack((np.ones(num_faces, dtype=np.uint8) * 3, faces)), fmt='%s', delimiter=' ', comments='')

if __name__ == '__main__':
    radius = 1.0  # Set the radius of the sphere
    num_latitude = 30  # Number of latitude divisions
    num_longitude = 30  # Number of longitude divisions

    sphere_vertices = create_sphere(radius, num_latitude, num_longitude)
    # save_as_stl(sphere_vertices, 'sphere.stl')
    
