import os
import socket

def count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words), words

def top_count_words(words, top_n=3):
    from collections import Counter
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

def handle_contractions(text):
    contractions = {"I'm": "I am","It's":"It is", "couldn't":"could not", "won't":"will not", "I'll":"I will", "You're":"You are", "that's":"that is", "":"", "can't": "cannot", "don't": "do not"}
    for contraction, expanded in contractions.items():
        text = text.replace(contraction, expanded)
    return text.split()

# Paths to text files
file1 = '/home/data/IF.txt'
file2 = '/home/data/AlwaysRememberUsThisWay.txt'

# Count words in each file
total_words_file1, words_file1 = count(file1)
total_words_file2, words_file2 = count(file2)

# The Grand total of words
grand_total_words = total_words_file1 + total_words_file2

# The Top 3 frequent words in IF.txt
top_words_file1 = top_count_words(words_file1)

# Handle contractions and top 3 frequent words in AlwaysRememberUsThisWay.txt
with open(file2, 'r') as file:
    text_file2 = file.read()
    words_no_contractions = handle_contractions(text_file2)
    top_words_file2 = top_count_words(words_no_contractions)

# Getting the container's IP address
container_ip_address = socket.gethostbyname(socket.gethostname())

# Writing results to output file
output_file = '/home/data/output/result.txt'
os.makedirs('/home/data/output', exist_ok=True)
with open(output_file, 'w') as file:
    file.write(f"The total number of words in IF.txt: {total_words_file1}\n")
    file.write(f"The total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n")
    file.write(f"The Grand total words in both the files is: {grand_total_words}\n")
    file.write(f"The top 3 words in IF.txt file are: {top_words_file1}\n")
    file.write(f"The top 3 words in AlwaysRememberUsThisWay.txt (after handling contractions) are: {top_words_file2}\n")
    file.write(f"The IP address of the container is: {container_ip_address}\n")

# Printing result.txt content to console
with open(output_file, 'r') as file:
    print(file.read())
