class Libro:
    # constructor
    posibles_estados=['disponible','prestado'] # atributo de clase
    contador_libros=0 # atributo de clase
    lectores_honor={}
    lectores={}
    libros=[]
    nunca_prestados=[]
    prestado_viejo={}
    generos={}

    
    def __init__(self,titulo:str,autor:str,editorial:str,ISBN:str,genero,anio:int,estado='disponible'):
        self.titulo=self.validar_cadena(titulo)# atributos de instancia
        self.autor=self.validar_cadena(autor)
        self.editorial=self.validar_cadena(editorial)
        self.ISBN=ISBN
        self.estado=self.setter_estado(estado)
        self.anio=anio
        self.genero=genero.lower()
        Libro.libros.append(self)
        Libro.contador_libros+=1
        Libro.nunca_prestados.append(self)
        if genero.lower() not in list(Libro.generos.keys()):
            Libro.generos[genero.lower()] = 1
        else:
            Libro.generos[genero.lower()] +=1
        
    @classmethod
    def mostrar_contador_libros(cls):
        print(f'El numero de libros creados es: {cls.contador_libros}')
    
        
    #visualizar la información de cada libro
    # def __str__(self):
    #     return f' El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial } con ISBN{self.ISBN}, y su estado es {self.estado}'
    
    def mostrar(self):
        return f' El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial } con ISBN{self.ISBN}, y su estado es {self.estado}'

    def getter_estado(self):
        return self.estado
    
    def getter_ISBN(self):# no se ha validado, puede construir un objeto libro incorrecto al pasar un ISBN no valido
        return self.ISBN
    
    def devolver_libro(self):
        if self.estado=='disponible':
            print('El libro ya se encuentra disponible')
        else:
            self.setter_estado('disponible')
            print('El libro ha sido devuelto y se encuentra disponible')
    
    def prestar_libro(self,lector):
        if self.getter_estado()=='disponible' and lector.lower() not in Libro.lectores.keys():
            Libro.lectores[lector.lower()] = 1
            Libro.prestado_viejo[lector.lower()] = (self.titulo,self.anio)
            self.estado='prestado'
            print(f'El libro {self.titulo} fue prestado con exito a {lector}')
            if self in Libro.nunca_prestados:
                Libro.nunca_prestados.remove(self)
        elif self.getter_estado()=='disponible' and lector.lower() in Libro.lectores.keys():
            self.estado='prestado'
            Libro.lectores[lector.lower()]+=1
            print(f'El libro {self.titulo} fue prestado con exito a {lector}')
            if self in Libro.nunca_prestados:
                Libro.nunca_prestados.remove(self)
            if self.anio < Libro.prestado_viejo[lector.lower()][1]:
                Libro.prestado_viejo[lector] = (self.titulo,self.anio) 
        else:
            print(f' El libro {self.titulo} no se encuentra disponible para prestar')
    
    def validar_cadena(self,cadena:str):
        if not isinstance(cadena,str):
            raise TypeError('El titulo debe ser una cadena de texto')
        if len(cadena)==0:
            raise ValueError('El titulo no puede estar vacio')
        return cadena
 
    def setter_estado(self,estado):
        estado=estado.lower()
        if estado not in Libro.posibles_estados:
            raise ValueError(f'El estado debe ser uno de los siguientes: {self.posibles_estados}')
        self.estado=estado
        return estado
    
    def __eq__(self,otro):
        if not isinstance(otro,Libro):
            raise TypeError('El objeto debe ser una instancia de la clase Libro')
        elif id(self)==id(otro):
            return True
        elif self.ISBN==otro.ISBN:
            return True
        else:
            return False
    
    @classmethod
    def quitar_no_prestados(cls):
        for l in cls.nunca_prestados:
            print(l.titulo)
        opcion=input('Ingrese 1 si quiere eliminarlos del catalogo. Cualquier otra opcion para mantenerlos: ')
        if opcion=='1':
            for i in list(cls.nunca_prestados):
                cls.libros.remove(i)
                print('Se actualizo el catalogo, los libros disponibles son: ')
            for t in cls.libros:
                print(t.titulo, t.ISBN)    

    @classmethod
    def prestados_promedio(cls):
        suma=0
        for i in Libro.lectores.values(): 
            suma+=int(i)
        try:
            print('Promedio por usuario', suma/len(Libro.lectores), 'libros')
        except ZeroDivisionError:
            print('Nunca se presto un libro')  

    @classmethod
    def prestado_mas_viejo(cls,lector):
        if lector.lower() in list(Libro.prestado_viejo.keys()):
            print('El libro prestado a ', lector,' mas viejo es ', Libro.prestado_viejo[lector.lower()][0], 'del anio ',Libro.prestado_viejo[lector.lower()][1])
        else:
            print(lector, 'no realizo prestamos')


    @classmethod
    def genero_popular(cls):
        ge=[]
        can=[]
        for i in list(Libro.generos.keys()):
            ge.append(i)
        for j in list(Libro.generos.values()):
            can.append(j)
        print(sorted(zip(can,ge), reverse=True))
        genero1=sorted(zip(can,ge), reverse=True)[0][1]
        genero2=sorted(zip(can,ge), reverse=True)[1][1]
        genero3=sorted(zip(can,ge), reverse=True)[2][1]
        l=0
        while l<3:
            tit=input('titulo (si ingresa vacio no desea agreagar libro): ')
            if l==0 and tit!='':
                aut=input('autor: ')
                reg=input('region: ')
                isb=input('isbn: ')
                an=input('anio: ')
                Libro(tit,aut,reg,isb,genero1,int(an))
                print('se registro ', tit)
            elif l==1 and tit!='':
                aut=input('autor: ')
                reg=input('region: ')
                isb=input('isbn: ')
                an=input('anio: ')
                Libro(tit,aut,reg,isb,genero2,int(an))
                print('se registro ', tit)

            elif l==2 and tit!='':
                aut=input('autor: ')
                reg=input('region: ')
                isb=input('isbn: ')
                an=input('anio: ')
                Libro(tit,aut,reg,isb,genero3,int(an))
                print('se registro ', tit)

            l+=1
    
        

