def main():
    motifs = [
        "AACGTA",
        "CCCGTT",
        "CACCTT",
        "GGATTA",
        "TTCCGG"
    ]
    print(Consensus(motifs))

def Count(motifs):
    count = {'A': [], 'C': [],'G': [],'T': []}

    for row in zip(*motifs):
        count['A'].append(row.count('A'))
        count['C'].append(row.count('C'))
        count['G'].append(row.count('G'))
        count['T'].append(row.count('T'))

    return count

def Consensus(motifs):
    consensus = ""

    counts = Count(motifs)
    
    for i in range(len(motifs[0])):
        column_counts = {
        'A': counts['A'][i],
        'C': counts['C'][i],
        'G': counts['G'][i],
        'T': counts['T'][i]
        }
        consensus += max(column_counts, key=column_counts.get)
    return consensus
main()
