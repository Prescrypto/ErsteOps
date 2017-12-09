from django.shortcuts import render, redirect


def home(request):
    ''' Login page '''
    print("HI")
    return render(request, 'home/login.html')

def logout_page(request):
    ''' logout url '''
    pass

