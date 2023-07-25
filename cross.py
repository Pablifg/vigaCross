import numpy as np
import matplotlib.pyplot as plt
<<<<<<< HEAD
from interaccion_usuario import entrada_datos
##### INTRODUCCIÓN DE DATOS AL PROGRAMA #######
	#tramos en metros, cargas en KN/m positivas hacia abajo, Rigideces en KNm2


#longTramos = np.array([2, 4, 4, 5, 5, 5, 5])
#cargasTramos = np.array([10, 10, 10, 10, 10, 10, 10])
#rigidecesTramos = np.array([1, 1, 1, 1, 1, 1, 1])
#apoyoIzq = "empotrado"
#apoyoDer = "empotrado"

entrada_por_consola = entrada_datos()
longTramos = np.array(entrada_por_consola["longTramos"])
cargasTramos = np.array(entrada_por_consola["cargasTramos"])
rigidecesTramos = np.array(entrada_por_consola["rigidecesTramos"])
apoyoIzq = entrada_por_consola["apoyoIzq"]
apoyoDer = entrada_por_consola["apoyoDer"]
noTramos = entrada_por_consola["noTramos"]
=======
import re


def calcular(longTramos:int, rigidecesTramos:float, apoyoIzq:str, apoyoDer:str):
	"""_summary_

	Args:
		longTramos (int): _description_
		rigidecesTramos (float): _description_
		apoyoIzq (str): _description_
		apoyoDer (str): _description_
>>>>>>> be74cab (First change)

	Returns:
		_type_: _description_
	"""    
	##### CÁLCULO DE DISTRIBUCIÓN DE MOMENTOS #######
	noTramos = longTramos.size
	print("número de tramos = ", noTramos)

<<<<<<< HEAD

print("número de tramos = ", noTramos)

factDist = np.zeros(noTramos*2)
=======
	factDist = np.zeros(noTramos*2)
>>>>>>> be74cab (First change)


	if apoyoIzq == "empotrado":
		factDist[0] = 0
	elif apoyoIzq == "articulado":
		factDist[0] = 1

	if apoyoDer == "empotrado":
		factDist[noTramos*2-1] = 0
	elif apoyoDer == "articulado":
		factDist[noTramos*2-1] = 1

	for i in range(1,noTramos,1):
		Lizq = longTramos[i-1]
		Lder = longTramos[i]
		EIizq = rigidecesTramos[i-1]
		EIder = rigidecesTramos[i]
		factDist[i*2-1] = (EIizq/Lizq)/(EIizq/Lizq+EIder/Lder)
		factDist[i*2] = (EIder/Lder)/(EIizq/Lizq+EIder/Lder)


	cargaEq = np.zeros(noTramos*2)


	for i in range(noTramos):
		q = cargasTramos[i]
		L = longTramos[i]
		cargaEq[i*2]= q*L**2/12
		cargaEq[i*2+1]= -q*L**2/12

	matEq = np.zeros((20,noTramos*2))

	for i in range(noTramos*2):
		MEP = cargaEq[i]
		matEq[0,i]= MEP

	for i in range(19): #numero de iteraciones
		for j in range(noTramos*2):
			if j == 0:
				Mdes = matEq[i,j]
				Meq = Mdes*factDist[j]*-1
				matEq[i,j+1] += Meq/2	
				matEq[i,j] = Mdes+Meq
			elif j == noTramos*2-1:
				Mdes = matEq[i,j]
				Meq = Mdes*factDist[j]*-1
				matEq[i+1,j-1] = Meq/2
				matEq[i,j] = Mdes+Meq
			else:

				if (j%2)==1: #casilla impar
					aux = matEq[i,j]
					Mdes = matEq[i,j]+matEq[i,j+1]
					Meq = Mdes*factDist[j]*-1
					matEq[i+1,j-1] = Meq/2
					matEq[i,j] += Meq

				else: #casilla par
					Mdes = aux + matEq[i,j]
					Meq = Mdes*factDist[j]*-1
					matEq[i,j+1] += Meq/2
					matEq[i,j] += Meq

	#print(matEq)
	Mresultados = np.zeros(noTramos*2)

	for j in range(noTramos*2):
		for i in range(20):
			Mresultados[j] += matEq[i,j]

	#print(Mresultados)
	return noTramos, Mresultados


