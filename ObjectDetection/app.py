from flask import Flask, jsonify, request
from inference_sdk import InferenceHTTPClient
import os
from werkzeug.utils import secure_filename

# Create a Flask instance
app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Create a directory for uploaded files
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Initialize the inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="zBWOOZ0KzvHmEfcIAgmL"
)

# Food label and calorie information
food_info = {
    0: {"name": "Ayam Bakar", "calories": 165},
    1: {"name": "Ayam Goreng", "calories": 250},
    2: {"name": "Bakso", "calories": 150},
    3: {"name": "Bakwan", "calories": 200},
    4: {"name": "Batagor", "calories": 220},
    5: {"name": "Bihun", "calories": 109},
    7: {"name": "Capcay", "calories": 70},
    9: {"name": "Gado-Gado", "calories": 123},
    10: {"name": "Ikan Goreng", "calories": 230},
    11: {"name": "Kerupuk", "calories": 502},
    12: {"name": "Martabak Telur", "calories": 367},
    13: {"name": "Mie", "calories": 138},
    14: {"name": "Nasi Goreng", "calories": 250},
    15: {"name": "Nasi Putih", "calories": 130},
    16: {"name": "Nugget", "calories": 300},
    17: {"name": "Opor Ayam", "calories": 182},
    18: {"name": "Pempek", "calories": 212},
    19: {"name": "Rendang", "calories": 195},
    20: {"name": "Roti", "calories": 265},
    21: {"name": "Sate", "calories": 220},
    22: {"name": "Sosis", "calories": 310},
    23: {"name": "Soto", "calories": 90},
    24: {"name": "Steak", "calories": 271},
    25: {"name": "Tahu", "calories": 76},
    26: {"name": "Telur", "calories": 155},
    27: {"name": "Tempe", "calories": 190},
    28: {"name": "Terong Balado", "calories": 65},
    29: {"name": "Tumis Kangkung", "calories": 43},
    30: {"name": "Udang", "calories": 99},
}

def allowed_file(filename):
    """Check if the uploaded file is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Home page with a form to upload an image."""
    return '''
        <!doctype html>
        <title>Image Upload</title>
        <h1>Upload an image to predict calories</h1>
        <form method="post" enctype="multipart/form-data" action="/result">
          <input type="file" name="image">
          <input type="submit" value="Upload">
        </form>
    '''

@app.route('/result', methods=['POST'])
def upload():
    """Handle the image upload and run the inference."""
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided."}), 400

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({"error": "No image file selected."}), 400

    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(file_path)

        # Run detection on the uploaded image
        try:
            # Use the CLIENT to infer
            response = CLIENT.infer(file_path, model_id="dataset-9cro2/1")
            predictions = response.get('predictions', [])
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        detection_results = []
        for prediction in predictions:
            class_id = prediction.get('class_id')
            confidence = prediction.get('confidence')
            
            # Map class_id to food_info
            food_info_entry = food_info.get(class_id, {"name": "Unknown", "calories": 0})
            food_name = food_info_entry["name"]
            calories = food_info_entry["calories"]

            detection_results.append({
                "food_name": food_name,
                "calories": calories,
            })

        return jsonify({
            "detection_results": detection_results
        }), 200
    else:
        return jsonify({"error": "Invalid file type."}), 400

if __name__ == '__main__':
    app.run(debug=True)
