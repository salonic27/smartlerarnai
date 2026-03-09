import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from genai_utils import generate_text
from code_utils import generate_code
from audio_utils import generate_audio
from image_utils import generate_image

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
DEMO_MODE = os.getenv('DEMO_MODE', 'true').lower() == 'true'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/explain', methods=['POST'])
def api_explain():
    data = request.json
    topic = data.get('topic', 'Machine Learning')
    depth = data.get('depth', 'intermediate')
    
    try:
        result = generate_text(topic, depth, DEMO_MODE)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/code', methods=['POST'])
def api_code():
    data = request.json
    algorithm = data.get('algorithm', 'Neural Network')
    complexity = data.get('complexity', 'basic')
    
    try:
        result = generate_code(algorithm, complexity, DEMO_MODE)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/audio', methods=['POST'])
def api_audio():
    data = request.json
    topic = data.get('topic', 'Introduction to AI')
    
    try:
        result = generate_audio(topic, DEMO_MODE)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/image', methods=['POST'])
def api_image():
    data = request.json
    concept = data.get('concept', 'Neural Network Diagram')
    style = data.get('style', 'technical')
    
    try:
        result = generate_image(concept, style, DEMO_MODE)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
