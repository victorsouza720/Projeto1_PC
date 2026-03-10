import math 
import randon 
import datetime 
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR_UTF-8')

#ENTRADAS
Capital = float (input('Digite o capital inicial (R$):'))
Aporte = float (inpout ('Digete o aporte incial (R%):'))
Meses = int (input('Prazo (meses): '))
CDI_anual = float (input ('CDI anula (%):'))/100
Perc_CDB = float (input(' Percentual em CDI (%):' ))/100
Perc_LCI = float (input(' Percentual em LCI (%):' ))/100
Taxa_FII = float (input(' Percentual em FII (%):' ))/100
Meta = float (input('meta financeira (R$): '))

#CONVERSÃO CDI 
CDI_mensal = math.pow((1+CDI_anual),1/12) -1

#TOTAL INVESTIDO 
Total_investido = Capital + (Aporte * Meses)

#CDB
Taxa_CDB = CDI_mensal *Perc_CDB
Montante_CDB = (Capital * math.pow ((1 + Taxa_CDB), Meses + (Aporte * Meses ))
lucro_CDB = Montante_CDB - Total_investido
Montante_CDB_liquido = Total_investido = (lucro_CDB * 0.85)

#LCI 
Taxa_LCI = CDI_mensal * Perc_LCI
Montante_LCI = (Capital * math.pow(1 + Taxa_LCI)), Meses + (Aporte * Meses )

#POUPANÇA 
Taxa_Poupança = 0.005
Montante_Poupança = (Capital * math.pow( 1 + Taxa_Poupança), Meses = (Aporte * Meses))

#FII - SIMULAÇÔES 