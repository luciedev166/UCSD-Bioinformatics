def main():
    motifs = [
        "AACGTA",
        "CCCGTT",
        "CACCTT",
        "GGATTA",
        "TTCCGG"
    ]

    print(count(motifs))

def count(motifs):
    count = {'A': [], 'C': [],'G': [],'T': []}

    for row in zip(*motifs):
        count['A'].append(row.count('A'))
        count['C'].append(row.count('C'))
        count['G'].append(row.count('G'))
        count['T'].append(row.count('T'))

    return count
main()
