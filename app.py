from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    raw = request.data.decode('utf-8')

    # Tenta parsear direto
    try:
        data = json.loads(raw)
        return jsonify(data)
    except Exception as e1:
        # Tenta "consertar" aspas duplas perdidas (comum do output JS escapado)
        try:
            fixed = raw.replace('\n', '').replace('\r', '')
            fixed = fixed.replace("'", '"')
            data = json.loads(fixed)
            return jsonify(data)
        except Exception as e2:
            return jsonify({
                'erro': 'Não foi possível parsear o JSON.',
                'msg1': str(e1),
                'msg2': str(e2),
                'input': raw
            }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
