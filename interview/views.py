import json
import math
import os
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

# from emotion import *
from interview.models import *
from interview.test import checkans
import speech_recognition as sr
def main(request):
    return render(request,'index.html')
def logout(request):
    auth.logout(request)
    return render(request,'index.html')
@login_required(login_url='/')
def adminhm(request):
    return render(request,'admin\index.html')
@login_required(login_url='/')
def block_or_unblock(request):
    ob = guide.objects.all()
    return render(request,'admin/blockor unblock guide.html' , {'val':ob})
@login_required(login_url='/')
def manage_guide(request):
    ob=guide.objects.all()
    return render(request,'admin/Manage guide.html', {'val':ob})
@login_required(login_url='/')
def manageguidesearch(request):
    n=request.POST['textfield']
    ob=guide.objects.filter(Q(First_name__icontains=n)|Q(Last_name__icontains=n))
    return render(request,'admin/Manage guide.html',{'val':ob})

@login_required(login_url='/')
def send_reply(request):
    return render(request,'admin/send reply.html')

@login_required(login_url='/')
def Verify_company(request):
    ob = company.objects.all()
    return render(request,'admin/Verify company.html', {'val':ob})

@login_required(login_url='/')
def company_search(request):
    n=request.POST['textfield']
    ob=company.objects.filter(name__icontains=n)
    return render(request,'admin/Verify company.html',{'val':ob})

@login_required(login_url='/')
def view_complaint(request):
    ob=Complaint_table.objects.all()
    return render(request,'admin/view compaint.html', {'val':ob})

@login_required(login_url='/')
def view_review(request):
    ob =review.objects.all()
    ob1 =company.objects.all()
    return render(request,'admin/view review.html', {'val':ob,'com':ob1})

@login_required(login_url='/')
def viewreviewsearch(request):
    n=request.POST['textfield']
    com=request.POST['select']
    ob1 = company.objects.all()
    ob=review.objects.filter(Q(date__icontains=n)|Q(LOGIN=com))
    return render(request,'admin/view review.html',{'val':ob,'com':ob1,'date':n})

@login_required(login_url='/')
def viewuser(request):
    ob=User.objects.all()
    return render(request,'admin/viewuser.html',{'val':ob})

@login_required(login_url='/')
def viewusersearch(request):
    n=request.POST['textfield']
    ob=User.objects.filter(First_name__icontains=n,)
    return render(request,'admin/viewuser.html',{'val':ob})

@login_required(login_url='/')
def add_job_veccancy(request):
    return render(request,'company/add job veccancy.html')

@login_required(login_url='/')
def add_veccancy(request):
    job=request.POST['textfield']
    v=  request.POST['textfield2']
    qualification = request.POST['textfield3']
    exp = request.POST['textfield4']
    salary = request.POST['textfield5']
    Details = request.POST['textfield6']
    Type = request.POST['textfield7']


    ob=vaccancy()
    ob.job=job
    ob.Vaccancy=v
    ob.qualification=qualification
    ob.exp=exp
    ob.salary=salary
    ob.details=Details
    ob.Vaccancy=Type
    ob.COMPANY=company.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("added sucessfully");window.location="Mange_job_veccancy"</script>''')

@login_required(login_url='/')
def edit_job(request,id):
    ob=vaccancy.objects.get(id=id)
    request.session['lid'] = ob.id
    return render(request,'company/edit_job_ veccancy.html',{'val':ob})

@login_required(login_url='/')
def edit_veccancy(request):
    job=request.POST['textfield']
    v=  request.POST['textfield2']
    qualification = request.POST['textfield3']
    exp = request.POST['textfield4']
    salary = request.POST['textfield5']
    Details = request.POST['textfield6']
    Type = request.POST['textfield7']
    ob=vaccancy.objects.get(id=request.session['lid'])
    ob.job=job
    ob.Vaccancy=v
    ob.qualification=qualification
    ob.exp=exp
    ob.salary=salary
    ob.details=Details
    ob.Vaccancy=Type
    # ob.COMPANY=company.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("edited sucessfully");window.location="Mange_job_veccancy"</script>''')

@login_required(login_url='/')
def delete_vaccancy(request, id):
    login_obj = vaccancy.objects.get(id=id)
    login_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/Mange_job_veccancy"</script>''')
"///////////////////////////////////////////////CHAT////////////////////////////////////////////////////"

@login_required(login_url='/')
def chat_with_candidate(request):
    ob = User.objects.all()
    return render(request,'company/fur_chat.html',{'val':ob})



@login_required(login_url='/')
def chatview(request):
    ob = User.objects.all()
    d=[]
    for i in ob:
        r={"name":i.First_name+" "+i.Last_name,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)


