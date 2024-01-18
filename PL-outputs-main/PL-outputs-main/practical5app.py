from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Define a route that returns a "Hello, World!" message
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Define a route for the /about page (GET request)
@app.route('/about')
def about():
    return 'This is the About page.'

# Define a route for the /submit page (POST request)
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get data from the submitted form
        data = request.form.get('input_data')
        return f'The submitted data is: {data}'
    else:
        # If someone tries to access /submit with a GET request
        return 'Invalid request method. Please use a POST request.'

# Run the application if the script is executed
if __name__ == '__main__':
    app.run(debug=True)
