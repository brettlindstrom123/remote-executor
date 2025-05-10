from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "remote_executor online"

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    print(f"Received TX: {data}")
    return jsonify({"status": "submitted", "tx": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
