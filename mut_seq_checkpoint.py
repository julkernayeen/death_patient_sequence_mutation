import os
import csv

# Change working directory to "F:\Genes\mutation_seq"
os.chdir("F:\\Genes\\mutation_seq")

# Print current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Open the "membrane.csv" file in read mode
try:
    membrane = open("membrane.csv", "r")
except FileNotFoundError:
    print("Error: The file 'membrane.csv' could not be found in the current directory.")
    exit()

# Open the "M.txt" file in read mode
try:
    seq = open("M.txt", "r")
except FileNotFoundError:
    print("Error: The file 'M.txt' could not be found in the current directory.")
    exit()

# Read the "membrane.csv" file using the CSV reader
reader = csv.reader(membrane)

# Skip the first line of the file
next(reader)

# Read the contents of the "M.txt" file
seq_reader = seq.read()

# Create an empty list to store mutations
mutation = []

# Extract the mutation information from the CSV file and store it in the "mutation" list
[mutation.append(r[1:2]) for r in reader]
mutation = [m for sublist in mutation for m in sublist]
mutation = [m.strip() for m in mutation]

# Create lists to store the starting and ending characters of each mutation, as well as the position in the sequence
f = []
l = []
positions = []

# Calculate the position of each mutation
for i in mutation:
    s = len(i)-1
    f.append(i[0])
    l.append(i[s:])
    positions.append(int(i[1:s])-1)

# Convert the wild-type sequence into a list of characters
wild = list(seq_reader)

# Calculate the number of mutations
loop = len(f)

# Iterate through each mutation
for j in range(loop):
    # Make a copy of the wild-type sequence
    w = wild[:]
    
    # Check if the starting character of the mutation matches the character at the mutation position in the wild-type sequence
    if w[positions[j]] == f[j]:
        # Replace the character at the mutation position with the ending character of the mutation
        w[positions[j]] = l[j]
        
        # Convert the mutated sequence back into a string
        mutate = "".join(w)
        
        # Create a name for the mutated sequence
        name = mutation[j]
        
        # Create a new file to store the mutated sequence
        try:
            seq = open("%s.txt" %name, "w")
        except:
            print("Error: Could not create a new file for the mutated sequence.")
            exit()
        
        # Write the mutated sequence to the file
        seq.write(mutate)
        
        # Close the file
        seq.close()
