matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
unzipped = zip(*matrix)
print(unzipped)
for row in unzipped:
    print(row)