import csv
import time
import networkx as nx

def readFile(path):
    file = open(path, 'r')
    
    reader = csv.reader(file)

    
    list = []
    for row in reader:
        list.append(row)

    file.close()

    return list

def createGraph(list):

    # Criar um grafo não direcionado
    grafo = nx.Graph()

    # Iterar sobre os elementos da lista
    for edge in list:
        for item in edge:
            partes = item.split(";")
            localizacao1 = partes[0]
            localizacao2 = partes[1]
            peso = float(partes[2])

            # Adicionar uma aresta com o peso ao grafo
            grafo.add_edge(localizacao1, localizacao2, weight=peso)
    
    print(grafo)

    return grafo

def aStar(graph, start_node, end_node):
    Itime_Astar = time.time()
    # Executa o algoritmo A*
    shortest_path = nx.astar_path(graph, start_node, end_node, weight="weight")
    shortest_distance = nx.astar_path_length(graph, start_node, end_node, weight='weight')
    Ftime_Astar = time.time()

    # Imprime o caminho mínimo e a distância
    print(f'Caminho mínimo de {start_node} até {end_node} com A*:')
    print(f'Distância A*: {shortest_distance}')
    print(f'Caminho A*: {shortest_path}')
    print(f"Tempo execução A*: {Ftime_Astar - Itime_Astar}\n")
    return Ftime_Astar - Itime_Astar, shortest_distance

def dijkstra(graph, start_node, end_node):
    Itime_Dijkstra = time.time()
    # Executa o algoritmo de Dijkstra
    shortest_paths = nx.single_source_dijkstra_path(graph, start_node, weight='weight')
    shortest_distances = nx.single_source_dijkstra_path_length(graph, start_node, weight='weight')
    Ftime_Dijkstra = time.time()

    for target_node in graph:
        if target_node != start_node:
            if target_node == end_node:
                path = shortest_paths[target_node]
                distance = shortest_distances[target_node]
                print(f"Caminho mínimo de {start_node} até {target_node} com Dijkstra:")
                print(f"Distância Dijkstra: {distance}")
                print(f"Caminho Dijkstra: {path}")
                print(f"Tempo execução Dijkstra: {Ftime_Dijkstra - Itime_Dijkstra}\n")
                return Ftime_Dijkstra - Itime_Dijkstra

listLisboa = readFile("./csvs/Metro_Stations_in_Lisboa.csv")
listDC = readFile("./csvs/Metro_Stations_in_DC.csv")
listSP = readFile("./csvs/Metro_Stations_in_SP.csv")
listParis = readFile("./csvs/Metro_Stations_in_Paris.csv")
listPequim = readFile("./csvs/Metro_Stations_in_Pequim.csv")

graphLisboa = createGraph(listLisboa)
graphDC = createGraph(listDC)
graphSP = createGraph(listSP)
graphParis = createGraph(listParis)
graphPequim = createGraph(listPequim)

f = open("./csvs/Resultados.csv", "a+", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["Cidade", "A-Star", "Dijkstra", "Origem", "Destino", "Distancia"])

