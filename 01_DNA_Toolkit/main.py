# Program to analyze DNA sequences
dna = input("Enter DNA sequence: ").upper() # used to uppercase the string
print(dna)

# Counting the number of each nucleotides
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

print("Number of A's:",  a_count )
print("Number of T's:", t_count )
print("Number of G's:", g_count )
print("Number of C's:", c_count )