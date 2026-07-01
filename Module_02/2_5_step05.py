def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(len(Text) - len(Pattern) + 1):
        c = HammingDistance(Text[i: i + len(Pattern)], Pattern)
        
        if c <= d:
            count+=1
    return count

def HammingDistance(p, q):
    count = 0
    
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))