def plot_result(noTramos:int, longTramos:float, cargasTramos:float, Mresultados:float):
	"""Ploteado de resultados de gráficas

	Args:
		noTramos (int): cantidad de tramos de la estructura
		cargasTramos (float): cargas aplicadas en los tramos
		Mresultados (float): _description_
	
	Return:
		Gráfica ploteada en matplotlib
	"""    
	#####PLOTEADO DE RESULTADOS #######

	paraPlot = np.zeros((noTramos,7))

	for i in range(noTramos):
		if i==0:
			x1 = 0
			x2 = longTramos[0]
			paraPlot[i,0] = x1
			paraPlot[i,1] = x2
		else:
			x1 = paraPlot[i-1,1]
			x2 = x1+longTramos[i]
			paraPlot[i,0] = x1
			paraPlot[i,1] = x2		

		paraPlot[i,2] = cargasTramos[i]
		paraPlot[i,3] = -Mresultados[i*2]
		paraPlot[i,4] = Mresultados[i*2+1]
		M1 = paraPlot[i,3]
		M2 = paraPlot[i,4]
		B = paraPlot[i,2]

		matA = np.array([[x1, 1],[x2, 1]])
		matB = np.array([[M1+B*x1**2/2],[M2+B*x2**2/2]])
		sol = np.linalg.solve(matA,matB)
		C1 = sol[0]
		C2 = sol[1]
		paraPlot[i,5] = np.squeeze(C1)
		paraPlot[i,6] = np.squeeze(C2)

	#print(paraPlot)



	contador = 0
	for i in range(noTramos):
		if i==0:
			x1 = paraPlot[i,0]
			x2 = paraPlot[i,1]
			B = paraPlot[i,2]
			C1 = paraPlot[i,5]
			C2 = paraPlot[i,6]
			xx = np.linspace(x1,x2,20)
			V = -B*xx+C1
			M = -B*xx**2/2+C1*xx+C2
		else:
			xxAnt = xx
			Vant = V
			Mant = M
			x1 = paraPlot[i,0]
			x2 = paraPlot[i,1]
			B = paraPlot[i,2]
			C1 = paraPlot[i,5]
			C2 = paraPlot[i,6]
			xx = np.linspace(x1,x2,20)
			V = -B*xx+C1
			M = -B*xx**2/2+C1*xx+C2		
			xx = np.append(xxAnt,xx)
			V = np.append(Vant,V)
			M = np.append(Mant,M)

	plt.subplot(2,1,1)
	plt.plot(xx,V)
	plt.subplot(2,1,2)
	plt.plot(xx,M)

	plt.show()


def main(longTramos:int, cargasTramos:float, rigidecesTramos:float, apoyoIzq:str, apoyoDer:str):

	noTramos, Mresultados = calcular(longTramos, rigidecesTramos, apoyoIzq, apoyoDer)

	plot_result(noTramos, longTramos, cargasTramos, Mresultados)


if __name__ == '__main__':
	##### INTRODUCCIÓN DE DATOS AL PROGRAMA #######
	#tramos en metros, cargas en KN/m positivas hacia abajo, Rigideces en KNm2
	with open("./input/entrada.txt", "r") as f:
		# Leer el contenido del archivo
		datos = f.read().splitlines()
		datos = list(filter(None, datos))
		#print(datos.split(":"))

		longitudTramos = []
		cargasTramos = []
		rigidecesTramos = []

		dicc = {}

		for linea in datos:
			nombre = linea.split(":")[0]
			next(datos)
		# 	nombre, valor = linea.split(":")
		# 	dicc[nombre] = valor.strip()
		# 	print(dicc)
		# 	break
			# nombre, valor = linea.split(":")
			# print("nombre: ", nombre)
			# print("valor: ",valor)
		# 	if nombre == "longitudTramos":
		# 		longitudTramos.append(valor)
		# 	elif nombre == "cargasTramos":
		# 		cargasTramos.append(valor)
		# 	elif nombre == "rigidecesTramos":
		# 		rigidecesTramos.append(valor)

		

	# longTramos = np.array(longitudTramos)
	# cargasTramos = np.array(cargasTramos)
	# rigidecesTramos = np.array(rigidecesTramos)

	apoyoIzq = "empotrado"
	apoyoDer = "empotrado"

	
	#main(longTramos, cargasTramos, rigidecesTramos, apoyoIzq, apoyoDer)
