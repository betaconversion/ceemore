from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('services/',views.service,name="service"),
    path('about-us/',views.about,name="about"),
    path('gallery/',views.gallery,name="gallery"),
    path('contact-us/',views.contact_us,name="contact_us"),
    path('reservation/',views.reservation,name="reservation"),
    path('jsons-message/',views.message,name="message"),

]