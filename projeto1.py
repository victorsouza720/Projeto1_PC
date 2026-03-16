import math
import random
import datetime
import statistics
import locale

#Monetário
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#Entrada de dados
capital = float(input("Digite o capital inicial (R$): "))
aporte = float(input("Digite o aporte mensal (R$): "))
meses = int(input("Prazo mensal: "))
cdi_anual = float(input("CDI anual (%): "))/100
perc_cdb = float(input("Percentual do CDI (%): "))/100
perc_lci = float(input("Percentual do LCI (%): "))/100
taxa_fii = float(input("Porcentalidade mensal FII (%): "))/100
meta = float(input("Meta financeira (R$): "))

#CDI
cdi_mensal = math.pow((1+cdi_anual),1/12) - 1
total_investido = capital + (aporte*meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb), meses) + (aporte * meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci), meses) + (aporte * meses))

#Poupança
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca), meses) + (aporte * meses))

#FII - Simulações
montante_fii = (capital * math.pow((1+ taxa_fii), meses) + (aporte * meses))
sim_fii1 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii2 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii3 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii4 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii5 = montante_fii * (1 + random.uniform (-0.03,0.03))

lista_fii = (sim_fii1, sim_fii2, sim_fii3, sim_fii4, sim_fii5)

media_fii = statistics.mean(lista_fii)
mediana_fii = statistics.median(lista_fii)
desvio_fii = statistics.stdev(lista_fii)


#Data de resgate
data_atual = datetime.date.today()
data_resgate = data_atual + datetime.timedelta(days = meses * 30)

#Indicador booleano meta financeira
meta_atingida = media_fii >= meta

#Gráfico ASCII
Escala = 1000

Barras_cdb = int(montante_cdb_liquido/Escala)
Barras_lci = int(montante_lci/Escala)
Barras_poupanca = int(montante_poupanca/Escala)
Barras_fii = int(montante_fii/Escala)

Grafico_cdb = "█" * Barras_cdb
Grafico_lci = "█" * Barras_lci
Grafico_poupança = "█" * Barras_poupanca
Grafico_fii = "█" * Barras_fii

#Relatório final
print("=====================================")
print("PyInvest - Simulador de Investimentos")
print("=====================================")
print("Data de simulação:", data_atual.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%Y"))
print("=====================================")
print("\n----TOTAL INVESTIDO----")
print("Total investido:", locale.currency(total_investido, grouping=True))
print("\n--- RESULTADOS FINANCEIROS ---")
print("CDB:", locale.currency(montante_cdb_liquido, grouping=True))
print(Grafico_cdb)
print("\n", locale.currency(montante_lci, grouping=True))
print(Grafico_lci)
print("\nPoupança:", locale.currency(montante_poupanca, grouping=True))
print(Grafico_poupança)
print("\nFII (média):", locale.currency(media_fii, grouping=True))
print(Grafico_fii)
print("\n--- ESTATÍSTICAS FII ---")
print("Mediana: ", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão: ", locale.currency(desvio_fii, grouping=True))
print("\nMeta atingida?", meta_atingida)
print("=====================================")
