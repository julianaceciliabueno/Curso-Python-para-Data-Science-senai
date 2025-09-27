
# Matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]

diagP = [0,0,0]  
diagS = [0,0,0]  

for i in range(len(matriz)):
    print(" ")  
    for j in range(len(matriz[i])):
        print(f"|{matriz[i][j]}", end="|")
        if i == j:
            diagP[j]==matriz[i][j]
        if i + j == len(matriz) - 1:
            diagS[j]==matriz[i][j]