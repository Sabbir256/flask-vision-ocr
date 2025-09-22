from flask import Blueprint, request, jsonify

ocr_bp = Blueprint('ocr', __name__)

@ocr_bp.route('/extract-text', methods=['POST'])
def extract_text():
    return jsonify({"message": "this is extracted text"}), 200