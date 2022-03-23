# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas_list = []
        # Iterate over the db results and create instances of ninjas with cls.
        for dict in results:
            ninjas_list.append( cls(dict) )
        return ninjas_list
    
    @classmethod
    def create_ninja(cls, data):
        mysql = connectToMySQL("dojos_and_ninjas_schema")
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return mysql.query_db(query, data)