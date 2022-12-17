from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'app/uploads'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename), buffer_size=16384)
        file.close()
        return 'File uploaded successfully'

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    print(filename)
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)
