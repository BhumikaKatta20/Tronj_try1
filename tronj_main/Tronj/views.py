from django.shortcuts import redirect,render
import sqlite3
from Tronj.forms import RegistrationForm,FresherForm,CompanyRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Tronj.models import Quiz_data,company_details,code_base,Avilable_work,Company_Profile,Employee,emp_Education,skilltest
from datetime import date,time,timedelta
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.db.models import Q
import numpy as np
import sqlite3
import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import StrMethodFormatter
import random
a= 0
lang='a'
marks=0
username=' '
cod= pd.read_csv('Tronj/coding_quiz.csv')
code=0
quiz = pd.read_csv('Tronj/quiz.csv')
base=quiz[quiz['Department'] == 'web']
cod_base=cod
randomlist=[]
first=second=third=fourth=fifth=sec_first=sec_second=sec_third=0
# Create your views here.
backgrd='palegoldenrod'

def posted_job(request,id):

	company=Avilable_work.objects.get(id=id)
	sk_lng=company.Skills_Required
	if sk_lng=="python":
		sk='Python Programming'
	if sk_lng=="Csharp":
		sk = 'C# Programming'
	if sk_lng=="web":
		sk = 'Web Designing'
	if sk_lng=="C":
		sk = 'C Programming'
	if sk_lng=="Cadvance":
		sk = 'C++ Programming'
	if sk_lng=="java":
		sk = 'java Programming'
	if sk_lng=="netframe":
		sk = '.netFreame Programming'
	if sk_lng=="PHP":
		sk = 'PHP Programming'

	return render(request,'Tronj/company/job_posted.html',{'backgrd':backgrd,'Fdata':company,
		'sk':sk,'sk_lng':sk_lng})

def	posted_job_update(request):
	ida = request.GET['id']
	status = request.GET['sta']
	Emp_email=request.GET['Emp_email']
	app_up = Avilable_work.objects.filter(id=ida)
	app_up.update(status=status)
	Cdata=Avilable_work.objects.filter(company=request.user)
	email = '1220tronj@gmail.com'
	password = 'Trobhuam#@1.'
	send_to_email = Emp_email
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	message="Your application number:\t"+ida+"\nApplication Status:\t"+status
	# subj=Employee+'resume for work based on:'+Skills_Required
	# print(subj)
	msg['Subject'] = "Update on your Application"
	# Attach the message to the MIMEMultipart object
	msg.attach(MIMEText(message, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
	server.sendmail(email, send_to_email, text)
	server.quit()
	return render(request,'Tronj/company/application.html',{'backgrd':backgrd,'Cdata':Cdata})
def register(request):
	if request.method == 'POST':
		form =RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'index.html' )
	else:
		form = RegistrationForm()
	backgrd = 'wal.jpg'
	return render(request, 'Tronj/register.html', {'form': form,'backgrd':backgrd})
def Com_signup(request):
	if request.method == 'POST':
		form =CompanyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'index.html' )
	else:
		form = CompanyRegistrationForm()
	backgrd = 'wal.jpg'
	return render(request, 'Tronj/registration/company_signup.html', {'form': form,'backgrd':backgrd})
def signin(request):

	return render(request,'Tronj/registration/signin.html',{'backgrd':backgrd})
def index(request):
	import sqlite3
	DBgame = sqlite3.connect('Tronj_db.sqlite3')
	game = DBgame.cursor()
	daa=game.execute(
		"SELECT * from Tronj_company_details;")
	DBgame.commit()
	print(daa)
	dat = pd.DataFrame(daa)
	print(dat)
	graph=0
	backgrd = 'palegoldenrod'
	parcontent = 'color: grey'
	fig, ax = plt.subplots()
	dat[4].value_counts().plot(ax=ax, kind='pie',)
	plt.savefig('Tronj\static\\app\images\output.png')
	#plt.savefig('output.png')
	headlingcontent = 'color: black'
	return render(request,'index.html',{'backgrd':backgrd,'parcontent':parcontent,'headlingcontent':headlingcontent,'graph':graph})
def info(request,id):
	company=company_details.objects.get(id=id)
	return render(request,'Tronj/company/info.html',{'c':company,'backgrd':backgrd})

def appli_info(request,id):

	company=Avilable_work.objects.get(id=id)
	return render(request,'Tronj/company/appli_info.html',{'backgrd':backgrd,'c':company})
def QA_Check(request):
	Ans1 = str(request.GET['A1'])
	Ans2 = str(request.GET['A2'])

	if request.user.is_staff:
		Fdata = Company_Profile.objects.get(user=request.user)
		backgrd = 'back30.jpg'
	else:
		Fdata = Employee.objects.get(user=request.user)
		backgrd = 'back7.jpg'
	answer1=Fdata.A1.upper()
	print(answer1)
	cont = {'user': request.user, 'Fdata': Fdata, 'backgrd': backgrd}
	if Fdata.A1.upper()==Ans1.upper() and Fdata.A2.upper()==Ans2.upper():
		return render(request, 'Tronj/registration/ConfQuestion_verifyirm.html', cont)
	else:
		return render(request, 'Tronj/registration/reset_password.html', cont)


