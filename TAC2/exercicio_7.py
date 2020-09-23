#importando as bibliotecas necessárias
import pandas as pd 
import xlrd

#abrindo o arquivo
with open(r"C:\Users\maias\Documents\GitHub\CFB017-SAINT\TAC2\WHOPOPTB.xls") as WHOPOPTB:

	#arquivo lido pelo pandas sendo passado para uma variável
	WHOTBDATA = pd.read_excel("WHOPOPTB.xls")

	#BRICS: Brazil, Russian Federation, India, China, South Africa
	BRICS = WHOTBDATA.iloc[[1, 8, 5, 2, 10]]

	#Total de óbitos
	BRICS_total_deaths = BRICS['TB deaths'].sum()

	#Média de óbitos
	BRICS_mean_deaths = BRICS['TB deaths'].mean()

	#imprimindo as variáveis
	print('BRICS total deaths:', BRICS_totatl_deaths, 
		'\n''BRICS mean deaths:', BRICS_mean_deaths)

	#fechando o arquivo
	WHOPOPTB.close()
