
#importando as bibliotecas necessárias
import pandas as pd 
import xlrd

#abrindo o arquivo
with open(r"C:\Users\maias\Documents\GitHub\CFB017-SAINT\TAC2\WHOPOPTB.xls") as WHOPOPTB:

	#arquivo lido pelo pandas sendo passado para uma variável
	WHOTBDATA = pd.read_excel("WHOPOPTB.xls")

	#variável para receber os valores em ordem crescente
	ascending_tb_deaths = WHOTBDATA.sort_values('TB deaths')

	#tiramos agora o index
	ascending_tb_deaths = ascending_tb_deaths.to_string(index=False)

	print(ascending_tb_deaths)

	#fechando o arquivo
	WHOPOPTB.close()