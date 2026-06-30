def main():
    Genome = "AAAAGGGG"
    symbol = "A"
    print(FasterSymbolArray(Genome, symbol))
    
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    k = n // 2
    ex_genome = Genome + Genome[:k]
    count = PatternCount(Genome, symbol)
    
    array[0] = count
    
    for i in range(1, n):
        old_char = ex_genome[i - 1]
        new_char = ex_genome[i + k - 1]
        
        if old_char == symbol:
            count -= 1
        if new_char == symbol:
            count += 1
        
        array[i] = count
        
    return array

def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Pattern) // 2):
        if Pattern[i] == Text:
            count += 1
    return count
    
main()