from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date
# Create your models here.
class UserProfile(models.Model):
	user = models.CharField(max_length=100,default='')
	city=models.CharField(max_length=100,default='')
	phone=models.IntegerField(default=0)


class Company_Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	Address = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=50, default='')
	State = models.CharField(max_length=50, default='')
	Postal_code = models.IntegerField(default=0)
	Phone_number = models.IntegerField(default=0)
	about_company=models.CharField(max_length=1150, default='')
	Q1 = models.CharField(max_length=150, default='')
	A1  = models.CharField(max_length=150, default='')
	Q2 = models.CharField(max_length=150, default='')
	A2 = models.CharField(max_length=150, default='')

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	Father_Name = models.CharField(max_length=150, default='')
	Date_of_birth = models.DateField("Date", default=datetime.now)
	Address = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=50, default='')
	State = models.CharField(max_length=50, default='')
	Postal_code= models.IntegerField(default=0)
	Phone_number = models.IntegerField(default=0)
	Communication_lng = models.CharField(max_length=150, default='')
	Carrer_Objective = models.CharField(max_length=500, default='')
	Marriage_status = models.CharField(max_length=50, default='')
	Strength = models.CharField(max_length=500, default='')
	years_of_experience = models.IntegerField(default=0)
	exp_Company_name = models.CharField(max_length=150, default='')
	experienced_programming_langauage = models.CharField(max_length=150, default='')
	experienced_Company_name=models.CharField(max_length=150, default='')

	Q1 = models.CharField(max_length=150, default='')
	A1 = models.CharField(max_length=150, default='')
	Q2 = models.CharField(max_length=150, default='')
	A2 = models.CharField(max_length=150, default='')
