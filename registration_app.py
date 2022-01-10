from flask import Flask, request


app = Flask(__name__)

@app.route('/registration', methods = ["POST"])
def get_userdata():
    if request.method == "POST":
        # Receive login, password
        login = request.form.get("login")
        password = request.form.get("password")
        passwordRepite = request.form.get("passwordRepite")
        if password != passwordRepite:
            print("Wrong passwordRepite")


    return (f"Welcome!{login}")