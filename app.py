from flask import Flask, render_template, request
from db import db
import utilities as uti

app=Flask(__name__)

# Rendering index.html file
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html',date=uti.get_date(), res=uti.get_weather(), quote=uti.generate_quote())
    
# Route to store data through a from, includes form validation
@app.route('/store_data',methods=['GET','POST'])
def store_data():
    invalid_pass_str = "Invalid password entered, valid password should be a combination of a-z, A-Z, 0-9 and !,@,#,$,%,&"
    if request.method=='POST':
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        form_validated = uti.form_validate(email=email, password=password)
        if form_validated ==  True:
            store_data_res = db.store_data(name=name, email=email, password=password)
            return render_template("index.html", date=uti.get_date(), res=uti.get_weather(), store_data_res=f"{store_data_res}. Following data has been stored: {name}, {email}, {password[:4] + '*' * (len(password) - 4)}", quote=uti.generate_quote())
        elif form_validated == "Invalid Email":
            return render_template("index.html", date=uti.get_date(), res=uti.get_weather(), store_data_res="Invalid Email", quote=uti.generate_quote())    
        else:
            return render_template("index.html", date=uti.get_date(), res=uti.get_weather(), store_data_res=invalid_pass_str, quote=uti.generate_quote())    

# Route to fetch form responses
@app.route('/form_responses',methods=['GET'])
def form_responses():
    form_responses = db.get_all_data()
    return render_template("form_responses.html", form_responses=form_responses)

# Route to download database data into a file
@app.route('/download_data',methods=['GET','POST'])
def download_data():
    download_data = db.download_db_data()
    return download_data

# Driver code
if __name__=="__main__":
    app.run(debug=True)