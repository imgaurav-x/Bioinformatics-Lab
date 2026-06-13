# Program to analyze DNA sequences
dna = input("Enter DNA sequence: ").upper() # used to uppercase the string
print(dna)

# Finding  the length of sequence
dna_length = len(dna)
print("Length of DNA sequence:", dna_length)

# Counting the number of each nucleotides
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

print("Number of A's:",  a_count )
print("Number of T's:", t_count )
print("Number of G's:", g_count )
print("Number of C's:", c_count )

# Calculating the GC content
gc_cont = g_count + c_count
gc_content_percentage = (gc_cont / dna_length) * 100
print("GC Content Percentage:", gc_content_percentage, "%") 

# Adding DNA to RNA transcription
rna = dna.replace("T", "U")
print("RNA sequence:", rna)

# Finding the reverse complement of DNA
reverse_complement = dna[::-1].replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()
print("Reverse complement of DNA:", reverse_complement)