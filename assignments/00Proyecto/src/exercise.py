def mostrar_datos(matriz_max,matriz_min,n,definicion,simbolo,palabra,palabras):
    print(f'Ordenados en forma descendente los {n} países con la mayor {definicion}:')
    for i in range (n):
        print(f'''{i+1}. {matriz_max[i][0]} con {matriz_max[i][1]} {simbolo} y un GDP de {matriz_max[i][4]}.
        Otros datos: La {definicion} {palabra} es {matriz_max[i][2]} {simbolo}. 
        Por lo tanto, podemos decir: {matriz_max[i][3]} {palabras}''')

    print(f'Ordenados en forma ascendente los {n} países con la menor {definicion}:')
    for i in range (n):
        print(f'''{i+1}. {matriz_min[i][0]} con {matriz_min[i][1]} {simbolo} y un GDP de {matriz_min[i][4]}.
        Otros datos: La {definicion} {palabra} es {matriz_min[i][2]} {simbolo}. 
        Por lo tanto {matriz_min[i][3]} {palabras}''')

def manipular_datos1(lista1,lista2):
    poblacion = []
    for i in range (1,len(lista1)):
        dato_poblacion = str((100*float(lista1[i])) / float(lista2[i]))
        poblacion.append(dato_poblacion)
    poblacion.insert(0, 'Total population')
    return poblacion

def manipular_datos2(lista1,lista2):
    vacuna_no_comple = []
    for i in range (1,len(lista1)):
        no_completo = str(float(lista1[i]) - float(lista2[i]))
        vacuna_no_comple.append(no_completo)
    vacuna_no_comple.insert(0, '% population not fully vaccinated')
    return vacuna_no_comple

def formar_matriz(lista1,lista2,lista3,lista4,lista5):
    matriz = []
    for i in range (len(lista1)):
        lista_pais = [lista1[i], lista2[i], lista3[i], lista4[i], lista5[i]]
        matriz.append(lista_pais)
    return matriz

def leer_datos():
    paises=[]
    num_vacuna_porcienpersonas=[]
    num_vacuna=[]
    porcen_vacuna=[]
    porcen_vacuna_comple=[]
    
    with open('/workspace/Proyecto-eq3/assignments/Worldwide_Vaccine_Data.csv', 'r') as f:  
        for line in f:
            lista_line = line.split(",")

            paises.append(lista_line[0])
            num_vacuna_porcienpersonas.append(lista_line[1])
            num_vacuna.append(lista_line[2])
            porcen_vacuna.append(lista_line[3])
            porcen_vacuna_comple.append(lista_line[4])

    gdp_imf=[]

    with open('/workspace/Proyecto-eq3/assignments/GDP_PerCapita.csv', 'r') as f:  
        for line in f:
            lista_line_gdp = line.split(",")
            gdp_imf.append(lista_line_gdp[3])

    poblacion = manipular_datos1(num_vacuna, num_vacuna_porcienpersonas)
    vacuna_no_comple = manipular_datos2(porcen_vacuna,porcen_vacuna_comple)

    matriz_informe1 = formar_matriz(paises,porcen_vacuna,porcen_vacuna_comple,vacuna_no_comple,gdp_imf) 
    matriz_informe2 = formar_matriz(paises,num_vacuna,num_vacuna_porcienpersonas,poblacion,gdp_imf)

    return matriz_informe1, matriz_informe2

def desglose(matriz,lista_nueva,index):
    for i in range (len(matriz)):
        lista_nueva.append(matriz[i][index])
    return lista_nueva 

def maximo(n,matriz):
    lista0 = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    desglose(matriz,lista0,0)
    desglose(matriz,lista1,1)
    desglose(matriz,lista2,2)
    desglose(matriz,lista3,3)
    desglose(matriz,lista4,4)
    
    lista0_max = []
    lista1_max = []
    lista2_max = []
    lista3_max = []
    lista4_max = []

    for maxi in range (n):
        maximo = max(lista1)
        lista1_max.append(maximo)
        for i in range (len(matriz)):
            if maximo in matriz[i] and maximo in matriz[i][1]:
                lista0_max.append(matriz[i][0])
                lista2_max.append(matriz[i][2])
                lista3_max.append(matriz[i][3])
                lista4_max.append(matriz[i][4])
        lista1.remove(maximo)

    matriz_max = formar_matriz(lista0_max,lista1_max,lista2_max,lista3_max,lista4_max)
    return matriz_max

