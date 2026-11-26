with open('data/notes.txt', 'w') as file:
    file.write("Line 1: Python is great for working with files.")
with open('data/notes.txt', 'a') as file:
    file.write("\nLine 2: You can read, write, and append text.")
with open('data/notes.txt', 'a') as file:
    file.write("\nLine 3: The 'with' statement keeps things clean.")
with open('data/notes.txt', 'a') as file:
    file.write("\nLine 4: Always close your files when you're done.")   
with open('data/notes.txt', 'r') as file:
    for line in file:
        print(line.strip())
