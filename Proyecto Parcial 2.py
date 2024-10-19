#!/usr/bin/python
# -*- coding: latin-1 -*-

# David Isaac Mijares Meza (32948)
# Steven Alexander McClellan Castro (37622)

import sys 

class Node:
    def __init__(self, val): # Un nodo tiene un valor y apunta al siguiente nodo
        self.val = val    
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None
        self.weight = 0 
        
    def empty(self): 
        if self.root == None:
            return True
        else: 
            return False
    
    def insert_left_node(self, val, prev_val): # Funcion para meter un valor a la derecha
        new_node = Node(val)
        if self.empty() == True: # Si el arbol esta vacio
            self.root = new_node # El nuevo nodo se vuelve en la raiz
            new_node.is_root = True # El nuevo nodo se vuelve la raiz
        else:
            prev_node = self.find_previous(prev_val, self.root) # Se obtiene el nodo anterior al que se va a agregar
            prev_node.left = new_node # Se agrega el nuevo nodo a la izquierda
        check = self.check_binary_tree(self.root, val) # Se revisa si el arbol esta correcto
        if check == "Incorrect": 
            print(check)
            sys.exit() # Detiene el programa
        self.weight += 1 # Se aumenta el peso del Arbol

    def insert_right_node(self, val, prev_val): # Funcion para meter un valor a la derecha
        new_node = Node(val)
        if self.empty() == True: # Si el arbol esta vacio
            self.root = new_node # El nuevo nodo se vuelve en la raiz
            new_node.is_root = True # El nuevo nodo se vuelve la raiz
        else:
            prev_node = self.find_previous(prev_val, self.root)
            prev_node.right = new_node # Agrega el nuevo nodo a la derecha del ultimo nodo agregado
        check = self.check_binary_tree(self.root, val) # Se revisa si el arbol esta correcto
        if check == "Incorrect":
            print(check)
            sys.exit() # Detiene el programa
        self.weight += 1 # Se aumenta el peso del Arbol

    def find_previous(self, val, root): 
        if root is None:# Revisa si el árbol está vacío
            return None
        
        if root.val == val: # Si el nodo padre es la raiz
            # Retorna los hijos si existen
            return root 
        
        # Recorre el subárbol izquierdo
        left = self.find_previous(val, root.left)
        if left != None:
            return left

        # Recorre el subárbol derecho
        right = self.find_previous(val, root.right)
        return right
    
    def check_binary_tree(self, root, val):
        if root is None:  # Caso base: si el nodo es nulo, no se encontro el valor
            return "Incorrect"
        elif root.val == val:  # Si encontramos el nodo con el valor que buscamos
            return "Correct"
        elif root.val > val:  # Si el valor es menor, busca en el subarbol izquierdo
            return self.check_binary_tree(root.left, val)
        else:  # Si el valor es mayor, busca en el subarbol derecho
            return self.check_binary_tree(root.right, val)
        
tree = Binary_Tree()

# Insertar nodos en el arbol
n = int(input("n: "))
while n>=100000:
    n = input("Error numero muy grande ")

tree_vals = []
keys = []

for i in range(0,n):
    nums = str(input(f" Introduce 3 num {i+1}: "))
    l = [int(i) for i in nums.split(' ')] # convertir string a lista de int
    tree_vals.append(l[0]) # Se guarda el primer valor como el valor a integrar al arbol
    
    while l[1]<-1 or l[1]>=n:  # Poner concidion para que los keys no excedan n y no sean menor a  -1
        l[1] = int(input("Error el indice izquierdo ingresado no entra dentro de los valores establecidos: "))
    keys.append(l[1]) # Se guarda el indice de lo que va a la izquierda en una lista 
    
    while l[2]<-1 or l[2]>= n:  # Poner concidion para que los keys no excedan n y no sean menor a  -1
        l[2] = int(input("Error el indice derecho ingresado no entra dentro de los valores establecidos: "))
    keys.append(l[2]) # Se guarda el indice de lo que va a la derecha en la misma lista

print(f"tree_vals: {tree_vals} \n")
print(f"keys: {keys} \n")

tree.insert_left_node(tree_vals[0], 0) # Se agrega el root

j = 0 
i = 0 
while j < len(keys):
    # insertar izquierdo
    if keys[j] != -1: # Si es -1 no se inserta nada
        tree.insert_left_node(tree_vals[keys[j]], tree_vals[i]) # insertar valores de acuerdo a lo establecido 

    #insertar derecho
    if keys[j+1] != -1: # Si es -1 no se inserta nada
        tree.insert_right_node(tree_vals[keys[j+1]], tree_vals[i]) # insertar valores de acuerdo a lo establecido 
    
    # Se aumentan los valores de los indices
    j += 2
    i += 1
print("Correct")