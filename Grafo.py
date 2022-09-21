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

colores_dict = {0:'pink', 1: 'blue', 2: 'green', 3:'red',4: 'orange',5: 'yellow'}
colores = []

for nodo in lista_nodos:
#Se agregan todos los municipios
    G.add_node(nodo)

for municipio in lista_municipios:
    i = 1
    while i < len(municipio):
        if municipio[i] == 1:
            G.add_edge(municipio[0],lista_nodos[i-1])
        i += 1
        
def coloreado_voraz(grafo):
    colores = {}
    nodos = grafo.nodes()
    for u in nodos:
        colores_vecinos = {colores[v] for v in grafo[u] if v in colores}
        for color in itertools.count():
            if color not in colores_vecinos:
                break
        colores[u] = color
    return colores

coloreado = coloreado_voraz(G)


for i,j in coloreado.items():
    colores.append(colores_dict[coloreado[i]])

pink = 0 #0
blue = 0 #1
green = 0 #2 
red = 0 #3
orange = 0 #4
yellow = 0 #5

for tonos in coloreado.values():
    
    if tonos == 0:
        pink += 1
    elif tonos == 1:
        blue += 1
    elif tonos == 2:
        green += 1
    elif tonos == 3:
        red += 1
    elif tonos == 4:
        orange += 1
    elif tonos == 5:
        yellow += 1


print (f"rosado: {pink}\nazul: {blue}\ngris: {green}\nrojo: {red}\nnaranja: {orange}\namarrillo: {yellow}")
print ("\nTotal : ",pink+blue+green+red+orange+yellow)                   
            

    
nx.draw(G,node_size=30, width=0.9,node_color = colores,font_weight="bold",with_labels = False)
plt.axis("off")
plt.show()


file = open("datos.txt","w")
num = 1
for i,j in coloreado.items():
    name_nodo = i
    color_nodo = colores_dict[coloreado[i]]
    file.write("\n")
    file.write("% s"%num)
    file.write(" - ")
    file.write(name_nodo)
    file.write(" - ")
    file.write(color_nodo)
    num += 1

file.close()



