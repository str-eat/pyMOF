import numpy as np
import pandas as pd
import os

class Crystal():
    def __init__(self):
        name = ""
        group = ""
        cell = []
        self.node = []
        self.edge = []
        self.edgeCenter = [] 
    
    def setName(self, input):
        self.name = input
        
    def setGroup(self, input):
        self.group = input
    
    def setCell(self, input):
        self.cell = input
        
    def appendNodeArray(self, input):
        self.node.append(input) 
    
    def appendEdgeArray(self, input):
        self.edge.append(input)
        
    def appendEdgeCenterArray(self, input):
        self.edgeCenter.append(input)
     

filename = os.path.join(os.getcwd(), '..\\datasets\\RCSRnets.txt')

def buildCrystalAttributeArray(attributeName, attributeArray, lineName):
    entry = ""
    for character in lineName[len(attributeName) + 3 : ]:
        if character is not " ":
            if character is "\n":
                attributeArray.append(entry)
                continue           
            entry = entry + character
        elif entry is not "":
            attributeArray.append(entry)
            entry = ""
    return attributeArray

crystalArray = []
numberCrystals = 0

with open(filename, mode='r') as file:
    for line in file:
        if "CRYSTAL" in line:
            crystal = Crystal()  
                             
        elif "NAME" in line:
            name = line[7:-1]
            crystal.setName(name)
            
        elif "GROUP" in line:
            group = line[8:-1]
            crystal.setGroup(group)
            
        elif "CELL" in line:
            cellArray = []
            cellArray = buildCrystalAttributeArray("CELL", cellArray, line)
            crystal.setCell(cellArray)
            
        elif "NODE" in line:
            nodeArray = []
            nodeArray = buildCrystalAttributeArray("NODE", nodeArray, line)
            crystal.appendNodeArray(nodeArray)
            
        elif "EDGE_CENTER" in line:
            edgeCenterArray = []
            edgeCenterArray = buildCrystalAttributeArray("EDGE_CENTER", edgeCenterArray, line)
            crystal.appendEdgeCenterArray(edgeCenterArray)
            
        elif "EDGE" in line:
            edgeArray = []
            edgeArray = buildCrystalAttributeArray("EDGE", edgeArray, line)
            crystal.appendEdgeArray(edgeArray)
            
        
            
        elif "END" in line:
            crystalArray.append(crystal)
            
print(crystalArray[18].name)
print(crystalArray[18].group)
print(crystalArray[18].cell)
print(crystalArray[18].node)
print(crystalArray[18].edge)
print(crystalArray[18].edgeCenter)