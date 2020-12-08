fname = "text.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

print(f"Кількість рядків:  {num_lines}")
print(f"Кількість слів:  {num_words}")
print(f"Кількість символів:  {num_chars}")
