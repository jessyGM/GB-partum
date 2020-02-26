class boleto:

    asistencia=[False,False,False,False,False]

    def replace_object(self, new_object):
        self.__dict__ = new_object.__dict__.copy()

    def toString(self):
        asis=''
        for obj in self.asistencia:
            asis+=str(obj)
            asis+='&'
        asis = asis[:-1]
        return '&'.join([str(self.numero),self.nombre,self.correo,self.celular,self.fecha,self.hora,self.codigo,asis])

    def __init__(self, data):
        atributos=data.split('&')
        self.numero=int(atributos[0])
        self.nombre=atributos[1]
        self.correo=atributos[2]
        self.celular=atributos[3]
        self.fecha=atributos[4]
        self.hora=atributos[5]
        self.codigo=atributos[6]
        self.codigo=self.codigo[:-1]

    #Geters
    def getNumero(self):
            return self.numero
    def getNombre(self):
            return self.nombre
    def getCorreo(self):
            return self.correo
    def getCelular(self):
            return self.celular
    def getFecha(self):
            return self.fecha
    def getHora(self):
            return self.hora
    def getCodigo(self):
            return self.codigo

    #Seters
    def setNumero(self, num):
        self.numero=num

    def setNombre(self, nom):
        self.nombre=nom

    def setCorreo(self, cor):
        self.correo=cor

    def setCelular(self, cel):
        self.celular=cel

    def setFecha(self, fec):
        self.fecha=fec

    def setHora(self, hor):
        self.hora=hor

    def setCodigo(self, cod):
        self.codigo=cod

    #Strings
    def toStringSql (self):
            return "'"+self.numero+"','"+self.nombre+"','"+self.correo+"','"+self.celular+"','"+self.fecha+"','"+self.hora+"','"+self.codigo
