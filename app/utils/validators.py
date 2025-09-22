from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'tiff', 'bmp', 'gif'}

def allowed_file(filename):
    return '.' in filename \
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file(file):
    if not file or file.filename == '':
        return False
    
    filename = secure_filename(file.filename)
    if not allowed_file(filename):
        return False
    
    return True