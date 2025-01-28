def main():
    # Reading content of text file in subdirectory
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # Generate word count
    word_count = words(file_contents)

    # Generate character counts
    char_count = count_characters(file_contents)

    # Print the report
    print_report("books/frankenstein.txt", word_count, char_count)

# Returns word count of text file
def words(file_contents):
    # Split the contents into words and return the length
    return len(file_contents.split())

# Returns a dictionary with the count of each character
def count_characters(file_contents):
    char_count = {}  # Initialize an empty dictionary

    for char in file_contents.lower():  # Convert text to lowercase and iterate through characters
        if char.isalnum():  # Consider only alphanumeric characters
            char_count[char] = char_count.get(char, 0) + 1  # Increment the count for the character

    return char_count

# Generates and prints the report
def print_report(file_path, word_count, char_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Sort characters by frequency in descending order
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    # Print character frequencies
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
