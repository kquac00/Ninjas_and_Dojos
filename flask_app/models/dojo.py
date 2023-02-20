from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninja = []

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []
        for dojoX in results:
            dojos.append( cls(dojoX))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        return result
        
    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos_and_ninjas.dojos WHERE name = %(name)s;"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data) 

    @classmethod
    def get_oneNinja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for item in results:
            n = {
                'id': item['ninjas.id'],
                'first_name': item['first_name'],
                'last_name' : item['last_name'],
                'age' : item['age'],
                'created_at' : item['created_at'],
                'updated_at' : item['updated_at']
            }
            dojo.ninja.append(Ninja(n))
        return dojo