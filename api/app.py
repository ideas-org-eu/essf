from flask import Flask, render_template
from api.endpoints import configure_routes


app = Flask(__name__, template_folder='../templates')

# Register routes
configure_routes(app)

# Route for index.html
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Failed to start the server: {str(e)}")
