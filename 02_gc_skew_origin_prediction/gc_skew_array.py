# Input:  A String Genome
# Output: The skew array of Genome as a list.
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




