# import the function that will return an instance of a connection
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
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        # Create an empty list to append our instances of dojos
        dojo_list = []
        
        # Iterate over the db results and create instances of dojos with cls.
        for dict in results:
            dojo_list.append( cls(dict) )
        return dojo_list
    
    # @classmethod
    # def get_dojo(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(dojo_id)s;"
    #     results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
    #     if results:
    #         return cls(results[0])

    @classmethod
    def create_new(cls, data):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return mysql.query_db(query, data)
    
    # @classmethod
    # def update_dojo(cls, data):
    #     query = "UPDATE dojos SET dojo_name = %(dojo_name)s, updated_at = NOW() WHERE id = %(dojo_id)s;"
    #     return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    # @classmethod
    # def delete_dojo(cls, data):
    #     query = "DELETE FROM dojos WHERE id = %(dojo_id)s;"
    #     return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
