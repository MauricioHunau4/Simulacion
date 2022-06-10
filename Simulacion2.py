import numpy as np

#Variables para fila y columnas
print("Filas: ")
n=int(input())
print("Columnas: ")
m=int(input())

#Variable alfa
print("phi en fracción: ")
phi=float(input())
print("muo en cP: ")
muo=float(input())
print("muw en cP: ")
muw=float(input())
print("ct en 1/psi: ")
co=float(input())
print("co en 1/psi: ")
ct=float(input())
print("perm en mD: ")
perm=float(input())
print("dx en m: ")
dx=float(input())
print("dy en m: ")
dy=float(input())
print("dz en m: ")
dz=float(input())
print("dt en s: ")
dt=float(input())
print("Boi adim: ")
Boi=float(input())
print("Bwi adim: ")
Bwi=float(input())
Swi=float(input("Sw inicial = "))
Soi=1-Swi
print("So inicial =", Soi)
kromax=float(input("kromax = "))
krwmax=float(input("krwmax = "))
no=float(input("no = "))
nw=float(input("nw = "))
Swc=float(input("Swc = "))
Sor=float(input("Sor = "))
Vpi=dx*dz*dy*phi
kro=kromax*((1-Swi-Sor)/(1-Sor-Swc))^no
krw=krwmax*((Swi-Swc)/(1-Sor-Swc))^nw
ao=kro*perm*dz*dy/(Boi*muo*dx)
aw=krw*perm*dz*dy/(Bwi*muw*dx)

#funcion para crear la matriz tridiagonal
def creaMatriz (fil, col):
    t=1
    l=-1
    h=0
    w=1
    x=1#modificar
    y=(2+a)#modificar
    f=-1; c=-1
    efil=[]
    k = 11
    o = 9
    i = 10
    for f in range (fil):
        ecol=[]
        f+=1
        for c in range (col):
            if(fil == f):
                if(c==h):
                    ecol.append(t)
                else:
                    ecol.append(0)
            else:
                if (c==0 and f==1):
                    u=1
                    ecol.append(u)
                    c+=1
                elif(f==k and c==o):
                    ecol.append(0)
                    k+=10
                    o+=10
                elif(f==i and c==i):
                    ecol.append(0)
                    i+=10
                elif (c != 0 and f==1):
                    u=0
                    ecol.append(u)
                    c+=1
                elif(c==l):
                    ecol.append(x)
                elif(c==h):
                    ecol.append(y)
                elif(c== z):
                    ecol.append(5)#otra variable y modificar
                elif(c==ñ):
                    ecol.append(5)#otra variable y modificar
                elif(c==w):
                    ecol.append(x)
                else:
                    ecol.append(0)
        l+=1
        h+=1
        w+=1
        z = h + 10
        ñ = h - 10
       
        efil.append(ecol)
        matri=np.array(efil,int)
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

#Variables para BHP y PI en matriz B
print("BHP en MPa: ")
MBHP = int(input())
BHP = MBHP * pow(10,6)
print("PI en MPa: ")
MPI = int(input())
PI = MPI * pow(10,6)
print("PBHP en MPa: ")
MPBHP = int(input())
PBHP = MPBHP * pow(10,6)

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

#para centros#
centro=Bo*(ao1+ao1+ao2+ao3)+Bw*(aw1+aw1+aw2+aw3)+(Vp*ct/dt)
sur=(Bo*ao1+Bw*aw1)
norte=(Bo*ao2+Bw*aw2)
este=(Bo*ao1+Bw*aw1)
oeste=(Bo*ao3+Bw*aw3)

#para bordes superiores#
centro=Bo*(ao1+ao1+ao2+ao3)+Bw*(aw1+aw1+aw2+aw3)+(Vp*ct/dt)-(Bo*ao2+Bw*aw2)
sur=(Bo*ao1+Bw*aw1)
este=(Bo*ao1+Bw*aw1)
oeste=(Bo*ao3+Bw*aw3)

#para bordes inferiores#
centro=Bo*(ao1+ao1+ao2+ao3)+Bw*(aw1+aw1+aw2+aw3)+(Vp*ct/dt)-(Bo*ao1+Bw*aw1)
norte=(Bo*ao2+Bw*aw2)
este=(Bo*ao1+Bw*aw1)
oeste=(Bo*ao3+Bw*aw3)

#para esquinas superiores#
centro=Bo*(ao1+ao1+ao2+ao3)+Bw*(aw1+aw1+aw2+aw3)+(Vp*ct/dt)-(Bo*ao1+Bw*aw1)-(Bo*ao2+Bw*aw2)
sur=(Bo*ao1+Bw*aw1)
oeste=(Bo*ao3+Bw*aw3)

#para esquinas inferiores#
centro=Bo*(ao1+ao1+ao2+ao3)+Bw*(aw1+aw1+aw2+aw3)+(Vp*ct/dt)-(Bo*ao3+Bw*aw3)-(Bo*ao1+Bw*aw1)
norte=(Bo*ao2+Bw*aw2)
este=(Bo*ao1+Bw*aw1)

pf=0.0
pp=0.0
Bo=Boi*(1-co*(pf-pp))
Vp=Vpi*(1-cf*(pf-pp))

So=(Bo/Vp)*(dt*(ao1*(pf1-pf)+ao2*(pf2-pf)+ao3*(pf3-pf)+ao4*(pf4-pf))+(Vpi*Soi/Boi))
Sw=(Bw/Vp)*(dt*(aw1*(pf1-pf)+aw2*(pf2-pf)+aw3*(pf3-pf)+aw4*(pf4-pf))+(Vpi*Swi/Bwi))

Qoprod=ao1*(pf2-PBHP)+ao1*(pf11-PBHP)-(1/dt)*((Vp*So/Bo)-(Vpi*Soi/Boi))
Qwprod=aw1*(pf2-PBHP)+aw1*(pf11-PBHP)-(1/dt)*((Vp*Sw/Bw)-(Vpi*Swi/Bwi))

Qwiny=aw1*(pf2-PBHP)+aw1*(pf11-PBHP)-(1/dt)*((Vp*Sw/Bw)-(Vpi*Swi/Bwi))
