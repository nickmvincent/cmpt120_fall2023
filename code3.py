scores = [1,2,4]
m = scores[0]
max_index = 0

for i in range(1, len(scores)):
    if (scores[i] >= max_index):
        m = scores[i]
        max_index = i

print(m)