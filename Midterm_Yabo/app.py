from calendar import error
from crypt import methods
from idlelib.iomenu import errors

from flask import Flask, render_template, request, render_template_string
from pyexpat.errors import messages

app = Flask(__name__)

@app.route("/", methods=['GET'])
def contact_form():
    return render_template_string('contact_form.html')

@app.route("/submit", methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    subject = request.form.get('subject')
    custom_subject = request.form.get('custom_subject')
    contact_methods = request.form.getlist('contact_methods')
    agreement = request.form.get('agreement')

    errors: list = []

    if not name or not email or not phone or not message:
        errors.appends("All fields except custom subject must be filled.")

    if not phone.isdigit():
        errors.append("Phone number must be numeric.")

    if subject == "Other" and not other_subject:






