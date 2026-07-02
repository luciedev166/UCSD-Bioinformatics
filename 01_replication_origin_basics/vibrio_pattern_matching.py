def main():
    Pattern = "CTTGATCAT"

    with open("Vibrio_cholerae.txt", "r") as file:
        Genome = file.read().strip()
        
    print(PatternMatching(Pattern, Genome))
    
def PatternMatching(Pattern, Genome):
    positions = []
    
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i: i + len(Pattern)] ==  Pattern:
            positions.append(i)
            
    return positions

main()