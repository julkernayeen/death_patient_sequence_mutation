import os
import csv

# Change the current working directory to the specified folder
os.chdir("F:\\Genes\\mutation_seq")
print("Current working directory: {0}".format(os.getcwd()))

# Open the "membrane.csv" file for reading
membrane = open("membrane.csv", "r")

# Open the "M.txt" file for reading
seq = open("M.txt", "r")

# Read the contents of the "membrane.csv" file using the csv reader
reader = csv.reader(membrane)

# Skip the first line of the file
next(reader)

# Read the contents of the "M.txt" file
seq_reader = seq.read()

# Create an empty list to store the mutation values
mutation = []

# Create empty lists to store the first character, last character, and position of each mutation
f = []
l = []
positions = []

# Loop through each row in the "membrane.csv" file
[mutation.append(r[1:2]) for r in reader]

# Flatten the list of mutation values
mutation = [m for sublist in mutation for m in sublist]

# Remove any whitespace from the mutation values
mutation = [m.strip() for m in mutation]

# Loop through each mutation value
for i in mutation:
    s = len(i)-1
    # Store the first character of the mutation
    f.append(i[0])
    # Store the last character of the mutation
    l.append(i[s:])
    # Store the position of the mutation (subtracting 1 to convert from 1-indexed to 0-indexed)
    positions.append(int(i[1:s])-1)

# Create a list from the contents of the "M.txt" file
wild = list(seq_reader)

# Store the number of mutations
loop = len(f)

# Loop through each mutation
for j in range(loop):
    # Copy the original sequence
    w = wild[:]
    # If the original sequence has the same character at the position of the mutation
    if w[positions[j]] == f[j]:
        # Replace that character with the mutated character
        w[positions[j]] = l[j]
        # Join the list of characters into a single string
        mutate = "".join(w)
        # Store the name of the mutation
        name = mutation[j]
        # Create a new file for each mutation and write the mutated sequence to it
        seq = open("%s.txt" %name, "w")
        seq.write(mutate)
        seq.close()
