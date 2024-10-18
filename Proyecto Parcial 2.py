#!/usr/bin/python
# -*- coding: latin-1 -*-

# David Isaac Mijares Meza (32948)
# Steven Alexander McClellan Castro (37622)

class Node:
    def __init__(self, val): # Un nodo tiene un valor y apunta al siguiente nodo
        self.val = val    
        self.left = None
        self.right = None
        self.parent = None
        
        self.is_right = False
        self.is_left = False
        self.is_root = False
        
class Binary_Tree:
    def __init__(self):
        self.root = None
        self.weight = 0 
        
    def empty(self): 
        if self.root == None:
            return True
        else: 
            return False
    
    def insert_node(self, val): 
        new_node = Node(val)
        if self.empty() == True: # Si el arbol esta vacio
            self.root = new_node # El nuevo nodo se vuelve en la raiz
            new_node.is_root = True # El nuevo nodo se vuelve la raiz
        else:
            parent, side = self.position(val)
            if side == "Izquierdo":
                parent.left = new_node
                new_node.is_left = True
                new_node.parent = parent
                
            else:
                parent.right = new_node
                new_node.is_right = True
                new_node.parent = parent               
                
        self.weight += 1 # Se aumenta el peso del Arbol
        
    def position(self, val): 
        aux = self.root
        
        while aux: 
            prev_aux = aux
            if val <= prev_aux.val: 
                aux = aux.left 
                lado = "Izquierdo"
                
            else:
                aux = aux.right
                lado = "Derecho"
        return prev_aux, lado
         
    def in_order(self, root):
        if root:
            self.in_order(root.left)  # Recorre el sub�rbol izquierdo
            print(root.val, end=" ")  # Imprime el valor del nodo actual
            self.in_order(root.right)  # Recorre el sub�rbol derecho
           
    def pos_order(self, root):
        if root:
            self.pos_order(root.left)  # Recorre el sub�rbol izquierdo
            self.pos_order(root.right)  # Recorre el sub�rbol derecho
            print(root.val, end=" ")  # Imprime el valor del nodo actual
           
    def pre_order(self, root):
        if root:
            print(root.val, end=" ")  # Imprime el valor del nodo actual
            self.pre_order(root.left)  # Recorre el sub�rbol izquierdo
            self.pre_order(root.right)  # Recorre el sub�rbol derecho
            
    def search(self, root, val):
        if root is None:  # Caso base: si el nodo es nulo, no se encontr� el valor
            return None
        elif root.val == val:  # Si encontramos el nodo con el valor que buscamos
            return root
        elif root.val > val:  # Si el valor es menor, busca en el sub�rbol izquierdo
            return self.search(root.left, val)
        else:  # Si el valor es mayor, busca en el sub�rbol derecho
            return self.search(root.right, val)
        
            
    def erase_node(self, val):
        if self.empty() == True: # Revisa si el arbol no esta vacio
            print("El arbol esta vacio")
        else:
            erase = self.search(self.root, val) # Da la posicion del nodo que se quiere borrar
            if self.weight == 1: # Checar si unicamente hay un valor en todo el arbol usando el peso
                self.root = None
                self.weight = 0
            num_branches = self.count_branches(erase) # Funcion para saber numero de hijos
            
            if num_branches == 0: # Si el nodo no tiene hijos
                if erase.is_left == True:
                    erase.parent.left = None
                else:
                    erase.parent.right = None
                self.weight -= 1
                

            elif num_branches == 1:# Si el nodo tiene 1 hijo
                if erase.is_root == True: # Si el nodo a borrar es la raiz
                    self.root = erase.left or erase.right # La raiz se actualiza al hijo de erase
                    self.root.parent = None # Se le borra el apuntador del papa a la nueva raiz

                elif erase.is_left == True: # Revisar si el nodo a borrar es izquierdo
                    erase.parent.left = erase.left or erase.right # Toma el valor del hijo de la variable que se va a borrar (erase)
                    erase.parent.left.parent = erase.parent # El papa del hijo de erase se vuelve el padre de erase 
                    erase.parent.left.is_left = True # Se defineel hijo de erase como variable izquierda al tomar el lugar de su papa
                    erase.parent.left.is_right = False
                    self.weight -= 1 # Se reduce el peso del arbol
                    
                elif erase.is_right == True: # Revisar si el nodo a borrar es derecho
                    erase.parent.right = erase.left or erase.right 
                    erase.parent.right.parent = erase.parent 
                    erase.parent.right.is_left = False
                    erase.parent.right.is_right = True
                    self.weight -= 1        
                    

            else: # Si el nodo tiene 2 hijos
                succesor = self.succesor(erase)
                self.erase_node(succesor.val) #Se borra la variable sucesora
                erase.val = succesor.val # Se actualiza el valor de la variable que se queria borrar al valor de la variable sucesora

    def count_branches(self, root): # Funcion para saber numero de hijos
        count = 0
        if root.left != None:
            count += 1
        if root.right != None:
            count += 1
        return count
    
    def succesor(self, erase): # Busca el valor del subarbol derecho que hasta la izquierda 
        temp = erase.right  
        while temp.left:
            temp = temp.left
        return temp 
        
tree = Binary_Tree()

# Insertar nodos en el arbol
n = int(input())
while n>=100000:
    n = input("Error numero muy grande ")

nums = []
for i in range(n):
    # Capturar Numero   indice Izquierdo    Indice Derecha 
    #nums[i] = str(input())
    pass

# 1 2 3
# keys -1 <= key <= n

# Preguntar como insertar los datos
# Preguntar sobe las condicionales 



# nums = str(input("Introduce primero la cantidad de numeros que tendra tu lista y despues escribe los numeros de la lista \n (todo separado por espacio): "))
# lista = []
# l = [int(i) for i in nums.split(' ')] # convertir string a lista de int
# for j in range(len(l)):
#     if j == 0:
#         pass
#     else:
#         lista.append(l[j])
