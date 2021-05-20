from django.shortcuts import render
import pymysql

def sample(request):
    return render (request, "sample.html")

def base(request):
    return render(request, "base.html")
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def gallary(request):
    return render(request, "gallary.html")

def login(request, em, password):
    db=pymysql.connect(host='localhost',user ='root', passwd='root', database='djangop')
    cursor = db.cursor()
    val = [em]
    key= "select * from customer where email = %s"
    cursor.execute(key,val)
    res = cursor.fetchall()
    db.commit()
    return render(request,"login.html",{'db1':db,'email1':em,'password':int(password),'res1':res})