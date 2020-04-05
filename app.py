from flask import Flask
from flask_restful import Api
from resources.hotel import Hotels, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_db():
    hotels_api.create_all()

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import hotels_api
    hotels_api.init_app(app)
    app.run(debug=True)


#http://127.0.0.1:5000/hotels