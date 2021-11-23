# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:38:43 2021

@author: GJK
"""

def distance(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    distance = (dx**2 + dy**2)**(1/2)
    return distance

def SSE(clusters, data, centroids):
    SSE = 0
    for i, cluster in enumerate(clusters):
        squaredDistOfCluster = 0
        for instance in cluster:
            squaredDistOfCluster += distance(centroids[i], data[instance])**2
        print(squaredDistOfCluster)
        SSE += squaredDistOfCluster
    return SSE
def printKMCIteration(clusters, nInstances, iteration, distanceTable, centroids):
    print(f'iteration    =  {iteration}')
    print(f'Centroid     =  C1 = {centroids[0]}, C2 = {centroids[1]}, C3 = {centroids[2]}')
    print('instances    = ', ['  A' + str(i+1) + '  ' for i in range(nInstances)] )
    print('C1 distances = ', [f'  {distanceTable[0][i]:2.2f}' for i in range(nInstances)])
    print('C2 distances = ', [f'  {distanceTable[1][i]:2.2f}' for i in range(nInstances)])
    print('C3 distances = ', [f'  {distanceTable[2][i]:2.2f}' for i in range(nInstances)])
    
def iterateKMC(data, centroids, iteration):
    distanceTable = [[0 for _ in range(len(data))] for _ in range(len(centroids))] 
    clusters = [[] for _ in range(len(centroids) )]
    for i, point in enumerate(data):
        cluster = -1
        minSoFar = 999999999999999999999999
        for j, centroid in enumerate(centroids):
            dx = point[0] - centroid[0]
            dy = point[1] - centroid[1]
            dist = (dx**2 + dy**2)**(1/2)
            distanceTable[j][i] = dist
            if dist < minSoFar:
                cluster = j
                minSoFar = dist
        clusters[cluster].append(i)
    new_centroids = []
    for cluster in clusters:
        totalX = 0
        totalY = 0
        for instance in cluster:
            point = data[instance]
            totalX += point[0]
            totalY += point[1]
        mean = (totalX/len(cluster), totalY/len(cluster))
        new_centroids.append(mean)   
    
    printKMCIteration(clusters, len(data), iteration, distanceTable, centroids)
    print(f'iteration {iteration+1} centroids = C1 = {new_centroids[0]}, C2 = {new_centroids[1]}, C3 = {new_centroids[2]}\n')
    
    for i, new_centroid in enumerate(new_centroids):
        centroids[i] = new_centroid 
    
    return clusters
data = [(2,10), (2,5), (8,4), (5,8), (7,5), (6,4), (1,2), (4,9)]
centroids = [(2,10), (5, 8), (1,2)]

iterateKMC(data, centroids, 1)
iterateKMC(data, centroids, 2)
iterateKMC(data, centroids, 3)
final_clusters = iterateKMC(data, centroids, 4)
print(SSE(final_clusters, data, centroids) )