def sub(request):
	Company_name = request.GET['Company_name']
	stippend= request.GET['stipend']
	CEmail=request.GET['CEmail']
	Skills_Required=request.GET['Skills_Required']
	Start_of_intern=request.GET['Start_of_intern']
	Fdata = Employee.objects.get(user=request.user)
	phone=str(Fdata.Phone_number)
	print(phone)
	subject = 'Resume for python'  # The subject line '''++'''
	first_part = '''<body><div style="width:90%;"><hr><div><h3><br>'''+str(request.user)+'''</h3><h4>'''+Fdata.Address+''' <br>'''+Fdata.city+'''<br>'''+Fdata.State+'''<br>Postal Code: '''+str(Fdata.Postal_code)+'''<br>Ph.no- '''+phone+'''<br>email:'''+request.user.email+'''</h4></div><br><hr>'''
	second_part = '''<h2>Career Objectives:</h2><br><p style="font-size:15px;">  '''+Fdata.Carrer_Objective+'''</p><br><br>.'''
	ed = '''<table border="1" cellspacing="4" cellpadding="2" style="margin-left:2%;"><tr style="font-size:20px;margin:10px 10px 10px 10px"><th>Educatoin details</th><th>Qualification</th><th>Institute</th><th>Board</th><th>Passed out Year</th><th>Percentage</th>'''
	SSLC = '''<tr style="font-size:13px;"><td  colspan="2">SSLC</td><td>'''+Fdata.SSLC_name+'''</td><td>'''+Fdata.SSLC_board+'''</td><td>'''+str(Fdata.SSLC_passed_year)+'''</td><td>'''+str(Fdata.SSLC_Percentage)+'''</td></tr>'''
	PUC = '''<tr style="font-size:13px;"><td>PUC</td><td>'''+Fdata.PUC_IN+'''</td><td>'''+Fdata.PUC_name+'''</td><td>'''+Fdata.PUC_board+'''</td><td>'''+str(Fdata.PUC_passed_year)+'''</td><td>'''+str(Fdata.PUC_Percentage)+'''</td></tr>'''
	DEGREE = '''<tr style="font-size:13px;"><td>Graduation</td><td>'''+Fdata.Graduation_IN+'''</td><td>'''+Fdata.Graduation_name+'''</td><td>'''+Fdata.Graduation_board+'''</td><td>'''+str(Fdata.Graduation_passed_year)+'''</td><td>'''+str(Fdata.Graduation_Percentage)+'''</td></tr>'''
	PostDEGREE = '''<tr style="font-size:13px;"><td>Post Graduation</td><td>'''+Fdata.PostGraduation_IN+'''</td><td>'''+Fdata.PostGraduation_name+'''</td><td>'''+Fdata.PostGraduation_board+'''</td><td>'''+str(Fdata.PostGraduation_passed_year)+'''</td><td>'''+str(Fdata.PostGraduation_Percentage)+'''</td></tr></table>'''
	third_part = ed + SSLC + PUC + DEGREE + PostDEGREE
	f = '''<h2>Personal Data:</h2><h4>Father- '''+Fdata.Father_Name+'''<br>Date of Birth-'''+str(Fdata.Date_of_birth)+'''<br>Languages Known- '''+Fdata.Communication_lng+'''<br>'''
	o = '''Marriage Status- '''+Fdata.Marriage_status+'''<br>Strengths- '''+Fdata.Strength+'''</h4>'''
	fourth_part = f + o
	fivth_part = 'Declaration- I hereby declare that the information given above is true and best of my knowledge</div></body>'

	Question1 = request.GET['Question1']
	Answer1 = request.GET['Answer1']
	Question2 = request.GET['Question2']
	Answer2 = request.GET['Answer2']
	Question3 = request.GET['Question3']
	Answer3 = request.GET['Answer3']
	additional=Question1+'\n'+Answer1+'\n'+Question2+'\n'+Answer2+'\n'+Question3+'\n'+Answer3+'\n'
	message = first_part + second_part  + third_part + fourth_part + fivth_part

	status="Applied"
	company=Company_name
	Employeee=request.user

	#insertfield=[company,status,stipend,Employee,Employee_email,Question1,Question2,Question3,Answer1,Answer2,Answer3,Skills_Required,Start_of_intern ,CEmail]
	temp = Avilable_work(company=Company_name,status=status,stipend=stippend,Employee=Employeee,Employee_email=request.user.email,
						   Question1=Question1,Question2=Question2,Question3=Question3,Answer1=Answer1,Answer2=Answer2,Answer3=Answer3,
						   Skills_Required=Skills_Required,CEmail=CEmail
	)
	temp.save()
	email = '1220Tronj@gmail.com'
	password = 'Trobhuam#@1.'
	email = '1220tronj@gmail.com'
	password = 'Trobhuam#@1.'
	send_to_email = CEmail
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	subj=str(Employee)+'resume for work based on:'+Skills_Required
	print(subj)
	msg['Subject'] ="resume"
	#Attach the message to the MIMEMultipart object
	msg.attach(MIMEText(message, 'html'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
	server.sendmail(email, send_to_email, text)
	server.quit()
	Cdata = Avilable_work.objects.filter(Employee=request.user)
	return render(request,'Tronj/Employee/Eapplication.html',{'backgrd':backgrd,'Cdata':Cdata})

def myAccount(request):
	if request.user.is_staff:
		Fdata = Company_Profile.objects.get(user=request.user)
		Fdataa = Company_Profile.objects.get(user=request.user)
		backgrd = 'back30.jpg'
	else:
		Fdata = Employee.objects.get(user=request.user)
		Fdataa=emp_Education.objects.get(user=request.user)
		backgrd='grey'
	cont={'user':request.user,'Fdataa':Fdataa,'Fdata':Fdata,'backgrd':backgrd	}
	return render(request,'Tronj/myAccount.html',cont)
def edit_Profile(request):
	if request.user.is_staff:
		Fdata = Company_Profile.objects.get(user=request.user)
		print(" ")
		backgrd = 'back7.jpg'
	else:
		Fdata = Employee.objects.get(user=request.user)
		backgrd = 'back7.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	cont={'user':request.user,'Fdata':Fdata,'backgrd':backgrd	}
	return render(request,'Tronj/edit_Profile.html',cont)
def Edu_Content(request):
	if request.user.is_staff:
		Fdata =  Company_Profile.objects.get(user=request.user)
		backgrd = 'back30.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	else:
		Fdata = emp_Education.objects.get(user=request.user)
		backgrd = 'back7.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	cont={'user':request.user,'Fdata':Fdata,'backgrd':backgrd	}
	return render(request,'Tronj/registration/Edu_Content.html',cont)
def Expre_Content(request):
	if request.user.is_staff:
		Fdata =  Company_Profile.objects.get(user=request.user)
		backgrd = 'back30.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	else:
		Fdata = Employee.objects.get(user=request.user)
		backgrd = 'back7.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	cont={'user':request.user,'Fdata':Fdata,'backgrd':backgrd	}
	return render(request,'Tronj/registration/Expre_Content.html',cont)

def Question_verify(request):
	username = request.GET['username']
	u = User.objects.get(username=username)
	d=u.id
	lib =sqlite3.connect('Tronj_db.sqlite3')
	task = lib.cursor()
	if u.is_staff==True:
		daa = pd.DataFrame(lib.execute(
			"SELECT * from Tronj_Company_Profile where user_id=="+str(d)+";"))

	else:
		daa = pd.DataFrame(lib.execute(
			"SELECT Q1,Q2 from Tronj_Employee where user_id=="+str(d)+";"))

	print(daa)
	if len(daa.loc[0, 0]) > 10 and len(daa.loc[0, 1]) > 10:
		Q1 = daa.loc[0, 0]
		Q2 = daa.loc[0, 1]
	else:
		Q1 = "Enter the email address"
		Q2 =  "Enter your Lastname"

	cont = {'backgrd': backgrd,'Q1':Q1,'Q2':Q2,'username':username}
	return render(request, 'Tronj/registration/reset_password.html', cont)
def ans_verify(request):
	username=request.GET['username']
	A1=request.GET['A1']
	A2=request.GET['A2']

	u = User.objects.get(username=username)
	d=u.id
	lib =sqlite3.connect('Tronj_db.sqlite3')
	task = lib.cursor()
	if u.is_staff==True:
		daa = pd.DataFrame(lib.execute(
			"SELECT Q1,Q2 from Tronj_Company_Profile where user_id=="+str(d)+";"))
		ans=pd.DataFrame(lib.execute(
			"SELECT A1,A2 from Tronj_Company_Profile where user_id=="+str(d)+";"))

	else:
		daa = pd.DataFrame(lib.execute(
			"SELECT Q1,Q2 from Tronj_Employee where user_id=="+str(d)+";"))
		ans=pd.DataFrame(lib.execute(
			"SELECT A1,A2 from Tronj_Employee where user_id=="+str(d)+";"))
	ansbase=ans=pd.DataFrame(lib.execute(
			"SELECT email,last_name from auth_user where id=="+str(d)+";"))
	print(daa)
	if len(ans.loc[0, 0]) >= 1 and len(ans.loc[0, 1]) >= 1:
		ans1=ans.loc[0,0]
		ans2=ans.loc[0,1]
	else:
		ans1 = ansbase.loc[0, 0]
		ans2 = ansbase.loc[0, 1]
	print(ans1.upper())
	print(ans2.upper())
	if ans1.upper()==A1.upper() and ans2.upper()==A2.upper():
		backgrd = 'back30.jpg'
		# print(daa.loc[0:45],daa.iloc[0:43])
		# print(daa[46], daa[44])
		cont = {'backgrd': backgrd,'msg':'verification successfull','username':username}
		return render(request, 'Tronj/registration/Confirm.html', cont)
	else:
		backgrd = 'back30.jpg'
		#print(daa.loc[0:45],daa.iloc[0:43])
		#print(daa[46], daa[44])
		if len(daa.loc[0, 0]) > 10 and len(daa.loc[0, 1]) > 10:
			Q1 = daa.loc[0, 0]
			Q2 = daa.loc[0, 1]
		else:
			Q1 = "Enter the email address"
			Q2 = "Enter your Lastname"
		print(Q1)
		print(Q2)
		msg="Incorrect answere"
		cont = {'backgrd': backgrd,'Q1':Q1,'Q2':Q2,'username':username,'msg':msg}
		return render(request, 'Tronj/registration/reset_password.html', cont)

def resetquestion(request):
	if request.user.is_staff:
		Fdata =  Company_Profile.objects.get(user=request.user)
		backgrd = 'back30.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	else:
		Fdata = Employee.objects.get(user=request.user)
		backgrd = 'back7.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	cont={'user':request.user,'Fdata':Fdata,'backgrd':backgrd	}
	return render(request,'Tronj/registration/reset_password.html',cont)
def QA_set(request):
	Q1=request.GET['Q1']
	A1=request.GET['A1']
	Q2=request.GET['Q2']
	A2=request.GET['A2']

	if request.user.is_staff:
		Fdata = Company_Profile.objects.filter(user=request.user).update(Q1=Q1, Q2=Q2, A1=A1, A2=A2)
		backgrd = 'back30.jpg'
	else:
		Fdata = Employee.objects.filter(user=request.user).update(Q1=Q1, Q2=Q2, A1=A1, A2=A2)
		backgrd = 'back7.jpg'
	cont={'user':request.user,'Fdata':Fdata,'backgrd':backgrd	}
	return render(request,'Tronj/registration/reset_password.html',cont)

def email_verify(request):
	if request.user.is_authenticated:
		backgrd = 'back30.jpg'
		CEmail = request.user.email
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	else:
		backgrd = 'back7.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	global code
	code=random.randint(10000,( 99999))
	message="<h1> Your verfication code is....</h1><br><h3>Code:"+str(code)
	CEmail=request.user.email
	email = '1220tronj@gmail.com'
	password = 'Trobhuam#@1.'
	send_to_email = CEmail
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	# subj=Employee+'resume for work based on:'+Skills_Required
	# print(subj)
	msg['Subject'] = "Verfication code"
	# Attach the message to the MIMEMultipart object
	msg.attach(MIMEText(message, 'html'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
	server.sendmail(email, send_to_email, text)
	server.quit()

	new_password='Bhuvana#@1.'
	#u = User.objects.get(username=request.user)
	#u.set_password(new_password)
	#u.save()
	cont = {'user': request.user,'backgrd': backgrd}
	return render(request, 'Tronj/registration/email_verify.html', cont)
def authen_email_confirm(request):
	global code
	print(code)
	verification =request.GET['Verification']
	username= request.user
	useremail= request.user.email
	print(username)
	print(verification)
	msg=" "
	if str(code)==verification:
		msg="Verification successsfull"
		print(msg)
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg,'username':username}
		return render(request, 'Tronj/registration/Confirm.html', cont)
	#new_password='Bhuvana#@1.'
	#u = User.objects.get(username=request.user)
	#u.set_password(new_password)
	#u.save()
	else:
		msg="Verfifcation unsuccessful"
		print(msg)
		cont = {'user': request.user,  'backgrd': backgrd,'msg':msg,'username':username,'useremail':useremail}
		return render(request, 'Tronj/registration/email_verify_second.html', cont)
def email_confirm(request):
	global code
	print(code)
	verfication = int(request.GET['Verification'])
	print(verfication)
	username= request.GET['username']
	useremail= request.GET['useremail']
	print(username)
	msg=" "
	if code==verfication:
		msg="Verification successsfull"
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg,'username':username}
		return render(request, 'Tronj/registration/Confirm.html', cont)
	#new_password='Bhuvana#@1.'
	#u = User.objects.get(username=request.user)
	#u.set_password(new_password)
	#u.save()
	else:
		msg="Verfifcation unsuccessful"
		cont = {'user': request.user,  'backgrd': backgrd,'msg':msg,'username':username,'useremail':useremail}
		return render(request, 'Tronj/registration/log.html', cont)
def Confirm(request):

	entered = request.GET['entered']
	re_entered = request.GET['re_entered']
	msg = " "
	if len(entered) == 0 or len(re_entered) == 0:
		msg = "Please fill the fields"
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg}
		return render(request, 'Tronj/registration/Confirm.html', cont)
	elif entered != re_entered:
		msg = "Password did not match"
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg}
		return render(request, 'Tronj/registration/Confirm.html', cont)
	elif len(entered) < 8:
		msg = msg + "Password is too-short"
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg}
		return render(request, 'Tronj/registration/Confirm.html', cont)
	else:
		msg = "Done!."
		print(msg)
		# ew_password='Bhuvana#@1.'
		username=str(request.user)
		u = User.objects.get(username=username)
		u.set_password(entered)
		u.save()
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg}
		return render(request, 'Tronj/registration/confirmation.html', cont)

