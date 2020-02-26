from boleto import boleto
import mysql.connector                    # import A correcta
# from mysql.connector import (connection)  # import B correcta

class database:
    
    def capturar(self, datos):
        resultado=""
        
        try:
            conexion = mysql.connector.connect(user='root', database='boletos')
            
            # Preparar el string insertCliente con el comando SQL INSERT
            boletodp = boleto(datos)
            
            insertAsistente = "INSERT INTO registro VALUES("+boletodp.toStringSql()+")"
            print(insertAsistente+"\n")
            # 2. Almacenar los datos
            statement = conexion.cursor()
            statement.execute(insertAsistente)
            conexion.commit()
            # 3. Cerrar
            statement.close()
            conexion.close()
            
            resultado = "Datos capturados: "+datos
        except:
            resultado = "Error en la Captura de Datos..."
        
        return resultado


    def consultar(self):
        # 1. Abrir el archivo para leer
        conexion = mysql.connector.connect(user='root',database='boletos')
        
        # Preparar el query a la BD y ejecutarlo
        query = "SELECT * FROM registro"
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar los datos de la tabla resultante
        datos=""
        boletodp = boleto(datos)
        tupla = statement.fetchone()
        # while tupla is not None:
        while(tupla != None):
            #AYUDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            boletodp.setNumero(tupla[0])
            boletodp.setNombre(tupla[1])
            boletodp.setCorreo(tupla[2])
            boletodp.setCelular(tupla[3])
            boletodp.setFecha(tupla[4])
            boletodp.setHora(tupla[5])
            boletodp.setCodigo(tupla[6])
            #AYUDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            datos = datos + boletodp.toString() + "\n"
            # print(tupla)
            tupla = statement.fetchone()
        
        # 3. Cerrar el archivo
        statement.close()
        conexion.close
        
        print(query+"\n")
        
        return datos
    def consultarBoleto(self,noBoleto):
        # 1. Abrir el archivo
        conexion = mysql.connector.connect(user="root", database="boletos")
        
        # Preparar query y ejecutarlo
        query = "SELECT * FROM registro WHERE noBoleto='"+noBoleto+"'"
        statement = conexion.cursor()
        statement.execute(query)
        
        # 2. Procesar datos del archivo
        datos = ""
        encontrado = False
       
        # cliente = archivoIn.readline()
        #AYUDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        boletodp = boleto(datos)
        tupla = statement.fetchone()
        # while (cliente != "" and not encontrado):
        if(tupla is not None):
        # if (tupla != None):
            # st = cliente.split("_")
            #AYUDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            boletodp.setNumero(tupla[0])
            boletodp.setNombre(tupla[1])
            boletodp.setCorreo(tupla[2])
            boletodp.setCelular(tupla[3])
            boletodp.setFecha(tupla[4])
            boletodp.setHora(tupla[5])
            boletodp.setCodigo(tupla[6])
            #AYUDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            datos = datos + boletodp.toString() + "\n"
            encontrado = True
            
        
        # 3. Cerrar el archivo
        statement.close()
        conexion.close()
        
        print(query)
        
        #if encontrado == False:
        if (not encontrado):
            datos = "No se localizo el boleto número "+noBoleto
        
        return datos
