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

    return paises


def main():
    #escribe tu código abajo de esta línea
    paises=leer_datos()
    print(paises[0])

if __name__=='__main__':
    main()