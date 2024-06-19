mat = [[3,5,9,15],
             [9,2,1,3],
             [15,7,4,11],
             [13,1,7,2]]
print(mat[0])
print(mat[1])
print(mat[2])
print(mat[3])
print(mat[0][3])
print(mat[1][2])
print(mat[2][1])
print(mat[3][0])
print("------------------")
for linha in range(0,4,1):
    print(mat[linha][3-linha])
print("------------------")
