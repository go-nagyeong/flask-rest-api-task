from flask_restful import Resource

class MainApi(Resource):
    def get(self):
        return {
            'status': 'success',
        }