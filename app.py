# pip install flask
from flask import Flask, jsonify, request, make_response
import service

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def test():
    status = 200
    try:
        return make_response(jsonify(
            {
                "status": status,
                "message": "masuk"
            }
        ), status)
    except Exception as e:
        status = 500
        e.with_traceback()
        return make_response(jsonify(
            {
                "status": status,
                "message": str(e)
            }
        ), status) 

@app.route("/list", methods=["GET"])
def list():
    status = 200
    try:
        return make_response(jsonify(
            {
                "status": status,
                "data": service.list()
            }
        ), status)
    except Exception as e:
        status = 500
        e.with_traceback()
        return make_response(jsonify(
            {
                "status": status,
                "message": str(e)
            }
        ), status) 

@app.route("/search", methods=["GET"])
def get_by_id():
    status = 200
    try:
        id = request.args.get("id")
        return make_response(jsonify(
            {
                "status": status,
                "data": service.get_by_id(id)
            }
        ), status)
    except Exception as e:
        status = 500
        e.with_traceback()
        return make_response(jsonify(
            {
                "status": status,
                "message": str(e)
            }
        ), status)
     
@app.route("/create", methods=["POST"])
def create():
    status = 200
    try:
        input = request.json
        service.create(input)
        return make_response(jsonify(
            {
                "status": status,
                "message": "Account Created Successfully"
            }
        ), status)
    except Exception as e:
        status = 500
        e.with_traceback()
        return make_response(jsonify(
            {
                "status": status,
                "message": "Something Wrong Happpened!"
            }
        ), status) 

@app.route("/update", methods=["PATCH"])
def update():
    status = 200
    try:
        id = request.args.get("id")
        input = request.json
        service.update(id, input)
        return make_response(jsonify(
            {
                "status": status,
                "message": "Account Updated Successfully"
            }
        ), status)
    except Exception as e:
        status = 500
        e.with_traceback()
        return make_response(jsonify(
            {
                "status": status,
                "message": "Something Wrong Happpened!"
            }
        ), status) 

@app.route("/delete", methods=["DELETE"])
def delete():
    status = 200
    try:
        id = request.args.get("id")
        service.delete(id)
        return make_response(jsonify(
            {
                "status": status,
                "message": "Account Deleted Successfully"
            }
        ), status)
    except Exception as e:
        status = 500
        e.with_traceback()
        return make_response(jsonify(
            {
                "status": status,
                "message": "Something Wrong Happpened!"
            }
        ), status) 

app.run()