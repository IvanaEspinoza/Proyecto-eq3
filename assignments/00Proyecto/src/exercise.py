def leer_datos():
    paises=[]
    num_vacunas=[]
    num_vacunas_poblacion=[]
    porcen_vacunacion=[]
    porcen_vacunacion_comple=[]
    num_vacunas_día=[]

    with open('/workspace/Proyecto-eq3/assignments/Global_COVID_Vaccination_Tracker.csv', 'r') as f:  
        for line in f:
            lista_line= line.split(",")

            paises.append(lista_line[0])
            num_vacunas.append(lista_line[1])
            num_vacunas_poblacion.append(lista_line[2])
            porcen_vacunacion.append(lista_line[3])
            porcen_vacunacion_comple.append(lista_line[4])
            num_vacunas_día.append(lista_line[5])


def max_min():
    n=int(input('¿Cuántos países quiere ver? (El número mencionado será igual para ambas categorías): '))


    
#def graficar():

def main():
    #escribe tu código abajo de esta línea
    ejecutar = input('''Seleccione una opción: 
    1. Países con mayor y menor población vacunada.
    2. Países que administraron vacunas la mayor cantidad y menor cantidad de días
    3. Gráfico de comparación entre población completamente vacunada y el PIB del país
    Su opción es: ''')

    if ejecutar == '1':
        max_min()
    elif ejecutar == '2':
        max_min()
    elif ejecutar == '3':
        graficar()
    else:
        print('Entrada inválida')
    

if __name__=='__main__':
    main()