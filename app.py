from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import os

app = Flask(__name__)
CORS(app)

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        
        response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    config={
        "system_instruction": "You are a helpful AI study assistant who explains clearly."
    }
)


        ai_reply = response.text

    except Exception as e:
        ai_reply = f"Error: {str(e)}"

    return jsonify({"reply": ai_reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

