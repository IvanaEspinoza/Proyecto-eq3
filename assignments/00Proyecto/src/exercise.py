# def mostrar_datos():

def manipular_datos1(lista1,lista2):
    dias = []
    for i in range (len(lista1)):
        dato_dias = str(int(lista1[i]) / int(lista2[i]))
        dias.append(dato_dias)
    return dias

def manipular_datos2(lista1,lista2):
    vacuna_no_comple=[]
    for i in range (len(lista1)):
        no_completo=str(int(lista1[i])-int(lista2[i]))
        vacuna_no_comple.append(no_completo)
    return vacuna_no_comple

def formar_matriz(lista1,lista2,lista3,lista4,lista5):
    matriz = []
    for i in range (len(lista1)):
        lista_pais = [lista1[i], lista2[i], lista3[i], lista4[i], lista5[i]]
        matriz.append(lista_pais)
    return matriz

def leer_datos():
    paises=[]
    num_vacunas=[]
    porcen_vacuna=[]
    porcen_vacuna_comple=[]
    num_vacuna_día=[]

    with open('/workspace/Proyecto-eq3/assignments/Global_COVID_Vaccination_Tracker.csv', 'r') as f:  
        for line in f:
            lista_line = line.split(",")

            paises.append(lista_line[0])
            num_vacuna.append(lista_line[1])
            porcen_vacuna.append(lista_line[3])
            porcen_vacuna_comple.append(lista_line[4])
            num_vacunas_día.append(lista_line[5])

    gdp_imf=[]

    with open('/workspace/Proyecto-eq3/assignments/GDP_PerCapita.csv', 'r') as f:  
        for line in f:
            lista_line_gdp = line.split(",")
            gdp_imf.append(lista_line_gdp[3])
        
    dias = manipular_datos1(num_vacunas,num_vacuna_día)
    vacuna_no_comple = manipular_datos2(porcen_vacuna,porcen_vacuna_comple)

    matriz_informe1 = formar_matriz(paises,porcen_vacuna,porcen_vacuna_comple,vacuna_no_comple,gdp_imf) 
    matriz_informe2 = formar_matriz(paises,num_vacunas,num_vacuna_día,dias,gdp_imf)

    return matriz_informe1, matriz_informe2, paises, porcen_vacuna_comple

def formar_lista(lista,matriz,i,ind):
    rang = len(matriz[i])-1
    for nuevo in range (1,rang):
        lista.append(matriz[i][ind+nuevo])

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
        maximo = max(n1)
        lista1_max.append(maximo)
        for i in range (len(matriz)):
            if maximo in matriz[i]:
                ind = matriz[i].index(maximo)
                lista0_max.append(matriz[i][ind-1])
                formar_lista(lista2_max,matriz,i,ind)
                formar_lista(lista3_max,matriz,i,ind)
                formar_lista(lista4_max,matriz,i,ind)
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
        minimo = max(n1)
        lista1_min.append(minimo)
        for i in range (len(matriz)):
            if minimo in matriz[i]:
                ind = matriz[i].index(minimo)
                lista0_min.append(matriz[i][ind-1])
                formar_lista(lista2_min,matriz,i,ind)
                formar_lista(lista3_min,matriz,i,ind)
                formar_lista(lista4_min,matriz,i,ind)
        lista1.remove(minimo)

    matriz_min = formar_matriz(lista0_min,lista1_min,lista2_min,lista3_min,lista4_min)
    return matriz_min
    
#def graficar():

def main():
    #escribe tu código abajo de esta línea
    ejecutar = input('''Seleccione una opción: 
    1. Países con mayor y menor población vacunada.
    2. Países que administraron la mayor y menor cantidad de vacunas.
    3. Gráfico de comparación entre los países con mayor y menor población vacunada por completo
    Su opción es: ''')
    n = input('¿Cuántos países quiere ver (El número mencionado será igual para ambas categorías)? ')
    matrices_listas = leer_datos()

    if ejecutar == '1':
        matriz_informe1 = matrices_listas[0]
        matriz_max = maximo(n,matriz_informe1)
        matriz_min = minimo(n,matriz_informe1)

    elif ejecutar == '2':
        matriz_informe2 = matrices_listas[1]        
        matriz_max = maximo(n,matriz_informe2)
        matriz_min = minimo(n,matriz_informe2)

    elif ejecutar == '3':
        paises = matrices_listas[2]
        vacuna_comple = matrices[3]
        graficar(paises,vacuna_comple)
    else:
        print('Entrada inválida')
    

if __name__=='__main__':
    main()