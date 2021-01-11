import turtle

#Exercicio 1 - parâmetro metros -> decimetros, milimetros, centimetros
def converte(a):
    return((a * 10), (a*100), (a*1000))

#Exercicio 2 - ano bissexto
def bissexto(ano):
    if (ano % 400 == 0) or ((ano % 4 == 0) and(ano % 100 != 0)): #ano bissexto: tem que ser divisivel por 4
        #e não por 100, mas se for divisivel por 400 também é bissexto
        return True
    else:
        return False

#Exercicio 3 - polígono em turtle
def poligono(lados, tam):  #n de lados e o tamanho do lado
    for i in range(lados): #percore o n de lados
        turtle.forward(tam) #se move n tamanho para frente, distancia dela
        turtle.left(360/lados) #se move n lados para a esquerda

#Exercicio 4 - polígono em cores
def cores_poli(cores, tam):
    for cor in cores:
        turtle.color(cor)
        turtle.forward(tam)
        turtle.left(360/len(cores))
        
#Exercicio 5 - numeros dentro de uma string
def numero(frase):
    contador = 0 #atribuindo uma variável
    for numero in frase: #percorrendo a string frase
        if numero.isdigit(): #se for True quer dizer que é um digito e soma um no contador
            contador += 1
    return contador

#Exercicio 6 - seq_gene e seq_ref
def contido(seq_ref, seq_gene):
    if seq_gene < seq_ref:
        if set(seq_ref).intersection(seq_ref):
            return 'Contido'
        else:
            return 'Não contido'
            
#Exercicio 7 - y em asteriscos
def impar(x):
    matriz = []
    for linha in range(x):
        matriz.append([])
        for coluna in range(x):
            matriz[i].append('')

    f = x // 2
    for linha in range(f):
        matriz[i][i] = '*'
    for coluna in range(x):
        for j in range(x):
            if i+j == x-1:
                matriz[i][j] = '*'

    for i in range(x):
        final = ' '.join(matriz[i])
        print(final)
        
#Exercício 8 - matriz simétrica
def simetrico(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
        return True

#Exercício 9 - multiplicação de matrizes
def mult_matrizes(m1,m2):
    num_linhas_m1, num_col_m1 = len(m1), len(m1[0])
    num_linhas_m2, num_col_m2 = len(m2), len(m2[0])
    C = []
    
    for linha in range(num_linhas_m1):
        C.append([])
        for coluna in range(num_col_m2):
            C[linha].append(0)
            for k in range(num_col_m1):
                C[linha][coluna] += m1[linha][k] * m2[k][coluna]
    return C
    
def main(): #função que chama todas as funções
    #ex1
    a = converte(input("Digite o parâmetro em metro: "))
    
    #ex2
    ano = bissexto(int(input("Digite o ano: ")))
    
    #ex3
    poligono(int(input("Digite o nº de lados: ")), float(input("Digite o tamanho do lado: ")))
    
    #ex 4
    cores = input("Digite as cores separando por virgula: ")
    cores = cores.split(",")
    tam = int(input("Digite o tamanho do lado: "))
    
    #ex 5
    frase = input("Digite a frase: ")
    
    #ex 6
    seq_gene = input("Digite a sequência gene separado por virgula: ")
    seq_ref = input("Digite a sequência ref separado por vírgula: ")
    seq_gene = seq_gene.split(",")
    seq_ref = seq_ref.split(",")
    
    #ex 7
    impar = int(input("Digite um número impar: "))
    
    #ex 8
    matriz = input("Digite a matriz: ")
    
    #ex 9
    m1 = input("Digite a matriz A: ")
    m2 = input("Digite a matriz B: ")