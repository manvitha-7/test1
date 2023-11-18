def readlines_and_compare(file1_path, file2_path):
    # Open file1 and read lines into a list
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        sentences_file1 = file1.read().splitlines()
        sentences_file2 = file2.read().splitlines()

    # Initialize a list to store line numbers where differences are found
    fault_lines = []

    # Compare lines from both files
    for i, (line1, line2) in enumerate(zip(sentences_file1, sentences_file2), start=1):
        if line1 != line2:
            fault_lines.append(i)
            print(line1, ": is different from :" ,line2)
    # Return the list of line numbers with differences
    return fault_lines

# Example usage
file1_path = r'd:\Downloads\file1.txt'
file2_path = r'd:\Downloads\file2.txt'

result = readlines_and_compare(file1_path, file2_path)
print("Differences found at lines:", result)
