def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

def write_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

file_contents = read_file("input.txt")
write_file("output.txt", file_contents)
