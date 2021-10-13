def formar_matriz():

def max_min():
    n=input('¿Cuántos países quiere ver (El número mencionado será igual para ambas categorías)?')
    
def graficar():

def main():
    #escribe tu código abajo de esta línea
    ejecutar = input('''Seleccione una opción: 
    1. Países con mayor y menor población vacunada.
    2. Países que administraron vacunas la mayor cantidad y menor cantidad de días
    3. Gráfico de comparación entre población completamente vacunada y el PIB del país''')

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