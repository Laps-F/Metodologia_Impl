import math
import matplotlib.pyplot as plt
import numpy as np
import csv

def readFile(path):
    file = open(path, 'r')
    
    reader = csv.reader(file)

    list = []
    for row in reader:
        list.append(row)

    file.close()

    return list

def convertData(list):
    cidades = [[] for _ in range(5)]
    for idx, line in enumerate(list):
        for item in line:
            if idx == 0:
                continue
            partes = item.split(";")
            cidade = partes[0]
            tempoAstar = float(partes[1])
            tempoDijkstra = float(partes[2])
            localizacao1 = partes[3]
            localizacao2 = partes[4]
            distancia = float(partes[5])
            if idx <= 90:
                cidades[0].append([cidade, tempoAstar, tempoDijkstra, localizacao1, localizacao2, distancia])
            elif idx <= 180:
                cidades[1].append([cidade, tempoAstar, tempoDijkstra, localizacao1, localizacao2, distancia])
            elif idx <= 270:
                cidades[2].append([cidade, tempoAstar, tempoDijkstra, localizacao1, localizacao2, distancia])
            elif idx <= 360:
                cidades[3].append([cidade, tempoAstar, tempoDijkstra, localizacao1, localizacao2, distancia])
            elif idx <= 450:
                cidades[4].append([cidade, tempoAstar, tempoDijkstra, localizacao1, localizacao2, distancia])
    return cidades

def graphCidades(cidade, temposAstar, temposDijkstra):
    count = 0
    somaTemposAstar = []
    somaTemposDijkstra = []

    for i in range(3):
        for _ in range(30):
            somaTemposAstar.append(temposAstar[count])
            somaTemposDijkstra.append(temposDijkstra[count])
            count += 1
        stdAstar = np.std(somaTemposAstar)
        confAstar = 1.96 * (stdAstar / np.sqrt(30))
        stdDijkstra = np.std(somaTemposDijkstra)
        confDijkstra = 1.96 * (stdDijkstra / np.sqrt(30))
        
        plt.errorbar(i, np.mean(somaTemposAstar), yerr=confAstar, fmt='o', color='blue', label=i)
        plt.errorbar(i, np.mean(somaTemposDijkstra), yerr=confDijkstra, fmt='o', color='red', label=i)   

        somaTemposAstar.clear()
        somaTemposDijkstra.clear()

    plt.xticks([0, 1, 2], ['Caminho1', 'Caminho2', 'Caminho3'])

    plt.ylabel('Tempo Médio')
    plt.title(cidade)
    plt.legend(['A-Star', 'Dijkstra'], loc='upper left', bbox_to_anchor=(1.05, 1),  borderaxespad=0)
    plt.subplots_adjust(right=0.8)
    path = './graphs/' + cidade + ".png"
    plt.savefig(path)
    plt.clf()
    plt.show()

def graphResultados(valorAstar, valorDijkstra):

    eficAstar = (valorAstar / (valorAstar + valorDijkstra)) * 100
    eficDijkstra = 100 - eficAstar

    labels = ['A-Star', 'Dijkstra']

    # Cria os dados para o gráfico de barras
    eficiencia = [eficAstar, eficDijkstra]

    # Cria o gráfico de barras verticais
    plt.bar(labels, eficiencia, color=['blue', 'red'])

    # Configurações do gráfico
    plt.ylabel('Porcentagem de Eficiência')

    # Configurações do gráfico
    plt.title('Comparação de Eficiência entre A-Star e Dijkstra')
    plt.savefig('./graphs/Resultados.png')

    # Mostrar o gráfico
    plt.show()

def ttest(Cidade, TemposAStar, TemposDijkstra, LocalI, LocalF, Distancia, csv_writer, countAstar, countDijkstra):
    result = []

    for i in range(30):
        result.append(TemposDijkstra[i] - TemposAStar[i])
    
    mean = np.mean(result)
    std = np.std(result)

    lower_bound = mean - 1.96*(std/math.sqrt(30))
    upper_bound = mean + 1.96*(std/math.sqrt(30))

    zero_in_interval = round(lower_bound, 4) <= 0 <= round(upper_bound, 4)

    if not zero_in_interval :
        if upper_bound > 0:
            countAstar = countAstar + 1
        elif upper_bound < 0:
            countDijkstra = countDijkstra + 1

    # csv_writer.writerow([Cidade, round(np.mean(TemposAStar),4), round(np.mean(TemposDijkstra),4) , round(lower_bound, 4), round(upper_bound, 4), "Falso" if zero_in_interval else "Verdadeiro", LocalI, LocalF, Distancia])

    return countAstar, countDijkstra

list = readFile("./csvs/Resultados.csv")
cidades = convertData(list)

path = "./csvs/Tests.csv"

f = open(path, "a+", newline="")
csv_writer = csv.writer(f)
# csv_writer.writerow(["Cidade", "Media A-Star", "Media Dijkstra", "Lim. Inferior", "Lim. Superior", "Diferenca estatistica", "Local Inicial", "Local Final", "Disntancia"])

tempos1Astar = []
tempos1Dijkstra = []

tempos2Astar = []
tempos2Dijkstra = []

tempos3Astar = []
tempos3Dijkstra = []

tempoAstar = []
tempoDijkstra = []

countAstar = 0
countDijkstra = 0

for cidade in cidades:
    for idx, line in enumerate(cidade):
        if idx < 30:
            tempos1Astar.append(line[1])
            tempos1Dijkstra.append(line[2])
            local1I = line[3]
            local1F = line[4]
            distancia1 = line[5]
        elif idx < 60:
            tempos2Astar.append(line[1])
            tempos2Dijkstra.append(line[2])
            local2I = line[3]
            local2F = line[4]
            distancia2 = line[5]
        elif idx < 90:
            tempos3Astar.append(line[1])
            tempos3Dijkstra.append(line[2])
            local3I = line[3]
            local3F = line[4]
            distancia3 = line[5]
    countAstar, countDijkstra = ttest(cidade[0][0], tempos1Astar, tempos1Dijkstra, local1I, local1F, distancia1, csv_writer, countAstar, countDijkstra)
    countAstar, countDijkstra = ttest(cidade[0][0], tempos2Astar, tempos2Dijkstra, local2I, local2F, distancia2, csv_writer, countAstar, countDijkstra)
    countAstar, countDijkstra = ttest(cidade[0][0], tempos3Astar, tempos3Dijkstra, local3I, local3F, distancia3, csv_writer, countAstar, countDijkstra)
    tempoAstar = np.concatenate((tempos1Astar, tempos2Astar, tempos3Astar))
    tempoDijkstra = np.concatenate((tempos1Dijkstra, tempos2Dijkstra, tempos3Dijkstra))
    # graphCidades(cidade[0][0], tempoAstar, tempoDijkstra)
    tempos1Astar.clear()
    tempos1Dijkstra.clear()
    tempos2Astar.clear()
    tempos2Dijkstra.clear()
    tempos3Astar.clear()
    tempos3Dijkstra.clear()

graphResultados(countAstar, countDijkstra)

# import matplotlib.pyplot as plt


