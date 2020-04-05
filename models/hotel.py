from sql_alchemy import hotels_api
class HotelModel (hotels_api.Model):
    __tablename__ = 'hotels'

    hotel_id = hotels_api.Column(hotels_api.String, primary_key = True)
    name = hotels_api.Column(hotels_api.String(80))
    avg = hotels_api.Column(hotels_api.Float(precision=1))
    daily = hotels_api.Column(hotels_api.Float(precision =2))
    city = hotels_api.Column(hotels_api.String(40))
    

    def __init__(self, hotel_id, name, avg, daily, city): #constructor
        self.hotel_id = hotel_id
        self.name = name
        self.avg = avg
        self.daily = daily
        self.city = city
    
    def json():
        return {
            'hotel_id' : self.hotel_id,
            'name' : self.name,
            'avg' : self.avg,
            'daily': self.daily,
            'city' : self.city
        }
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id = hotel_id).first()
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        hotels_api.session.add(self)
        hotels_api.session.commit()

    def update_hotel(self, name, avg, daily, city):
        self.name = name
        self.avg = avg
        self.daily = daily
        self.city = city

    def delete_hotel(self):
        hotels_api.session.delete(self)
        hotels_api.session.commit()