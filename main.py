import pyfiglet
from usuarios import acciones
ascii_banner = pyfiglet.figlet_format("Bienvenido a CHATS!")

print(ascii_banner)

print("""
#################################################
|                                               |   
|                -Sign in(sig)                  |
|                -Login(log)                    |
|                                               |    
#################################################
""")
hazel = acciones.Acciones()
dato = input("")

if dato == "sig":
    hazel.registro()
if dato == "log":
    hazel.login()
    

