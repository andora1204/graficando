import csv
import matplotlib.pyplot as plt

def lector_csv(paquete):
	with open(paquete, 'r') as archivo_csv:
		leyendo = csv.reader(archivo_csv, delimiter=',')
		#con el metodo next obtenemos solo el encabezado
		encabezado = next(leyendo)
		lista = []
		
		for filas in leyendo:
			#creamos tuplas del encabezado con las filas usando zip
			union_encabez_filas = zip(encabezado, filas)
			#print (list(union_encabez_filas))
			#crea una lista de tuplas (encabezado,items) con el print de arriba se puede verificar
			diccionario_comprehesions = {key:value for key, value in union_encabez_filas}
			#print(diccionario_comprehesions)
			#ok ahora cada fila es un diccionario con (clave:valor), necsitamos incluirlo en una lista
			
			lista.append(diccionario_comprehesions)
		return (lista)
		
		

def genera_graf_barra(x,y):
	
	fig, ax = plt.subplots()

	ax.bar(x, y)

	plt.savefig(f'./imgs/{pais_grafica}_bar.png')

	plt.close()

def genera_pie_grafica(labels,values):

	fig, ax = plt.subplots()

	ax.pie(values, labels=labels)

	ax.axis('equal')

	plt.savefig(f'./imgs/{pais_grafica}_pie.png')			

	plt.close()

	
	

	

if __name__ == '__main__':
	data = lector_csv('./data.csv')
	usuario = input('nombre pais=> ')
	pais_grafica = usuario

	for i in data:
		if i['Country/Territory'] == usuario:
			poblacion_1970 = i['1970 Population']
			poblacion_1980 = i['1980 Population']
			poblacion_1990 = i['1990 Population']
			poblacion_2000 = i['2000 Population']
			poblacion_2010 = i['2010 Population']
			poblacion_2015 = i['2015 Population']
			poblacion_2020 = i['2020 Population']
			poblacion_2022 = i['2022 Population']
			
	encabezado =['poblacion_1970','poblacion_1980', 'poblacion_1990', 'poblacion_2000', 'poblacion_2010', 'poblacion_2015', 'poblacion_2020', 'poblacion_2022']
	
	habitantes = []
	habitantes.append(int(poblacion_1970))
	habitantes.append(int(poblacion_1980))
	habitantes.append(int(poblacion_1990))
	habitantes.append(int(poblacion_2000))
	habitantes.append(int(poblacion_2010))
	habitantes.append(int(poblacion_2015))
	habitantes.append(int(poblacion_2020))
	habitantes.append(int(poblacion_2022))

	genera_graf_barra(encabezado,habitantes)

	genera_pie_grafica(encabezado, habitantes)
	
	


	
