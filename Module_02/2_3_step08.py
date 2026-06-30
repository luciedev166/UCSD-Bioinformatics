def main():
    Genome = "AAAAGGGG"
    symbol = "A"
    print(SymbolArray(Genome, symbol))
    
def SymbolArray(Genome, symbol):
    idx = {}
    n = len(Genome)
    k = n // 2
    Genome = Genome + Genome[:n // 2]
    
    for i in range(len(Genome) - k):
        idx[i] = PatternCount(Genome[i:i + k], symbol)
    return idx
    
# Reproduce the PatternCount function here.
def PatternCount(Text, Pattern):
    return Text.count(Pattern)
    
            
main()