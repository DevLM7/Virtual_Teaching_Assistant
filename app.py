from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os
from answer_engine import build_answer

app = Flask(__name__)
CORS(app)

@app.route("/api/", methods=["POST"])
def answer_question():
    try:
        data = request.get_json()

        question = data.get("question")
        image_data = data.get("image")

        if not question:
            return jsonify({"error": "Missing 'question' field"}), 400

        if image_data:
            image_bytes = base64.b64decode(image_data)
            with open("uploaded_image.webp", "wb") as img_file:
                img_file.write(image_bytes)
            

        response = build_answer(question)
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
