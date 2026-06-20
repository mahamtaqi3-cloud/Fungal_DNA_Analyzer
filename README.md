# 🧬 Fungal DNA Sequence Analysis using Python

## 📌 Project Overview

This project performs basic DNA sequence analysis on a fungal genome sequence stored in a FASTA file. Using Python and BioPython, the script reads the DNA sequence, calculates nucleotide composition, determines GC content, searches for user-defined DNA motifs, and visualizes nucleotide frequencies with a bar chart.


---

## 🎯 Features

- Read DNA sequences from a FASTA file
- Display the complete DNA sequence
- Calculate sequence length
- Count the number of:
  - Adenine (A)
  - Thymine (T)
  - Guanine (G)
  - Cytosine (C)
- Calculate GC Content (%)
- Search for a user-defined DNA motif
- Display motif positions in the sequence
- Generate and save a nucleotide frequency bar chart

---

## 📂 Project Structure

```
Fungal-DNA-Analysis/
│
├── fungi.fasta              # Input DNA sequence
├── fungal_analysis.py       # Python analysis script
├── fungal_dna_graph.png     # Output nucleotide frequency graph
├── README.md
```

---

## 🛠 Requirements

- Python 3.x
- BioPython
- Matplotlib

Install the required packages using:

```bash
pip install biopython matplotlib
```

---

## 📥 Input

The program reads a DNA sequence from:

```
fungi.fasta
```

Example FASTA format:

```fasta
>Fungal_DNA
ATGCGTAGCTAGCTAGCGTAGCTAGCTAGC...
```

---

## ▶️ How to Run

Run the script using:

```bash
python fungal_analysis.py
```

The program will:

1. Read the DNA sequence
2. Print the sequence
3. Print sequence length
4. Count nucleotides
5. Calculate GC content
6. Ask the user to enter a DNA motif
7. Display motif positions
8. Generate a nucleotide frequency graph
9. Save the graph as:

```
fungal_dna_graph.png
```

---

## 📊 Example Output

```
DNA Sequence:
ATGCGTAGCTAGCTAGC...

Sequence Length:
1054

Nucleotide Count
A = 280
T = 250
G = 260
C = 264

GC Content = 49.72%

Enter motif to search:
ATG

Motif found at positions:
[1, 245, 621]
```

---

## 📈 Output Graph

The program creates a bar chart showing the nucleotide frequencies and saves it as:

```
fungal_dna_graph.png
```

The graph displays the counts of:

- A
- T
- G
- C

---

## 🧬 Bioinformatics Concepts Used

- FASTA file parsing
- DNA sequence analysis
- Nucleotide composition
- GC content calculation
- DNA motif searching
- Data visualization

---

## 📚 Python Libraries Used

- BioPython (`Bio.SeqIO`)
- Matplotlib

---

## 🚀 Future Improvements

Possible future enhancements include:

- Reverse complement generation
- DNA to RNA transcription
- Protein translation
- ORF (Open Reading Frame) prediction
- Sequence alignment
- Multiple FASTA file support
- FASTQ file support
- Interactive graphical interface
- Export analysis results to CSV or Excel

---

## 👩‍💻 Author

**Maham Taqi**