def fConfirm(request):
	global code
	username = request.GET['username']

	entered= request.GET['entered']
	re_entered = request.GET['re_entered']
	msg=" "
	print(username)
	if len(entered)==0 or len(re_entered)==0:
		msg="Please fill the fields"
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg, 'username': username, }
		return render(request, 'Tronj/registration/Confirm.html', cont)
	elif entered!=re_entered:
		msg = "Password did not match"
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg, 'username': username, }
		return render(request, 'Tronj/registration/Confirm.html', cont)
	elif len(entered)<8:
		msg=msg+"Password is too-short"
		cont = {'user': request.user, 'backgrd': backgrd, 'msg': msg, 'username': username, }
		return render(request, 'Tronj/registration/Confirm.html', cont)
	else:

		msg = "Done!."
		#ew_password='Bhuvana#@1.'
		u = User.objects.get(username=username)
		u.set_password(entered)
		u.save()
		cont = {'user': request.user,  'backgrd': backgrd,'msg':msg,'username':username,}
		return render(request, 'Tronj/registration/confirmation.html', cont)
def femail_verify(request):
	global username
	username = request.GET['username']
	print(username)
	try:
		u = User.objects.get(username=username)
		useremail=u.email
		global code
		code = random.randint(10000,( 99999))
		message = "<h1> Your verfication code is....</h1><br><h3>Code:" +str(code)
		CEmail = u.email
		email = '1220tronj@gmail.com'
		password = 'Trobhuam#@1.'
		send_to_email = CEmail
		msg = MIMEMultipart()
		msg['From'] = email
		msg['To'] = send_to_email
		# subj=Employee+'resume for work based on:'+Skills_Required
		# print(subj)
		msg['Subject'] = "Verfication code"
		# Attach the message to the MIMEMultipart object
		msg.attach(MIMEText(message, 'html'))

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(email, password)
		text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
		server.sendmail(email, send_to_email, text)
		server.quit()

		return render(request, 'Tronj/registration/email_verify.html', {'backgrd': backgrd,'username':username,'useremail':useremail})
	except:
		errormsg = "The username is Case sensitive.\n Retry or The given user is does not exists"
		return render(request, 'Tronj/registration/forgot.html', {'backgrd': backgrd, 'errormsg': errormsg})
def ansforgot(request):
	username = request.GET['username']
	print(username)
	try:
		u = User.objects.get(username=username)
		username = request.GET['username']
		u = User.objects.get(username=username)
		d = u.id
		lib = sqlite3.connect('Tronj_db.sqlite3')
		task = lib.cursor()
		if u.is_staff == True:
			daa = pd.DataFrame(lib.execute(
				"SELECT Q1,Q2 from Tronj_Company_Profile where user_id==" + str(d) + ";"))

		else:
			daa = pd.DataFrame(lib.execute(
				"SELECT Q1,Q2 from Tronj_Employee where user_id==" + str(d) + ";"))
		print(daa)
		print(daa.loc[0, 1])
		print(daa.loc[0, 0])
		backgrd = 'back30.jpg'
		if len(daa.loc[0, 0]) > 10 and len(daa.loc[0, 1]) > 10:
			Q1 = daa.loc[0, 0]
			Q2 = daa.loc[0, 1]
		else:
			Q1 = "Enter the email address"
			Q2 = "Enter your Lastname"
		cont = {'backgrd': backgrd, 'Q1': Q1, 'Q2': Q2, 'username': username}
		return render(request, 'Tronj/registration/reset_password.html', cont)
	except:
		errormsg = "The username is Case sensitive.\n Retry or The given user is does not exists"
		return render(request, 'Tronj/registration/ansforgo.html', {'backgrd': backgrd, 'errormsg': errormsg})
	#new_password='Bhuvana#@1.'
	#u = User.objects.get(username=request.user)
	#u.set_password(new_password)
	#u.save()
	#cont = {'backgrd': backgrd}
	#return render(request, 'Tronj/registration/email_verify.html', cont)
