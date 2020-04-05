from flask_restful import Resource, reqparse
from models.hotel import HotelModel
        
class Hotels(Resource):
    def get(self):
        return{'hotels': [hotel.json() for hotel in HotelModel.query.all()]} # SELECT * FROM HOTELS

class Hotel(Resource):
#atributos
    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank")
    arguments.add_argument('avg', type=float, required=True, help= "The field 'avg' cannot be left blank")
    arguments.add_argument('daily')
    arguments.add_argument('city')

    #get method
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'messege': 'Sorry! Hotel not found ):'}, 404
    
    # post method
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel '{}' already exists.".format(hotel_id)}, 400 #bad request

        data = Hotel.arguments.parse_args()
        new_hotel_object = HotelModel(hotel_id, **data)
        new_hotel = new_hotel_object.json()
        try:
            hotel.save_hotel()
        except: 
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500 #internal server error 
        return hotel.json(), 200

    def put(self, hotel_id):
    #put method
        #verifica se ja esxiste hotel e attualiza
        data = Hotel.arguments.parse_args()
        hotel_finded = Hotel.find_hotel(hotel_id)
        if hotel_finded:
            hotel_finded.update_hotel(**data)
            hotel_finded.save_hotel()
            return hotel_finded.json(), 200
        
        #se nao estiver cadastrado cria um novo
        hotel = HotelModel(hotel_id, **data)
        try:
            hotel.save_hotel()
        except: 
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500 #internal server error 
        
        return hotel.json(), 201 #  201 = criado


    
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except: 
                return {'message': 'An internal error ocurred trying to delete hotel.'}, 500 #internal server error 
            return {'message':'Hotel deleted.'}
        return {'message:': 'Hotel not found.'},404