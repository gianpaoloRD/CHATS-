from notas import nota as message
class Acciones:

    def new(self,login):
        receptor =input("Saludos para quien es el mensaje(e-mail): ")
        titulo = input("introduzca el titulo del mensaje: ")
        mensaje = input("""
        Escriba su mensaje:\n
        """)
        sms = message.Nota(login[0],receptor,titulo,mensaje)
        enviado = sms.enviar()

        if enviado[0]>= 1:
            print("nota enviada correctamente")
        else:
            print("La nota no se pudo enviar, intentelo de nuevo.")    

    def ver(self,login):
        print(f"\nSaludos {login[1]} tus mensajes son los siguientes:")

        sms = message.Nota(0,login[3])
        enviado = sms.mensajes()
        for i in enviado:
           print("#########################################")
           print(f"Titulo: {i[0]}")
           print(f"Cuerpo: {i[1]}")
           print("#########################################\n")            



