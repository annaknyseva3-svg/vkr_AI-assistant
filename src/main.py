"""
Точка входа в приложение. Flask-сервер с маршрутами.
"""
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os

from app.routes.generate import generate_bp
from app.database.db_manager import init_db

load_dotenv()

app = Flask(__name__)

# Регистрация маршрутов
app.register_blueprint(generate_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
