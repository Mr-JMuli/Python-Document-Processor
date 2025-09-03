def process_file(input_file, output_file):
    try:
        # Read the contents of input.txt
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Count the number of words
        words = text.split()
        word_count = len(words)
        
        # Convert all text to uppercase
        upper_text = text.upper()
        
        # Write the processed text and word count to output.txt
        with open(output_file, 'w') as file:
            file.write(upper_text + '\n')
            file.write(f'\nTotal number of words: {word_count}\n')
        
        # Print success message
        print(f"File '{output_file}' has been created successfully.")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")

# Call the function with input and output file names
process_file('input.txt', 'output.txt')