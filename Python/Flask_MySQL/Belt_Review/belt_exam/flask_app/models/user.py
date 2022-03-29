from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import band
from flask import flash
import re  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)  

# model the class after the user table from our database
class User:
    db = "band_together"
    def __init__( self , data ):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.bands = []
    
    # add user into database and returns id to be used in program
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"""
        results = connectToMySQL(cls.db).query_db(query, data)
        
        # returns newly created user id
        return results

    # gets users in database based on their id (data)
    @classmethod
    def get_by_user_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        
        # If the length of the search is less tha 1. Didn't find a matching user
        if not results:
            flash("Id does not exist in database")
            return False
        return cls(results[0])

    #  gets user in databse based on thier email
    @classmethod
    def get_by_email(cls,data):
        # Perform a serch to see if the email(data) provided is in the server
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)

        # If the length of the search is less tha 1. Didn't find a matching user
        if not results:
            flash("Email/username does not exist in database")
            return False
        return cls(results[0])

    #  checks if user entered appropriate data into input fields in home page
    @staticmethod
    def validate_register(form_data):
        is_valid = True

        # validate that user enterred email does not exist in the db already
        if User.get_by_email(form_data):
            flash("Email is in use")
            is_valid = False 
        # validate first name to make sure its only letters, at least two characters, and it was submitted
        if len(form_data["first_name"]) < 2:
            flash("First name must be at least 2 characters long!", "register")
            is_valid = False
        elif not form_data["first_name"].isalpha():
            flash("First name must only include letters", "register")
            is_valid = False

        # validate last name to make sure its only letters, at least two characters, and it was submitted    
        if len(form_data["last_name"]) < 2:
            flash("Last name must be at least 2 characters long!", "register")
            is_valid = False
        elif not form_data["last_name"].isalpha():
            flash("Last name must only include letters", "register")
            is_valid = False

        # validate the email follows the correct email format, and it was submitted   
        if not EMAIL_REGEX.match(form_data["email"]):
            flash("Please enter a valid email", "register")
            is_valid = False

        # validate password is at least 8 characters long, and it was submitted
        if len(form_data["password"]) < 8:
            flash("Password must be at least 8 characters long!", "register")
            is_valid = False

        # validates password confirmation matches password
        if form_data["password"] !=  form_data["conf_pass"]:
            flash("Password confirmation must match password", "register")
            is_valid = False
        return is_valid

    # validates that emmal/username and password is the right combination for user
    @staticmethod
    def validate_login(form_data):
        
        is_valid = True
        
        user_from_db = User.get_by_email(form_data)

        if not user_from_db:
            flash("Invalid Email/Password")
            is_valid = False

        elif not bcrypt.check_password_hash(user_from_db.password, form_data["password"]):
            flash("Invalid Email/Password")
            is_valid = False
        # If you want to add extra password validation add here    
        return is_valid

    @classmethod
    def get_band_of_user(cls,data):
        query = "SELECT * FROM users LEFT JOIN bands ON users.id = bands.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            user = cls(results[0])
            if results[0]["bands.id"]:
                user.bands = []
                for row in results:
                    data = {
                        "user_id": row["user_id"],
                        "id": row["bands.id"],
                        "band_name": row["band_name"],
                        "music_genre": row["music_genre"],
                        "home_city": row["home_city"],
                        "created_at": row["bands.created_at"],
                        "updated_at": row["bands.updated_at"]
                    }
                user.bands.append(band.Band(data))
        return user
