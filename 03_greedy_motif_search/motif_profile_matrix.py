def main():
    motifs = [
        "CAG"
    ]
    print(Profile(motifs))

def Count(motifs):
    count = {'A': [], 'C': [],'G': [],'T': []}

    for row in zip(*motifs):
        count['A'].append(row.count('A'))
        count['C'].append(row.count('C'))
        count['G'].append(row.count('G'))
        count['T'].append(row.count('T'))

    return count
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    profile = {'A': [], 'C': [], 'G':[], 'T': []}
    base_count_per_col = Count(Motifs)

    for base in base_count_per_col:
        for i in range(k):
            profile[base].append(base_count_per_col[base][i] / t)

    return profile
main()
