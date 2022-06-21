""" Codigo de Jose Manuel Pedro Mendez, 315073120 correspondiente a la practica 01 Adoquinamiento"""
import pandas as pd
import numpy as np
import random
import sys
import re
import math 

""" Funciones auxiliares que nos permitiran cumplir una de nuestras condiciones(precondiciones),
    es decir, que m sea potencia de 2 """
def Log2(x):
    return (math.log10(x) / math.log10(2));

def esPotenciaDos(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));

class Paving:
    """ Clase que nos permite representar el Adoquinamiento"""

    def __init__(self,cuadricula, count):
        """ Funcion que nos permite crear una instancia de nuestra clase
    
        Args: cuadricula mxm donde m es potencia de 2 (cuadricula)
        contador que nos permite representar las etiquetas que diferencian nuestros adoquines en forma de L

        Returns: Nothing
    
        """
        self.cuadricula = cuadricula
        self.count = count

    def cobblestone(self, tupla1,tupla2,tupla3):
        """ Funcion que coloca los adoquines en forma de L
    
        Args: tuplas donde pondremos 

        Returns: Nothing
    
        """
        x1,y1=tupla1
        x2,y2=tupla2
        x3,y3=tupla3
        self.count = self.count+1
        self.cuadricula[x1][y1]=self.count
        self.cuadricula[x2][y2]=self.count
        self.cuadricula[x3][y3]=self.count
        print(pd.DataFrame(self.cuadricula))

    #def pavingAlgorithm(num, x(columnas),y(filas)):
    def pavingAlgorithm(self,num,column,rows):
        auxA=0
        auxB=0
        """ Casos base, con n=1 -> 1x1"""
        if (num==1):
            print(pd.DataFrame(self.cuadricula))
            return #Aunque no regresamos nada, esto nos permitira terminar la ejecucion

        """ Casos base, con n=2 -> 2x2"""
        if (num ==2):
            self.count = self.count+1
            for numC in range(num):
                for numR in range(num):
                    if (self.cuadricula[column+numC][rows+numR])==0:
                        self.cuadricula[column+numC][rows+numR] =self.count
            print(pd.DataFrame(self.cuadricula))
            return #Aunque no regresamos nada, esto nos permitira terminar la ejecucion

        """Recorrido para buscar lugares disponibles, es decir, que no sean 0, 
        recordemos que nuestro arreglo al inicio esta corformado por puros 0,
        Y por cada ejecucion vamos cambiando estos por los representadores de 
        nuestros adoquines en L(count)"""
        for numC in range(column,num+column):
            for numR in range(rows,num+rows):
                if (self.cuadricula[numC][numR] != 0):
                    auxA = numC
                    auxB = numR

        """ Subregiones donde podemos encontrar el cuadro especial """
        # Subregion (x,y)
        if (auxA < column+int(num/2) and auxB >= rows+int(num/2)):
            x1=column+int(num/2)
            y1=rows+int(num/2)-1
            x2=column+int(num/2)
            y2=rows+int(num/2)
            x3=column+int(num/2)-1
            y3=rows+int(num/2)-1
            self.cobblestone((x1,y1),(x2,y2),(x3,y3))
        # Subregion (x,-y)
        elif (auxA>=column+int(num/2) and auxB >= rows+int(num/2)):
            x1=column+int(num/2)-1
            y1=rows+int(num/2)
            x2=column+int(num/2)
            y2=rows+int(num/2)-1
            x3=column+int(num/2)-1
            y3=rows+int(num/2)-1
            self.cobblestone((x1,y1),(x2,y2),(x3,y3))

        # Subregion (-x,-y)
        elif (auxA>=column+int(num/2) and auxB < rows+int(num/2)):
            x1=column+int(num/2)-1
            y1=rows+int(num/2)
            x2=column+int(num/2)
            y2=rows+int(num/2)
            x3=column+int(num/2)-1
            y3=rows+int(num/2)-1
            self.cobblestone((x1,y1),(x2,y2),(x3,y3))

        # Subregion (-x,y)
        elif (auxA<column+int(num/2) and auxB < rows+int(num/2)):
            x1=column+int(num/2)
            y1=rows+int(num/2)-1
            x2=column+int(num/2)
            y2=rows+int(num/2)
            x3=column+int(num/2)-1
            y3=rows+int(num/2)
            self.cobblestone((x1,y1),(x2,y2),(x3,y3))

        #Llamadas recursivas para generar las 4 subregiones
        newQ=int(num/2)
        self.pavingAlgorithm(newQ, column+newQ, rows)
        self.pavingAlgorithm(newQ, column, rows+newQ)
        self.pavingAlgorithm(newQ, column, rows)
        self.pavingAlgorithm(newQ, column+newQ, rows+newQ)

def entradaValida():
    """ Funcion que nos permite obtener una entrada valida para la ejecucion de neustro algoritmo """
    args = sys.argv
    if len(args)>2:
        raise ValueError(f"Entrada invalida, python3 solo puede tener 2 parametros, no {len(args)} :D")
    else:
        num_format = re.compile(r'^\-?[1-9][0-9]*$')
        num_pos = args[1]
        num = re.match(num_format, num_pos )
        if num:
            numF = int(num_pos)
            
            if numF<0 or not esPotenciaDos(numF) or numF==1:
                raise ValueError("El segundo parametro, es decir, m debe de ser potencia de 2 y no puede ser negativo")
            else:
                print(f"Trabajareomos con m={numF}, es decir, con un arreglo de {numF}x{numF}")
                return numF
        else:
            raise ValueError(f"El segundo parametro {num_pos} no representa un entero POSITIVO")

#Obtenemos una entrada valida
m= entradaValida()
#print(type(m))

#creamos la cuadricula
cuadricula = np.zeros((m,m))
x_r = random.randint(0,m-1)
y_r = random.randint(0,m-1)

# Asignar el cuadro especial en donde quieras, debi comentar esto? ja, no lo se, ya me estaras diciendo, je
#x_r=0 
#y_r =0

print(f"El cuadro especial random sera: ({x_r},{y_r}) sera representado por un -1.0")
cuadricula[x_r][y_r] =-1
a=cuadricula.shape[0]
play = Paving(cuadricula,0)
play.pavingAlgorithm(a,0,0)
