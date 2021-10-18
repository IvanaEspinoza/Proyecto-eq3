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

    return paises


def main():
    #escribe tu código abajo de esta línea
    paises=leer_datos()
    print(paises[0])

if __name__=='__main__':
    main()