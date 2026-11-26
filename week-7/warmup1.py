with open('warmup1.txt', 'w') as file:
    file.write("Python is great for working with files.")
with open('warmup1.txt', 'a') as file:
    file.write("\nYou can read, write, and append text.")
with open('warmup1.txt', 'a') as file:
    file.write("\nThe 'with' statement keeps things clean.")
with open('warmup1.txt', 'a') as file:
    file.write("\nAlways close your files when you're done.")   
with open('warmup1.txt', 'r') as file:
    for line in file:
        print(line.strip())
