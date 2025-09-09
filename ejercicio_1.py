class Vehiculo:
    def __init__(self,patente,marca,anio,posicion=0):
        self.patente=patente
        self.marca=marca
        self.anio=anio
        self.posicion=posicion

    def __str__(self):
        return f"Auto: #{self.patente} \nCarga: {self.marca} \nAño: {self.anio}"
    

    def desplazamiento(self,metros):
        try:
            met=float(metros)
            self.posicion+=met
            print(self.patente," avanazo ",met,'')

        except:
            print('No ingreso numeros')


class Autos(Vehiculo):
    listaautos=[]

    def __init__(self, patente, marca,modelo, anio,ruedas,posicion=0):
        super().__init__(patente,marca,anio)
        if patente.lower() not in (auto.patente.lower() for auto in Autos.listaautos):
            self.patente=patente
            self.marca=marca
            self.modelo=modelo
            self.anio=anio
            self.ruedas=ruedas
            self.posicion=posicion
            Autos.listaautos.append(self)
        else:
            print('Esa auto ya esta registrado')
        


    def desplazamiento(self,metros):
        super().desplazamiento(metros)
        return 'por tierra'

class Lancha(Vehiculo):
    lanchas=[]

    def __init__(self, patente, marca,anio,posicion,marca_motor):
        super().__init__(patente,marca,anio)
        if patente.lower() not in (lancha.patente.lower() for lancha in Lancha.lanchas):
            self.posicion=posicion
            self.marca_motor=marca_motor
            Lancha.lanchas.append(self)
        else:
            print('Esa lancha ya esta registrada')

    def __str__(self):
        return f"Lancha {self.marca} ({self.anio}), motor {self.marca_motor}, patente {self.patente}, posicion {self.posicion_inicial}"

    def desplazamiento(self,metros):
        super().desplazamiento(metros)
        print(' por water')
        print(self.posicion)

class Velero(Vehiculo):
    listaveleros=[]
    def __init__(self,patente,marca,anio,posicion,cant_velas):
        super().__init__(patente,marca,anio)
        if patente.lower() not in (pat.patente.lower() for pat in Velero.listaveleros):
            try:
                int(cant_velas)
                self.patente=patente
                self.marca=marca
                self.anio=anio
                self.posicion=posicion
                self.cant_velas=cant_velas
                Velero.listaveleros.append(self)
            except:
                print('Cantidad de velas no es un numero ')
        else:
            print('Patente de velero ya esta registrada')
    
    def desplazamiento(self,metros):
        super().desplazamiento(metros)
        print('por agua a vela', self.posicion)

class Anfibio(Vehiculo):
    listaanfibios=[]
    tipos_despla=['terrestre','marino']
    def __init__(self,patente,marca,anio,posicion,tipo_desplazamiento='terrestre'):
        super().__init__(patente,marca,anio,posicion)
        if patente.lower() not in (pat.patente.lower() for pat in Anfibio.listaanfibios):
                if tipo_desplazamiento.lower() in Anfibio.tipos_despla:
                    self.patente=patente
                    self.marca=marca
                    self.anio=anio
                    self.posicion=posicion
                    self.tipo_desplazamiento=tipo_desplazamiento
                    Anfibio.listaanfibios.append(self)
                else:
                    print('El desplazamiento no es ni marino ni terrestre')
        else:
            print('La patente ya fue registrada')

    def desplazamiento(self,metros):
        super().desplazamiento(metros)
        if self.tipo_desplazamiento.lower()=='terrestre':
            print('por tierra')
        else:
            print('Por agua')


furgon1 = Autos("ABC123", "Mercedes", 'A1000',4, 2020)
furgon3 = Autos("abc123", "Volvo", 'B2000',4, 2021)
lancha1=Lancha('abc123','mercedez',2020,0,'nashe')
lancha2=Lancha('AbC123','mercedes',2021,2,'nahe')
lancha1.desplazamiento(100)
velero1=Velero("ABC123", "Mercedes", 2020,0,3)
velero2=Velero("ABd123", "Mercedes", 2020,0,3)
velero1.desplazamiento(50)
anfibio1=Anfibio('AbC123','mercedes',2021,0,'marINO')
anfibio2=Anfibio('AbC123','mercedes',2021,0,'TERRestre')
anfibio1.desplazamiento(75)