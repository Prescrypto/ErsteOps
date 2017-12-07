from django.shortcuts import render, redirect
from emergency.models import Emergency

def emergency(request):
    emergencies = Emergency.objects.all().order_by("-created_at")[:10]
    ctx={'emergencies': emergencies}
    return render(request, "notifications/emergency.html", ctx)