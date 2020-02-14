class boleto:

    def replace_object(self, new_object):
        self.__dict__ = new_object.__dict__.copy()

    def toString(self):
        asis=''
        for obj in self.asistencia:
            asis+=str(obj)
            asis+='_'
        asis = asis[:-1]
        return '_'.join([self.codigo,self.nombre,self.correo,self.institucion,str(self.transporte),asis,str(self.numero)])

    def __init__(self, data):
        atributos=data.split('_')
        self.asistencia=[]

        self.codigo=atributos[0]
        self.nombre=atributos[1]
        self.correo=atributos[2]
        self.institucion=atributos[3]
        self.transporte= (atributos[4]=='True')
        for i in range(5,10):
            self.asistencia.append(atributos[i]=='True')
        self.numero=int(atributos[10])
