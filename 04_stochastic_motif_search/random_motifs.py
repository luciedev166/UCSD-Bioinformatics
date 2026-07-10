import random

def main():
    k = 3
    t = 5

    dna = [
        "TTACCTTAAC",
        "GATGTCTGTC",
        "ACGGCGTTAG",
        "CCCTAACGAG",
        "CGTCAGAGGT",
    ]
    print(RandomMotifs(dna, k, t))

def RandomMotifs(Dna, k, t):
    
    set_motifs = []
    for row in Dna:
        i = random.randint(0, len(row) - k)
        set_motifs.append(row[i:i + k])

    return set_motifs
main()