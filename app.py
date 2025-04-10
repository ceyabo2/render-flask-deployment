from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You could save these details to a database or send via email
        return render_template('contact.html', name=name, email=email, message=message)
    return render_template('contact.html', name=None, email=None, message=None)

if __name__ == "__main__":
    app.run(debug=True)