# Caminho em Lisboa
for i in range(30):
    timeAstar, distancia = aStar(graphLisboa, "Rato", 'Intendente')
    timeDijkstra = dijkstra(graphLisboa, "Rato", 'Intendente')
    csv_writer.writerow(["Lisboa", round(timeAstar,5), round(timeDijkstra, 5), "Rato", 'Intendente', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphLisboa, "Alto dos Moinhos", 'Laranjeiras')
    timeDijkstra = dijkstra(graphLisboa, "Alto dos Moinhos", 'Laranjeiras')
    csv_writer.writerow(["Lisboa", round(timeAstar,5), round(timeDijkstra, 5), "Alto dos Moinhos", 'Laranjeiras', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphLisboa, "Roma", 'Anjos')
    timeDijkstra = dijkstra(graphLisboa, "Roma", 'Anjos')
    csv_writer.writerow(["Lisboa", round(timeAstar,5), round(timeDijkstra, 5), "Roma", 'Anjos', distancia])

# Caminho em Washington DC
for i in range(30):
    timeAstar, distancia = aStar(graphDC, "Cleveland Park", 'Benning Road')
    timeDijkstra = dijkstra(graphDC, "Cleveland Park", 'Benning Road')
    csv_writer.writerow(["Washington DC", round(timeAstar,5), round(timeDijkstra, 5), "Cleveland Park", 'Benning Road', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphDC, "Addison Road - Seat Pleasant", 'Morgan Boulevard')
    timeDijkstra = dijkstra(graphDC, "Addison Road - Seat Pleasant", 'Morgan Boulevard')
    csv_writer.writerow(["Washington DC", round(timeAstar,5), round(timeDijkstra, 5), "Addison Road - Seat Pleasant", 'Morgan Boulevard', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphDC, "Court House", 'Federal Triangle')
    timeDijkstra = dijkstra(graphDC, "Court House", 'Federal Triangle')
    csv_writer.writerow(["Washington DC", round(timeAstar,5), round(timeDijkstra, 5), "Court House", 'Federal Triangle', distancia])

# Caminho em Sao Paulo
for i in range(30):
    timeAstar, distancia = aStar(graphSP, "Estacao Sagrado Coracao", 'Cidade Universitaria')
    timeDijkstra = dijkstra(graphSP, "Estacao Sagrado Coracao", 'Cidade Universitaria')
    csv_writer.writerow(["Sao Paulo", round(timeAstar,5), round(timeDijkstra, 5), "Estacao Sagrado Coracao", 'Cidade Universitaria', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphSP, "Santa Cecilia", 'Republica')
    timeDijkstra = dijkstra(graphSP, "Santa Cecilia", 'Republica')
    csv_writer.writerow(["Sao Paulo", round(timeAstar,5), round(timeDijkstra, 5), "Santa Cecilia", 'Republica', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphSP, "Estacao Jardim Romano", 'Tamanduatei')
    timeDijkstra = dijkstra(graphSP, "Estacao Jardim Romano", 'Tamanduatei')
    csv_writer.writerow(["Sao Paulo", round(timeAstar,5), round(timeDijkstra, 5), "Estacao Jardim Romano", 'Tamanduatei', distancia])

# Caminho em Paris
for i in range(30):
    timeAstar, distancia = aStar(graphParis, "Pont de Sevres", 'Olympiades')
    timeDijkstra = dijkstra(graphParis, "Pont de Sevres", 'Olympiades')
    csv_writer.writerow(["Paris",  round(timeAstar,5), round(timeDijkstra, 5), "Pont de Sevres", 'Olympiades', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphParis, "Saint-Sebastien - Froissart", 'Chemin Vert')
    timeDijkstra = dijkstra(graphParis, "Saint-Sebastien - Froissart", 'Chemin Vert')
    csv_writer.writerow(["Paris",  round(timeAstar,5), round(timeDijkstra, 5), "Saint-Sebastien - Froissart", 'Chemin Vert', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphParis, "Boulogne - Pont de Saint-Cloud", 'Sevres - Babylone')
    timeDijkstra = dijkstra(graphParis, "Boulogne - Pont de Saint-Cloud", 'Sevres - Babylone')
    csv_writer.writerow(["Paris",  round(timeAstar,5), round(timeDijkstra, 5), "Boulogne - Pont de Saint-Cloud", 'Sevres - Babylone', distancia])

# Caminho em Pequim
for i in range(30):
    timeAstar, distancia = aStar(graphPequim, "Jiaohuachang", 'Bei\'anhe')
    timeDijkstra = dijkstra(graphPequim, "Jiaohuachang", 'Bei\'anhe')
    csv_writer.writerow(["Pequim",  round(timeAstar,5), round(timeDijkstra, 5), "Jiaohuachang", 'Bei\'anhe', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphPequim, "Xingong", 'Xihongmen')
    timeDijkstra = dijkstra(graphPequim, "Xingong", 'Xihongmen')
    csv_writer.writerow(["Pequim",  round(timeAstar,5), round(timeDijkstra, 5), "Xingong", 'Xihongmen', distancia])

for i in range(30):
    timeAstar, distancia = aStar(graphPequim, "Life Science Park", 'Yizhuang Culture Park')
    timeDijkstra = dijkstra(graphPequim, "Life Science Park", 'Yizhuang Culture Park')
    csv_writer.writerow(["Pequim",  round(timeAstar,5), round(timeDijkstra, 5), "Life Science Park", 'Yizhuang Culture Park', distancia])
