from web.python_api import python_api_handler
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('user_input',type=str,location='json')
parser.add_argument('user_ip',type=str,location='json')


python_api_hl = python_api_handler()


class request_openai(Resource):

    def post(self):

        res_dict = {'code':0,'message':'success','res':''}
        args = parser.parse_args()
        user_request_input = args['user_input']
        print(f'user request in manager.py:{user_request_input}')
        user_ip=args['user_ip']
        print(f'user ip in manager.py:{user_ip}')
        try:
            res = python_api_hl.generate_massage(user_request_input,user_ip)
            print(f'user ip in manager.py:{user_ip}')
            res_dict['res'] = res
        except Exception as e:
            res_dict['code'] = 1
            res_dict['message'] = 'call failde'
            res_dict['res'] = '!!! The api call is abnormal, please check the backend log'
        return res_dict


api.add_resource(request_openai, '/request_openai')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9200,debug=True)

