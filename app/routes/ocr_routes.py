from flask import Blueprint, request, jsonify
from werkzeug.exceptions import RequestEntityTooLarge
from app.utils.validators import validate_file
from app.utils.helpers import error_response, success_response
from app.services.ocr_service import OCRService

ocr_bp = Blueprint('ocr', __name__)
ocr_service = OCRService()

@ocr_bp.route('/extract-text', methods=['POST'])
def extract_text():
    try:
        if 'file' not in request.files:
            return error_response("No file provided")
        
        file = request.files['file']
        
        if not validate_file(file):
            return error_response("Invalid file type")
        
        result = ocr_service.extract_text_from_image(file)
        return success_response(result)
    
    except RequestEntityTooLarge:
        return error_response("Uploaded file is too large. Maximum file size is 10MB.", 413)
    except Exception as e:
        return error_response(str(e), 500)