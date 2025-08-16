from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # We will pass an integer as the primary key (pk). i.e. http://localhost:8000/record/2
    path('record/<int:pk>', views.customer_record, name='record'),
]

