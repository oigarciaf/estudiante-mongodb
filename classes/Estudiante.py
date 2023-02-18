from classes.DbMongo import DbMongo
class Estudiante:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__collection = "estudiante"

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        col = db["estudiante"]
        consulta = {"nombre": "carlos"}
        nuevoValor = {"$set":{"nombre":"josue"}}
        col.update_one(consulta,nuevoValor) 

       