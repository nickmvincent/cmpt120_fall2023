scores = [1,2,4]
maxsofar = 0
maxposofar = -1

for i in range(len(scores)):
    if (scores[i] >= maxsofar):
        maxsofar = scores[i]
        maxposofar = i

print(maxsofar)