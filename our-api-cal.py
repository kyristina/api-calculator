from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    num1 = request.args.get('num1', type = float)
    num2 = request.args.get('num2', type = float)
    result = num1 + num2
    return jsonify({"result": result})


@app.route('/subtract', methods=['GET'])
def subtract():
    num1 = request.args.get('num1', type = float)
    num2 = request.args.get('num2', type = float)
    result = num1 - num2
    return jsonify({"result": result})


@app.route('/multiply', methods=['GET'])
def multiply():
    num1 = request.args.get('num1', type = float)
    num2 = request.args.get('num2', type = float)
    result = num1 * num2
    return jsonify({"result": result})


@app.route('/divide', methods=['GET'])
def divide():
    num1 = request.args.get('num1', type = float)
    num2 = request.args.get('num2', type = float)
    if num2 == 0:
        return jsonify({"error": "Division by zero"}), 400
    result = num1 / num2
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
