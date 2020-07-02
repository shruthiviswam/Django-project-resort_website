from django import forms
from . models import members,guest,EmployeeData

class signupForm(forms.ModelForm):
    class Meta:
        model=members
        fields=['title','firstname','lastname','username','gender','number','date_of_birth','country','address','mail','password','joindate','upload_file']


class guestForm(forms.ModelForm):
    class Meta:
        model=guest
        fields=['username','password','name','mail','phone','city','country','arrive','depart','people','room','bedding','comments']

class signupForm1(forms.Form):
    title_choice=[
        ('Mr.','Mr.'),
        ('Ms.','Ms.'),
        ('Mrs.','Mrs.')
    ]
    title=forms.CharField(widget=forms.Select(choices=title_choice))
    firstname = forms.CharField(label='FistName', widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    username=forms.CharField(widget=forms.TextInput())

    GENDER_CHOICES=(
        ('M','M'),
        ('F','F')
    )
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    number=forms.CharField(widget=forms.TextInput())
    date_of_birth = forms.DateField(widget=forms.TextInput())
   
    country_choice=[
        ('India','India'),
        ('Pakistan','Pakistan'),
        ('China','China')
    ]
    country=forms.CharField(widget=forms.Select(choices=country_choice))
    address=forms.CharField(widget=forms.Textarea())
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    confirmpassword=forms.CharField(widget=forms.PasswordInput())
    joindate=forms.DateField()
    upload_file=forms.FileField()
    terms=forms.BooleanField()

    def clean_confirmpassword(self):
        password=self.cleaned_data['password']
        confirmpassword=self.cleaned_data['confirmpassword']
        if not password==confirmpassword:
            raise forms.ValidationError("Passwords not matching!")
        return password

class signinForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())

class EmployeeForm2(forms.ModelForm):
    class Meta:
        model=EmployeeData
        fields = ['name','dept','upload_file']

class MailSendingForm(forms.Form):
    subject=forms.CharField()
    message=forms.CharField()
    from_mail=forms.CharField()
    to_mail=forms.CharField()
    attachment=forms.FileField()
