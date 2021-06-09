from flask import Flask,jsonify
from app.chat import predict
app =Flask(__name__)
@app.route('/message/<string:ms>',methods=["GET"])
def message(ms):
    try:
        prediction=predict(ms)
        return jsonify(prediction)
    except:
        return jsonify({'error': 'error during prediction'})