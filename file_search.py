import os


def find_file_path(file_name):
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            file_extension = os.path.splitext(file_name)[1]
            print(file_extension)
            return os.path.abspath(os.path.join(root, file_name))
    return None


file_name = "NPTEL DSA with PYTHON.pdf"
print(find_file_path(file_name))
