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
    
@ocr_bp.route('/bulk-extract-text', methods=['POST'])
def bulk_extract_text():
    try:
        if 'files' not in request.files:
            return error_response("No files provided")
        
        files = request.files.getlist('files')
        
        # Filter out invalid files
        files = [file for file in files if file.filename and validate_file(file)]
        
        if len(files) == 0:
            return error_response("No files provided")
        
        results: list[dict] = ocr_service.extract_text_from_images(files)
        return success_response({"data": results})
    
    except RequestEntityTooLarge:
        return error_response("Uploaded files are too large. Maximum file size is 10MB per file.", 413)
    except Exception as e:
        return error_response(str(e), 500)