@login_required(login_url='/')
def coun_msg(request,id):
    ob1=chat.objects.filter(fromid__id=id,toid__id=request.session['lid'])
    ob2=chat.objects.filter(fromid__id=request.session['lid'],toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.fromid.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=User.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.First_name,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})


@login_required(login_url='/')
def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chat()
    ob.fromid=Login.objects.get(id=request.session['lid'])
    ob.toid=Login.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist




"//////////////////////////////////////////////////////////////////////////////////////////////////"
@login_required(login_url='/')
def company_home(request):
    return render(request,'company/companyindex.html')

def company_register(request):
    return render(request,'company register.html')

def add_register(request):
    name=request.POST['textfield']
    place = request.POST['textfield2']
    phone = request.POST['textfield3']
    email= request.POST['textfield4']
    website= request.POST['textfield5']
    username= request.POST['textfield6']
    password = request.POST['textfield7']
    ob=Login()
    ob.username=username
    ob.password=password
    ob.type='pending'
    ob.save()
    obb=company()
    obb.name=name
    obb.place=place
    obb.phone=phone
    obb.Email=email
    obb.Website=website
    obb.LOGIN = ob
    obb.save()
    return HttpResponse('''<script>alert("regesterd sucessfully");window.location="/"</script>''')

@login_required(login_url='/')
def accept(request,id):
    ob=Login.objects.get(id=id)
    ob.type='company'
    ob.save()
    return HttpResponse('''<script>alert("accepted successfully ");window.location="/Verify_company"</script>''')

@login_required(login_url='/')
def reject(request,id):
    ob=Login.objects.get(id=id)
    ob.type='reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected successfully ");window.location="/Verify_company"</script>''')

@login_required(login_url='/')
def Mange_job_veccancy(request):
    ob=vaccancy.objects.all()
    return render(request,'company/Mange job veccancy.html',{'val':ob})

@login_required(login_url='/')
def add_text_type(request):
    return render(request,'guide/add text type.html')

@login_required(login_url='/')
def reply(request,id):
    request.session['cid']=id
    return render(request,'admin/send reply.html')

@login_required(login_url='/')
def sendreply(request):
    reply = request.POST['textfield']
    obb = Complaint_table.objects.get(id=request.session['cid'])
    obb.Reply = reply
    obb.save()
    return HttpResponse('''<script>alert("updated sucessfully");window.location="/view_complaint"</script>''')

@login_required(login_url='/')
def Guid_home(request):
    return render(request,'guide/guidindex.html')

@login_required(login_url='/')
def manage_test_type(request):
    ob=test.objects.all()
    return render(request,'guide/manage test type.html', {'val':ob})

@login_required(login_url='/')
def add_test(request):
    return render(request,'guide/add text type.html')

@login_required(login_url='/')
def addtest(request):
    examname=request.POST['textfield']
    date=  request.POST['textfield2']
    ob=test()
    ob.Exam_name=examname
    ob.GUIDE=guide.objects.get(LOGIN__id=request.session['lid'])
    ob.date=datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Added sucessfully");window.location="manage_test_type"</script>''')

@login_required(login_url='/')
def edit_test(request,id):
    request.session['gid']=id
    ob=test.objects.get(id=id)
    return render(request,'guide/edittest.html',{'val':ob})

@login_required(login_url='/')
def edit_test_post(request):
    examname = request.POST['textfield']
    date= request.POST['textfield2']
    ob = test.objects.get(id=request.session['gid'])
    ob.Exam_name = examname
    ob.date = date
    ob.save()
    return HttpResponse('''<script>alert("updated sucessfully");window.location="/manage_test_type"</script>''')

@login_required(login_url='/')
def delete_test(request, id):
    test_obj = test.objects.get(id=id)
    test_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/manage_test_type"</script>''')

@login_required(login_url='/')
def add_guide(request):
    return render(request,'admin/addguide.html')

@login_required(login_url='/')
def block_guide(request,id):
    ob=Login.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert("blocked successfully ");window.location="/block_or_unblock"</script>''')

@login_required(login_url='/')
def unblock_guide(request,id):
    ob=Login.objects.get(id=id)
    ob.type='user'
    ob.save()
    return HttpResponse('''<script>alert("unblocked successfully ");window.location="/block_or_unblock"</script>''')

@login_required(login_url='/')
def delete_guide(request, id):
    login_obj = Login.objects.get(id=id)
    login_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/manage_guide"</script>''')

@login_required(login_url='/')
def edit_guide(request,id):
    request.session['gid']=id
    ob=guide.objects.get(id=id)
    return render(request,'admin/editguide.html',{'val':ob})

