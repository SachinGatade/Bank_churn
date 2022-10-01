import numpy as np,json,pickle

class churn():
    def __init__(self,customer_id,credit_score,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country,gender):
        self.customer_id=customer_id
        self.credit_score=credit_score
        self.age=age
        self.tenure=tenure
        self.balance=balance
        self.products_number=products_number
        self.credit_card=credit_card
        self.active_member=active_member
        self.estimated_salary=estimated_salary
        self.country=country
        self.gender=gender

    def model(self):
        with open("model_rf.pickle","rb") as f:
            self.mod=pickle.load(f)

        with open("column_list.json","r") as f:
            self.cols=json.load(f)

    def final(self):
        self.model()
        arr=np.zeros(len(self.cols["column"]))

        arr[0]=self.customer_id
        arr[1]=self.credit_score
        arr[2]=self.age
        arr[3]=self.tenure
        arr[4]=self.balance
        arr[5]=self.products_number
        arr[6]=self.credit_card
        arr[7]=self.active_member
        arr[8]=self.estimated_salary

        country="country_"+self.country
        country_index=self.cols["column"].index(country)
        arr[country_index]=1

        gender="gender_"+self.gender
        gender_index=self.cols["column"].index(gender)
        arr[gender_index]=1

        output=self.mod.predict([arr])

        return output








