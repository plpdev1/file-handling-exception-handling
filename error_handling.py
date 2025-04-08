def get_filename_and_read():
    filename = input("Please enter the filename: ")
    # Open file and read content
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

# Call the function
get_filename_and_read()