def freset_password(request):
	username = request.GET['username']
	try:
		u = User.objects.get(username=username)
		return render(request, 'Tronj/registration/reset_password.html', {'backgrd': backgrd})
	except:
		errormsg="The username is Case sensitive.\n Retry or The given user is does not exists"
		return render(request, 'Tronj/registration/forgot.html', {'backgrd': backgrd,'errormsg':errormsg})
def ansbaseforgot(request):

	return render(request, 'Tronj/registration/ansforgo.html', {'user': request.user, 'backgrd': backgrd})

def forgot(request):

	return render(request, 'Tronj/registration/forgot.html', {'user': request.user, 'backgrd': backgrd})


def edit(request):

		
	return render(request,'Tronj/edit.html',{'user':request.user,'backgrd':backgrd})

def skill_test(request):
	backgrd = 'back10.jpg'
	return render(request,'Tronj/skilltest.html',{'user':request.user,'backgrd':backgrd})


def round1(request):
	global base, cod_base, lang
	lang = request.GET['lan']
	de_date=date(2020, 1, 20)
	sk=skilltest.objects.get(user=request.user)
	print("Selected language is:", lang)
	predate =date(2020,3,20)
	trail=0
	flag=False
	print()
	if lang=="python":
		predate=sk.python_Date
		trail=sk.python_count
		sub='Python Programming'
		marks=sk.python
	if lang=="Csharp":
		predate = sk.Csharp_Date
		trail = sk.Csharp_count
		sub = 'C# Programming'
		marks = sk.Csharp
	if lang=="web":
		predate = sk.web_Date
		trail = sk.web_count
		sub = 'Web Designing'
		marks = sk.web
	if lang=="C":
		predate = sk.C_Date
		trail = sk.C_count
		sub = 'C Programming'
		marks = sk.C
	if lang=="Cadvance":
		predate = sk.Cadvance_Date
		trail = sk.Cadvance_count
		sub = 'C++ Programming'
		marks = sk.Cadvance
	if lang=="java":
		predate = sk.java_Date
		trail = sk.java_count
		sub = 'java Programming'
		marks = sk.java
	if lang=="netframe":
		predate = sk.netframe_Date
		trail = sk.netframe_count
		sub = '.netFreame Programming'
		marks = sk.netframe
	if lang=="PHP":
		predate = sk.PHP_Date
		trail = sk.PHP_count
		sub = 'PHP Programming'
		marks = sk.PHP
	present=date.today()
	#
	valid_chek_date= present- timedelta(days=7)
	print('all information \n 	predate:',predate,'\nde_date:',de_date,'\nvalid_chek_date',valid_chek_date)
	if (predate == de_date or de_date > valid_chek_date) and trail<4:

		cod_base = cod[cod['Department'] == lang]
		cod_base = cod_base.reset_index()
		base = quiz[quiz['Department'] == lang]
		base = base.reset_index()
		global randomlist
		randomlist = []
		while len(randomlist) <= 4:
			n = random.randint(0, (len(base) - 1))
			flag = 0
			for m in randomlist:
				if m == n:
					flag = 1
			if flag == 0:
				randomlist.append(n)
			print(randomlist)
		global first, second, third, fourth, fifth
		first = randomlist[0]
		second = randomlist[1]
		third = randomlist[2]
		fourth = randomlist[3]
		fifth = randomlist[4]
		print('questions')
		print(base.loc[first], base.loc[second], base.loc[third], base.loc[fourth], base.loc[fifth])
		print(' the round one function')
		Q1 = Quiz_data()
		Q2 = Quiz_data()
		Q3 = Quiz_data()
		Q4 = Quiz_data()
		Q5 = Quiz_data()
		Q1.question = base.loc[first, 'Question']
		Q1.option1 = base.loc[first, 'op1']
		Q1.option2 = base.loc[first, 'op2']
		Q1.option3 = base.loc[first, 'op3']
		Q1.option4 = base.loc[first, 'op4']
		Q1.group = 'group1'
		Q2.question = base.loc[second, 'Question']
		Q2.option1 = base.loc[second, 'op1']
		Q2.option2 = base.loc[second, 'op2']
		Q2.option3 = base.loc[second, 'op3']
		Q2.option4 = base.loc[second, 'op4']
		Q2.group = 'group2'
		Q3.question = base.loc[third, 'Question']
		Q3.option1 = base.loc[third, 'op1']
		Q3.option2 = base.loc[third, 'op2']
		Q3.option3 = base.loc[third, 'op3']
		Q3.option4 = base.loc[third, 'op4']
		Q3.group = 'group3'
		Q4.question = base.loc[fourth, 'Question']
		Q4.option1 = base.loc[fourth, 'op1']
		Q4.option2 = base.loc[fourth, 'op2']
		Q4.option3 = base.loc[fourth, 'op3']
		Q4.option4 = base.loc[fourth, 'op4']
		Q4.group = 'group4'
		Q5.question = base.loc[fifth, 'Question']
		Q5.option1 = base.loc[fifth, 'op1']
		Q5.option2 = base.loc[fifth, 'op2']
		Q5.option3 = base.loc[fifth, 'op3']
		Q5.option4 = base.loc[fifth, 'op4']
		Q5.group = 'group5'
		backgrd = 'back10.jpg'
		Question_set = [Q1, Q2, Q3, Q4, Q5]
		return render(request, 'Tronj/quiz/round1.html',
					  {'backgrd': backgrd, 'user': request.user, 'language': lang, 'val': Question_set})
	else:
		print('the flase part')
		return render(request, 'Tronj/quiz/quize_timeout.html',{
			'sub':sub,'predate':predate,'trail':trail,'marks':marks
		}
					 )













def round2(request):
	if request.user.is_staff:
		backgrd = 'back30.jpg'
	else:
		backgrd = 'back7.jpg'
	print(base)
	print('/n/n')
	print(lang)
	print('')
	print(cod_base)
	global marks
	marks=0

	try:
		Ans1=request.GET['group1']
	except:
		Ans1='Nothing'
	try:
		Ans2=request.GET['group2']
	except:
		Ans2='Nothing'
	try:
		Ans3=request.GET['group3']
	except:
		Ans3='Nothing'
	try:
		Ans4=request.GET['group4']
	except:
		Ans4='Nothing'
	try:
		Ans5=request.GET['group5']
	except:
		Ans5='Nothing'
	print(Ans1,Ans2,Ans3,Ans4,Ans5)
	global first,second,third,fourth,fifth
	print(first,second,third,fourth,fifth)
	if Ans1==base.loc[first,'Answer']:
		marks=marks+20
	if Ans2==base.loc[second,'Answer']:
		marks=marks+20
	if Ans3==base.loc[third,'Answer']:
		marks=marks+20
	if Ans4==base.loc[fourth,'Answer']:
		marks=marks+20
	if Ans5==base.loc[fifth,'Answer']:
		marks=marks+20
	print(marks)
	print(cod_base)
	q1=code_base()
	q2=code_base()
	q3=code_base()
	while len(randomlist) <= 2:
		n = random.randint(0, (len(cod_base)-1))
		flag = 0
		for m in randomlist:
			if m == n:
				flag = 1
		if flag == 0:
			randomlist.append(n)
	global sec_first,sec_second,sec_third

	sec_first =randomlist[0]
	sec_second = randomlist[1]
	sec_third = randomlist[2]
	print('the value',randomlist)
	print(cod_base.loc[sec_first],cod_base.loc[sec_second],cod_base.loc[sec_third])
	q1.question=cod_base.loc[sec_first,'Question']
	q1.group='first'
	q2.question=cod_base.loc[sec_second,'Question']
	q2.group='second'
	q3.question=cod_base.loc[sec_third,'Question']
	q3.group='third'
	print(cod_base.loc[sec_first,'Question'])
	print(cod_base.loc[sec_second,'Question'])
	print(cod_base.loc[sec_third,'Question'])
	question_set={q1,q2,q3}
	print('round1:',marks)
	return render(request,'Tronj/quiz/round2.html',{'backgrd':backgrd,'user':request.user,'valu':question_set})

