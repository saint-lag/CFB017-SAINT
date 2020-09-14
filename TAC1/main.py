import csv

refArquivo = open("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TcCLB50671780.fasta")
refArquivoMulti = open("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")

## QUESTÃO 1 ##

def questao1():

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

    '''Para cada linha no arquivo que tenha '>', uma copia é gerada como elemento de uma lista '''

    primeira_linha = ""
    lines = []
    for linha in refArquivoMulti:
        for caracter in linha:
            if caracter == ">":
            
                primeira_linha += linha

            lines.append(primeira_linha)
    
    '''Para cada elemento da lista de linhas, é adicionado um novo elemento no limite entre '>' e '|' '''

    labels = []
    cabecalho = ""
    for element in lines:
        for caracter in element:
            if element != "|":
                cabecalho = caracter
            
            if element == "|":
                break

        labels.append(cabecalho)

    '''TODO Um dicionário que receba as labels como key, e o que vem após elas até o próximo '>' como sequência'''    

    #dicionario = {}

    
    #print ("Labels: %s"%labels)
    #print("")

    refArquivoMulti.close()



## QUESTÃO 3 ##

def questao3():
    pass

## QUESTÃO 4 ##


# A) A finalidade da função upper - retorna todas letras em maiúsculo -, além das questões de boas práticas, é  ???????
# B) A função de 'rstrip' é um método built-in é retornar uma cópia da string original, cujo caractéres repetidos - espaço em branco, como default- 
# sejam removidos. Por exemplo, o próprio espaço em branco - como no caso do código 5 - ou qualquer outros caractéres escolhidos.
# C)
# D)


