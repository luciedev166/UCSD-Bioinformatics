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

def PatternCount(Text, Pattern):
    return Text[:len(Text)//2].count(Pattern)

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1]))