def result(request):
	print('/n/n/n/n/n')
	print(lang)

	rawA1=request.GET['first']
	rawA2=request.GET['second']
	rawA3=request.GET['third']
	Ans1=rawA1.split()
	Ans2=rawA2.split()
	Ans3=rawA3.split()

	if request.user.is_staff:
		backgrd = 'back30.jpg'
	else:
		backgrd = 'back7.jpg'
	global sec_first, sec_second, sec_third

	print(sec_first, sec_second, sec_third)
	cans1=(cod_base.loc[sec_first,'Keywords']).split()
	cans2=(cod_base.loc[sec_second,'Keywords']).split()
	cans3=(cod_base.loc[sec_third,'Keywords']).split()
	print(cans1)
	print('**************************************************************************************')
	print('caluculation')
	canstotal =( len(cans3) + len(cans2) + len(cans1))*10

	print(canstotal)
	Total=0

	for given in Ans1:
		for req in cans1:
			if given.startswith(req):
				print(given)
				Total=Total+10
	for given in Ans2:
		for req in cans2:
			if given.startswith(req):
				Total=Total+10
				print(given)
				print(Total)
	for given in Ans3:
		for req in cans3:
			if given.startswith(req):
				Total=Total+10
				print(given)
				print(Total)
	if Total==0:
		Total=1
	print(Total)
	print(Ans1)
	print(Ans2)
	print(Ans3)
	print('bcskjbcsa')
	print(marks,Total)
	print(marks,'+',Total,')/100+',canstotal,')*100')
	scored=(((marks+Total)/(100+canstotal))*100)
	print('score:',scored)
	tem=Employee.objects.get(user=request.user)
	print('database value',tem.python)
	print('calculated value',Total)
	sk = skilltest.objects.get(user=request.user)
	if lang=="python":
		predate = sk.python_Date
		trail = (sk.python_count +1)
		skilltest.objects.filter(user=request.user).update(python_Date=date.today(),python_count=trail)
		if tem.python<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(python=scored)
			print('dadadadadadadadadadad')
	if lang=="Csharp":
		predate = sk.Csharp_Date
		trail = (sk.Csharp_count + 1)
		skilltest.objects.filter(user=request.user).update(Csharp_Date=date.today(), Csharp_count=trail)
		if tem.Csharp<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(Csharp=scored)
			print('dadadadadadadadadadad')
	if lang=="web":
		predate = sk.web_Date
		trail = (sk.web_count + 1)
		skilltest.objects.filter(user=request.user).update(web_Date=date.today(), web_count=trail)
		if tem.web<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(web=scored)
			print('dadadadadadadadadadad')
	if lang=="C":
		predate = sk.C_Date
		trail = (sk.C_count + 1)
		skilltest.objects.filter(user=request.user).update(C_Date=date.today(), C_count=trail)
		if tem.C<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(C=scored)
			print('dadadadadadadadadadad')
	if lang=="Cadvance":
		predate = sk.Cadvance_Date
		trail = (sk.Cadvance_count + 1)
		skilltest.objects.filter(user=request.user).update(Cadvance_Date=date.today(), Cadvance_count=trail)
		if tem.Cadvance<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(Cadvance=scored)
			print('dadadadadadadadadadad')
	if lang=="java":
		predate = sk.java_Date
		trail = (sk.java_count + 1)
		skilltest.objects.filter(user=request.user).update(java_Date=date.today(), java_count=trail)
		if tem.java<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(java=scored)
			print('dadadadadadadadadadad')
	if lang=="netframe":
		predate = sk.netframe_Date
		trail = (sk.netframe_count + 1)
		skilltest.objects.filter(user=request.user).update(netframe_Date=date.today(), netframe_count=trail)
		if tem.netframe<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(netframe=scored)
			print('dadadadadadadadadadad')
	if lang=="PHP":
		predate = sk.PHP_Date
		trail = (sk.PHP_count + 1)
		skilltest.objects.filter(user=request.user).update(PHP_Date=date.today(), PHP_count=trail)
		if tem.PHP<=scored:
			Fdata=skilltest.objects.filter(user=request.user).update(PHP=scored)
			print('dadadadadadadadadadad')
	Fdata=Employee.objects.get(user=request.user)
	return render(request,'Tronj/quiz/result.html',{'Fdata':Fdata,'backgrd':backgrd,'user':request.user, 'scored':scored,'lang':lang})

def to_apply(request):
	Quiz_data()
	cata=' '
	print('@@@@@@@@@@@@@@@@@@')
	parcontent = 'color: white'
	headlingcontent = 'color: floralwhite'
	if request.user.is_staff:
		backgrd = 'back10.jpg'
		Fdata = Company_Profile.objects.get(user=request.user)


	else:

		backgrd='back10.jpg'
		Fdata = Employee.objects.get(user=request.user)
		Fdata = skilltest.objects.get(user=request.user)
		cata = company_details.objects.filter(
			Q(python__lte=Fdata.python) & Q(Csharp__lte=Fdata.Csharp) & Q(web__lte=Fdata.web) & Q(C__lte=Fdata.C) & Q(
				Cadvance__lte=Fdata.Cadvance) & Q(java__lte=Fdata.java) & Q(netframe__lte=Fdata.netframe) & Q(
				PHP__lte=Fdata.PHP))
		print(cata)
		for a in cata:
			print(a.id)

	#cata = company_details.objects.filter(python=Fdata.python)
	return render(request,'Tronj/to_apply.html',{'backgrd':backgrd,'user':request.user,'company_data':cata,'Fdata':Fdata})

def company_form(request):
	python=request.GET['python']
	C = request.GET['C']
	java = request.GET['java']
	Cadvance = request.GET['Cadvance']
	web=request.GET['web']
	PHP = request.GET['PHP']
	netframe=request.GET['netframe']
	Cloud = request.GET['Cloud']
	qw=[python,Cloud,web,C,Cadvance,java,netframe,PHP]
	if request.user.is_staff:
		backgrd = 'back30.jpg'
		Fdata = Company_Profile.objects.get(user=request.user)
		Company_Profile.objects.filter(user=request.user).update(python=python, Cloud=Cloud, web=web, C=C,
																 Cadvance=Cadvance, java=java, netframe=netframe,
																 PHP=PHP)
	else:
		backgrd = 'back7.jpg'
		Fdata = Employee.objects.get(user=request.user)
	return render(request,'Tronj/myAccount.html',{'backgrd':backgrd,'Fdata':Fdata})