@login_required(login_url='/')
def edit_guide_post(request):
    firstname = request.POST['textfield']
    lname = request.POST['textfield2']
    address = request.POST['textarea']
    phone = request.POST['textfield3']
    email = request.POST['textfield4']
    obb = guide.objects.get(id=request.session['gid'])
    obb.First_name = firstname
    obb.Last_name = lname
    obb.Address = address
    obb.Phone = phone
    obb.Email = email
    obb.save()
    return HttpResponse('''<script>alert("updated sucessfully");window.location="/manage_guide"</script>''')

@login_required(login_url='/')
def add_guidecode(request):
    firstname=request.POST['textfield']
    lname=request.POST['textfield2']
    address = request.POST['textarea']
    phone = request.POST['textfield3']
    email= request.POST['textfield4']
    username= request.POST['textfield5']
    password = request.POST['textfield6']
    ob=Login()
    ob.username=username
    ob.password=password
    ob.type='guide'
    ob.save()
    obb=guide()
    obb.First_name=firstname
    obb.Last_name=lname
    obb.Address=address
    obb.Phone=phone
    obb.Email=email
    obb.LOGIN = ob
    obb.save()
    return HttpResponse('''<script>alert("added sucessfully");window.location="/manage_guide"</script>''')

@login_required(login_url='/')
def manage_question(request):
    ob = Questions.objects.all()
    ob1 = test.objects.all()
    return render(request, 'guide/manage question.html',{'val':ob,'tst':ob1})

@login_required(login_url='/')
def delete_Question(request, id):
    Questions_obj = Questions.objects.get(id=id)
    Questions_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/manage_question"</script>''')

@login_required(login_url='/')
def edit_Question(request,id):
    request.session['qid']=id
    ob=Questions.objects.get(id=id)
    return render(request,'guide/Edit question.html',{'val':ob})

@login_required(login_url='/')
def edit_question_post(request):
    # test1=request.POST['select']
    question= request.POST['textfield']
    option1= request.POST['textfield2']
    option2= request.POST['textfield3']
    option3= request.POST['textfield4']
    option4= request.POST['textfield5']
    Answer= request.POST['textfield6']
    ob = Questions.objects.get(id=request.session['qid'])
    ob.Question = question
    ob.option1 = option1
    ob.option2 = option2
    ob.option3 = option3
    ob.option4 = option4
    ob.Answer = Answer
    ob.save()
    return HttpResponse('''<script>alert("Updated sucessfully");window.location="manage_question"</script>''')

@login_required(login_url='/')
def Testsearch(request):
    n=request.POST['select']
    ob1 = test.objects.all()
    ob=Questions.objects.filter(TEST_id=n)
    return render(request,'guide/manage question.html', {'val':ob,'tst':ob1,'n':int(n)})


@login_required(login_url='/')
def add_question(request):
    ob = test.objects.all()
    return render(request,'guide/Add question.html',{'val':ob})

@login_required(login_url='/')
def add_question_post(request):
    test1=request.POST['select']
    question=  request.POST['textfield']
    option1 = request.POST['textfield2']
    option2 = request.POST['textfield3']
    option3 = request.POST['textfield4']
    option4 = request.POST['textfield5']
    answer = request.POST['textfield6']
    ob=Questions()
    ob.TEST=test.objects.get(id=test1)
    ob.Question=question
    ob.option1=option1
    ob.option2=option2
    ob.option3=option3
    ob.option4=option4
    ob.Answer=answer
    ob.save()
    return HttpResponse('''<script>alert("added sucessfully");window.location="manage_question"</script>''')

@login_required(login_url='/')
def Send_reply(request):
    return render(request, 'guide/Send reply.html')

@login_required(login_url='/')
def view_doubt(request):
    ob=doubt.objects.filter(GUIDE__LOGIN__id=request.session['lid'])
    return render(request, 'guide/view doubt.html',{"val":ob})

@login_required(login_url='/')
def view_doubt_search(request):
    date = request.POST['textfield']
    ob=doubt.objects.filter(GUIDE__LOGIN__id=request.session['lid'], date=date)
    return render(request, 'guide/view doubt.html',{"val":ob, 'date': str(date)})

@login_required(login_url='/')
def doubtreply(request,id):
    request.session['cid']=id
    return render(request,'guide/Send reply.html')

@login_required(login_url='/')
def doubt_reply(request):
    reply = request.POST['textfield']
    obb =doubt.objects.get(id=request.session['cid'])
    obb.reply = reply
    obb.save()
    return HttpResponse('''<script>alert("updated sucessfully");window.location="/view_doubt"</script>''')

@login_required(login_url='/')
def view_guid_line(request):
    ob = guideline.objects.filter(GUIDE__LOGIN__id=request.session['lid'])
    return render(request, 'guide/view guid line.html',{"val":ob})

