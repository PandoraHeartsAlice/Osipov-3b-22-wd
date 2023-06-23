import os


def find_files(directory, extension):
    if not os.path.isdir(directory):
        raise Exception("Директория не найдена")

    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))

    return files


directory = "/path/to/directory"
extension = ".txt"
try:
    files = find_files(directory, extension)
    if len(files) > 0:
        print("Found the following files with extension", extension + ":")
        for file in files:
            print(file)
    else:
        print("Files with extension", extension, "not found")
except Exception as e:
    print(e)
