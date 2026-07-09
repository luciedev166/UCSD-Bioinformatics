def main():
    Motifs = [
        'AACGTA',
        'CCCGTT',
        'CACCTT',
        'GGATTA',
        'TTCCGG',
    ]
    print(ProfileWithPseudocounts(Motifs))

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    base = {
        'A': [],
        'C': [],
        'G': [],
        'T': [],
    }

    for row in zip(*Motifs):
        for _ in base:
            base[_].append(row.count(_) + 1) 

    return base
def ProfileWithPseudocounts(Motifs):
    counts = CountWithPseudocounts(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {
        'A': [],
        'C': [],
        'G': [],
        'T': [],
    }

    for key in counts:
        for _ in range(k):
            profile[key].append(counts[key][_] / (t + 4))
    return profile
main()