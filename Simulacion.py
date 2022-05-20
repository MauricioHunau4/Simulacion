import numpy as np

#Variables para fila y columnas, la matriz es cuadrada (igual filas que columnas)
print("Filas: ")
n=int(input())
print("Columnas: ")
m=int(input())

#Variable alfa, la cual queda al despejar la ecuación de difusividad
print("phi en fracción: ")
phi=float(input()) #porosidad en fracción
print("mu en cP: ")
mu=float(input()) #viscosidad en cP
print("ct en 1/psi: ")
ct=float(input()) #compresibilidad total (fluido + formación)
print("perm en mD: ")
perm=float(input()) #permeabilidad de la roca
print("dx en m: ")
dx=float(input()) #diferencial de posición en el eje x
print("dt en s: ")
dt=float(input()) #diferencial de tiempo
num=(phi*mu*pow(10,-3)*ct*pow(dx,2))
print(num) #numerador
den=(perm*9.87*pow(10,-16)*dt*6894.75729)
print(den) #denominador
a=num/den 
print(a)

#funcion para crear la matriz tridiagonal
def creaMatriz (fil, col):
    t=(1+a)
    l=-1
    h=0
    w=1
    x=-1
    y=(2+a)
    f=-1; c=-1
    efil=[]
    for f in range (fil):
        ecol=[]
        f+=1
        for c in range (col):
            if(fil == f):
                if(c==l):
                    ecol.append(x)
                elif(c==h):
                    ecol.append(t)
                else:
                    ecol.append(0)
            else:
                if (c==0 and f==1):
                    u=1
                    ecol.append(u)
                    c+=1
                elif (c != 0 and f==1):
                    u=0
                    ecol.append(u)
                    c+=1
                elif(c==l):
                    ecol.append(x)
                elif(c==h):
                    ecol.append(y)
                elif(c==w):
                    ecol.append(x)
                else:
                    ecol.append(0)
        l+=1
        h+=1
        w+=1
        efil.append(ecol)
        matri=np.array(efil,float)
    print("Matriz tridiagonal")
    print (matri)
    return matri

#para invertir la matriz
def invertirMatriz(matriz):
    inversa = np.linalg.inv(matriz)
    print("Matriz inversa")
    print(inversa)
    return inversa


#para crear la matriz B
def matrizB (BHP, PI, fil):
    f=-1
    efil=[]
    for f in range(fil):
        if(f == 0):
            efil.append(BHP)
        else:
            efil.append(PI)
        f+=1
        matriza=np.array(efil,float)
    print("Matriz B")
    print(matriza)
    return matriza

#Variables para BHP (bottom hole pressure) y PI (presión inicial en la formación) en matriz B
print("BHP en MPa: ")
MBHP = int(input())
BHP = MBHP * pow(10,6)
print("PI en MPa: ")
MPI = int(input())
PI = MPI * pow(10,6)

#crear Matriz A
def matrizA(fil, col, a):
    l=0
    f=-1; c=-1
    efil=[]
    x=a
    for f in range (fil):
        ecol=[]
        f+=1
        for c in range (col):
            if (c==0 and f==1):
                u=1
                ecol.append(u)
                c+=1
            elif (c != 0 and f==1):
                u=0
                ecol.append(u)
                c+=1
            elif(c==l):
                ecol.append(x)
            else:
                ecol.append(0)
        l+=1
        efil.append(ecol)
        matri=np.array(efil,float)
    print("Matriz A")
    print (matri)
    return matri

matrizA(m,n,a)

#multiplicaciones de matrices
O = np.dot(invertirMatriz(creaMatriz(n,m)), matrizA(m,n,a))
I = np.dot(O, matrizB(BHP, PI, n))

print("Multiplicacion de la inverza de matriz tridiagonal y matriz A")
print(O)
print("Multiplicacion de Matriz B y de la multiplicacion de la inverza de matriz tridiagonal y matriz A")
print(I.tolist())

#el loop que quieras ponerle
print("nº loop: ")
g=int(input())
for i in range(g):
    final = np.dot(O, I)
    print(final.tolist())
    I = final
