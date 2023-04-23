def count_words(filename):
    # count the appropriate number of words
    try:
        with open(filename, encoding ="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} not found")
    else:
        words = content.split()
        num_words = len(words)
        print(f"{filename} has about {num_words} number of words")

filenames = ["File\guest.txt", "File\example.txt", "a.txt", "File\exp2.txt"]
for filename in filenames:
    count_words(filename)