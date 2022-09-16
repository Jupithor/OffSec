#!/usr/bin/python

import sys

graph = []
index = 0
filename=sys.argv[1]
f = open(filename,"r")
for line in f:
  graph.append([line[0:16].strip(),line[17:23],0,[]])
  if index > 0:
    graph[0][3] += [index]
  index += 1
while True:
  weight = 0
  for node in graph:
    distance = 0
    code1 = node[1]
    code2 = graph[node[2]][1]
    for i in range(6):
      if code1[i] != code2[i]:
        distance += 1
    weight += distance
  print("Graph weight: ",weight)
  n1 = input("Node:       ")
  if len(n1) == 0:
    break
  n2 = input("New parent: ")
  i1 = 0; i2 = 0
  for i in range(len(graph)):
    if graph[i][0] == n1:
      i1 = i
    if graph[i][0] == n2:
      i2 = i
  if (i1==0 | i1==i2):
    print("Invalid node!")
  else:
    i3 = graph[i1][2]
    graph[i3][3].remove(i1)
    graph[i1][2] = i2
    graph[i2][3] += [i1]
f.close()