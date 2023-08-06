def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

input_filename = "input.txt"
output_filename = "output.txt"

num_words = count_words(input_filename)

with open(output_filename, 'w') as file:
    file.write(f"Number of words: {num_words}")
