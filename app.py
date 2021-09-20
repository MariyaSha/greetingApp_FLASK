# from flask import Flask

# app = Flask(__name__)

# @app.route("/hi")
# def hello_world():
#     html = '''
#     <body bgcolor="black">
#     <img src="https://raw.githubusercontent.com/MariyaSha/SimpleGreetingApp/main/logo.png">
#     <br>
#     <p>Type your name to get a greeting</p>
#     <br>
#     <input type="text" id="lname" name="lname"><br><br>
#     <form method="post">
#         <button type="submit" name="greet">GREET</button>
#     </form>
#     <style>
#         body {
#             text-align: center;
#         }
#         p {
#             color: white;
#             font-family: Shanti;
#             font-size: 1.3em;
#         }
#         img {
#             margin: 200px 0 30px 0;
#         }
#         input {
#           width: 350px;
#           margin: 0 10px;
#           height: 50px;
#           border-radius: 10px;
#           font-family: Shanti;
#           font-size: 1.3em;
#           text-align: center;
#         }
#         button {
#           width: 150px;
#           margin: 20px;
#           height: 50px;
#           background-color: #008e71;
#           border: none;
#           border-radius: 10px;
#           font-family: Raleway;
#           font-size: 1.4em;
#           font-weight: 700;
#           color: white;

#         }
#         button:hover {
#             background-color: #0b6c59;
#             font-size: 1.5em;
#         }
#         input:focus {
#             outline: none;
#             border: solid 5px #00FFCE;
#         }

#     </style>
#     </body>
#     '''
#     return html

# def contact():
#     if request.method == 'POST':
#         if request.form['greet'] == 'GREET':
#             pass # do something
#         elif request.form['submit_button'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown

# def submit(): 
#     if request.method == "POST":
#         if request.form.get("lname"):
#             # do something
#             print("this happens")
#         elif request.form.get("submit_b"):
#             # do something else
#             print("orrrrr this happens")
#     elif request.method == "GET":
#             # do something
#             print("3. this happens ORRRRRRRRRRRR")

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'manbearpig_MUDMAN6'

@app.route('/hello')
def index():
    flash("what's your name?")
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    flash("Hi there " + str(request.form['name_input'] + ", great to see you!"))
    return render_template('index.html')