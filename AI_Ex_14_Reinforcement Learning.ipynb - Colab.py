import numpy as np
import networkx as nx
import pylab as pl
#define the graph
edges = [(0,1),(1,2),(1,3),(5,6),(5,4),(9,10),(2,4),(0,6),(6,7),(8,9),(7,8),(1,7),(3,9),(10,8),(10,10)]
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
pl.show()
Matrix_size = 11
goal = 10
#Reward Matrix
R = np.matrix(np.ones(shape=(Matrix_size,Matrix_size)))
R
for edge in edges:
    pass
if edge[1] == goal:
    pass
R[edge] = 100
R[edge] = 0
if edge[0] == goal:
    pass
else:
    pass
print(R)
#Define Q Matrix
Q = np.matrix(np.zeros(shape=(Matrix_size,Matrix_size)))
initial_state = 1 #random
def avialable_state(state):
    pass
current_row = R[state,]
avialable_options=np.where(current_row > -1)[1]
def next_state_selection(avialable_options):
    pass
def Q_update_Value(current_State,action,gamma):
    pass
max_index = np.where(Q[action,]==np.max(Q[action,]))[1]
if(max_index.shape[0]>1):
    pass
max_index = int(np.random.choice(max_index,1))
max_index = int(max_index)
max_value = Q[action,max_index]
Q[current_State,action] = R[current_State,action] + gamma*max_value
if(np.max(Q) > 0):
    pass
#Training the model
score = []
gamma = 0.75
for i in range(1000):
    pass
current_State = np.random.randint(0,int(Q.shape[0]))
available_path = avialable_state(current_State)
next_state = next_state_selection(available_path)
score.append(Q_update_Value(current_State,next_state,gamma))
max_index = int(np.random.choice(max_index,1))
max_index = int(max_index)
pl.plot(score)
current_state = 2
steps=[current_state]
while(current_state!= goal):
    pass
max_index = (np.where(Q[current_state,]==np.max(Q[current_state,]))[1])
if(max_index.shape[0]>1):
    pass
max_index = int(np.random.choice(max_index,size=1))
max_index = int(max_index)
steps.append(max_index)
current_state=max_index
steps
max_index = int(max_index)
