from sql_alchemy import hotels_api
class UserModel (hotels_api.Model):
    __tablename__ = 'users'

    users_id = hotels_api.Column(hotels_api.Integer, primary_key = True)
    login = hotels_api.Column(hotels_api.String(40))
    password = hotels_api.Column(hotels_api.String(40))
    

    def __init__(self, login, password): #constructor
        self.login = login
        self.password = password

    
    def json():
        return {
            'user_id' : self.user_id,
            'login' : self.login
        }
    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id = user_id).first()
        if user:
            return user
        return None

    def save_user(self):
        hotels_api.session.add(self)
        hotels_api.session.commit()

    def delete_user(self):
        hotels_api.session.delete(self)
        hotels_api.session.commit()