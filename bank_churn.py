from flask import Flask,redirect,render_template,request
app=Flask(__name__)
from config import churn
import mysql.connector

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    data=request.form
    
    customer_id=int(data["customer_id"])
    credit_score=int(data["credit_score"])
    age=int(data["age"])
    tenure=int(data["tenure"])
    balance=float(data["balance"])
    products_number=int(data["products_number"])
    credit_card=int(data["credit_card"])
    active_member=int(data["active_member"])
    estimated_salary=float(data["estimated_salary"])
    country=data["country"]
    gender=data["gender"]

    result=churn(customer_id,credit_score,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country,gender).final()
    result=int(result[0])

    conn=mysql.connector.connect(host="localhost",database="sac",user="root",password="SachinG!7396")
    cur=conn.cursor()

    query="insert into bank_churn(customer_id,credit_score,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country,gender,predict) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(customer_id,credit_score,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country,gender,result)

    cur.execute(query,data)
    conn.commit()
    conn.close()

    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)


