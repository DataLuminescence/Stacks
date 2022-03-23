# import the function that will return an instance of a connection
from Python.Flask_MySQL.CRUD.Dojos_and_Ninjas.flask_app.controllers.dojos import dojos
from Python.Flask_MySQL.CRUD.Dojos_and_Ninjas.flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        # Create an empty list to append our instances of dojos
        dojo_list = []
        # Iterate over the db results and create instances of dojos with cls.
        for dict in results:
            dojo_list.append( cls(dict) )
        return dojo_list
    
    @classmethod
    def create_new(cls, data):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        return mysql.query_db(query, data)



    @classmethod
    def join_dojos_and_ninjas(cls,data):
        
        query ="select * from dojo LEFT JOIN ninjas ON dojo.id = ninjas.dojo_id where dojo_id = %(dojo_id)s;"
        ninjas_in_dojos = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        
        if len(ninjas_in_dojos != 0):

            for ninjas in ninjas_in_dojos:
                ninjas_data = {
                    'id': ninjas['ninjas.id'],
                    'first_name': ninjas['first_name'],
                    'last_name': ninjas['last_name'],
                    'age': ninjas['age'],
                    'dojo_id': ninjas['dojo_id'],
                    'created_at': ninjas['ninjas.created_at'],
                    'updated_at': ninjas['ninjas.updated_at']
                }
                ninjas_in_dojos.ninjas.append(Ninja(ninjas_data))
            return ninjas_in_dojos
        return "Nothing here"
        