# prueba de la clase
if __name__=='__main__':
    #try:
            carlos=Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567890','terror',2020)
            #print(carlos)
            #print(carlos.mostrar())
            #carlos.setter_estado('prestado')
            #print(carlos.getter_estado())
            carlos1=Libro('Cien años de soledaddddddd','Gabriel Garcia Marquez','Sudamericana','1234567891','lirico',2021)
            #print(Libro.contador_libros)
            #print(carlos1)
            carlos2=Libro('Cien años de ','Gabriel Garcia Marquez','Sudamericana','1234567889','risa',20)
            carlos3=Libro('Cien años de ','Gabriel Garcia Marquez','Sudamericana','123456788','risa',20)
            #print(carlos==carlos2)
            #print(carlos==carlos1)
            carlos.prestar_libro('agustin')
            carlos1.prestar_libro('Venezia')
            print(Libro.lectores)
            print(Libro.prestado_viejo)
            carlos2.prestar_libro('agustin')
            print(Libro.lectores)
            print(Libro.prestado_viejo)
            Libro.prestado_mas_viejo('Agustin')
            #print(Libro.lectores)
            #print(max(Libro.lectores))
            #a_agregar=max(Libro.lectores.items() , key=lambda x: x[1])
            #Libro.lectores_honor[a_agregar[0]] = a_agregar[1]
            #print(Libro.lectores_honor)
            #print(Libro.lectores_honor)
            #Libro.quitar_no_prestados()
            #Libro.prestados_promedio()
            Libro.genero_popular()

    #except TypeError as e:
           # print('El error es:',e)
    #except ValueError as e:
            #print('El error es:',e)
    #except Exception as e:
            #print('El error es:',e)
        