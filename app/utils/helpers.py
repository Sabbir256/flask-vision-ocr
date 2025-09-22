from flask import jsonify

def error_response(msg: str, status_code:int=400):
    return jsonify({"success": False, "message": msg}), status_code

def success_response(data: dict):
    return jsonify({**data, **{"success": True}}), 200