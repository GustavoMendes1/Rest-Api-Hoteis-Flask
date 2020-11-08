from flask_restful import Resource, Api, reqparse
from models.hotel import HotelModel
hoteis =[
    {
        'hotel_id': '1', 
        'nome': 'Teste1',
        'estrelas': 4.3, 
        'diaria': 380.90,
        'cidade' : 'Rio de janeiro'
    },
    {
        'hotel_id': '2', 
        'nome': 'Teste2',
        'estrelas': 4.3, 
        'diaria': 380.90,
        'cidade' : 'Rio de janeiro'
    },
    {
        'hotel_id': '3', 
        'nome': 'Teste3',
        'estrelas': 4.3, 
        'diaria': 380.90,
        'cidade' : 'Rio de janeiro'
    }
]

class Hoteis(Resource):
    
    def get(self):
        return {'hoteis':hoteis}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def findHotelById(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.findHotelById(hotel_id)
        if hotel:
            return hotel
        return{'message': 'Hotel not found.'},404

    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id,**dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200


    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id,**dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.findHotelById(hotel_id)

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel,200

        hoteis.append(novo_hotel)
        return novo_hotel,201
        

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id']!= hotel_id]
        print(hoteis)
        return {'message':'Hotel deletado.'}