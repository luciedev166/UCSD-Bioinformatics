def main():
    pattern = "ATTCTGGA"
    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    d = 3
    print(ApproximatePatternMatching(text, pattern, d))
    

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] 
    
    for i in range(len(Text) - len(Pattern) + 1):
        c = HammingDistance(Text[i: i + len(Pattern)], Pattern)
        
        if c <= d:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    count = 0
    
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
    
main()
# # Insert your Hamming distance function on the following line.