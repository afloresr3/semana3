class For:
    def __init__(self,lim=6):
        self.n=lim

    def usoFor(self):
        #ciclo repetitivo automaticode que se ejecuta desde un valor inicial hasta alcanzar un valor final:
        nombre = "Alan"
        datos=["Alan",19,False]
        # pos    0     1   2
        numeros=(2,5.6,4,1)
        persona= {"nombre": "Alan", "edad": 19, "fac": "faci"}
        listaNotas= [(30,40),(20,49,50),(50,40)]
        listaAlumnos= [{"nombre":"Erick","final":70},{"nombre":"Yady","final":"60"},{"nombre":"Danny","final":90}]
        # for i in range(5): #(0,1,2,3,4)
        #     print("i={}".format(i))
        # for i in range (2,5): #(2,3,4)
        #     print("i={}".format(i))
        # for i in range(10,2,-2): #(10,8,6,4)
        #     print("i={}".format(i))
        # for i in range(3,self.n,3): #(3,6,9)
        #     print("i={}".format(i),end=" ")
        #long= len(nombre)
        #for pos in range(long): #(0,1,2,3,4,5)
        # """     print(nombre[pos],end=" ")
        
        # for pos,elem in enumerate(datos): #((0,"daniel"),(1,50),(2,true))
        #     print(pos," ",elem)
        
        # for pos,elem in enumerate(nombre): #((0,"daniel"),(1,50),(2,true))
        #     if pos%2==0 and pos!=0:
        #         print(elem) """

        for pos,elem in enumerate(nombre): #presenta los elementos de nombre
            print(elem)

        # for pos,elem in enumerate(nombre): #presenta los elementos que se encuentran en la pocicion par de nombre excluyendo la posición cero
        #     if pos%2==0 and pos!=0:
        #         print(elem)

        for clave, valor in persona.items(): #leer un diccionario en un ciclo for
            print (clave,valor,end=(" "))




bucleA = For()
bucleA.usoFor()

#bucleE = For(12)
#bucleE.usoFor

