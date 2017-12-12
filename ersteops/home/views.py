import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home(request):
    ''' Login page '''
    logger = logging.getLogger('django_info')
    login_template = "home/login.html"
    if not request.user.is_anonymous():
        return redirect("emergencydashbord")

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            logger.info("Success login auth to: {}".format(username))
            login(request, user)
            return redirect('emergencydashbord')
        else:
            logger.info("Error on login auth to: {}".format(username))
            return render(request, login_template, {"auth_error": "Tu email o password no coinciden, intenta de nuevo"})

    return render(request, login_template)

def logout_page(request):
    ''' logout url '''
    pass

