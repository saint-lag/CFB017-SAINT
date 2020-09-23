#importando as bibliotecas necessárias
import pandas as pd 
import xlrd

#abrindo o arquivo
with open(r"C:\Users\maias\Documents\GitHub\CFB017-SAINT\exercicio_1\WHOPOPTB.xls") as WHOPOPTB:

	#arquivo lido pelo pandas sendo passado para uma variável
	WHOTBDATA = pd.read_excel("WHOPOPTB.xls")

	#devemos normalizar a população: 
	#[População (1000s)] . 1000/100.000 = [População (1000s)]/100
	pop_normal = WHOTBDATA['Population (1000s)']/100

	#criando nova coluna para quantidade de óbitos
	WHOTBDATA['Death rate'] = WHOTBDATA['TB deaths']/pop_normal

	#imprimindo as colunas sem index
	print(WHOTBDATA.to_string(index=False))

	#fechando o arquivo
	WHOPOPTB.close()
