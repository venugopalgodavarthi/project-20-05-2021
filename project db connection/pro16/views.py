from django.shortcuts import render
import pymysql
from django.http import HttpResponse

def sample(request):
    db = pymysql.connect(host="localhost", user="root",passwd='root', database='djangop')
    cursor=db.cursor()
    cursor.execute("select * from customer")
    res = cursor.fetchall()
    return render(request,'sample.html',{"db": db ,"res": res})

def register(request, cusid, cusname, email, phone):
    db = pymysql.connect(host="localhost", user="root", passwd='root', database='djangop')
    cursor=db.cursor()
    val = [int(cusid), str(cusname), str(email), int(phone)]
    key="insert into customer(cid, cname, email, phone)values(%s,%s,%s,%s)"
    cursor.execute(key,val)
    res=cursor.rowcount
    db.commit()
    return render(request,"register.html",{'db':db ,"res":res,'id':cusid,'name':cusname,'email':email,'phone':phone})
    
def login(request, email , password):
    db = pymysql.connect(host="localhost", user="root", passwd='root', database='djangop')
    cursor=db.cursor()
    val=[email,password]
    key="select * from customer where email=%s and phone=%s"
    cursor.execute(key,val)
    res = cursor.fetchall()
    db.commit()
    return render(request,"login.html", {'db':db,'res':res,'email':email,'pass': int(password)})