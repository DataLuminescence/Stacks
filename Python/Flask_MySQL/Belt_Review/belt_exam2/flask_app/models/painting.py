from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

# model the class after the user table from our database
class Painting:
    db = "users_paintings"
    def __init__( self , data ):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.title = data["title"]
        self.description = data["description"]
        self.price = data["price"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    #--------------------------------------------------------------------------------------------------
    # validate_register - validates if user entered appropriate data into input fields for new painting
    #--------------------------------------------------------------------------------------------------

    @staticmethod
    def validate_register(form_data):
        is_valid = True

        if  not form_data["title"] or not form_data["description"] or not form_data["price"]:
            flash("All fields must be filled out to proceed", "register")
            is_valid = False
        if len(form_data["title"]) < 2:
            flash("Painting title must be at least 2 characters long!", "register")
            is_valid = False
        if len(form_data["description"]) < 10:
            flash("Description must be at least 10 characters long!", "register")
            is_valid = False
        if len(form_data["price"]) < 0:
            flash("Price must be at least 2 characters long!", "register")
            is_valid = False

        return is_valid

    #--------------------------------------------------------------------------------------------------
    # get_all_paintings - get information from all the paintings in our databse to display in dashboard
    #--------------------------------------------------------------------------------------------------

    @classmethod
    def get_all_paintings(cls,data): # getting all paintings with artists
        query = """SELECT * FROM paintings JOIN users 
                ON paintings.user_id = users.id;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        paintings = []

        if results:
            for row in results:
                temp_painting =  cls(row)
                data = {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "password": row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]
                }
                temp_painting.creator = user.User(data)
                paintings.append(temp_painting)
        return paintings



    #--------------------------------------------------------------------------------------------------
    # create_painting - add painting into database and returns id in register_painting route
    #--------------------------------------------------------------------------------------------------

    @classmethod
    def create_painting(cls, data):
        query = """INSERT INTO paintings (user_id, title, description, price, created_at, updated_at) 
        VALUES (%(user_id)s, %(title)s, %(description)s, %(price)s, NOW(), NOW());"""

        results = connectToMySQL(cls.db).query_db(query, data)
        
        # returns newly created user id
        return results

    #--------------------------------------------------------------------------------------------------
    # view_painting - view painting in the database based on id of the painting
    #--------------------------------------------------------------------------------------------------

    # gets query information of all paintings based on user id
    @classmethod
    def get_painting_by_id(cls,data):
        query = """SELECT * FROM paintings JOIN users 
                ON paintings.user_id = users.id
                WHERE paintings.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        if results:
            row = results[0]
            paintings= cls(row)
            data = {
                    "id": row["users.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "email": row["email"],
                    "password": row["password"],
                    "created_at": row["users.created_at"],
                    "updated_at": row["users.updated_at"]
                }
            paintings.creator = user.User(data)
            return paintings

        # returns dictionary of band data associated to an id
        return results

    #--------------------------------------------------------------------------------------------------
    # delete_painting - delete painting in the database based on id of the painting
    #--------------------------------------------------------------------------------------------------
    
    @classmethod
    def delete_painting(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)

    #--------------------------------------------------------------------------------------------------
    # update_painting_by_id - edit the contents of current painting data in databse
    #--------------------------------------------------------------------------------------------------

    @classmethod
    def update_painting_by_id(cls, data):
        query = "UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)

    #--------------------------------------------------------------------------------------------------
    # END
    #--------------------------------------------------------------------------------------------------