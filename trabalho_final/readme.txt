
Projeto Final

O objetivo deste projeto é aplicar todos os conhecimentos adquiridos na disciplina de programação para biociências e disciplinas de pré-requisito para resolver um problema cotidiano da área de bioinformática. 

Caso: Foi realizado o sequenciamento de RNA de um organismo com parentesco com o Rhodnius prolixus chamado de Rhodnius desconhecidus. Queremos saber qual a natureza
dos genes mais expressos em cada condição. No entanto, o R. desconhecidus foi recentemente sequenciado e não possui ainda a descrição completa do produto de cada gene anotado. 
Portanto, devemos buscar por genes do seu parente próximo que tenham homologia baseando-se na similaridade por sequência. Para resolver este problema, desenvolva um código em Python
que atenda os critérios e realize as funções seguintes:


a) Leia da linha de comando nesta ordem:

i) uma tabela xlsx com dados de quantificação (Tabela 1) para quatro bibliotecas de RNA-Seq;
ii) Um arquivo multi-FASTA contendo as sequências de DNA dos genes de R. desconhecidus (Arquivo 1);
iii) Um arquivo multi-FASTA contendo sequências de aminoácidos de R. prolixus (Arquivo 2);

b) A Tabela 1 contém os identificadores dos genes e os valores de expressão não-normalizados para cada uma das duas réplicas (Rep1 e Rep2) para cada condição (A e B);

c) Crie colunas adicionais para adicionar os níveis de expressão normalizados por CPM (counts per million) de cada réplica. 
Nomeie essas colunas como Rep1_A_CPM, Rep2_A_CPM, Rep1_B_CPM e Rep2_B_CPM;

d) Crie colunas adicionais que vão armazenar a expressão normalizada (CPM) média por condição. 
Nomeie as colunas como Cond_A_CPM_media e Cond_B_CPM_media;

e) Selecione os cinco genes mais expressos de cada condição baseado na expressão média.

f) Realize uma busca BLAST da sequência de DNA dos 10 genes selecionados anteriormente contra as sequências de aminoácidos de R. prolixus.

g) A partir do resultado do BLAST, imprima o melhor hit para cada um dos 10 genes baseado no maior valor de bitscore. Em caso de bitscores iguais, selecione o hit com menor e-value. Caso o empate persista, selecione qualquer um dos hits empatados.

h) A saída impressa no terminal deverá conter os seguintes dados:

gene_id     Cond_A_CPM_media     Cond_B_CPM_media      id_proteína_encontrada               

Onde gene_id é um dos genes mais expressos na condição A ou B; 
Cond_A_CPM_media e Cond_B_CPM_media são os valores médios de CPM para cada condição; 
e id_proteína_encontrada é o identificador da sequência de proteína com melhor hit em R. prolixus.
