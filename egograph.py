import networkx as nx
from networkx import algorithms
# from dataf import dataframe
import pickle

from collections import Mapping
import json


def egodata(graphname):
    corenumber = {}
    connectedcomponents = {}
    triangles = {}
    coefficient = {}
    egonetSize = {}
    cc = list()
    tri = list()
    coeff = list()
    egoSize = list()
    hasrisk = list()
    corenumberlist = list()

    for node in graphname.nodes():
        ego_graph = nx.ego_graph(graphname, node)

        if len(graphname.node[node]) is not 0:
            hasrisk.append(graphname.node[node]["negemo"])

        # Core number
        corenumber[node] = max(nx.core_number(ego_graph).values())
        corenumberlist.append(max(nx.core_number(ego_graph).values()))

        # egonetSize
        egonetSize[node] = ego_graph.size()
        egoSize.append(ego_graph.size())

        # Triangle count
        triangleCount = nx.triangles(ego_graph, node)
        triangles[node] = triangleCount  # adding the count for that node in dictionary
        tri.append(triangleCount)

        # Clustering co-efficients
        coeff_temp = nx.average_clustering(ego_graph)
        coefficient[node] = coeff_temp  # adding the count for that node in dictionary
        coeff.append(coeff_temp)

        # Connected components minus ego
        ego_graph.remove_node(node)
        number = nx.number_connected_components(ego_graph)  # adding the count for that node in dictionary
        connectedcomponents[node] = number
        cc.append(number)

    print corenumber
    print connectedcomponents
    print triangles
    print coefficient
    print egonetSize



file = open("dictionaryOfGraph.pckl","rb")
dict_of_scores = pickle.load(file)
print (type(dict_of_scores))
print (str(dict_of_scores))
graphs= open("test.json","r")
dct_for_graph = {}
for i in graphs:
    item = json.loads(i)
    #print item.values()
    #print item.keys()
    for key,value in item.items():
        # print "key ",key
        # print "value ",value
        for val in range(len(value)):
            # print value[val]
            if value[val] in dict_of_scores.keys():

                dct_for_graph[int(key)] = {value[val]: dict_of_scores[value[val]]}

# print( str(dct_for_graph))

G = nx.Graph()
q = list(dct_for_graph.items())
while q:
    v, d = q.pop()
    # print v, " V"
    # print d, " D"
    # G.add_edge(v,d)
    G.add_node(v)
    for nv, nd in d.items():
        # print nv, " NV"
        # print nd," ND"
        G.add_node(nv,attr_dict=nd)
        G.add_edge(v, nv)
        # if isinstance(nd, Mapping):
        #     q.append((nv, nd))
# for data in G.nodes():
    # print G.node[data]

G.remove_edges_from(G.selfloop_edges())
egodata(G)
            # if value[val] ==
    # for key,value in item:
    #     print "key ",key
    #     print "value ",value
# print(str(dict_of_scores))
# # print dict_of_scores.items()
#
# for key, value in dict_of_scores.items():
#     print "key " + str(key)
#     print "value " + str(value)
# #     for k, v in value.items():
# #         print "k" + str(type(k))
# #         print "v" + str(type(v))
#
# G  = nx.Graph(dct_for_graph)
# print(G.nodes())
# # print(G.edges())

# G=nx.from_dict_of_dicts(dict_of_scores)
#
# # print G
#
# def __init__(self, graphname, riskfactor, name, filtervalue):
#         graphname = graphname
#         riskfactor = riskfactor
#         name = name
#         filtervalue = filtervalue
#
