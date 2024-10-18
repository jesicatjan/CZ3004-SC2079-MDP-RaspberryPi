def append_to_file(filename, line):
    with open(filename, 'a') as file:  # Open the file in append mode
        file.write(line + "\n")  # Write the line with a newline character

def read_from_file(filename):
    with open(filename, 'r') as file:  # Open the file in read mode
        lines = file.readlines()  # Read all lines into a list
    return [line.strip() for line in lines]  # Strip whitespace characters

def read_last_line_from_file(filename):
    with open(filename, 'r') as file:  # Open the file in read mode
        for line in file:
            pass  # Iterate over all lines (the last line will remain)
    return line.strip()  # Return the last line

def clear_file(filename):
    with open(filename, 'w') as file:  # Open the file in write mode
        pass