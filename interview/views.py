from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

# Create your views here.
from interview.VacancyForm import VacancyForm
from interview.models import *


def main(request):
    return render(request,'index.html')

def adminhm(request):
    return render(request,'admin\index.html')

def block_or_unblock(request):
    ob = guide.objects.all()
    return render(request,'admin/blockor unblock guide.html' , {'val':ob})

def manage_guide(request):
    ob=guide.objects.all()
    return render(request,'admin/Manage guide.html', {'val':ob})

def manageguidesearch(request):
    n=request.POST['textfield']
    ob=guide.objects.filter(Q(First_name__icontains=n)|Q(Last_name__icontains=n))
    return render(request,'admin/Manage guide.html',{'val':ob})

def send_reply(request):
    return render(request,'admin/send reply.html')

def Verify_company(request):
    ob = company.objects.all()
    return render(request,'admin/Verify company.html', {'val':ob})

def company_search(request):
    n=request.POST['textfield']
    ob=company.objects.filter(name__icontains=n)
    return render(request,'admin/Verify company.html',{'val':ob})

def view_complaint(request):
    ob=Complaint_table.objects.all()
    return render(request,'admin/view compaint.html', {'val':ob})

def view_review(request):
    ob =review.objects.all()
    ob1 =company.objects.all()
    return render(request,'admin/view review.html', {'val':ob,'com':ob1})

def viewreviewsearch(request):
    n=request.POST['textfield']
    com=request.POST['select']
    ob1 = company.objects.all()
    ob=review.objects.filter(Q(date__icontains=n)|Q(LOGIN=com))
    return render(request,'admin/view review.html',{'val':ob,'com':ob1,'date':n})

def viewuser(request):
    ob=User.objects.all()
    return render(request,'admin/viewuser.html',{'val':ob})

def viewusersearch(request):
    n=request.POST['textfield']
    ob=User.objects.filter(First_name__icontains=n,)
    return render(request,'admin/viewuser.html',{'val':ob})

def add_job_veccancy(request):
    return render(request,'company/add job veccancy.html')


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


def edit_job(request,id):
    ob=vaccancy.objects.get(id=id)
    request.session['lid'] = ob.id
    return render(request,'company/edit_job_ veccancy.html',{'val':ob})


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

def delete_vaccancy(request, id):
    login_obj = vaccancy.objects.get(id=id)
    login_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/Mange_job_veccancy"</script>''')
"///////////////////////////////////////////////CHAT////////////////////////////////////////////////////"

def chat_with_candidate(request):
    ob = User.objects.all()
    return render(request,'company/fur_chat.html',{'val':ob})




def chatview(request):
    ob = User.objects.all()
    d=[]
    for i in ob:
        r={"name":i.First_name+" "+i.Last_name,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)



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

def accept(request,id):
    ob=Login.objects.get(id=id)
    ob.type='company'
    ob.save()
    return HttpResponse('''<script>alert("accepted successfully ");window.location="/Verify_company"</script>''')

def reject(request,id):
    ob=Login.objects.get(id=id)
    ob.type='reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected successfully ");window.location="/Verify_company"</script>''')

def Mange_job_veccancy(request):
    ob=vaccancy.objects.all()
    return render(request,'company/Mange job veccancy.html',{'val':ob})

def add_text_type(request):
    return render(request,'guide/add text type.html')

def reply(request,id):
    request.session['cid']=id
    return render(request,'admin/send reply.html')

def sendreply(request):
    reply = request.POST['textfield']
    obb = Complaint_table.objects.get(id=request.session['cid'])
    obb.Reply = reply
    obb.save()
    return HttpResponse('''<script>alert("updated sucessfully");window.location="/view_complaint"</script>''')

def Guid_home(request):
    return render(request,'guide/guidindex.html')

def manage_test_type(request):
    ob=test.objects.all()
    return render(request,'guide/manage test type.html', {'val':ob})


def add_test(request):
    return render(request,'guide/add text type.html')


def addtest(request):
    examname=request.POST['textfield']
    date=  request.POST['textfield2']
    ob=test()
    ob.Exam_name=examname
    ob.GUIDE=guide.objects.get(LOGIN__id=request.session['lid'])
    ob.date=datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Added sucessfully");window.location="manage_test_type"</script>''')


def edit_test(request,id):
    request.session['gid']=id
    ob=test.objects.get(id=id)
    return render(request,'guide/edittest.html',{'val':ob})

def edit_test_post(request):
    examname = request.POST['textfield']
    date= request.POST['textfield2']
    ob = test.objects.get(id=request.session['gid'])
    ob.Exam_name = examname
    ob.date = date
    ob.save()
    return HttpResponse('''<script>alert("updated sucessfully");window.location="/manage_test_type"</script>''')


def delete_test(request, id):
    test_obj = test.objects.get(id=id)
    test_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/manage_test_type"</script>''')

def add_guide(request):
    return render(request,'admin/addguide.html')

def block_guide(request,id):
    ob=Login.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert("blocked successfully ");window.location="/block_or_unblock"</script>''')

def unblock_guide(request,id):
    ob=Login.objects.get(id=id)
    ob.type='user'
    ob.save()
    return HttpResponse('''<script>alert("unblocked successfully ");window.location="/block_or_unblock"</script>''')

def delete_guide(request, id):
    login_obj = Login.objects.get(id=id)
    login_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/manage_guide"</script>''')

def edit_guide(request,id):
    request.session['gid']=id
    ob=guide.objects.get(id=id)
    return render(request,'admin/editguide.html',{'val':ob})

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

