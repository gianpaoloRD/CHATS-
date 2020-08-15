from basededatos import conexion as conecta

connect = conecta.connectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self,remitente = 0,receptor = "",titulo = "",mensaje = ""): 
        self.remitente = int(remitente)
        self.receptor = receptor
        self.titulo = titulo 
        self.mensaje = mensaje

    def enviar(self):
        sql = "INSERT INTO mensajes VALUE ( null, %s , %s, %s , %s)"
        sms = (self.remitente,self.receptor,self.titulo,self.mensaje)

        cursor.execute(sql,sms)
        database.commit()

        return [cursor.rowcount,self]
    def mensajes(self):
        hola =f"SELECT titulo,mensaje FROM mensajes WHERE gmail_R = '{self.receptor}'"
        cursor.execute(hola)
        result = cursor.fetchall()
        return result
