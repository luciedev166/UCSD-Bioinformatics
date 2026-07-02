def main():
    skew = [0]
    genome = "GAGCCACCGCGATA"
    
    for n in genome:
        if n == "G":
            skew.append(skew[-1] + 1)
        elif n == "C":
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    
    for _ in skew:
        print(_,end=" ")
main()