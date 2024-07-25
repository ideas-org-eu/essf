from flask import request, jsonify
from essf.models.ethics_model import check_ethics
from essf.models.sustainability_model import check_sustainability

def configure_routes(app):
    @app.route('/api/evaluate/ethics', methods=['POST'])
    def evaluate_ethics():
        content = request.json
        result = check_ethics(content)
        return jsonify(result)

    @app.route('/api/evaluate/sustainability', methods=['POST'])
    def evaluate_sustainability():
        content = request.json
        result = check_sustainability(content)
        return jsonify(result)
