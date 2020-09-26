
#importando as bibliotecas necessárias
import pandas as pd 
import xlrd

#abrindo o arquivo
with open(r"C:\Users\maias\Documents\GitHub\CFB017-SAINT\exercicio_1\WHOPOPTB.xls") as WHOPOPTB:

	#variável com o arquivo já lido pelo pandas
	WHOTBDATA = pd.read_excel("WHOPOPTB.xls")

	#pandas já reconhece que queremos a coluna das mortes por TB
	TB_deaths = WHOTBDATA["TB deaths"]

	#utilizando funções básicas do pandas 
	TB_total_deaths = TB_deaths.sum()
	TB_min_deaths = TB_deaths.min()
	TB_max_deaths = TB_deaths.max()
	TB_mean_deaths = TB_deaths.mean()
	TB_median_deaths = TB_deaths.median()

	#imprimindo as variáveis
	print("Exercícios 1 até 5:\n\n",WHOTBDATA)
	print("\nTB_total_deaths: ",TB_total_deaths)
	print("\nTB_min_deaths: ",TB_min_deaths)
	print("\nTB_max_deaths: ",TB_max_deaths)
	print("\nTB_mean_deaths: ",TB_mean_deaths)
	print("\nTB_median_deaths: ",TB_median_deaths)

	#fechando o arquivo
	WHOPOPTB.close()
