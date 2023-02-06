import networkx as nx
import random
import matplotlib.pyplot as plt

t = 200
count_history = {}
node_status = [{}] * t

def count (d, N):
    infected = 0
    susceptible = 0
    recovered = 0
    for value in d.values():
        if value == 'I':
            infected += 1
        elif value == 'R':
            recovered += 1
        else:
            susceptible += 1
    return ({'I' : infected/N,
             'S' : susceptible/N,
             'R' : recovered/N})

def step (graph, N, b, y, i):
    nodes = list(graph.nodes())
    for node in nodes:
        if (node_status[i-1][node] == 'S'):
            neighbor = random.choice(nodes)
            if (node_status[i-1][neighbor] == "I" and (random.random() <= b)):
                node_status[i][node] = 'I'
                graph.nodes[node]['status'] = 'I'
        elif (node_status[i-1][node] == 'I' and random.random() <= y):
            node_status[i][node] = 'R'
            graph.nodes[node]['status'] = 'R'
    count_history[i] = count(node_status[i], N)
    return graph




def runOneSim (graph, N, I, S, R, max_time, b, y):
    # Read the edge-list file and create an undirected graph
    G = nx.read_edgelist(graph, delimiter='  ', create_using=nx.Graph())


    # Assign a status for each node based on the given fractions
    num_infected = int(N * I)
    num_susceptible = int(N * S)
    num_recovered = int(N * R)

    # Randomly assign a status to each node
    nodes = list(G.nodes())
    random.shuffle(nodes)

    for node in nodes[:num_infected]:
        node_status[0][node] = 'I'
        G.nodes[node]['status'] = 'I'
    for node in nodes[num_infected:num_infected+num_susceptible]:
        node_status[0][node] = 'S'
        G.nodes[node]['status'] = 'S'
    for node in nodes[num_infected+num_susceptible:]:
        node_status[0][node] = 'R'
        G.nodes[node]['status'] = 'R'

    
    count_history[0] = count(node_status[0], N)

    for i in range(1, max_time):
        graph = step (G, N, b, y, i)
        if i == 1 or i == 
    return (count_history.copy())

def avg(sims, t, N):
    avgI = []
    avgS = []
    avgR = []
    numberOfSims = len (sims)
    for t in range (1, t):
        i = 0
        s = 0
        r = 0
        for sim in sims:
            i += sim[t]["I"]
            s += sim[t]["S"]
            r += sim[t]["R"]
        
        avgI.append(i/numberOfSims)
        avgS.append(s/numberOfSims)
        avgR.append(r/numberOfSims)
    return (avgI, avgS, avgR)


def run (simAmount, graph, N, i, s, r, max_time, b, y):
    allSims = [{}] * simAmount
    for simNumber in range (0, simAmount):
        allSims[simNumber] = runOneSim (graph, N, i, s, r, max_time, b, y)
    for sim in allSims:
        print (sim)
        print ()
        print ()
    
    I, S, R = avg (allSims, max_time, N)
    print ("Average susceptible at each step: ")
    print (S)
    print ()

    print ("Average infected at each step: ")
    print (I)
    print ()

    print ("Average recovered at each step: ")
    print (R)
    print ()

run (1, 'smallerExample.txt', 100, .1, .9, 0, 200, .1, .05)









    