from Bio import SeqIO

for record in SeqIO.parse("fungi.fasta", "fasta"):
    sequence = str(record.seq)

print("DNA Sequence:")
print(sequence)

print("\nSequence Length:", len(sequence))

from Bio import SeqIO

for record in SeqIO.parse("fungi.fasta", "fasta"):
    sequence = str(record.seq)

print("DNA Sequence:")
print(sequence)

print("\nSequence Length:", len(sequence))

print("\nNucleotide Count")
print("A =", sequence.count("A"))
print("T =", sequence.count("T"))
print("G =", sequence.count("G"))
print("C =", sequence.count("C"))

from Bio import SeqIO

for record in SeqIO.parse("fungi.fasta", "fasta"):
    sequence = str(record.seq)

print("DNA Sequence:")
print(sequence)

print("\nSequence Length:", len(sequence))

print("\nNucleotide Count")
print("A =", sequence.count("A"))
print("T =", sequence.count("T"))
print("G =", sequence.count("G"))
print("C =", sequence.count("C"))

g = sequence.count("G")
c = sequence.count("C")

gc_content = ((g + c) / len(sequence)) * 100

print("\nGC Content =", round(gc_content, 2), "%")

motif = input("\nEnter motif to search: ")

positions = []

for i in range(len(sequence)):
    if sequence[i:i+len(motif)] == motif:
        positions.append(i + 1)

print("Motif found at positions:")
print(positions)

import matplotlib.pyplot as plt

labels = ['A', 'T', 'G', 'C']

values = [
    sequence.count('A'),
    sequence.count('T'),
    sequence.count('G'),
    sequence.count('C')
]

plt.bar(labels, values)

plt.xlabel("Nucleotides")
plt.ylabel("Count")
plt.title("Fungal DNA Analysis")

plt.show()

import matplotlib.pyplot as plt

labels = ['A', 'T', 'G', 'C']

values = [
    sequence.count('A'),
    sequence.count('T'),
    sequence.count('G'),
    sequence.count('C')
]

plt.bar(labels, values)

plt.xlabel("Nucleotides")
plt.ylabel("Count")
plt.title("Fungal DNA Analysis")

plt.savefig("fungal_dna_graph.png", dpi=300, bbox_inches="tight")

plt.show()