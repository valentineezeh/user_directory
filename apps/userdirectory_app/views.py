from django.shortcuts import render, redirect
from validate_email import validate_email
from .models import UserDirectory

# Create your views here.
def index(request):
    return render(request, 'userdirectory_app/index.html')

def add_user(request):
    context = {
        'loading': False
    }
    return render(request, 'userdirectory_app/add_user.html', context)

def create(request):
    user_name = request.POST['name']
    user_email = request.POST['email']
    is_valid = validate_email(user_email)

    if user_email.strip() == '' or user_name.strip() == '':
        context = {
            'errors': {
                'name': 'This Field is required',
                'email': 'This Field is required'
            }
        }
        return render(request, 'userdirectory_app/add_user.html', context)

    elif is_valid == False:
        context = {
            'errors': {
            'email': 'Invalid email format'
        }
        }
        return render(request, 'userdirectory_app/add_user.html', context)

    elif user_name.isalpha() == False:
        context = {
            'errors': {
                'name': 'Name must be alphabetical without space',
            }
        }
        return render(request, 'userdirectory_app/add_user.html', context)
    else: 
        user = UserDirectory(
            name = user_name,
            email = user_email
            )
        user.save()
        return redirect(user_list)

def user_list(request):
    users = UserDirectory.objects.all()
    context = {'users': users}
    return render(request, 'userdirectory_app/user_list.html', context)