# import the function that will return an instance of a connection
from pydoc import classname
from sqlite3 import connect
from unittest import result
from mysqlconnection import connectToMySQL
from flask import request

# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_db').query_db(query)
        # Create an empty list to append our instances of users
        users_list = []
        # Iterate over the db results and create instances of users with cls.
        for dict in results:
            users_list.append( cls(dict) )
        return users_list
    
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_db").query_db(query, data)
        if results:
            return cls(results[0])

    @classmethod
    def create_user(cls, data):
        mysql = connectToMySQL("users_db")
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return mysql.query_db(query, data)
    
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL("users_db").query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL("users_db").query_db(query, data)
