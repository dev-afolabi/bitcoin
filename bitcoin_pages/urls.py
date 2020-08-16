from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about-us$', views.about, name='about-us'),
    url(r'^contact-us$', views.contact, name='contact'),
    url(r'^frequently-asked-question$', views.faq, name='faq'),
    url(r'^services$', views.services, name='services'),
]