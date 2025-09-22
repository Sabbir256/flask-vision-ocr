from flask import Blueprint, request, jsonify
from app.utils.validators import validate_file
from werkzeug.exceptions import RequestEntityTooLarge

ocr_bp = Blueprint('ocr', __name__)

@ocr_bp.route('/extract-text', methods=['POST'])
def extract_text():
    try:
        if 'file' not in request.files:
            return jsonify({"success": False, "message": "No file provided"}), 400
        
        file = request.files['file']
        
        if not validate_file(file):
            return jsonify({"success": False, "message": "Invalid file type"}), 400
        
        return jsonify({"success": True, "text": "Extracted text"}), 200
    
    except RequestEntityTooLarge:
        return jsonify({
            "success": False, 
            "message": "Uploaded file is too large. Maximum file size is 10MB."
        }), 413
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500