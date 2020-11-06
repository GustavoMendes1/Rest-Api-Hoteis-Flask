from flask_restful import Resource, Api, reqparse

hoteis =[
    {
        'hotel_id': '1', 
        'nome': 'Teste1',
        'estrelas': 4.3, 
        'diraria': 380.90,
        'cidade' : 'Rio de janeiro'
    },
    {
        'hotel_id': '2', 
        'nome': 'Teste2',
        'estrelas': 4.3, 
        'diraria': 380.90,
        'cidade' : 'Rio de janeiro'
    },
    {
        'hotel_id': '3', 
        'nome': 'Teste3',
        'estrelas': 4.3, 
        'diraria': 380.90,
        'cidade' : 'Rio de janeiro'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis':hoteis}

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return{'message': 'Hotel not found.'},404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diraria')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_hotel = {
            'hotel_id' :hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diraria': dados['diraria'],
            'cidade': dados['cidade'],
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200


    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass

