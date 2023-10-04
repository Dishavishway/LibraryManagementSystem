from django.urls import path
from lib.views import *

app_name = 'lib'

urlpatterns = [
    path('', Welcome),
    path('new-user',SignUpForm, name= 'SignUpForm'),
    path('store-user',StoreDetails, name='StoreDetails'),
    path('login',loginView, name='login'),
    path('home',Home, name='Home'),
    path('add',addForm, name='addForm'),
    path('store-book',AddBookDetails, name='AddBookDetails'),
    path('show-data',show_data, name='show_data'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('delete', delete_data, name='delete_data'),
    path('delete-data', delete_data, name='delete_book'),

]