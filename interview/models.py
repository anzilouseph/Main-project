from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=60)
    type=models.CharField(max_length=60)

class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    First_name=models.CharField(max_length=60)
    Last_name=models.CharField(max_length=60)
    gender=models.CharField(max_length=60)
    place=models.CharField(max_length=60)
    post=models.CharField(max_length=60)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email = models.CharField(max_length=60)
    photo=models.FileField()

class Complaint_table(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Complaint=models.CharField(max_length=60)
    Date=models.DateField(max_length=60)
    Reply=models.CharField(max_length=60)

class company(models.Model):
     LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
     name = models.CharField(max_length=60)
     place = models.CharField(max_length=60)
     phone = models.BigIntegerField()
     Email = models.CharField(max_length=60)
     Wedsite = models.CharField(max_length=60)

class review(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    review=models.CharField(max_length=60)
    date=models.DateField(max_length=60)

class guide(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    First_name=models.CharField(max_length=60)
    Last_name=models.CharField(max_length=60)
    Address=models.CharField(max_length=60)
    Phone=models.BigIntegerField()
    Email=models.CharField(max_length=60)

class doubt(models.Model):
    GUIDE = models.ForeignKey(guide, on_delete=models.CASCADE)
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    doubt=models.CharField(max_length=60)
    reply=models.CharField(max_length=60)
    date=models.DateField(max_length=60)

class chat(models.Model):
    fromid=models.ForeignKey(Login,on_delete=models.CASCADE,related_name="f")
    toid=models.ForeignKey(Login,on_delete=models.CASCADE,related_name="t")
    date=models.DateField()
    message=models.CharField(max_length=1000)

class guideline(models.Model):
    GUIDE = models.ForeignKey(guide, on_delete=models.CASCADE)
    guidelines = models.CharField(max_length=60)
    details = models.CharField(max_length=60)

class tip(models.Model):
    GUIDE=models.ForeignKey(guide, on_delete=models.CASCADE)
    tips=models.CharField(max_length=60)
    details=models.CharField(max_length=60)

class test(models.Model):
    GUIDE=models.ForeignKey(guide, on_delete=models.CASCADE)
    Exam_name=models.CharField(max_length=60)
    date=models.CharField(max_length=60)

class Questions(models.Model):
    TEST = models.ForeignKey(test, on_delete=models.CASCADE)
    Question=models.CharField(max_length=60)
    option1=models.CharField(max_length=60)
    option2=models.CharField(max_length=60)
    option3=models.CharField(max_length=60)
    option4=models.CharField(max_length=60)
    Answer=models.CharField(max_length=60)

class vaccancy(models.Model):
    COMPANY = models.ForeignKey(company, on_delete=models.CASCADE)
    job = models.CharField(max_length=600)
    Vaccancy=models.CharField(max_length=60)
    qualification = models.CharField(max_length=60)
    exp = models.CharField(max_length=60)
    salary=models.CharField(max_length=60)
    details=models.CharField(max_length=700)

class vac_qn(models.Model):
    vaccancy= models.ForeignKey(vaccancy, on_delete=models.CASCADE)
    Question = models.TextField()
    Answer = models.CharField(max_length=500)


class app_req(models.Model):
    date = models.DateField(max_length=60)
    status = models.CharField(max_length=60)
    vaccancy = models.ForeignKey(vaccancy, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class test_result(models.Model):
    quetion=models.ForeignKey(Questions, on_delete=models.CASCADE)
    date = models.DateField()
    res=models.CharField(max_length=60)
    ans=models.CharField(max_length=60)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class upload(models.Model):
    cv=models.CharField(max_length=60)
    date = models.DateField()
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class answer_details(models.Model):
    vac_qn=models.ForeignKey(vac_qn, on_delete=models.CASCADE)
    ans=models.CharField(max_length=60)
    emot=models.CharField(max_length=60)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(max_length=60)
    oans=models.CharField(max_length=60)

# class result(models.Model):
#     Exam_name=models.CharField(max_length=60)
#     Result=models.CharField(max_length=60)
#     date=models.DateField(max_length=60)
#     USER=models.ForeignKey(User, on_delete=models.CASCADE)
#     TEST=models.ForeignKey(test, on_delete=models.CASCADE)
#
#     detail=models.CharField(max_length=60)
#     type=models.CharField(max_length=60)
#     COMPANY_ID=models.ForeignKey(Complaint, on_delete=models.CASCADE)

# class Request(models.Model):
#      date=models.CharField(max_length=60)
#      status=models.CharField(max_length=60)
#      job=models.ForeignKey(Complaint, on_delete=models.CASCADE)
#      user = models.ForeignKey(Complaint, on_delete=models.CASCADE)
#

# class mark(models.Model):
#     Date=models.DateField()
#     TEST_ID = models.ForeignKey(Questions, on_delete=models.CASCADE)
#     QUESTION_ID = models.ForeignKey(Questions, on_delete=models.CASCADE)
#     USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)



















# Create your models here.
