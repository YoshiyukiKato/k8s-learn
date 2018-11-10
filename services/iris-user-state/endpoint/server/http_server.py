from flask import Flask, jsonify, request
from state import user_service
from state import iris_service

user = user_service.UserStateService()
iris = iris_service.IrisStateService()
app = Flask(__name__)


@app.route('/<string:user_id>', methods=["GET"])
def get(user_id):
    return jsonify({"state": user.get(user_id)})


@app.route('/<string:user_id>', methods=["POST"])
def update(user_id):
    try:
        iris_id = request.json["iris_id"]
        user.update(user_id, iris.get(iris_id))
        return jsonify({"status": "success"})
    except Exception as e:
        # logging e
        print(e)
        return jsonify({"status": "fail"})


app.run(host='0.0.0.0', port=8080, debug=True)
