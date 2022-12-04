#!/bin/python
import csv
import math

# PROBLEM 2
# adjMatrix = []
# with open("numpaths_82.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     vertex = 0
#     for row in csvreader:
#         list = row.split(',')
#         for v in list:
#             if v == "blank":
#                 adjMatrix[vertex][v] = None
#             else:
#                 adjMatrix[vertex][v] = v

# PROBLEM 3
# socks = []
# threshold = 0.25
# pairs = 0
# with open("socks_82.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         try:
#             socks.append(float(row[0]))
#         except ValueError:
#             continue
 
# socks.sort()
# print(socks)
# i = 0
# while i < len(socks)-1:
#     if abs(socks[i] - socks[i+1]) <= threshold:
#         print("pair", socks[i], socks[i+1])
#         pairs = pairs + 1
#         i = i + 2
#         continue
#     elif abs(socks[i] - socks[i+1]) > threshold:
#         i = i + 1
#         continue

# print(pairs)

# PROBLEM 4

lamps = []
with open("streetlamps.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[0] == "s_i":
            continue
        else:
            lamp = (int(row[0]), int(row[1]), int(row[2]))
            lamps.append(lamp)

l = [[0] * 2000] * (len(lamps))
for i in range(len(lamps)):
    l[i][0] = 0
for j in range(2000):
    l[0][j] = 2**31

print(l[5][0])

for i in range(1, len(lamps)-1):
    for j in range(1, 1999):
        if lamps[i][1] < j:
            l[i][j] = 2**31
        if lamps[i][0] > j:
            l[i][j] = l[i-1][j]
        l[i][j] = min(l[i-1][j], lamps[i][2] + l[i-1][lamps[i][0]-1])
# sorted(lamps, key=lambda lamp: lamp[2])
print(l[len(l)-1][len(l[0])-1])
