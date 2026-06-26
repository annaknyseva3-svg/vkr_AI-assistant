"""
API-эндпоинт для генерации коммерческого предложения.
"""
from flask import Blueprint, request, jsonify, render_template
from app.models.generator import ProposalGenerator

generate_bp = Blueprint('generate', __name__)
generator = ProposalGenerator()

@generate_bp.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'GET':
        return render_template('generate.html')
    
    data = request.get_json() or {}
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    
    try:
        proposal = generator.generate(query)
        return jsonify({'proposal': proposal}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