def Empeditpre(request):
	if request.user.is_staff:
		Fdata = Company_Profile.objects.get(user=request.user)
		backgrd = 'back30.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	else:
		Fdata = Employee.objects.get(user=request.user)
		backgrd = 'back7.jpg'
		parcontent = 'color: white'
		headlingcontent = 'color: floralwhite'
	try:
		Date_of_birth = request.GET['DOB']
	except:
		Date_of_birth=Fdata.Date_of_birth
	flag = False
	Address = request.GET['Address']
	Address_error = ' '
	a = re.findall(r'[@!$%]', Address)
	print(a)
	if len(a) > 0:
		flag = True
		Address_error = '@ , !, %, $, ^ are not vaild'
	first_name = request.GET['first_name']
	first_name_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', first_name)
	if len(a) > 0:
		flag = True
		first_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	Father_Name = request.GET['Father_Name']
	Father_Name_error = ' '
	a = re.findall(r'[0-9@!$%^]', Father_Name)
	if len(a) > 0:
		flag = True
		Father_Name_error = 'numbers, @ , !, %, $, ^ are not vaild'
	city = request.GET['city']
	city_error = ' '
	a = re.findall(r'[0-9@!$%^]', city)

	if len(a) > 0:
		flag = True
		city_error = 'numbers, @ , !, %, $, ^ are not vaild'
	last_name = request.GET['last_name']
	last_name_error = ' '
	a = re.findall(r'[0-9@!$%^]', last_name)
	if len(a) > 0:
		flag = True
		last_name_error = 'numbers, @ , !, %, $, ^ are not vaild'
	State = request.GET['State']
	State_error = ' '
	a = re.findall(r'[0-9@!$%^]', State)
	if len(a) > 0:
		flag = True
		State_error = 'numbers, @ , !, %, $, ^ are not vaild'
	email = request.GET['email']
	email_error = ' '
	a = re.findall(r'[@]', email)
	b = re.findall(r'[.]', email)
	if len(a) != 1 or len(b) > 1:
		flag = True
		email_error = " Invalid"
	Postal_code_error = ' '
	try:
		Postal_code = int(request.GET['Postal_code'])
		p = request.GET['Postal_code']
		if  len(p) != 6:
			flag = True
			Postal_code_error = 'only 6 digits are valid'
	except:
		Postal_code_error = 'only numbers are valid'
	ph_no_error = ' '
	try:
		Phone_number = int(request.GET['Phone_number'])
		p=str(Phone_number)
		if len(p) != 10:
			flag = True
			ph_no_error = 'only 10 digits phone number is vaild.'
	except:
		Postal_code_error = 'only numbers are valid'
	Communication_lng = request.GET['Communication_lng']
	Communication_lng_error=' '
	a = re.findall(r'[0-9@!$%^#*]', Communication_lng)
	if len(a) > 0 :#and len(Communication_lng)<10
		flag = True
		Communication_lng_error = 'numbers, @ , !, %, $, ^ #, * and less than 10 Characters or too short are not vaild'
	Carrer_Objective = request.GET['Carrer_Objective']
	Carrer_Objective_error=' '
	a = re.findall(r'[0-9@!$%*#^]', Carrer_Objective)
	if len(a) > 0 or len(Carrer_Objective)<250:
		flag = True
		Carrer_Objective_error = 'numbers, @ , !, %, $, ^ #, * and less than 250 Characters or too short are not vaild'
	Marriage_status = request.GET['Marriage_status']
	Strength = request.GET['Strength']
	Strength_error=' '
	a = re.findall(r'[0-9@!$%#*^]', Strength)
	if len(a) > 0 or len(Strength)<100:
		flag = True
		Strength_error = 'numbers, @ , !, %, $, ^ #, * and less than 100 Characters or too short are not vaild'
	if flag==True:
		Fdata = Employee.objects.get(user=request.user)
		print('the error',Strength_error)
		return render(request, 'Tronj/edit_Profile.html', {'backgrd': backgrd, 'Fdata': Fdata,
					'Address_error':Address_error,'first_name_error':first_name_error,'city_error':city_error,
					'last_name_error':last_name_error,'State_error':State_error,'ph_no_error':ph_no_error,'Postal_code_error':Postal_code_error,
					'Communication_lng_error':Communication_lng_error,'Carrer_Objective_error':Carrer_Objective_error,'Father_Name_error':Father_Name_error
					,'Strength_error':Strength_error})
	else:

		Fdata = Employee.objects.filter(user=request.user).update(Father_Name=Father_Name,
																  Date_of_birth=Date_of_birth,
																  Address=Address, city=city,
																  State=State, Postal_code=Postal_code,
																  Phone_number=Phone_number,
																  Communication_lng=Communication_lng,
																  Carrer_Objective=Carrer_Objective,
																  Marriage_status=Marriage_status,Strength=Strength)
		Fdata = Employee.objects.get(user=request.user)
		cont = {'user': request.user, 'Fdata': Fdata, 'backgrd': backgrd}
		return render(request, 'Tronj/confirm/edit_Profile.html', cont)
def comeditpre(request):
	flag=False
	Address=request.GET['Address']
	Address_error=' '
	a=re.findall(r'[@!$%]',Address)
	print(a)
	if len(a)>0:
		flag=True
		Address_error='@ , !, %, $, ^ are not vaild'
	first_name = request.GET['first_name']
	first_name_error=' '
	a = re.findall(r'[0-9@!$%^]', first_name)
	if len(a) > 0:
		flag = True
		first_name_error='numbers, @ , !, %, $, ^ are not vaild'
	city = request.GET['city']
	city_error=' '
	a = re.findall(r'[0-9@!$%^]', city)

	if len(a) > 0:
		flag = True
		city_error='numbers, @ , !, %, $, ^ are not vaild'
	last_name = request.GET['last_name']
	last_name_error=' '
	a = re.findall(r'[0-9@!$%^]', last_name)
	if len(a) > 0:
		flag = True
		last_name_error='numbers, @ , !, %, $, ^ are not vaild'
	State = request.GET['State']
	State_error=' '
	a = re.findall(r'[0-9@!$%^]', State)
	if len(a) > 0:
		flag = True
		State_error='numbers, @ , !, %, $, ^ are not vaild'
	email=request.GET['email']
	email_error = ' '
	a = re.findall(r'[@]', email)
	b = re.findall(r'[.]', email)
	if len(a) != 1 or len(b) > 1:
		flag = True
		email_error = " Invalid"

	Postal_code_error = ' '
	try:
		Postal_code = int(request.GET['Postal_code'])
		p=str(Postal_code)
		if len(p) != 6:
			flag = True
			Postal_code_error = 'only 6 digits are valid'
	except:
		Postal_code_error = 'only numbers are valid'
	ph_no_error = ' '
	try:
		Phone_number = int(request.GET['Phone_number'])
		p=str(Phone_number)
		if len(p) != 10:
			flag = True
			ph_no_error = 'only 10 digits phone number is vaild.'
	except:
		ph_no_error = 'only numbers are valid'
	about_company=request.GET['about_company']
	about_company_error=' '
	if len(about_company) < 100:
		flag = True
		print(len(about_company),' is the length')
		print(about_company)
		about_company_error = 'minimum 100 Characters or given is too short '
	if request.user.is_staff:
		backgrd = 'back30.jpg'
		Fdata = Company_Profile.objects.get(user=request.user)
	else:
		backgrd = 'back7.jpg'
		Fdata = Employee.objects.get(user=request.user)

	#qw=[python,Cloud,web,C,Cadvance,java,netframe,PHP]
	if flag==True:
		Fdata = Company_Profile.objects.get(user=request.user)

		return render(request, 'Tronj/edit_Profile.html', {'backgrd': backgrd, 'Fdata': Fdata,
					'Address_error':Address_error,'first_name_error':first_name_error,'city_error':city_error,
					'last_name_error':last_name_error,'State_error':State_error,'about_company_error':about_company_error,
					'ph_no_error':ph_no_error,'Postal_code_error':Postal_code_error})
	else:
		if request.user.is_staff:
			backgrd = 'back30.jpg'

			a=User.objects.filter(id=request.user.id).update(first_name=first_name)
			Company_Profile.objects.filter(user=request.user).update(Address=Address,State=State,Postal_code=Postal_code,
																	 Phone_number=Phone_number,about_company=about_company,city=city)
			#auth_user.objects.filter(user=request.user).update(first_name=first_name,city=city,last_name=last_name)														 )
			Fdata = Company_Profile.objects.get(user=request.user)
		return render(request,'Tronj/confirm/edit_Profile.html',{'backgrd':backgrd,'Fdata':Fdata})