@login_required(login_url='/')
def add_guidlines(request):
    return render(request,'guide/add guidlines.html')

@login_required(login_url='/')
def addguidlines(request):
    guidlines=  request.POST['textfield2']
    detail = request.POST['textfield3']
    ob=guideline()
    ob.guidelines=guidlines
    ob.details=detail
    ob.GUIDE = guide.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added sucessfully");window.location="view_guid_line"</script>''')




def log_in(request):
    uname=request.POST['textfield']
    password=request.POST['textfield2']
    try:
        ob=Login.objects.get(username=uname,password=password)
        if ob.type=='admin':
            var=auth.authenticate(username='admin',password='admin')
            if var is not None:
                auth.login(request,var)
            return redirect("/adminhm")
        elif ob.type=='company':
            request.session['lid']=ob.id
            var = auth.authenticate(username='admin', password='admin')
            if var is not None:
                auth.login(request, var)
                return redirect("/company_home")
        elif ob.type=='guide':
            request.session['lid'] = ob.id
            var = auth.authenticate(username='admin', password='admin')
            if var is not None:
                auth.login(request, var)
            return redirect("/Guid_home")
        else:
            return HttpResponse('''<script>alert("invalid username or password");window.location="/"</script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password");window.location="/"</script>''')


@login_required(login_url='/')
def Manage_job_veccancy(request):
    ob=company.objects.all()
    return render(request,'company/Mange job veccancy.html', {'val':ob})



#home

@login_required(login_url='/')
def verify_application(request):
    ob = app_req.objects.all()
    return render(request, 'company/verify application.html', {'val': ob})


@login_required(login_url='/')
def applicationsearch(request):
    n=request.POST['textfield']
    ob=app_req.objects.filter(date__icontains=n)
    return render(request,'company/verify application.html',{'val':ob, 'n': n})


@login_required(login_url='/')
def acceptapplication(request,id):
    ob=app_req.objects.get(id=id)
    ob.status='Accepetd'
    ob.save()
    return HttpResponse('''<script>alert("accepted successfully ");window.location="/verify_application"</script>''')

@login_required(login_url='/')
def rejectapplication(request,id):
    ob=app_req.objects.get(id=id)
    ob.status='Rejected'
    ob.save()
    return HttpResponse('''<script>alert("rejected successfully ");window.location="/verify_application"</script>''')

@login_required(login_url='/')
def add_tips(request):
    return render(request,'guide/add tips.html')

@login_required(login_url='/')
def addtips(request):
    tip1=  request.POST['textfield2']
    detail = request.POST['textfield3']
    ob=tip()
    ob.tips=tip1
    ob.details=detail
    ob.GUIDE = guide.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added sucessfully");window.location="view_tips"</script>''')

@login_required(login_url='/')
def view_tips(request):
    ob=tip.objects.filter(GUIDE__LOGIN__id=request.session['lid'])
    return render(request, 'guide/view tips.html',{'val':ob})


@login_required(login_url='/')
def view_Review(request):
    ob =review.objects.all()
    ob1 =company.objects.all()
    return render(request,'guide/view Review.html', {'val':ob,'com':ob1})

@login_required(login_url='/')
def viewReviewsearch(request):
    n=request.POST['textfield']
    ob=review.objects.filter(date__icontains=n)
    return render(request,'guide/view Review.html',{'val':ob,'date':n})


# ///////////////////////////////////////// webservice ///////////////////////////////////////



