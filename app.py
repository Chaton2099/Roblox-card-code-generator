from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

def generate_roblox_code():
    def random_section(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    return f"{random_section(4)}-{random_section(4)}-{random_section(4)}-{random_section(4)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_code')
def generate_code():
    code = generate_roblox_code()
    return jsonify({"code": code})

if __name__ == '__main__':
    app.run(debug=True)
