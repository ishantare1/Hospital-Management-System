# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import mysql.connector
# Create your views here.
 
def homepage(request):
    return render(request,"index.html")

def dochome(request):
    return render(request,"doctor.html")
def doclogin(request):
    return render(request,"doctor login.html")
def docl(request):
    # if (request.method == "POST"):
    #     docId=request.POST['ID']
    #     password=request.POST['password']
    #     con = mysql.connector.connect(host="localhost", user="root", password="root", database="test", port="3306")
    #     operation = con.cursor()
    #
    #     sql = "select * from doctorlogintable55 where docId=%s,password=%s"
    #     values=(docId,password)
    #     operation.execute(sql,values)
    #     record=operation.fetchone()
    #         for data in record:
                
    return render(request, "doctor.html")


        # con.commit()
        # con.close()

def docprofile(request):
    return render(request,"docotor profile.html")
def docpass(request):
    return render(request,"doctor password.html")
def docp(request):
    docId = input("docId")
    oPass = input("oPass")
    nPass = input("nPass");
    cnPass = input("cnPass");
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="test", port="3306")
    operation = con.cursor()


    sql = "update doctorlogintable55 set docId=%s where pasword=%s"
    values = (docId,oPass,nPass,cnPass)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "doctor login.html")


def home(request):
    return render(request,"about us.html")

def front(request):
    return render(request, "appointment book.html")
def fronta(request):
    if(request.method=="POST"):
        aId=request.POST['aId']
        mId=request.POST['mId']
        fName=request.POST['fName']
        age=request.POST['age']
        gender=request.POST['gender']
        contact=request.POST['contact']
        department=request.POST['department']
        consultant=request.POST['consultant']
        date=request.POST['date']
        time=request.POST['time']

        con = mysql.connector.connect(host="localhost", user="root", password="root", database="test", port="3306")
        operation = con.cursor()

        sql = "insert into appointbooktable55 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(aId,mId,fName,age,gender,contact,department,consultant,date,time)
        operation.execute(sql,values)
        con.commit()
        con.close()
        return render(request, "index.html")


def back(request):
    return render(request,"feedback.html")
def backa(request):
     if(request.method=="POST"):
        feedbackId=request.POST['feedbackId']
        fName=request.POST['fName']
        mId=request.POST['mId']
        description=request.POST['description']
        rating=request.POST['rating']

        con = mysql.connector.connect(host="localhost", user="root", password="root", database="test", port="3306")
        operation = con.cursor()

        sql = "insert into feedbacktable55 values(%s,%s,%s,%s,%s)"
        values=(feedbackId,fName,mId,description,rating)
        operation.execute(sql,values)
        con.commit()
        con.close()
        return render(request, "index.html")


def us(request):
    return render(request,"contact us.html")

def admin(request):
    return render(request,"admin login.html")

def homepage(request):
    return render(request,"index.html")

def our(request):
    return render(request,"our services.html")

