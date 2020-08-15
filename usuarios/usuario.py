from basededatos import conexion as conecta

connect = conecta.connectar()
database = connect[0]
cursor = connect[1]

class Usuarios:



    def __init__(self,nombre,apellido,email,password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):    

        sql ="INSERT INTO registro VALUE (null,%s,%s,%s,%s,NOW());"
        usuario = (self.nombre, self.apellido, self.email, self.password)
        try:
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount, self] #rowcount hace un conteo de los usuarios nuevos registrados
        except:
           result = [0,self]        
        
        return result
    def logueado(self):

        sql = "SELECT * FROM registro WHERE gmail = %s AND clave = %s"
        usuario = (self.email,self.password)

        cursor.execute(sql,usuario)
        result = cursor.fetchone()

        
        return result



