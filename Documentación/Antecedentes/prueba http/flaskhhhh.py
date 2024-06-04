from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='template')
data = {'gasto': [], 'presion': [], 'vibracion': []}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        content = request.get_json()
        gasto = content['gasto']
        presion = content['presion']
        vibracion = content['vibracion']

        # Busca si ya existe un valor para gasto, presion y vibracion
        for i, existing_data in enumerate(data['gasto']):
            if existing_data == gasto:
                data['presion'][i] = presion
                data['vibracion'][i] = vibracion
                print(f"Updated data: gasto={gasto}, presion={presion}, vibracion={vibracion}")
                return jsonify({'success': True})

        # Si no existe, agrega los nuevos valores
        data['gasto'].append(gasto)
        data['presion'].append(presion)
        data['vibracion'].append(vibracion)
        print(f"Added new data: gasto={gasto}, presion={presion}, vibracion={vibracion}")
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error receiving data: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

    try:
        content = request.get_json()
        gasto = content['gasto']
        presion = content['presion']
        vibracion = content['vibracion']
        data['gasto'].append(gasto)
        data['presion'].append(presion)
        data['vibracion'].append(vibracion)
        print(f"Received data: gasto={gasto}, presion={presion}, vibracion={vibracion}")
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error receiving data: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/get_data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')    # entonces  ejecutar en modo debuggin