class emp_Education(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	SSLC_name = models.CharField(max_length=150, default='')
	SSLC_board = models.CharField(max_length=150, default='')
	SSLC_Percentage = models.IntegerField(default=0)
	SSLC_passed_year = models.IntegerField(default=0)
	PUC_IN = models.CharField(max_length=150, default='')
	PUC_name = models.CharField(max_length=150, default='')
	PUC_board = models.CharField(max_length=150, default='')
	PUC_Percentage = models.IntegerField(default=0)
	PUC_passed_year = models.IntegerField(default=0)
	Graduation_IN = models.CharField(max_length=150, default='')
	Graduation_name = models.CharField(max_length=150, default='')
	Graduation_board = models.CharField(max_length=150, default='')
	Graduation_Percentage = models.IntegerField(default=0)
	Graduation_passed_year = models.IntegerField(default=0)
	PostGraduation_IN = models.CharField(max_length=150, default='')
	PostGraduation = models.IntegerField(default=0)
	PostGraduation_name = models.CharField(max_length=150, default='')
	PostGraduation_board = models.CharField(max_length=150, default='')
	PostGraduation_Percentage = models.IntegerField(default=0)
	PostGraduation_passed_year = models.IntegerField(default=0)
class fresher_Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	Date_of_birth=models.DateField("Date",default=datetime.now)
	Location=models.CharField(max_length=50,default='')
	Address=models.CharField(max_length=150,default='')
	city=models.CharField(max_length=50,default='')
	Phone_number=models.IntegerField(default=0)
	python=models.IntegerField(default=0)
	Csharp=models.IntegerField(default=0)
	web=models.IntegerField(default=0)
	C=models.IntegerField(default=0)
	Cadvance=models.IntegerField(default=0)
	java=models.IntegerField(default=0)
	netframe=models.IntegerField(default=0)
	PHP=models.IntegerField(default=0)
	pincode=models.IntegerField(default=0)
	SSLC = models.IntegerField(default=0)
	PUC = models.IntegerField(default=0)
	Graduation = models.IntegerField(default=0)
	PostGraduation = models.IntegerField(default=0)
	years_of_experience = models.IntegerField(default=0)
	experienced_programming_langauage = models.CharField(max_length=150, default='')


class skilltest(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	Csharp = models.IntegerField(default=0)
	web = models.IntegerField(default=0)
	C = models.IntegerField(default=0)
	Cadvance = models.IntegerField(default=0)
	java = models.IntegerField(default=0)
	netframe = models.IntegerField(default=0)
	PHP = models.IntegerField(default=0)
	python = models.IntegerField(default=0)
	Csharp_count = models.IntegerField(default=0)
	web_count = models.IntegerField(default=0)
	C_count = models.IntegerField(default=0)
	Cadvance_count = models.IntegerField(default=0)
	java_count = models.IntegerField(default=0)
	netframe_count = models.IntegerField(default=0)
	PHP_count = models.IntegerField(default=0)
	python_count = models.IntegerField(default=0)
	Csharp_Date = models.DateField("Date", default=date(2020, 1, 20))
	web_Date = models.DateField("Date", default=date(2020, 1, 20))
	C_Date =models.DateField("Date", default=date(2020, 1, 20))
	Cadvance_Date = models.DateField("Date", default=date(2020, 1, 20))
	java_Date = models.DateField("Date", default=date(2020, 1, 20))
	netframe_Date = models.DateField("Date", default=date(2020, 1, 20))
	PHP_Date = models.DateField("Date", default=date(2020, 1, 20))
	python_Date = models.DateField("Date", default=date(2020, 1, 20))



class Avilable_work(models.Model):
	company=models.CharField(max_length=50)
	offer_id=models.IntegerField(default=0)
	status=models.CharField(max_length=50)
	stipend=models.IntegerField(default=0)
	Employee = models.CharField(max_length=50)
	Employee_email = models.CharField(max_length=50)
	Question1 = models.CharField(max_length=150)
	Question2 = models.CharField(max_length=150)
	Question3 = models.CharField(max_length=150)
	Answer1 = models.CharField(max_length=250)
	Answer2 = models.CharField(max_length=250)
	Answer3 = models.CharField(max_length=250)
	Skills_Required=models.CharField(max_length=50)
	CEmail=models.EmailField(max_length=254)


class company_details(models.Model):
	Company_name=models.CharField(max_length=50)
	Address=models.CharField(max_length=50)
	stipend=models.IntegerField(default=0)
	city=models.CharField(max_length=50)
	Skills_Required=models.CharField(max_length=50)
	Question1 = models.CharField(max_length=150,default="what is your aim?")
	Question2 = models.CharField(max_length=150,default="Why should we give you this job?")
	Question3=models.CharField(max_length=150,default="Why you want this Job?")
	job_offered=models.CharField(max_length=50)
	job_type=models.CharField(max_length=50,default="internship")
	Start_of_intern=models.DateField("Date")
	Date_posted=models.DateField("Date")
	CEmail=models.EmailField(max_length=254)
	jobdescription=models.CharField(max_length=120)
	years_of_experience=models.IntegerField()
	experienced_programming_langauage=models.CharField(max_length=120)
	python=models.IntegerField()
	Csharp=models.IntegerField()
	web=models.IntegerField()
	C=models.IntegerField()
	Cadvance=models.IntegerField()
	java=models.IntegerField()
	netframe=models.IntegerField()
	PHP=models.IntegerField()
	about_the_company=models.CharField(max_length=120,default=' ')

class Quiz_data():
	question: str
	option1: str
	option2: str
	option3: str
	option4: str
	group: str
	def q_data(self,val,num,g):
		question=val.loc[num,'Question']
		option1=val.loc[num,'op1']
		option2=val.loc[num,'op2']
		option3=val.loc[num,'op3']
		option4=val.loc[num,'op4']
		group=g

		print(question,option1,option2,option3,option4,group)


class code_base():
	question:str
	group:str
	answer:str
	def codq(self,val,num,g):
		question=val.loc[num,'Question']
		answer=val.loc[num,'Question']
		group=g
