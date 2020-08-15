import usuarios.usuario as modelo
from notas import acciones as modulo 
import pyfiglet
import smtplib
from shooter import play as juegos
nota = modulo.Acciones()
jugar = juegos.juego()
class Acciones:

    def verificacion(self,email):
        print(f"se le enviara un codigo de verificación al siguiente email {email}")
        mensaje = "codigo de verificacion 12345"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('chatsRD2002@gmail.com','chats8520')

        server.sendmail("chatsRD2002@gmail.com",email, mensaje)
        print("enviado")


    def registro(self):
        ascii_banner = pyfiglet.figlet_format("Registro")
        print(ascii_banner)
        nombre = input("¿Cúal es tu nombre?")
        apellido = input("¿Cúal es tu apellido?")
        email = input("¿Cúal es tu e-mail?")
        self.verificacion(email)
        codigo = int(input("Codigo: "))
        password = input("¿Cúal es tu contraseña?")
        if codigo == 12345:
            usuario = modelo.Usuarios(nombre, apellido, email, password)
            registro = usuario.registrar()
            if registro[0] >= 1:
                print(f"Bien {registro[1].nombre} te has registrado con el e-mail {registro[1].email}")
            else:
                print("no te has registrado bien intentalo de nuevo!!")
    


    def login(self):
        ascii_banner = pyfiglet.figlet_format("Logueo")
        print(ascii_banner)
        email = input("e-mail: ")  
        password = input("contraseña: ")        
        usuario = modelo.Usuarios("","", email, password)
        login = usuario.logueado()
        if email == login[3]:
            print(f"{login[1]} te has logueado correctamente")
            ascii_banner = pyfiglet.figlet_format("MENU")
            print(ascii_banner)            
            self.menu(login)

    def menu(self,login):

        print(f"""
        {login[1]} {login[0]}
        ########################################################
        |                                                      |   
        |                -Enviar  Mensajes     (1)             |
        |                -Mostrar mensaje      (2)             |
        |                -juego                (3)             |  
        |                -Salir              (salir)           |  
        |                                                      |
        ########################################################

        """)
        principal = input()
        if principal == "1":
            nota.new(login)
            self.menu(login)

        if principal == "2":
            nota.ver(login)
            self.menu(login)

        if principal == "3":
            jugar.tick()
            self.menu(login)

        elif principal == "salir":
            print("adios")