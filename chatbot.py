import google.generativeai as genai
import os

# Set your API key
genai.configure(api_key=os.getenv("GENAI_API_KEY"))
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = genai.chat.completions.create(
        model="your-model-name",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({"response": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)
# Replace 'your-model-name' with the actual model you want to use
# Make sure to set the GENAI_API_KEY environment variable with your API key
