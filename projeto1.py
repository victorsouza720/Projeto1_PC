import math 
import random
import datetime 
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#ENTRADAS
Capital = float (input('Digite o capital inicial (R$):'))
Aporte = float (input ('Digite o aporte incial (R%):'))
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
Montante_CDB = (Capital * math.pow ((1 + Taxa_CDB), Meses + (Aporte * Meses )))
lucro_CDB = Montante_CDB - Total_investido
Montante_CDB_liquido = Total_investido = (lucro_CDB * 0.85)

#LCI 
Taxa_LCI = CDI_mensal * Perc_LCI
Montante_LCI = (Capital * math.pow((1 + Taxa_LCI), Meses) + (Aporte * Meses ))

#POUPANÇA
Taxa_poupança = 0.005
Montante_poupança = (Capital * math.pow((1 + Taxa_poupança), Meses) + (Aporte * Meses))



#FII - SIMULAÇÕES
Montante_fii = (Capital * math.pow((1 + Taxa_FII), Meses) + (Aporte * Meses))
Sim_FII1 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII2 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII3 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII4 = Montante_fii * (1 + random.uniform (-0.03, 0.03))
Sim_FII5 = Montante_fii * (1 + random.uniform (-0.03, 0.03))

Lista_FII = (Sim_FII1, Sim_FII2, Sim_FII3, Sim_FII4, Sim_FII5)

Media_fii = statistics.mean (Lista_FII)
Mediana_fii = statistics.median (Lista_FII)
Desvio_fii = statistics.stdev (Lista_FII)

#DATA DE RESGATE
Data_atual = datetime.datetime.now()
Data_final = Data_atual + datetime.timedelta(days = Meses * 30)

#SE A META FOI ATINGIDA OU NÃO
Meta_atingida = Media_fii >= Meta

#ESCALA PARA GERAR O GRAFICO ASCII
Escala = 1000

Barras_CDB = int(Montante_CDB_liquido / Escala)
Barras_LCI = int(Montante_LCI / Escala)
Barras_poupanca = int(Montante_poupança / Escala)
Barras_FII = int(Media_fii / Escala)

Grafico_CDB = "█" * Barras_CDB
Grafico_LCI = "█" * Barras_LCI
Grafico_poupanca = "█" * Barras_poupanca
Grafico_FII = "█" * Barras_FII

#ORGANIZAÇÃO DOS PRINTS PARA A SAIDA IGUAL O MODELO
print("\n========================================")
print("PyInvest - Simulador de Investimentos")
print("========================================")
print("Data da simulação:", Data_atual.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", Data_final.strftime("%d/%m/%Y"))
print("\nTotal investido:", locale.currency(Total_investido, grouping=True))
print("\n--- RESULTADOS FINANCEIROS ---")
print("CDB:", locale.currency(Montante_CDB_liquido, grouping=True))
print(Grafico_CDB)
print("\nLCI/LCA:", locale.currency(Montante_LCI, grouping=True))
print(Grafico_LCI)
print("\nPoupança:", locale.currency(Montante_poupança, grouping=True))
print(Grafico_poupanca)
print("\nFII (média):", locale.currency(Media_fii, grouping=True))
print(Grafico_FII)
print("\n--- ESTATÍSTICAS FII ---")
print("Mediana:", locale.currency(Mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(Desvio_fii, grouping=True))
print("\nMeta atingida:", Meta_atingida)
print("========================================")
