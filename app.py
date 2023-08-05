import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=["POST"])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']
    if username == 'verify' and password == '12345':
        account_sid = 'AC63a912284e734e7648f9efcc4c67e984'
        auth_token = '204794ff176fa305c6a3b0e984fa64ec'
        client = Client(account_sid, auth_token)
        verification = client.verify \
            .services('VAe5a9d5a15419befb80e10605a6918703') \
            .verifications \
            .create(to=mobile_number, channel='sms')
        print(verification.status)
        return render_template("otp_verify.html")
    else:
        return "Entered Username or Password is wrong"

if __name__ == "__main__":
    app.run()