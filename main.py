import pyfiglet

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

dato = input("")

if dato == "sig":
    ascii_banner = pyfiglet.figlet_format("Registro")
    print(ascii_banner)
    nombre = input("¿Cúal es tu nombre?")
    apellido = input("¿Cúal es tu apellido?")
    email = input("¿Cúal es tu e-mail?")
    password = input("¿Cúal es tu contraseña?")
if dato == "log":
    ascii_banner = pyfiglet.figlet_format("Logueo")
    print(ascii_banner)
    email = input("e-mail: ")  
    password = input("contraseña: ") 

    

