# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:29:07 2022

@author: emmananuel garay
"""
import openpyxl
import networkx as nx
import matplotlib.pyplot as plt
import itertools


book = openpyxl.load_workbook('antioquia.xlsx',data_only=True) #Leer el archivo
hoja=book.active #Fijar hoja
celdas = hoja['A2' :'DV126'] #Delimitar celdas
lista_municipios = [] #Lista con todos los municipios y sus datos
lista_nodos = [] #Lista con los nombres de los municipios

for fila in celdas: 
#Se recorre las filas del archivo una por una
    municipio = ([celda.value for celda in fila])
    lista_municipios.append(municipio)

for municipio in lista_municipios:
#Se obtiene los nombres de los municipios
    lista_nodos.append(municipio[0])
    
G = nx.Graph()

colores_dict = {0:'pink', 1: 'blue', 2: 'green', 3:'red'}
colores = ["red","blue","green"]

for nodo in lista_nodos:
#Se agregan todos los municipios
    G.add_node(nodo)

for municipio in lista_municipios:
    i = 1
    while i < len(municipio):
        if municipio[i] == 1:
            G.add_edge(municipio[0],lista_nodos[i-1])
        i += 1
        
def coloreado_voraz(grafo,colors):
    for node in G.nodes():
        G.nodes[node]['color'] = 'white' # Color blanco por defecto (NO COLOREADO)

    #Algoritmo principal
    i = 0
    for color in colors:
        if(i == G.number_of_nodes): #Si ya se pintaron todos los nodos terminar el algoritmo 
            break
        for node in G.nodes():
            if (G.nodes[node].get('color') == 'white'):
                flag = True
                for x in G[node]:
                    if (flag == False): #Si un vecino es del mismo color ya no se busca mas
                        break
                    if(G.nodes[x].get('color') == color):
                        flag = False
                if(flag):
                    #Si no se ha pintado aun el nodo y ninguno de sus 
                    #venciones es de color "color", entonces se pinta el nodo
                    G.nodes[node]['color'] = color
                    i += 1
    
    nodeColors = [G.nodes[node].get('color') for node in G.nodes()] 

    nx.draw(G,node_size=30, width=0.9,node_color = nodeColors,with_labels = False)
    plt.axis("off")
    plt.show()  
    return nodeColors

colores_usados=coloreado_voraz(G, colores)

blue = 0 #1
green = 0 #2 
red = 0 #3
white = 0


for tonos in colores_usados:
    
    if tonos == "blue":
        blue += 1
    elif tonos == "green":
        green += 1
    elif tonos == "red":
        red += 1
    elif tonos == "white":
        white += 1

print (f"azul: {blue}\nverde: {green}\nrojo: {red}\nBlanco: {white}")
print ("\nTotal : ",blue+green+red+white)

                    
file = open("datos.txt","w")
num = 1
for i in colores_usados:
    name_nodo = lista_nodos[num-1]
    color_nodo = i
    file.write("\n")
    file.write("% s"%num)
    file.write(" - ")
    file.write(name_nodo)
    file.write(" - ")
    file.write(color_nodo)
    num += 1

file.close()