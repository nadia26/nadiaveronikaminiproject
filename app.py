from flask import Flask,render_template,request


app=Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login ():
    if request.method=="GET":
        return render_template('login.html')
    else:
        return redirect(url_for('home'))

@app.route("/register")
def register():
    if request.method=="GET":
        return render_template('register.html', message = "")
    else:
        password = request.form["password"]
        confirm = request.form["confirm_password"]
        if (password == confirm):
            username = request.form["username"]
            name = request.form["name"]
            #check if existing username
            #add user
            return redirect(url_for('home'))
        else:
            return render_template('register.html', message = "passwords don't match")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.debug=True
    app.run()
