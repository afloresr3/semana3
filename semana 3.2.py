class For:
    def __init__(self,lim=6):
        self.n=lim

    def usoFor(self):
        nombre = "Alan"
        datos=["Alan",19,False]
        numeros=(2,5.6,4,1)
        persona= {"nombre": "Alan", "edad": 19, "fac": "faci"}
        listaNotas= [(30,40),(20,49,50),(50,40,10,45),(5,15)]
        listaAlumnos= [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]

        # print("Suma de notas con un for") #For para sumar las notas de una lista de diccionarios. 
        # acu=0
        # for alumnos in listaAlumnos:
        #     acu =  acu + alumnos["final"]
        # print(acu,"\n")

        # print("Elementos de la lista")#For para presentar cada elemento de una lista de diccionarios.
        # for alumnos in listaAlumnos:
        #     for c,v in alumnos.items():
        #         print(c,v,)
        # print("\n")

        print("Suma de notas con dos for") #Uso de dos for para sumar las notas de una lista de diccionarios.
        acu1=0
        for alumnos in listaAlumnos:
            for c,v in alumnos.items():
                if c=="final":
                    acu1 = acu1+v
        print(acu1,"\n")

        print("Promedio usando un contador") #Presenta el promedio de las notas 
        cont=0
        for alumnos in listaAlumnos:
            cont+=1
            for c,v in alumnos.items():
                if c=="final":
                    acu1 = acu1+v
        print(acu1/cont,"\n") #También se puede usar el "len(listaAlumnos)" en vez del contador

        print("Elementos de la lista y elementos de la tupla") #Presenta los elementos de la lista y los elementos de la tupla
        for notas in listaNotas:
            print(notas)
            for nota in notas:
                print(nota)
        print("\n")

        print("Suma y promedio") #Suma y promedio de listaNotas usando un contador y un acumulador
        acu2=0
        cont2=0
        for notas in listaNotas:
            for nota in notas:
                acu2+=nota
                cont2+=1
        print(acu2,acu2/cont2,"\n")

        print("Suma y promedio parciales") #Presenta suma y promedios parciales y total
        acu3=0
        cont3=0
        for notas in listaNotas:
            acuParcial=0
            for nota in notas:
                acu3+=nota
                acuParcial+=nota
                cont3+=1
            print(acuParcial,acuParcial/len(notas))
        print("Suma y promedio total \n",acu3,acu3/cont3)
        print("\n")


        print("For mejorado y terminado") #!Programa final
        acuf,contf=0,0
        for notas in listaNotas:
            print(notas)
            acuParcialf=0
            for nota in notas:
                acuParcialf+=nota
            contf+=len(notas)
            acuf+=acuParcialf
            print(acuParcialf,acuParcialf/len(notas))
        print(acuf,acuf/contf)





bucle1 = For()
bucle1.usoFor()