# def login_code(request):
#     username = request.POST['uname']
#     password = request.POST['pass']
#     try:
#         users = Login.objects.get(Username=username, Password=password)
#         if users is None:
#             data = {"task": "invalid"}
#
#         else:
#             data = {"task": "valid", "id": users.id}
#             r = json.dumps(data)
#             return HttpResponse(r)
#     except:
#         data = {"task": "invalid"}
#         r = json.dumps(data)
#         print(r)
#         return HttpResponse(r)
#
# def registration(request):
#     firstname = request.POST['Firstname']
#     lastname = request.POST['Lastname']
#     place = request.POST['Place']
#     post_office = request.POST['Post']
#     pin_code = request.POST['Pin']
#     phone = request.POST['Phone']
#     gender = request.POST['Gender']
#     photo = request.POST['photo']
#     email_id = request.POST['Email']
#     username = request.POST['Username']
#     password = request.POST['Password']
#
#     lob = Login()
#     lob.username = username
#     lob.password = password
#     lob.Type = 'user'
#     lob.save()
#     user_obj = User()
#     user_obj.First_name = firstname
#     user_obj.Last_name = lastname
#     user_obj.place   = place
#     user_obj.Post = post_office
#     user_obj.Pin = pin_code
#     user_obj.Phone = phone
#     user_obj.Gender = gender
#     user_obj.email = email_id
#     user_obj.save()
#     data = {"task": "success"}
#     r = json.dumps(data)
#     return HttpResponse(r)
#
# def send_complaint_app(request):
#     complaints = request.POST["Complaint"]
#     u_id = request.POST["uid"]
#     date = datetime.now()
#     reply = "waiting"
#     complaint_obj = Complaint_table()
#     complaint_obj.Complaint = complaints
#     complaint_obj.Date = date
#     complaint_obj.Reply = reply
#     complaint_obj.UID = User.objects.get(LID__id=u_id)
#     complaint_obj.save()
#     data = {'task': 'success'}
#     r = json.dumps(data)
#     return HttpResponse(r)
#
#
# def reply_app(request):
#     user_id = request.POST['lid']
#     complaint_obj = Complaint_table.objects.filter(UID__LID__id=user_id)
#     data = []
#     for i in complaint_obj:
#         row = {'Complaint': i.Complaint, 'Reply': i.Reply, 'Date': str(i.Date)}
#         data.append(row)
#     r = json.dumps(data)
#     return HttpResponse(r)
#
#
# def view_result(request):
#     user_id = request.POST['lid']
#     test_obj= test_result.objects.filter(UID__LID__id=user_id)
#     data = []
#     for i in test_obj:
#         row = {'quetion': i.quetion, 'result': i.res, 'Date': str(i.date)}
#         data.append(row)
#     r = json.dumps(data)
#     return HttpResponse(r)
#
# def view_Tips(request):
#     user_id = request.POST['lid']
#     tip_obj = tip.objects.filter(UID__LID__id=user_id)
#     data = []
#     for i in tip_obj:
#         row = {'tips': i.tips, 'details': i.details}
#         data.append(row)
#     r = json.dumps(data)
#     return HttpResponse(r)
#
# def doubt1(request):
#     doubt = request.POST["doubt"]
#     user = request.POST["user"]
#     date = datetime.now()
#     reply = "waiting"
#     doubt_obj = doubt()
#     doubt_obj.USER = user
#     doubt_obj.doubt = doubt
#     doubt_obj.reply = reply
#     doubt_obj.UID = User.objects.get(LID__id=u_id)
#     doubt_obj.save()
#     data = {'task': 'success'}
#     r = json.dumps(data)
#     return HttpResponse(r)
#
# def reply_doubt(request):
#     user_id = request.POST['lid']
#     doubt_obj = doubt.objects.filter(UID__LID__id=user_id)
#     data = []
#     for i in doubt_obj:
#         row = {'USER': i.USER, 'doubt': i.doubt,'reply': i.reply, 'Date': str(i.date)}
#         data.append(row)
#     r = json.dumps(data)
#     return HttpResponse(r)
#
# def search_job(request):
#     user_id = request.POST['lid']
#     job_obj = vaccancy.objects.filter(UID__LID__id=user_id)
#     data = []
#     for i in job_obj:
#         row = {'job': i.job, 'qualification': i.qualification,'experiance': i.exp,'salary': i.salary,'details': i.details}
#         data.append(row)
#     r = json.dumps(data)
#     return HttpResponse(r)
#
# def view_question(request):
#     user_id = request.POST['lid']
#     question_obj = Questions.objects.filter(UID__LID__id=user_id)
#     data = []
#     for i in question_obj:
#         row = {'TEST': i.TEST, 'Question': i.Question,'option1': i.option1,'option2': i.option2,'option3': i.option3,'option4': i.option4,'Answer': i.Answer}
#         data.append(row)
#     r = json.dumps(data)
#     return HttpResponse(r)
#
# def job_apply(request):
#     user_id = request.POST['lid']
#     job_obj = vaccancy.objects.filter(UID__LID__id=user_id)
#     data = []
#     for i in job_obj:
#         row = {'COMPANY': i.COMPANY, 'job': i.job ,'experiance': i.exp,'salary': i.salary,'details': i.details}
#         data.append(row)
#     r = json.dumps(data)
#     return HttpResponse(r)



#________________________________ANDROID________________________________________

def login2(request):
    username=request.POST['uname']
    password=request.POST['pass']
    ob=Login.objects.get(username=username,password=password)
    if ob is None:
        data={"task":"invalid"}
    else:
        data={"task":"success",'id':str(ob.id)}
    r=json.dumps(data)
    print(r)
    return HttpResponse(r)

