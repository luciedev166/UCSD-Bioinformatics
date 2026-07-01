def main():
    genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

    print(MinimumSkew(genome))
def MinimumSkew(Genome):
    positions = [] 

    skew = SkewArray(Genome)
    min_val = min(skew)

    for i in range(len(skew)):
        if skew[i] == min_val:
            positions.append(i)
    return positions

def SkewArray(Genome):
    skew = [0]

    for n in Genome:
        if n == "G":
            skew.append(skew[-1] + 1)
        elif n == "C":
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])     
    return skew

main()