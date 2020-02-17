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
