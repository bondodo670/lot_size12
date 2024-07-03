from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        current_lot_size = float(request.form['current_lot_size'])
        current_loss = float(request.form['current_loss'])
        risk_amount = float(request.form['risk_amount'])
        
        new_lot_size = current_lot_size * (risk_amount / current_loss)
        return jsonify({'new_lot_size': f"{new_lot_size:.2f}"})
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
app = Flask(__name__)