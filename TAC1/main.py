

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
    refArquivoMulti = open("/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")

    '''Para cada linha no arquivo que tenha '>', uma copia é gerada como elemento de uma lista '''

    cabecalho = ""
    sequencia = ""
    label_list = []
    seq_list = []
    label_seq = {}

    for line in refArquivoMulti.readlines():
        line = line.strip()
        for i in line:
            if i == ">":
                if cabecalho != "":
                    cabecalho.join(line)
                    label_list.append(cabecalho)
                
            elif i != ">":
                sequencia.join(line)
                
            elif i == ">":
                break
        
        seq_list.append(sequencia)
        sequencia = ""
        cabecalho = ""
    
    refArquivoMulti.close()
    
    # TODO Dicionário que receba os valores das listas atribuindo Labels como keys e Seq's como values.
 
    for element in label_list:
        label_seq
        pass
    
    print(label_list, seq_list, label_seq)

#Teste
if __name__ == "__main__":
    questao2()
    print("That's it")

## QUESTÃO 3 ##

def questao3():
    #codigo original
    refArquivoEntrada = open("C:/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/species.csv")
    refArquivoEntrada.readline()
    for linha in refArquivoEntrada:
        data = linha.split(",")
        if data[3].upper().rstrip() == "BIRD":
            print ("%s\t%s\t%s\t%s" %(data[0], data[1], data[2], data[3].rstrip()))
    refArquivoEntrada.close()
    
import csv
def questao3_1():
    #codigo simples utilizando os métodos csv do python, deletando tabulações
    with open("C:/Users/maias/Documents/GitHub/CFB017-SAINT/TAC1/species.csv") as csv_file:
        all_data = csv.reader(csv_file, delimiter=',')
        for line in all_data:
            if line[3].upper().rstrip() == "BIRD":
                 print(*lines,sep="\t")
    csv_file.close()


## QUESTÃO 4 ##


# A) A finalidade da função upper - retornar todas letras em maiúsculo - 
# é de impedir que seja necessário pensar em todas formas de se escrever a mesma coisa, como no exemplo: BIRD, Bird ou bird
# B) A função de 'rstrip' é um método built-in é retornar uma cópia da string original, cujo caractéres repetidos - espaço em branco, como default- 
# sejam removidos. Por exemplo, o próprio espaço em branco - como no caso do código 5 - ou qualquer outros caractéres escolhidos. Como no caso de 3_1, tabulações.
# C) Caso não fosse o caso de se usar o "upper()", o padrão não seria encontrado. "Bird", "BIRD" e "bird" não são o mesmo termo para o computador.
# D) O "rstrip()" nos é fundamental nesse caso para que não ocorra o problema de não retornar valores. 
# Espaços em branco - "" -, linhas saltadas "\n" e demais, atrapalham na leitura e busca de termos, então devem ser ponderado que o algorítmo elimine-os nas buscas.