def eduedit(request):
	flag=False
	SSLC_name =request.GET['SSLC_name']
	SSLC_name_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', SSLC_name)
	if len(a) > 0:
		flag = True
		SSLC_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	SSLC_board =request.GET['SSLC_board']
	SSLC_board_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', SSLC_board)
	if len(a) > 0:
		flag = True
		SSLC_board_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	SSLC_Percentage_error = ' '
	try:
		SSLC_Percentage = int(request.GET['SSLC_Percentage'])
		if len(SSLC_Percentage) != 2:
			flag = True
			SSLC_Percentage_error = 'Invalid.'
	except:
		SSLC_Percentage_error = 'only numbers are valid'
	SSLC_passed_year_error = ' '
	try:
		SSLC_passed_year = int(request.GET['SSLC_passed_year'])
		if len(SSLC_passed_year) != 4:
			flag = True
			SSLC_passed_year_error = 'Invalid. '
	except:
		SSLC_passed_year_error = 'only numbers are valid'
	PUC_IN = request.GET['PUC_IN']
	PUC_IN_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', PUC_IN)
	if len(a) > 0:
		flag = True
		PUC_IN_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	PUC_name = request.GET['PUC_name']
	PUC_name_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', PUC_name)
	if len(a) > 0:
		flag = True
		PUC_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	PUC_board = request.GET['PUC_board']
	PUC_board_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', PUC_board)
	if len(a) > 0:
		flag = True
		PUC_board_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'


	PUC_Percentage_error = ' '
	try:
		PUC_Percentage = int(request.GET['PUC_Percentage'])
		if len(PUC_Percentage) != 2:
			flag = True
			PUC_Percentage_error = 'Invalid.'
	except:
		PUC_Percentage_error = 'only numbers are valid'
	PUC_passed_year_error = ' '
	try:
		PUC_passed_year = int(request.GET['PUC_passed_year'])
		if len(PUC_passed_year) != 4:
			flag = True
			PUC_passed_year_error = 'Invalid. '
	except:
		PUC_passed_year_error = 'only numbers are valid'

	Graduation_IN = request.GET['Graduation_IN']
	first_name_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', Graduation_IN)
	if len(a) > 0:
		flag = True
		Graduation_IN_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	Graduation_name = request.GET['Graduation_name']
	first_name_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', Graduation_name)
	if len(a) > 0:
		flag = True
		Graduation_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	Graduation_board = request.GET['Graduation_board']
	first_name_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', Graduation_board)
	if len(a) > 0:
		flag = True
		Graduation_board_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'

	Graduation_Percentage_error = ' '
	try:
		Graduation_Percentage = int(request.GET['Graduation_Percentage'])
		if len(Graduation_Percentage) != 2:
			flag = True
			Graduation_Percentage_error = 'Invalid.'
	except:
		Graduation_Percentage_error = 'only numbers are valid'
	Graduation_passed_year_error = ' '
	try:
		Graduation_passed_year = int(request.GET['Graduation_passed_year'])
		if len(Graduation_passed_year) != 4:
			flag = True
			Graduation_passed_year_error = 'Invalid. '
	except:
		Graduation_passed_year_error = 'only numbers are valid'

	PostGraduation_IN = request.GET['PostGraduation_IN']
	PostGraduation_IN_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', PostGraduation_IN)
	if len(a) > 0:
		flag = True
		PostGraduation_IN_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	PostGraduation_name = request.GET['PostGraduation_name']
	PostGraduation_name_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', PostGraduation_name)
	if len(a) > 0:
		flag = True
		PostGraduation_name_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	PostGraduation_board = request.GET['PostGraduation_board']
	PostGraduation_board_error = ' '
	a = re.findall(r'[0-9@!$%#*^]', PostGraduation_board)
	if len(a) > 0:
		flag = True
		PostGraduation_board_error = 'numbers, @, #, *, !, %, $, ^ are not vaild'
	PostGraduation_Percentage_error = ' '
	try:
		PostGraduation_Percentage = int(request.GET['PostGraduation_Percentage'])
		if len(PostGraduation_Percentage) != 2:
			flag = True
			PostGraduation_Percentage_error = 'Invalid.'
	except:
		PostGraduation_Percentage_error = 'only numbers are valid'
	PostGraduation_passed_year_error = ' '
	try:
		PostGraduation_passed_year = int(request.GET['PostGraduation_passed_year'])
		if len(PostGraduation_passed_year) != 4:
			flag = True
			PostGraduation_passed_year_error = 'Invalid. '
	except:
		PostGraduation_passed_year_error = 'only numbers are valid'

	if flag==True:
		backgrd = 'back7.jpg'
		Fdata = emp_Education.objects.get(user=request.user)
		return render(request, 'Tronj/registration/Edu_Content.html', {'backgrd': backgrd, 'Fdata': Fdata,
				'SSLC_name_error': SSLC_name_error,'SSLC_board_error': SSLC_board_error,'SSLC_Percentage_error': SSLC_Percentage_error,
			'SSLC_passed_year_error':SSLC_passed_year_error,
			'PUC_IN_error': PUC_IN_error,'PUC_name_error': PUC_name_error,' PUC_board_error': PUC_board_error,'PUC_Percentage_error':PUC_Percentage_error,
		'PUC_passed_year_error':PUC_passed_year_error,'Graduation_IN_error':Graduation_IN_error,'Graduation_name_error':Graduation_name_error,
		'Graduation_board_error':Graduation_board_error, 'Graduation_Percentage_error':Graduation_Percentage_error, 'Graduation_passed_year_error':Graduation_passed_year_error,
		'PostGraduation_IN_error':PostGraduation_IN_error, 'PostGraduation_name_error':PostGraduation_name_error, 'PostGraduation_board_error':PostGraduation_board_error
			, 'PostGraduation_Percentage_error':PostGraduation_Percentage_error, 'PostGraduation_passed_year_error':PostGraduation_passed_year_error
		})
	else:
		emp_Education.objects.filter(user=request.user).update(SSLC_name=SSLC_name,SSLC_board=SSLC_board,
													  SSLC_Percentage=SSLC_Percentage,SSLC_passed_year=SSLC_passed_year,
													  PUC_IN=PUC_IN,PUC_name=PUC_name,PUC_board=PUC_board,
													  PUC_Percentage=PUC_Percentage,PUC_passed_year=PUC_passed_year,
													  Graduation_IN=Graduation_IN,Graduation_board=Graduation_board,
													  Graduation_Percentage=Graduation_Percentage,Graduation_passed_year=Graduation_passed_year,
													  PostGraduation_IN=PostGraduation_IN,PostGraduation_name=PostGraduation_name,
													  PostGraduation_board=PostGraduation_board,PostGraduation_Percentage=PostGraduation_Percentage,
													  PostGraduation_passed_year=PostGraduation_passed_year
													)

		backgrd = 'back7.jpg'
		Fdata = emp_Education.objects.get(user=request.user)
		return render(request,'Tronj/confirm/Edu_Content.html',{'backgrd':backgrd,'Fdata':Fdata})
