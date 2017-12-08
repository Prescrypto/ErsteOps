from django.shortcuts import render, redirect
from emergency.models import Emergency, AttentionDerivation

def emergency(request):
    emergencies = Emergency.objects.all().order_by("-created_at")[:10]
    ctx={'emergencies': emergencies}
    return render(request, "notifications/emergency.html", ctx)


def derivation(request):
    derivations = AttentionDerivation.objects.all().order_by("-created_at")[:10]
    ctx={'derivations': derivations}
    return render(request, "notifications/derivation.html", ctx)