def minimo(n,matriz):
    lista0 = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    desglose(matriz,lista0,0)
    desglose(matriz,lista1,1)
    desglose(matriz,lista2,2)
    desglose(matriz,lista3,3)
    desglose(matriz,lista4,4)
    
    lista0_min = []
    lista1_min = []
    lista2_min = []
    lista3_min = []
    lista4_min = []

    for mini in range (n):
        minimo = min(lista1)
        lista1_min.append(minimo)
        for i in range (len(matriz)):
            if minimo in matriz[i] and minimo in matriz[i][1]:
                lista0_min.append(matriz[i][0])
                lista2_min.append(matriz[i][2])
                lista3_min.append(matriz[i][3])
                lista4_min.append(matriz[i][4])
        lista1.remove(minimo)

    matriz_min = formar_matriz(lista0_min,lista1_min,lista2_min,lista3_min,lista4_min)
    return matriz_min   

def maximo_graficar(n,matriz):
    lista0 = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    desglose(matriz,lista0,0)
    desglose(matriz,lista1,1)
    desglose(matriz,lista2,2)
    desglose(matriz,lista3,3)
    desglose(matriz,lista4,4)
    
    lista0_max = []
    lista1_max = []
    lista2_max = []
    lista3_max = []
    lista4_max = []

    for maxi in range (n):
        maximo = max(lista2)
        lista2_max.append(maximo)
        for i in range (len(matriz)):
            if maximo in matriz[i] and maximo in matriz[i][2]:
                lista0_max.append(matriz[i][0])
        lista2.remove(maximo)

    return lista0_max, lista2_max

def minimo_graficar(n,matriz):
    lista0 = []
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []

    desglose(matriz,lista0,0)
    desglose(matriz,lista1,1)
    desglose(matriz,lista2,2)
    desglose(matriz,lista3,3)
    desglose(matriz,lista4,4)
    
    lista0_min = []
    lista1_min = []
    lista2_min = []
    lista3_min = []
    lista4_min = []

    for mini in range (n):
        minimo = min(lista2)
        lista2_min.append(minimo)
        for i in range (len(matriz)):
            if minimo in matriz[i] and minimo in matriz[i][2]:
                lista0_min.append(matriz[i][2])
        lista2.remove(minimo)

    return lista0_min, lista2_min

def graficar(lista1,lista2):
    xs = [i for i,_ in enumerate(lista1)]

    plt.bar(xs, lista2)

    plt.ylabel('% Población vacunada por completo')
    plt.title("Porcentaje de vacunación completa por países")

    plt.xticks([i for i,_ in enumerate(lista1)], lista1)

    plt.savefig('grafico_barras.png')
    plt.show()
    
def main():
    #escribe tu código abajo de esta línea
    ejecutar = input('''Seleccione una opción: 
    1. Países con mayor y menor población vacunada.
    2. Países que administraron la mayor y menor cantidad de vacunas.
    3. Gráfico de comparación entre los países con mayor y menor población vacunada por completo.
    Su opción es: ''')
    n = int(input('¿Cuántos países quiere ver (El número mencionado será igual para ambas categorías)? '))
    matrices_listas = leer_datos()

    if ejecutar == '1':
        matriz_informe1 = matrices_listas[0]
        matriz_max1 = maximo(n,matriz_informe1)
        matriz_min1 = minimo(n,matriz_informe1)
        definicion1 = 'poblacion vacunada'
        simbolo1 = '%'
        palabra1 = 'por completo'
        palabras1 = '% no se le han administrado todas las dosis.'
        mostrar_datos(matriz_max1,matriz_min1,n,definicion1,simbolo1,palabra1,palabras1)

    elif ejecutar == '2':
        matriz_informe2 = matrices_listas[1]        
        matriz_max2 = maximo(n,matriz_informe2)
        matriz_min2 = minimo(n,matriz_informe2)
        definicion2 = 'cantidad de vacunas administradas'
        simbolo2 = 'dosis'
        palabra2 = 'por cada 100 personas'
        palabras2 = 'personas se tomaron en cuneta para el cálculo.'
        mostrar_datos(matriz_max2,matriz_min2,n,definicion2,simbolo2,palabra2,palabras2)

    elif ejecutar == '3':
        matriz_grafica = matrices_listas[0]
        grafica_min = minimo_graficar(n, matriz_grafica)
        grafica_max = maximo_graficar(n, matriz_grafica)
        paises = grafica_min[0] + grafica_max[0]
        vacuna_completa = grafica_min[1] + grafica_max[1]
        graficar(paises, vacuna_completa)

    else:
        print('Entrada inválida')
    
if __name__=='__main__':
    main()