def Userregistration(request):
    firstname=request.POST['fname']
    lastname = request.POST['lname']
    plc = request.POST['plc']
    pst = request.POST['post']
    pin = request.POST['pin']
    ph = request.POST['ph']
    username= request.POST['un']
    password=request.POST['pwd']
    email=request.POST['email']
    gender=request.POST['gender']
    pic=request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(pic.name,pic)
    lob = Login()
    lob.username = username
    lob.password = password
    lob.type='user'
    lob.save()
    ob = User()
    ob.LOGIN = lob
    ob.First_name = firstname
    ob.Last_Name=lastname
    ob.place = plc
    ob.gender=gender
    ob.post = pst
    ob.pin = pin
    ob.phone = ph
    ob.email=email
    ob.photo=fs
    ob.save()
    data={"task":"success"}
    r=json.dumps(data)
    return HttpResponse(r)

def view_dbt_reply(request):
    id = request.POST['lid']
    ob = doubt.objects.filter(USER__LOGIN__id=id)
    data = []
    for i in ob:
        row = {"doubt": i.doubt, "reply": i.reply, "date":str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def view_gd(request):
    ob = guide.objects.all()
    data = []
    for i in ob:
        row = {"guide": i.First_name+" "+i.Last_name, "gid": i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def view_company(request):
    ob = company.objects.all()
    data = []
    for i in ob:
        row = {"cmp": i.name, "cid": i.id,"lid":i.LOGIN.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def view_cp(request):
    ob = guide.objects.all()
    data = []
    for i in ob:
        row = {"cmp": i.First_name+" "+i.Last_name, "cid": i.id,"lid":i.LOGIN.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def view_comp_reply(request):
    id = request.POST['lid']
    ob = Complaint_table.objects.filter(USER__LOGIN__id=id)
    data = []
    for i in ob:
        row = {"complaint": i.Complaint, "reply": i.Reply, "date":str(i.Date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def sendcomp(request):
    complaints=request.POST['comp']
    lid=request.POST['lid']
    ob=Complaint_table()
    ob.Complaint= complaints
    ob.Date=datetime.today()
    ob.Reply='pending'
    ob.USER=User.objects.get(LOGIN__id=lid)
    ob.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)
def read_pdf(file_path):
    import PyPDF2
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        txt=""
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            txt=txt+text+" "
        return txt
def upldcv(request):
    from knn import predict
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        # from interview.sampleee import pdf_reader
    cv=request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(cv.name,cv)
    lid=request.POST['lid']
    save_image_path = r'C:\Users\91953\PycharmProjects\mockinterview\media/' + fs
    resume_text = read_pdf(save_image_path)
    res = predict(resume_text)
    print(res,"=================================================")
    ob=upload()
    ob.USER=User.objects.get(LOGIN__id=lid)
    ob.cv=fs
    ob.date=datetime.today()
    ob.save()
    data = {"task": "success","res":res}
    r = json.dumps(data)
    return HttpResponse(r)
def uploadresume(request):
    # from mock_app.sampleee import pdf_reader
    # lid = request.POST['lid']
    # vid = request.POST['vid']
    # resu = request.POST['file']/*-/////////////////////-------/
    # ob = Application()
    # ob.STUDENT = Student.objects.get(LOGIN__id=lid)
    # ob.VACCANCY = Job_and_vacancy.objects.get(id=vid)
    # ob.date = datetime.today()
    # ob.status = "pending"
    # ob.save()
    cv = request.FILES['file']
    fn = FileSystemStorage()
    fs = fn.save(cv.name, cv)
    lid = request.POST['lid']
    # save_image_path = './media/' + fs
    # resume_text = read_pdf(save_image_path)
    # res = predict(resume_text)
    # print(res, "=================================================")
    ob = upload()
    ob.User = User.objects.get(LOGIN__id=lid)
    ob.Cv = fs
    ob.save()
    import base64
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(cv)
    fh = open(r"C:\Users\hp\PycharmProjects\mock_project\media\\" + timestr + ".pdf", "wb")
    path =timestr + ".pdf"
    fh.write(a)
    fh.close()
    # text=pdf_reader(r"C:\Users\hp\PycharmProjects\mock_project\media\\" + timestr + ".pdf")
    # vec1=text_to_vector(text)
    # vec2=text_to_vector(ob.VACCANCY.qualification)
    print("+++++++++++++++++++++++++++")
    # print(vec2)
    print("+++++++++++++++++++++++++++")
    # sim=get_cosine(vec1,vec2)
    # oj=Resume()
    # oj.APPLICATION=ob
    # oj.score=sim*100
    # oj.date=datetime.today()
    # oj.resume=path
    # oj.save()
    return JsonResponse({"task": "ok"})

# def upldcv(request):
#     cv=request.POST['file']
#     import base64
#     timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
#     print(timestr)
#     a = base64.b64decode(cv)
#     fh = open(r"D:\Django project\Career_Guidance_project\media\\" + timestr + ".pdf", "wb")
#     path = timestr + ".pdf"
#     fh.write(a)
#     fh.close()
#     # fn=FileSystemStorage()
#     # fs=fn.save(cv.name,cv)
#     save_image_path = './media/' + path
#     resume_text = read_pdf(save_image_path).lower()
#     print(resume_text)
#     res = predict(resume_text)
#     print(res,"=================================================")
#
#     data = {"task": "ok","res":res}
#     r = json.dumps(data)
#     return HttpResponse(r)
def senddbt(request):
    dbt=request.POST['dbt']
    lid=request.POST['lid']
    gid=request.POST['gid']
    ob=doubt()
    ob.doubt= dbt
    ob.date=datetime.today()
    ob.reply='pending'
    ob.USER=User.objects.get(LOGIN__id=lid)
    ob.GUIDE=guide.objects.get(id=gid)
    ob.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)
def view_tips1(request):
    gid=request.POST['gid']
    ob = tip.objects.filter(GUIDE__id=gid)
    data = []
    for i in ob:
        row = {"tips": i.tips,"det": i.details}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def career_prediction(request):
    job=request.POST['job']
    print(job)
    ob=vaccancy.objects.filter(job__icontains=job)
    data = []
    for i in ob:
        row = {"cmp": i.COMPANY.name,"job":i.job,"vac":i.Vaccancy,"qual":i.qualification,"sal":i.salary,"det":i.details,"vid":i}
        data.append(row)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)
def mocktest(request):
    ob=vaccancy.objects.all()
    data = []
    for i in ob:
        row = {"cmp": i.COMPANY.name,"job":i.job,"vac":i.Vaccancy,"qual":i.qualification,"sal":i.salary,"det":i.details,"cid":i.id,"vid":i.pk}
        data.append(row)
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)
def test_result1(request):
    cid = request.POST['gid']
    lid = request.POST['lid']
    print("ggggggggggggggggggggggggggggggg")
    op=User.objects.get(LOGIN_id=lid)
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(`interview_answer_details`.ans) FROM `interview_vac_qn` JOIN `interview_answer_details` ON `interview_answer_details`.`vac_qn_id`=`interview_vac_qn`.id where `interview_answer_details`.`user_id`=3",[cid])
    ob=cursor.fetchall()
    print(ob,"=====")
    data = []
    for i in ob:
        row = {"job": i[1], "vac":0,"res": i[0]}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def result(request):
    cid = request.POST['gid']
    lid = request.POST['lid']
    op=User.objects.get(LOGIN_id=lid)
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT *, SUM(`interview_answer_details`.ans) FROM `interview_vac_qn` JOIN `interview_answer_details` ON `interview_answer_details`.`vac_qn_id`=`interview_vac_qn`.id INNER JOIN `interview_vaccancy` ON `interview_vaccancy`.`id`=`interview_vac_qn`.`vaccancy_id` WHERE `interview_answer_details`.`user_id`=%s",[op.pk])
    ob=cursor.fetchall()
    print(ob,"=====")
    # ob = answer_details.objects.filter(VAC_QN__VACCANCY__COMPANY__id=cid).annotate(sum=Sum("ans")).values('date','sum').distinct()
    # print(ob,"=========")
    data = []
    for i in ob:
        row = {"job": i[13],"Emotion":i[6],"res": i[19]}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def add_vac_qstion(request,id):
    q1=vac_qn.objects.filter(vaccancy_id=id)
    if 'submit' in request.POST:
        qstion=request.POST['qstion']
        ans=request.POST['ans']
        qa=vac_qn(Question=qstion,Answer=ans,vaccancy_id=id)
        qa.save()
        return HttpResponse("<script>alert('Added');window.location='/Mange_job_veccancy'</script>")
    
    return render(request,'company/add_vac_qstion.html',{'qa':q1})
    

def view_exam(request):
    gid=request.POST['gid']
    ob = test.objects.filter(GUIDE__id=gid)
    data = []
    for i in ob:
        row = {"exam": i.Exam_name,"date": str(i.date),"vac":0,"tid":i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def view_test(request):
    ob = test.objects.all()
    data = []
    for i in ob:
        row = {"exam": i.Exam_name,"date": str(i.date),"vac":0,"tid":i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def view_rules(request):
    cid=request.POST['gid']
    ob = guideline.objects.filter(GUIDE__id=cid)
    data = []
    for i in ob:
        row = {"tips": i.guidelines,"det": i.details}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def in_message2(request):
    fromid = request.POST['fid']
    toid = request.POST['toid']
    message=request.POST['msg']
    ob=chat()
    ob.fromid=Login.objects.get(id=fromid)
    ob.toid=Login.objects.get(id=toid)
    ob.message=message
    ob.date=datetime.today()
    # ob.Time = datetime.today()
    ob.save()
    data = {"status": "send"}
    r = json.dumps(data)
    return HttpResponse(r)
def view_message2(request):
    fromid=request.POST['fid']
    toid=request.POST['toid']
    lmid = request.POST['lastmsgid']
    data1 = []
    ob=chat.objects.filter(Q(toid__id=toid,fromid__id=fromid,id__gt=lmid)|Q(toid__id=fromid,fromid__id=toid,id__gt=lmid)).order_by('id')
    for i in ob:
        row = {"fromid": i.fromid.id,"date": str(i.date),"message":i.message,"msgid":i.id}
        data1.append(row)
    r = json.dumps({'res1':data1})
    return HttpResponse(r)

def get_question(request):
    vid = request.POST['pid']
    ob = Questions.objects.filter(TEST__id=vid)
    data = []
    for i in ob:
        row = {"qid": i.id, "question":i.Question, "op1": i.option1, "op2": i.option2,"op3":i.option3,"op4":i.option4,"answer":i.Answer}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def and_view_questions(request):
    test_id=request.POST['tid']
    ob = vac_qn.objects.filter(vaccancy_id=test_id)
    data = []
    for i in ob:
        row = {"qid": i.pk, "questions":i.Question,"answers":i.Answer}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def answertest(request):
    qid=request.POST['qid']
    lid = request.POST['lid']
    ans = request.POST['ans']
    res = request.POST['res']
    ob=test_result()
    ob.quetion=Questions.objects.get(id=qid)
    ob.USER=User.objects.get(LOGIN__id=lid)
    ob.date=datetime.today()
    ob.res=res
    ob.ans=ans
    ob.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)
def mark(request):
    scid = request.POST['scid']
    mark = request.POST['mark']
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)
def voice(request):
        print("=================================heloooo======================================")
        scrid = request.POST['scid']
        lid = request.POST['lid']
        qid = request.POST['qid']
        tid = request.POST['tid']
        file = request.FILES['file']
        im = request.FILES['file1']
        fn=FileSystemStorage()
        image = fn.save(im.name,im)
        # image = secure_filename(im.filename)
        import time
        ffl = time.strftime("%Y%m%d_%H%M%S")
        reg = time.strftime("%Y%m%d_%H%M%S")+ ".jpg"
        kk = "pic.jpg"
        fn.save(os.path.join(r'C:\Users\syamr\Downloads\mockinterview\mockinterview\media\emotion', reg), im)
        ff = fn.save(file.name,file)
        # ff = secure_filename(file.filename)
        print(ff)
        fl = ff.split('.')
        # print(fl[1])
        # import time
        ffl = time.strftime("%Y%m%d_%H%M%S")
        req = time.strftime("%Y%m%d_%H%M%S") + "." + str(fl[1])
        fn.save(os.path.join(r'C:\Users\syamr\Downloads\mockinterview\mockinterview\media\audio', req),file)
        # fn.save(req,req)
        print(req, "++++++=====++++====+++")
        print("====ff1=====", ffl)
        os.system('ffmpeg -i static\\audio\\' + req + ' static\\audio\\' + ffl + ".wav")
        ans = "no answer"
        try:
            ans = silence_based_conversion(ffl)
        except:
            pass
        print("ans", ans)
        q = vac_qn.objects.get(id=qid)
        oans = q.Answer
        print(oans)
        mark = 10

        sim = checkans(oans, ans)
        omark = sim * mark
        print("omark", omark)
        if omark != 0.0:
            my_matches = []  # my_tool.check(ans)
            print(len(my_matches))
            if len(my_matches) > 5 and len(my_matches) < 10:
                omark = omark - 0.3
            elif len(my_matches) > 10 and len(my_matches) < 20:
                omark = omark - 0.6
        em = ""
        print("emotion", em)
        qw = answer_details()
        qw.ans=ans
        qw.emt=em
        qw.user=User.objects.get(LOGIN__id=lid)
        qw.oans=oans
        qw.date=datetime.today()
        qw.vac_qn=vac_qn.objects.get(id=qid)
        qw.save()
        data = {"task": omark}
        r = json.dumps(data)
        return HttpResponse(r)

def silence_based_conversion(fl):
    path = r'./static/audio/'+fl+'.wav'
    r = sr.Recognizer()
    file=path
    # recognize the chunk
    with sr.AudioFile(file) as source:
        r.adjust_for_ambient_noise(source)
        audio_listened = r.listen(source)
    try:
        rec = r.recognize_google(audio_listened)
        print(rec)
        return rec
    except sr.UnknownValueError as e:
        print("Could not understand audio")
        print(e)
        return "na"
    except sr.RequestError as e:
        print("Could not request results. check your internet connection")
        print(e)
        return "na"

import re
WORD = re.compile(r'\w+')
from collections import Counter
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


