from django.urls import path
from . import views

urlpatterns=[
    path('homepage',views.home,name='homepage'),
    path('about',views.about,name='about'),
    path('offers',views.offers,name='offers'),
    path('features',views.features,name='features'),
    path('gallery',views.gallery,name='gallery'),
    path('events',views.events,name='events'),
    path('contact',views.contact,name='contact'),
    path('membership',views.membership,name='membership'),
    path('guest',views.guest,name='guest'),
    path('membersdetails',views.membersdetails,name='membersdetails'),
    path('book',views.book),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin),
    path('setSession',views.setSession,name='setSession'),
    path('setSession2',views.setSession2,name='setSession2'),
    path('img',views.img),
    path('booking',views.booking),
    path('employeedetails',views.employeedetails),
    path('employeeform',views.employeeform),
    path('mailsending',views.MailSending),
    path('guestbook',views.guestbook,name='guestbook')
]