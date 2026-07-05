file = open("02_FASTA_Analyzer/sample.fasta", "r")
lines = file.readlines()
print(lines)
header = lines[0]    # header line
sequence = lines[1] # first sequence line

header = header.strip()
sequence = sequence.strip()

print("Header:", header)
print("Sequence:", sequence)

# Extract sequence name
name = header[1:]
print("Sequence Name:", name)

# Calculate sequence length
length = len(sequence)
print("Length:", length)

# Calculate GC content
gc_count = sequence.count("G") + sequence.count("C")
gc_percentage = (gc_count / length) * 100

print("GC Content:", gc_percentage, "%")

# Convert to RNA
rna = sequence.replace("T", "U")
print("RNA:", rna)

file.close()