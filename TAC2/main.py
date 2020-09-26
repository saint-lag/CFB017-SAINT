
#importando bibliotecas 
import pandas
import pandas as pd
import xlrd 


def AbsoluteQuantCalculator(sheet, m, b):
	'''Insert: sheet, m and b values ... y = mx - b '''
	
	#criando dataframe que recebe a planilha
	df = pd.read_excel(sheet)

	#recebendo as colunas
	df_q = df[['Target_Name', 'Stage']]


	# Quantity = 10^(Ct - b)/m
	df_q['Quantity'] = 10 ** (df['CT'] - b)*(1/m)

	#juntando df e df_q
	df_final = pd.merge(df,df_q)

	# df_final como uma nova planilha
	df_final.to_excel('Users/maias/Documents/GitHub/CFB017-SAINT/TAC2', sheet_name = 'AbsQuantSheet.xlrd')

	print(df_final)


AbsoluteQuantCalculator('Users/maias/Documents/GitHub/CFB017-SAINT/TAC2/Valores_CT.xlrd', 10, 8)