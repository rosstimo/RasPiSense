from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
        "Tim": {"age": 19, "gender": "male"},
        "Bill": {"age": 28, "gender": "male"}
        }


class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self, name):
        print(name)
        return {"data": "Posted"}

api.add_resource(HelloWorld,"/helloworld/<string:name>")

if __name__ == "__main__":
	app.run(debug=True)