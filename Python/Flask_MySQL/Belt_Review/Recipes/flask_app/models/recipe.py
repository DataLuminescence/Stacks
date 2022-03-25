from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

# model the class after the user table from our database
class Recipe:
    db = "recipes"
    def __init__( self , data ):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.under_30 = data["under_30"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#  checks if user entered appropriate data into input fields in home page
    @staticmethod
    def validate_recipe(form_data):
        pass

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipies JOIN users ON recipies.user_id = users.id;"
        results = connectToMySQL("recipies_db").query_db(query)
        