# import the function that will return an instance of a connection
from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas_list = []
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
        
        # Obtain joined data after ninja is created by create_ninja.
        query ="select * from dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id where dojo_id = %(dojo_id)s;"
        joined_dojos_and_ninjas_data = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        
        # Validates 
        if joined_dojos_and_ninjas_data:
            dojo = cls(joined_dojos_and_ninjas_data[0])

            for ninjas in joined_dojos_and_ninjas_data:
                
                ninjas_data = {
                    'id': ninjas['ninjas.id'],
                    'first_name': ninjas['first_name'],
                    'last_name': ninjas['last_name'],
                    'age': ninjas['age'],
                    'dojo_id': ninjas['dojo_id'],
                    'created_at': ninjas['ninjas.created_at'],
                    'updated_at': ninjas['ninjas.updated_at']
                }
                dojo.ninjas_list.append(Ninja(ninjas_data))

            return dojo
        return "Nothing here"
        
