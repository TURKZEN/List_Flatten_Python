liste = [[1, 2], [3, 4], [5, 6, 7]]
tersinin_tersi = []
tersi = liste[::-1]
for i in tersi:
        a = i[::-1]
        tersinin_tersi.append(a)
print(tersinin_tersi)   