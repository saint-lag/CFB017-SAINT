
import numpy as np
import pandas as pd 


#WHOTBDATA = pd.read_excel("Users/maias/Documents/GitHub/CFB017-SAINT/TAC2/WHOPOPTB.xls")

with open(r"C:\Users\maias\Documents\GitHub\CFB017-SAINT\TAC2\WHOPOPTB.xls") as WHOPOPTB:

	WHOTBDATA = pd.read_excel("WHOPOPTB.xls")

	TB_deaths = WHOTBDATA["TB deaths"]
	TB_total_deaths = TB_deaths.sum()
	TB_min_deaths = TB_deaths.min()
	TB_max_deaths = TB_deaths.max()
	TB_mean_deaths = TB_deaths.mean()
	TB_median_deaths = TB_deaths.median()

	print("Exercícios 1 até 5:\n\n",WHOTBDATA)
	print("\nTB_total_deaths: ",TB_total_deaths)
	print("\nTB_min_deaths: ",TB_min_deaths)
	print("\nTB_max_deaths: ",TB_max_deaths)
	print("\nTB_mean_deaths: ",TB_mean_deaths)
	print("\nTB_median_deaths: ",TB_median_deaths)

	print("\nExercícios 5 até 7:\n")

	BRICS_TB_total_deaths = ""


	WHOPOPTB.close()