import networkx as nx
import random

t = 200
count_history = {}
node_status = [{}] * t

## make node_status an aray of dictionaries
## add in one step through t
def count (d):
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
    return ({'I' : infected,
             'S' : susceptible,
             'R' : recovered})

def step (graph, b, y, i):
    nodes = list(graph.nodes())
    for node in nodes:
        if (node_status[i-1][node] == 'S'):
            neighbor = random.choice(nodes)
            if (node_status[i-1][neighbor] == "I" and (random.random() <= b)):
                node_status[i][node] = 'I'
        elif (node_status[i-1][node] == 'I' and random.random() <= y):
            node_status[i][node] = 'R'
    count_history[i] = count(node_status[i])




def runOneSim (I, S, R, t, b, y):
    # Read the edge-list file and create an undirected graph
    G = nx.read_edgelist('example.txt', delimiter='  ', create_using=nx.Graph())

    # Total number of nodes in the graph
    N = G.number_of_nodes()

    # Assign initial fractions for I, S, and R

    # Assign a status for each node based on the given fractions
    num_infected = int(N * I)
    num_susceptible = int(N * S)
    num_recovered = int(N * R)

    # Randomly assign a status to each node
    nodes = list(G.nodes())
    random.shuffle(nodes)

    for node in nodes[:num_infected]:
        node_status[0][node] = 'I'
    for node in nodes[num_infected:num_infected+num_susceptible]:
        node_status[0][node] = 'S'
    for node in nodes[num_infected+num_susceptible:]:
        node_status[0][node] = 'R'

    
    count_history[0] = count(node_status[0])

    for i in range(1, t):
        step (G, b, y, i)
    return (count_history.copy())

def avg(sims, t):
    avgI = []
    avgS = []
    avgR = []
    for t in range (1, t):
        i = 0
        s = 0
        r = 0
        for sim in sims:
            i += sim[t]["I"]
            s += sim[t]["S"]
            r += sim[t]["R"]
        
        avgI.append(i/t)
        avgS.append(s/t)
        avgR.append(r/t)
    return (avgI, avgS, avgR)


def run (simAmount, i, s, r, t, b, y):
    allSims = [{}] * simAmount
    for i in range (0, simAmount):
        allSims[i] = runOneSim (i, s, r, t, b, y)
    for sim in allSims:
        print (sim)
        print ()
        print ()
    
    I, S, R = avg (allSims, t)
    print ("Average susceptible at each step: ")
    print (S)
    print ()

    print ("Average infected at each step: ")
    print (I)
    print ()

    print ("Average recovered at each step: ")
    print (R)
    print ()

run (3, .05, .95, 0, 10, .1, .05)









    