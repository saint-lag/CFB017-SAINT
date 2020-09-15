import csv


## QUESTÃO 1 ##

def questao1():
'''FUNCIONANDO'''

    refArquivo = open("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TcCLB50671780.fasta")
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


def questao2():
'''MEMORY ERROR'''

    refArquivoMulti = open("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")

    '''Para cada linha no arquivo que tenha '>', uma copia é gerada como elemento de uma lista '''

    cabecalho = ""
    sequencia = ""
    label_list = []
    seq_list = []
    label_seq = {}

    for line in refArquivoMulti:
        line = line.strip()
        for i in line:
            if i == ">":
                cabecalho.join(line)
                label_list.append(cabecalho)
                
            elif:
                sequencia.join(line)
                
            elif i == ">":
                break
        
        seq_list.append(sequencia)
        sequencia = ""
        
    '''TODO Um dicionário que receba as labels como key - label_list - e as values - seq_list.'''    


    
    #print ("Labels: %s"%labels)
    #print()

    refArquivoMulti.close()


## QUESTÃO 3 ##

def questao3():

    refArquivoEntrada = open("C:/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/species.csv")
    refArquivoEntrada.readline()
    for linha in refArquivoEntrada:
        data = linha.split(",")
        if data[3].upper().rstrip() == "BIRD":
            print ("%s\t%s\t%s\t%s" %(data[0], data[1], data[2], data[3].rstrip()))
    refArquivoEntrada.close()

print(questao3)

## QUESTÃO 4 ##


# A) A finalidade da função upper - retorna todas letras em maiúsculo -, além das questões de boas práticas, é  ???????
# B) A função de 'rstrip' é um método built-in é retornar uma cópia da string original, cujo caractéres repetidos - espaço em branco, como default- 
# sejam removidos. Por exemplo, o próprio espaço em branco - como no caso do código 5 - ou qualquer outros caractéres escolhidos.
# C)
# D)


