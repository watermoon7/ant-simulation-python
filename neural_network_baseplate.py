'''
Created on 7 Sept 2022

@author: coding
'''
import numpy as np
import random

class neural_network():
    
    def __init__(self, numInputNodes, numHiddenLayers, numHiddenNodes, numOutputNodes, bias = 2):
        
        self.inputNodes = numInputNodes
        self.hiddenLayers = numHiddenLayers
        self.hiddenNodes = numHiddenNodes
        self.outputNodes = numOutputNodes
        
        self.bias = bias        
        
        self.inputNodes = [random.randint(1, 100)/100 for x in range(self.inputNodes)]
        self.outputWeights = [random.randint(1, 1000)/100 for x in range(self.outputNodes)]
        
        self.weights = {}
        
        for i in range(1, self.hiddenLayers+1):
            layerName = f'weights{i}'
            '''
            setattr(self, layerName, [])
            for o in range(self.hiddenNodes):
                vars(self)[layerName].append(random.randint(1, 1000)/100)
            '''
            e = []
            for o in range(self.hiddenNodes):
                e.append(random.randint(1, 1000)/100)
            self.weights[layerName] = e
        
    
nn1 = neural_network(5, 4, 12, 4)
print('end:')
print(vars(nn1))

