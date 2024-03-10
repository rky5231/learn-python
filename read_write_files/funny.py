file = open("funny.txt", "r")
file_wc = open("funny_word_count.txt", "w")
for line in file:
    words = line.split()
    file_wc.write(f"wordcount: {str(len(words))} {line.strip()} ")

file.close()
file_wc.close()
