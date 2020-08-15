import mysql.connector 

def connectar():
    database = mysql.connector.connect(
        host="db4free.net",
        user="gianpaolo2002",
        passwd="gianpaolo",
        database="dbchats2002",
        port=3306
    )

    cursor = database.cursor(buffered= True)
    return [database,cursor]

"""
connect = conexion.connectar()
database = connect[0]
cursor = connect[1]
"""
