from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add_contact', views.add_contact, name="add_contact"),
    path('delete_contact/<str:contact_id>', views.delete_contact, name="delete_contact")
]