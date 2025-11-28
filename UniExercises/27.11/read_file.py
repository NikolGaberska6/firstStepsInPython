def read_the_file(file_name):
    try:
        with open(file_name) as f:
            print(f.read())
    except FileNotFoundError:
        print("File Not Found")

read_the_file("file2")