def Exp_edit(request):
	flag= False
	exp_Company_name=request.GET['exp_Company_name']
	exp_Company_name_error = ' '
	a = re.findall(r'[0-9@!$%^]', exp_Company_name)
	if len(a) > 0:
		flag = True
		exp_Company_name_error = 'numbers, @ , !, %, $, ^ are not vaild'
	years_of_experience_error = ' '
	try:
		years_of_experience=int(request.GET['years_of_experience'])
		if years_of_experience>7:
			flag=True
			years_of_experience_error = 'more than 7 years of experience is not accepted'
	except:
		flag=True
		years_of_experience_error = 'Type the number of years worked letters are not valid'
	experienced_programming_langauage=request.GET['experienced_programming_langauage']
	if len(a) > 0:
		flag = True
		city_error = 'numbers, @ , !, %, $, ^ are not vaild'
	if flag==True:
		backgrd = 'back30.jpg'
		Fdata = Employee.objects.get(user=request.user)
		return render(request, 'Tronj/registration/Expre_Content.html', {'backgrd': backgrd,'exp_Company_name_error':exp_Company_name_error,
			'years_of_experience_error':years_of_experience_error,'Fdata': Fdata})
	else:
		Employee.objects.filter(user=request.user).update(
			experienced_programming_langauage=experienced_programming_langauage,
			years_of_experience=years_of_experience,
			exp_Company_name=exp_Company_name
			)
		backgrd = 'back7.jpg'
		Fdata = Employee.objects.get(user=request.user)
		return render(request,'Tronj/confirm/Expre_Content.html',{'backgrd':backgrd,'Fdata':Fdata})

def joboffered(request):
	flag=False
	python = int(request.GET['python'])
	Csharp = int(request.GET['Csharp'])
	web = int(request.GET['web'])
	C = int(request.GET['C'])
	Cadvance = int(request.GET['Cadvance'])
	java = int(request.GET['java'])
	netframe = int(request.GET['netframe'])
	PHP = int(request.GET['PHP'])
	years_of_experience=int(request.GET['years_of_experience'])
	Company_name = request.GET['Company_name']
	experienced_programming_langauage = request.GET['experienced_programming_langauage']
	job_type = request.GET['job_type']
	Fdata=Company_Profile.objects.get(user=request.user)
	stipend_error = ' '
	stipend=request.GET['stipend']
	try:
		stipend = int(request.GET['stipend'])
		p = request.GET['stipend']
		if len(p) < 3:
			flag = True
			stipend_error = 'minimum 1000/- of stipend is required'
	except:
		stipend_error = 'only numbers are valid'
	Start_of_intern_error = " "
	Skills_Required=request.GET['Skills_Required']
	Start_of_intern =" "
	try:
		Start_of_intern=request.GET['Start_of_intern']
		dat=date(int(Start_of_intern[:4]),int(Start_of_intern[5:7]),int(Start_of_intern[8:]))
		da=date.today()
		if dat < da:
			Start_of_intern_error = "Invalid"
	except:
		Start_of_intern_error = "Select the date"
	jobdescription=request.GET['jobdescription']
	jobdescription_error = " "
	if len(jobdescription)<50:
		flag=True
		jobdescription_error = "Fill the field or Too short"
	email_error = " "
	email=request.GET['email']
	a = re.findall(r'[@]',email)
	b=re.findall(r'[.]',email)
	if len(a) != 1 or len(b)>1:
		flag = True
		email_error = " Invalid"
	Question1_error = " "
	Question2_error = " "
	Question3_error = " "
	Question2 = request.GET['Question2']
	if len(Question2)<10:
		flag=True
		Question2_error = "Fill the field or Too short"
	Question3 = request.GET['Question3']
	if len(Question3)<10:
		flag = True
		Question3_error = "Fill the field or Too short"
	Question1 = request.GET['Question1']
	if len(Question1)<10:
		flag = True
		Question1_error = "Fill the field or Too short"
	Address_error = " "
	Address=request.GET['Address']
	if len(Address)<10:
		flag = True
		Address_error = "Fill the field or Too short"
	city_error=" "
	city=request.GET['city']
	if len(city)<5:
		flag = True
		city_error = "Invalid or fill the field"
		print(city_error)
	Date_post = date.today()


	if len(Question1)<10:
		flag = True
		Question1_error = "Fill the field Too short"

	about_the_company=Fdata.about_company

	backgrd = 'back10.jpg'
	if flag==True:

		return render(request, 'Tronj/confirm/to_apply.html', {'user': request.user, 'Fdata': Fdata, 'backgrd': backgrd,
												   'email_error': email_error, 'stipend_error': stipend_error,
												   'Start_of_intern_error': Start_of_intern_error,
												   'jobdescription_error': jobdescription_error,
												   'Question1_error': Question1_error,
												   'Question2_error': Question2_error,
												   'Question3_error': Question3_error, 'Address_error': Address_error,
												   'city_error': city_error,
															   'stipend': stipend,
															   'about_the_company': about_the_company,
															   'job_type': job_type,
															   'Question3': Question3, 'Question2': Question2,
															   'Question1': Question1,
															   'Skills_Required': Skills_Required,
															   'Start_of_intern': Start_of_intern,
															   'jobdescription': jobdescription, 'email': email,
															   'python': python, 'Csharp': Csharp, 'web': web, 'C': C,
															   'Cadvance': Cadvance, 'java': java,
															   'netframe': netframe, 'PHP': PHP,
															   'Company_name': Company_name, 'Address': Address,
															   'city': city, 'years_of_experience': years_of_experience,
															   'experienced_programming_langauage': experienced_programming_langauage,
															   'Date_posted': Date_post
															   })
	else:
		temp=company_details(stipend=stipend,about_the_company=about_the_company,job_type=job_type,Question3=Question3,Question2=Question2,Question1=Question1,Skills_Required=Skills_Required,Start_of_intern=Start_of_intern,jobdescription=jobdescription,CEmail=email,python=python,Csharp=Csharp,web=web,C=C,Cadvance=Cadvance,java=java,netframe=netframe,PHP=PHP,Company_name=Company_name,Address=Address,city=city,years_of_experience=years_of_experience,experienced_programming_langauage=experienced_programming_langauage,Date_posted=Date_post)
		temp.save()
		Cdata = company_details.objects.filter(Company_name=request.user)
		return render(request, 'Tronj/company/Capplication.html', {'user': request.user, 'backgrd': backgrd, 'Fdata': Fdata,
			'Cdata':Cdata}
			)

def customerMain(request):
	args={'user':request.user}
	return render(request,'Tronj/home.html',args)

def Capplication(request):
	Cdata=company_details.objects.filter(Company_name=request.user)
	return render(request,'Tronj/company/Capplication.html',{'Cdata':Cdata,'backgrd':backgrd})

def	Cappli_review(request):
	backgrd = 'back10.jpg'
	Cdata=Avilable_work.objects.filter(company=request.user)
	return render(request,'Tronj/company/application.html',{'Cdata':Cdata,'backgrd':backgrd})

def	updatee(request):
	ida = request.GET['id']
	status = request.GET['sta']
	Emp_email=request.GET['Emp_email']
	app_up = Avilable_work.objects.filter(id=ida)
	app_up.update(status=status)
	Cdata=Avilable_work.objects.filter(company=request.user)
	email = '1220tronj@gmail.com'
	password = 'Trobhuam#@1.'
	send_to_email = Emp_email
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = send_to_email
	message="Your application number:\t"+ida+"\nApplication Status:\t"+status
	# subj=Employee+'resume for work based on:'+Skills_Required
	# print(subj)
	msg['Subject'] = "Update on your Application"
	# Attach the message to the MIMEMultipart object
	msg.attach(MIMEText(message, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string()  # You now need to convert the MIMEMultipart object to a string to send
	server.sendmail(email, send_to_email, text)
	server.quit()
	return render(request,'Tronj/company/application.html',{'backgrd':backgrd,'Cdata':Cdata})

def Eapplication(request):
	Cdata =Avilable_work.objects.filter(Employee=request.user)
	return render(request,'Tronj/Employee/Eapplication.html',{'backgrd':backgrd,'Cdata':Cdata})


