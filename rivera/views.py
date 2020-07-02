from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import members,guest,EmployeeData
from . forms import signupForm,signinForm,EmployeeForm2,MailSendingForm,guestForm
from django.core.mail.message import EmailMessage

# Create your views here.

def home(request):
    return render (request,'rivera/home.html')

def about(request):
    return render (request,'rivera/about.html')

def offers(request):
    return render (request,'rivera/offers.html')

def features(request):
    return render (request,'rivera/features.html')

def gallery(request):
    return render (request,'rivera/gallery.html')

def events(request):
    return render (request,'rivera/events.html')

def contact(request):
    return render (request,'rivera/contact.html')

def membership(request):
    return render (request,'rivera/membership.html')

def guest(request):
    return render (request,'rivera/guest.html')


def membersdetails(request):
    details=members.objects.all()
    return render(request,'rivera/membersdetails.html',{'details':details})

def book(request):
    return render (request,'rivera/book.html')

def signup(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST,request.FILES)
        if form.is_valid():
            mail = request.POST.get('mail')
            form.save()

            email=EmailMessage("Rivera - Registration Successful!","Hello.Congrats! Your Membership with Rivera is now active.","shruthiviswam@gmail.com",[mail])
            email.send()

            return HttpResponse('Your Membership is Registered Successfully!')

    return render(request,'rivera/signup.html',{'form':form}) 

def guestbook(request):
    form=guestForm()
    if request.method=='POST':
        form=guestForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('Your Booking is  Successfull!')

    return render(request,'rivera/guest.html',{'form':form}) 


# def signup1(request):
#     form=signupForm1()
#     if request.method=='POST':
#         form=signupForm1(request.POST,request.FILES)
#         if form.is_valid:
#             title = request.POST.get('title')
#             firstname=request.POST.get('firstname')
#             lastname=request.POST.get('lastname')
#             username=request.POST.get('username')
#             gender=request.POST.get('gender')
#             date_of_birth=request.POST.get('date_of_birth')
#             email = request.POST.get('email')
#             password=request.POST.get('password')
#             confirmpassword=request.POST.get('confirmpassword')
#             number = request.POST.get('number')
#             address=request.POST.get('address')
#             country=request.POST.get('country')
#             joindate=request.POST.get('joindate')
#             upload_file=request.POST.get('upload_file')

#             m=members()
#             m.title=title
#             m.firstname=firstname
#             m.lastname=lastname
#             m.username=username
#             m.gender=gender
#             m.date_of_birth=date_of_birth
#             m.email=email
#             m.password=password
#             m.confirmpassword=confirmpassword
#             m.number=number
#             m.address=address
#             m.country=country
#             m.joindate=joindate
#             m.upload_file=upload_file

#             m.save()
#             return HttpResponse('Your Membership is Registered Successfully!')

#         else:
#             return HttpResponse(form.errors)
#     return render(request,'rivera/signup.html',{'form':form})


def signin(request):
    form=signinForm()
    if request.method=='POST':
        form=signinForm(request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            password=request.POST.get('password')

            g=guests()

            g.username=username
            g.password=password

            g.save()
            return HttpResponse('Sign In Successfull!')

        else:
            return HttpResponse(form.errors)
    return render(request,'rivera/signin.html',{'form':form})


def setSession(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        userdata=members.objects.filter(username=username,password=password)

        if userdata:
            form=signinForm
            request.session['username']=username
            user=request.session['username']
            request.session['sessionpassword']=password
            return render(request,'rivera/showSession.html',{'form':form,'user':user})

    return render(request,'rivera/setSession.html')

def setSession2(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        neww=guest.objects.filter(username=username,password=password)

        if neww:
            form=guestForm
            request.session['username']=username
            user=request.session['username']
            request.session['sessionpassword']=password
            return render(request,'rivera/showSession2.html',{'form':form,'user':user})

    return render(request,'rivera/setSession2.html')

def img(request):
    mem=members.objects.all()
    return render(request,'rivera/img.html',{'mem':mem})

def employeedetails(request):
    employees=EmployeeData.objects.all()
    return render(request,'rivera/employeedetails.html',{'employees':employees})
    

def employeeform(request):
    form=EmployeeForm2()
    if request.method=='POST':
        form=EmployeeForm2(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponse('Data Saved!')

    return render(request,'rivera/empmodel.html',{'form':form})

def booking(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your Booking is Successfull!')
        else:
            return HttpResponse(forms.errors)

    return render(request,'rivera/signup.html',{'form':form}) 

def MailSending(request):
    form=MailSendingForm
    if request.method=='POST':
        form=MailSendingForm(request.POST,request.FILES)
        if form.is_valid:
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            from_mail=request.POST.get('from_mail')
            to_mail=request.POST.get('to_mail')
            attachment=request.POST.get('attachment')
            
            email=EmailMessage(subject,message,from_mail,[to_mail])

            email.attach(attachment.name,attachment.read(),attachment.content_type)

            email.send()

            return HttpResponse('Mail Sent Successfully!')
    
    else:
        form=MailSendingForm()

    return render(request,'rivera/mailsend.html',{'form':form})