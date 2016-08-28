import json
#import arff
import numpy as np
from scipy.io import arff

#dataset = arff.load(open('input_k3_hier.arff','r'))
#data = np.array(dataset['data'])
#print data

factors = np.array([
    [1.0,0.8,0.6,0.5,0.9,1.0,0.6,0.0,0.0,0.0,0.0,0.7],
    [0.9,0.7,0.9,1.0,0.7,1.0,0.7,0.0,0.4,0.5,0.0,0.8],
    [0.5,0.0,1.0,0.7,0.9,0.7,0.6,0.0,0.0,0.0,0.5,0.0],
    [0.9,0.8,1.0,0.7,0.9,1.0,0.5,0.0,0.0,0.0,0.0,1.0],
    [0.8,0.7,0.9,0.7,0.8,1.0,0.8,0.7,0.0,0.0,0.0,0.9],
    [0.9,0.9,0.85,0.9,1.0,0.6,0.9,0.4,0.6,0.0,0.0,0.8],
    [0.4,0.0,0.8,1.0,1.0,0.8,0.8,0.0,0.8,0.0,0.0,0.7],
    [0.9,0.0,0.6,0.8,0.5,1.0,0.5,0.0,0.0,0.0,0.0,0.8],
    [0.8,0.7,0.4,0.7,0.0,0.4,0.4,0.6,0.6,0.0,0.0,0.0],
    [0.0,0.0,0.0,0.0,0.0,0.8,0.3,0.5,0.5,0.5,0.5,0.5],
    [1.0,1.0,0.8,0.8,1.0,1.0,1.0,0.8,1.0,1.0,1.0,0.7]
])

ds2 = arff.loadarff('input_k4_em.arff')
print ds2[0]


def writeCluster(cluster):
    if '1' in cluster:
        return 0
    elif '2' in cluster:
        return 1
    elif '3' in cluster:
        return 2
    elif '4' in cluster:
        return 3
    elif '5' in cluster:
        return 4

def assignName(i):
    if i==0:
        return "Ontorion"
    elif i==1:
        return "PoolParty"
    elif i==2:
        return "Knowledge Store"
    elif i==3:
        return "Metaphacts"
    elif i==4:
        return "Semaphore 4"
    elif i==5:
        return "Anzo SDP"
    elif i==6:
        return "RAVN ACE"
    elif i==7:
        return "CloudSpace"
    elif i==8:
        return "Synaptica ETMS"
    elif i==9:
        return "SAP HANA"
    elif i==10:
        return "EKG"


result = []
for i in xrange(len(factors)):
    result.append({
        "cluster": writeCluster(ds2[0][i][11]),
        "radius": np.linalg.norm(factors[i])*20,
        "name": assignName(i)
    })

torender = open('toRender_k4.json',"w")
torender.write(json.dumps(result))