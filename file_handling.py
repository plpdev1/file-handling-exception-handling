def read_and_write_file(input_file, output_file):
    # Open input file for reading
    with open(input_file, 'r') as file:
        content = file.read()  # Read content from the file
        modified_content = content.upper()  # Modify content convert to uppercase
    
    # Open output file for writing
    with open(output_file, 'w') as file:
        file.write(modified_content)  # Write modified content to new file

    print(f"Modified content written to {output_file}")

# Call the function with actual filenames
input_file = "input.txt"
output_file = "output.txt"
read_and_write_file(input_file, output_file)
