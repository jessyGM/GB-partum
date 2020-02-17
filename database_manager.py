import boleto

class database:

    def __init__(self, filename):
        self.boletosDB=loadObjects(filename)

def loadFile(filename):
    file= open(filename, 'r')
    try:
        lines=file.readlines()
    finally:
        file.close()
    return lines

def loadObjects(filename):
    boletos=[]
    for line in loadFile(filename):
        boletos.append(boleto.boleto(line))
    return boletos

def savefile(filename,database):
    file=open(filename,'w')
    try:
        for obj in database.boletosDP:
            file.write(obj.toString())
    finally:
        file.close()
