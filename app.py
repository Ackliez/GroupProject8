from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    # Simple response logic
    if "hello" in user_input.lower():
        response = "Hello! How can I assist you today?"
    elif "bye" in user_input.lower():
        response = "Goodbye! Have a great day!"
    else:
        response = "I’m here to help with any questions you have!"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
