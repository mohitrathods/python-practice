# # #MATRIX MULTI.
# #first row * first col
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix2 = [
#     [10, 11],
#     [12, 13],
#     [14, 15]
# ]
# #
# r1 = len(matrix1)
# c1 = len(matrix1[0])
# r2 = len(matrix2)
# c2 = len(matrix2[0])
# #
# result = [[0] * c2 for _ in range(r1)]
# #
# for i in range(r1):#3
#     for j in range(c2):#2
#         for k in range(c1):#2
#             result[i][j] += matrix1[i][k] * matrix2[k][j] #
# print(result)

# Define the matrices
matrix1 = [[1, 2],
           [3, 4]]

matrix2 = [[5, 6],
           [7, 8]]

# Create an empty result matrix
result = [[0, 0],
          [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print(result)