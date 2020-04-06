from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("localhost", 27017)
db = client.dbsparta


@app.route("/")
def home():
    return render_template("homework4.html")


@app.route("/orders", methods=["POST"])
def post_orders():
    name_received = request.form["name_give"]
    count_received = request.form["count_give"]
    address_received = request.form["address_give"]
    phone_received = request.form["phone_give"]

    order = {
        "name": name_received,
        "count": count_received,
        "address": address_received,
        "phone": phone_received
    }

    db.orders.insert_one(order)
    return jsonify({"result": "success", "msg": "주문이 완료되었습니다."})


@app.route("/orders", methods=["GET"])
def get_orders():
    order = list(db.orders.find({}, {"_id": 0}))
    return jsonify({"result": "success", "msg": "주문을 받아왔습니다.", "order": order})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
