from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from lib.models import *
from twilio.rest import Client

def Welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())

def SignUpForm(request):
    res = render(request, 'sign_up_form.html')
    return res

def StoreDetails(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        
        if (len(User.objects.filter(username = username))):
            userStatus = 1
        else:
            user = User()
            user.name = request.POST['name']
            user.username = request.POST['username']
            user.phone_number = request.POST['phone number']
            user.enroll = request.POST['enroll']
            user.email = request.POST['email']
            user.password = request.POST['password']
            
            user.save()
            userStatus = 2
            
    else: 
        userStatus = 3
        
    context = {'userStatus': userStatus}
    res = render(request, 'message.html', context)
    return res

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password)
        
        if len(user) == 0:
            loginError = "Invalid Username or Password"
            res = render(request, 'login.html', {'loginError': loginError})
        else:
            # Login Success
            request.session['username'] = user[0].username
            request.session['name'] = user[0].name
            
            # # Twilio API code
            # account_sid = 'AC85c74b953e10fe431e7123fa7fd94894'
            # auth_token = '328040aa99a67251eb499896688e8da4'
            # client = Client(account_sid, auth_token)
            
            # users = User.objects.get(username=username)  # Get the user object

            # message = client.messages.create(
            #     from_='+18149805813',
            #     body='You logged in successfully....!! Welcome to Library Management System.',
            #     to='+917049486969'
            # )
            # print(message.sid)
            
            res = render(request, 'home.html')
    else:  
        res = render(request, 'login.html')
    return res

def Home(request):
    if 'name' not in request.session.keys():
        res = render("login")
    else:
        res = render(request, 'home.html')
    return res

def addForm(request):
    res = render(request, 'add.html')
    return res

def AddBookDetails(request):
    if request.method == 'POST':
        book_id = request.POST['book_id']

        if len(Book.objects.filter(book_id=book_id)):
            userStatus = 1
        else:
            book = Book()
            book.book_id = request.POST['book_id']
            book.book_name = request.POST['book_name']
            book.author = request.POST['author']
            book.price = request.POST['price']

            user = User.objects.get(username=request.session['username'])
            book.username = user  # Assign the User instance to the username field

            book.save()
            userStatus = 2
    else:
        userStatus = 3

    context = {'userStatus': userStatus}
    res = render(request, 'AddMessage.html', context)
    return res



def show_data(request):
    username = request.session['username']  # Assuming you're storing the username in the session
    user = User.objects.get(username=username)
    books = Book.objects.filter(username=user)  # Filter books by the user object
    context = {'user': user, 'books': books}
    return render(request, 'show_data.html', context)

def delete_data(request):
    username = request.session['username']  # Assuming you're storing the username in the session
    user = User.objects.get(username=username)
    books = Book.objects.filter(username=user)  # Filter books by the user object
    context = {'user': user, 'books': books}
    return render(request, 'delete_data.html', context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)

    if request.method == 'POST':
        book.delete()
        return render(request, 'home.html')

    context = {'book': book}
    return render(request, 'delete_book.html', context)
# def delete(request):
#         if request.method == 'POST':
#             book_id = request.POST['book_id']
#             book = get_object_or_404(Book, book_id=book_id)
#             book.delete()
            
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Redirect back to the previous page
#         else:
#             return redirect('delete_data') 