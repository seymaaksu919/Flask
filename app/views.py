from click import Context
from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)
@app.route('/')
def Definition():
    return "<html><body><h1>İlk Flask Denemesi</h1></body></html>"

@app.route('/hello') #Adresimde Flash hello varsa bu fonksiyonu çağır.
def Hello():
    return render_template("hello.html") # Flask’ta bir HTML dosyasını tarayıcıda görüntülemek için kullanırız.


@app.route('/hello-admin') #Adresimde Flash hello varsa bu fonksiyonu çağır.
def HelloAdmin():
    return render_template("hello-admin.html") # Flask’ta bir HTML dosyasını tarayıcıda görüntülemek için kullanırız.


@app.route("/hello-user/<name>") #Değişken name şeklinde tanımlanır.
def HelloUser(name):
    if name.lower() =="admin":
        return redirect(url_for("HelloAdmin"))
    return render_template("hello-user.html",name=name)

@app.route("/add/<number1>/<number2>")
def Add(number1,number2):
    calculation= int(number1)+int(number2)
    return render_template("add.html", number1=number1,number2=number2,result=calculation)
@app.route("/login",methods=["GET","POST"])
def Login():
    if request.method =="POST":
        username=request.form["username"]
        return redirect(url_for("HelloUser",name=username))
    else:
        return render_template("login.html")


@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/result", methods=["POST"])
def Result():
    ContextData = {
    'name':request.form["name"],
    'physics':request.form["physics"],
    'maths':request.form["maths"],
    'chemistry':request.form["chemistry"]
    }
    return render_template("student_result.html", **ContextData)
