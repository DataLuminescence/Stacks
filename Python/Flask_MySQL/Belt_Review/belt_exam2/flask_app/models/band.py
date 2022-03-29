from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

# model the class after the user table from our database
class Band:
    db = "band_together"
    def __init__( self , data ):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.band_name = data["band_name"]
        self.genre = data["genre"]
        self.homecity = data["homecity"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#  checks if user entered appropriate data into input fields in new sighting page
    @staticmethod
    def validate_register(form_data):
        is_valid = True

        if  not form_data["band_name"] or not form_data["genre"] or not form_data["homecity"]:
            flash("All fields must be filled out to proceed", "register")
            is_valid = False
        if len(form_data["band_name"]) < 2:
            flash("Band name must be at least 2 characters long!", "register")
            is_valid = False
        if len(form_data["genre"]) < 2:
            flash("Genre must be at least 2 characters long!", "register")
            is_valid = False
        if len(form_data["homecity"]) < 2:
            flash("Home City must be at least 2 characters long!", "register")
            is_valid = False

        return is_valid

    # add band into database and returns id in register_band route "/register_band"
    @classmethod
    def create_band(cls, data):
        query = """INSERT INTO bands (user_id, band_name, genre, homecity, created_at, updated_at) 
        VALUES (%(user_id)s, %(band_name)s, %(genre)s, %(homecity)s, NOW(), NOW());"""
        results = connectToMySQL(cls.db).query_db(query, data)
        
        # returns newly created user id
        return results

    # edits band in the database and returns id 
    @classmethod
    def update_band_by_band_id(cls, data):
        query = "UPDATE bands SET band_name = %(band_name)s, genre = %(genre)s, homecity = %(homecity)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        # If the user has no bands flash that
        if not results:
            flash("User has no bands in the database")
            return False
        
        return 

    # gets query information of all bands based on user id
    @classmethod
    def get_user_and_band_by_band_id(cls,data):
        query = """SELECT * FROM bands JOIN users 
                ON bands.user_id = users.id
                WHERE bands.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        if results:
            bands= cls(results[0])
            bands.creator = user.User(results[0])
            return bands


        # returns dictionary of band data associated to an id
        return results

    # gets query information of all bands based on user id
    @classmethod
    def get_all_user_and_band(cls,data): # getting all bands with founders, change name EDIT
        query = """SELECT * FROM bands JOIN users 
                ON bands.user_id = users.id;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        bands = []

        if results:
            for row in results:
                temp_band =  cls(row)
                data = {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "password": row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]
                }
                temp_band.creator = user.User(data)
                bands.append(temp_band)
        return bands
        
    # delete band in the database based on id of the band
    @classmethod
    def delete_band(cls, data):
        query = "DELETE FROM bands WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)