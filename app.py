from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/killswitch', methods=['GET'])
def killswitch():
    # Returns JSON with a killswitch status
    return jsonify({'kill': False})  # Set 'kill' to True to activate killswitch

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