def manage_question(request):
    ob = Questions.objects.all()
    ob1 = test.objects.all()
    return render(request, 'guide/manage question.html',{'val':ob,'tst':ob1})

def delete_Question(request, id):
    Questions_obj = Questions.objects.get(id=id)
    Questions_obj.delete()
    return HttpResponse('''<script>alert("deleted successfully ");window.location="/manage_question"</script>''')

def edit_Question(request,id):
    request.session['gid']=id
    ob=Questions.objects.get(id=id)
    return render(request,'guide/Edit question.html',{'val':ob})

def edit_question_post(request):
    test1=request.POST['select']
    question= request.POST['textfield']
    option1= request.POST['textfield2']
    option2= request.POST['textfield3']
    option3= request.POST['textfield4']
    option4= request.POST['textfield5']
    Answer= request.POST['textfield6']
    ob = Questions.objects.get(id=request.session['gid'])
    ob.Question = question
    ob.option1 = option1
    ob.option2 = option2
    ob.option3 = option3
    ob.option4 = option4
    ob.Answer = Answer
    ob.save()
    return HttpResponse('''<script>alert("added sucessfully");window.location="manage_question"</script>''')


def Testsearch(request):
    n=request.POST['select']
    ob1 = test.objects.all()
    ob=Questions.objects.filter(TEST_id=n)
    return render(request,'guide/manage question.html', {'val':ob,'tst':ob1})



def add_question(request):
    ob = test.objects.all()
    return render(request,'guide/Add question.html',{'val':ob})


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


def Send_reply(request):
    return render(request, 'guide/Send reply.html')

def view_doubt(request):
    ob=doubt.objects.filter(GUIDE__LOGIN__id=request.session['lid'])
    return render(request, 'guide/view doubt.html',{"val":ob})

def view_doubt_search(request):
    date = request.POST['textfield']
    ob=doubt.objects.filter(GUIDE__LOGIN__id=request.session['lid'], date=date)
    return render(request, 'guide/view doubt.html',{"val":ob, 'date': str(date)})

def doubtreply(request,id):
    request.session['cid']=id
    return render(request,'guide/Send reply.html')

def doubt_reply(request):
    reply = request.POST['textfield']
    obb =doubt.objects.get(id=request.session['cid'])
    obb.reply = reply
    obb.save()
    return HttpResponse('''<script>alert("updated sucessfully");window.location="/view_doubt"</script>''')


def view_guid_line(request):
    ob = guideline.objects.filter(GUIDE__LOGIN__id=request.session['lid'])
    return render(request, 'guide/view guid line.html',{"val":ob})

def add_guidlines(request):
    return render(request,'guide/add guidlines.html')

def addguidlines(request):
    guidlines=  request.POST['textfield2']
    detail = request.POST['textfield3']
    ob=guideline()
    ob.guidelines=guidlines
    ob.details=detail
    ob.GUIDE = guide.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added sucessfully");window.location="view_guid_line"</script>''')


def log_out(request):
    return render(request, 'guide/admi login.html')

def log_in(request):
    uname=request.POST['textfield']
    password=request.POST['textfield2']
    ob=Login.objects.get(username=uname,password=password)
    if ob.type=='admin':
       return HttpResponse('''<script>alert("Welcome to Admin home");window.location="/adminhm"</script>''')
    elif ob.type=='company':
        request.session['lid']=ob.id
        return HttpResponse('''<script>alert("Welcome to company");window.location="/company_home"</script>''')
    elif ob.type=='guide':
        request.session['lid'] = ob.id
        return HttpResponse('''<script>alert("Welcome to guide");window.location="/Guid_home"</script>''')
    else:
        return HttpResponse('''<script>alert("invalid username or password");window.location="/"</script>''')

def Manage_job_veccancy(request):
    ob=company.objects.all()
    return render(request,'company/Mange job veccancy.html', {'val':ob})



#home
def verify_application(request):
    ob = app_req.objects.all()
    return render(request, 'company/verify application.html', {'val': ob})

def applicationsearch(request):
    n=request.POST['textfield']
    ob=app_req.objects.filter(date__icontains=n)
    return render(request,'company/verify application.html',{'val':ob, 'n': n})

def acceptapplication(request,id):
    ob=app_req.objects.get(id=id)
    ob.status='Accepetd'
    ob.save()
    return HttpResponse('''<script>alert("accepted successfully ");window.location="/verify_application"</script>''')

def rejectapplication(request,id):
    ob=app_req.objects.get(id=id)
    ob.status='Rejected'
    ob.save()
    return HttpResponse('''<script>alert("rejected successfully ");window.location="/verify_application"</script>''')

def add_tips(request):
    return render(request,'guide/add tips.html')

def addtips(request):
    tip1=  request.POST['textfield2']
    detail = request.POST['textfield3']
    ob=tip()
    ob.tips=tip1
    ob.details=detail
    ob.GUIDE = guide.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added sucessfully");window.location="view_tips"</script>''')

def view_tips(request):
    ob=tip.objects.all()
    return render(request, 'guide/view tips.html',{'val':ob})



def view_Review(request):
    ob =review.objects.all()
    ob1 =company.objects.all()
    return render(request,'guide/view Review.html', {'val':ob,'com':ob1})

def viewReviewsearch(request):
    n=request.POST['textfield']
    ob=review.objects.filter(date__icontains=n)
    return render(request,'guide/view Review.html',{'val':ob,'date':n})
