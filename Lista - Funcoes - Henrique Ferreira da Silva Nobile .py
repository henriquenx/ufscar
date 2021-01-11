import turtle

#Exercicio 1 
def converte(a):
    return((a * 10), (a*100), (a*1000))

#Exercicio 2 
def bissexto(ano):
    if (ano % 400 == 0) or ((ano % 4 == 0) and(ano % 100 != 0)): 
        return True
    else:
        return False

#Exercicio 3
def poligono(lados, tam):  
    for i in range(lados): 
        turtle.forward(tam) 
        turtle.left(360/lados) 

#Exercicio 4 
def cores_poli(cores, tam):
    for cor in cores:
        turtle.color(cor)
        turtle.forward(tam)
        turtle.left(360/len(cores))
        
#Exercicio 5 
def numero(frase):
    contador = 0 
    for numero in frase: 
        if numero.isdigit():
            contador += 1
    return contador

#Exercicio 6 
def contido(seq_ref, seq_gene):
    if seq_gene < seq_ref:
        if set(seq_ref).intersection(seq_ref):
            return 'Contido'
        else:
            return 'Não contido'
            
#Exercicio 7 
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
        
#Exercício 8 
def simetrico(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
        return True

#Exercício 9 
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

# Exercício 10
def addlin(arquivo, texto, linha):
    arquivo = open(arquivo, 'a')
    arquivo[linha].write('\n',texto)
    arquivo.close()

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
    
    #ex 10
    arquivo = input('Qual o nome do arquivo, com sua respectiva extensão?')
    texto = input('Qual o texto você gostar de adicionar?')
    linha = int(input('A qual linha você gostaria de adicionar o texto acima?'))
    addlin(arquivo, texto, linha)
