import csv

refArquivo = open("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TcCLB50671780.fasta")
refArquivoMulti = open("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")

## QUESTÃO 1 ##

primeira_linha = refArquivo.readline()[1:-1]
cabecalho = ""

for caracter in primeira_linha:
    if caracter != "|":
        cabecalho += caracter
    if caracter == "|":
        break

sequencia = ""
for linha in refArquivo:
    sequencia += linha.replace('\n','')
print ("Cabecalho: %s"%cabecalho)
print ("Sequencia: %s"%sequencia)
refArquivo.close()


## QUESTÃO 2 ##

'''TODO laço for que crie uma chave para cada vez que encontrar '>' e tenha como value tudo que venha depois de '>'. '''

dicionario = {}

for linha in refArquivoMulti.readline():
    for caracter in linha:
        if caracter == ">":
            cabecalho += linha
        

cabecalho = refArquivoMulti.readline()[1:-1]
sequencia = ""
for linha in refArquivoMulti:
    sequencia += linha.replace('\n','')
print ("Cabecalho: %s"%cabecalho)
print ("Sequencia: %s"%sequencia)
refArquivoMulti.close()



## QUESTÃO 3 ##



## QUESTÃO 4 ##


# A) A finalidade da função upper - retorna todas letras em maiúsculo -, além das questões de boas práticas, é  ???????
# B) A função de 'rstrip' é um método built-in é retornar uma cópia da string original, cujo caractéres repetidos - espaço em branco, como default- 
# sejam removidos. Por exemplo, o próprio espaço em branco - como no caso do código 5 - ou qualquer outros caractéres escolhidos.
# C)
# D)


