from flask import request, jsonify
from models.ethics_model import check_ethics
from models.sustainability_model import check_sustainability
from utils.validators import validate_input

def configure_routes(app):

    @app.route('/api/evaluate/ethics', methods=['POST'])
    def evaluate_ethics():
        try:
            content = request.json
            is_valid, error_message = validate_input(content)
            if not is_valid:
                return jsonify({"error": error_message}), 400
            result = check_ethics(content)
            return jsonify(result)
        except Exception as e:
            app.logger.error(f"Error in evaluate_ethics: {str(e)}")
            return jsonify({"error": "An internal error occurred."}), 500

    @app.route('/api/evaluate/sustainability', methods=['POST'])
    def evaluate_sustainability():
        try:
            content = request.json
            is_valid, error_message = validate_input(content)
            if not is_valid:
                return jsonify({"error": error_message}), 400
            result = check_sustainability(content)
            return jsonify(result)
        except Exception as e:
            app.logger.error(f"Error in evaluate_sustainability: {str(e)}")
            return jsonify({"error": "An internal error occurred."}), 500
