from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from interview.VacancyForm import VacancyForm
from interview.models import *


def main(request):
    return render(request,'admin/admi login.html')

def adminhm(request):
    return render(request,'admin/admin home.html')

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
    return render(request,'admin/view review.html',{'val':ob,'com':ob1})

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
    vaccancy=  request.POST['textfield2']
    qualification = request.POST['textfield3']
    exp = request.POST['textfield4']
    salary = request.POST['textfield5']
    Details = request.POST['textfield6']
    Type = request.POST['textfield7']
    ob=vaccancy()



    return HttpResponse('''<script>alert("added sucessfully");window.location="/Manage_job_veccancy"</script>''')


def chat_with_candidate(request):
    return render(request,'company/chat with candidate.html')

def company_home(request):
    return render(request,'company/company home.html')

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
    ob.Username=username
    ob.password=password
    ob.type='company'
    ob.save()
    obb=guide()
    obb.Name=name
    obb.Place=place
    obb.Phone=phone
    obb.Email=email
    obb.Website=website
    obb.LOGIN = ob
    obb.save()
    return HttpResponse('''<script>alert("regesterd sucessfully");window.location="/company_register"</script>''')

def accept(request,id):
    ob=company.objects.get(id=id)
    ob.type='company'
    ob.save()
    return HttpResponse('''<script>alert("accepted successfully ");window.location="/Verify_company"</script>''')

def reject(request,id):
    ob=company.objects.get(id=id)
    ob.type='reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected successfully ");window.location="/Verify_company"</script>''')

def Mange_job_veccancy(request):
    return render(request,'company/Mange job veccancy.html')

def Add_question(request):
    return render(request,'guide/Add question.html')

def add_text_type(request):
    return render(request,'guide/add text type.html')

def add_tips(request):
    return render(request,'guide/add tips.html')

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
    return render(request,'guide/Guid home.html')

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
    return render(request, 'guide/manage question.html')

def manage_test_type(request):
    return render(request, 'guide/manage test type.html')

def Send_reply(request):
    return render(request, 'guide/Send reply.html')

def view_doubt(request):
    return render(request, 'guide/view doubt.html')

def view_guid_line(request):
    return render(request, 'guide/view guid line.html')

def view_Review(request):
    return render(request, 'guide/view Review.html')

def log_out(request):
    return render(request, 'guide/admi login.html')

def log_in(request):
    uname=request.POST['textfield']
    password=request.POST['textfield2']
    ob=Login.objects.get(username=uname,password=password)
    if ob.type=='admin':
       return HttpResponse('''<script>alert("Welcome to Admin home");window.location="/adminhm"</script>''')
    elif ob.type=='company':
        return HttpResponse('''<script>alert("Welcome to company");window.location="/company_home"</script>''')
    elif ob.type=='guid':
        return HttpResponse('''<script>alert("Welcome to guid");window.location="/Guid_home"</script>''')
    else:
        return HttpResponse('''<script>alert("invalid username or password");window.location="/"</script>''')



#def company_home(request):
  #  return render(request,'company/company home.html')

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
    return render(request,'company/verify application.html',{'val':ob})

def acceptapplication(request,id):
    ob=app_req.objects.get(id=id)
    ob.type='app_req'
    ob.save()
    return HttpResponse('''<script>alert("accepted successfully ");window.location="/Verify_company"</script>''')

def rejectapplication(request,id):
    ob=app_req.objects.get(id=id)
    ob.type='reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected successfully ");window.location="/Verify_company"</script>''')




