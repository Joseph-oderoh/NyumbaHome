from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Nyumbani
# Create your views here.
@login_required
def homepage(request):
    return render(request, 'index.html')

@login_required
def homes(request):
    all_homes = Nyumbani.objects.all()
    all_homes = all_homes[::-1]
    params = {
        'all_hoods': all_homes,
    }
    return render(request, 'nyumbani.html', params)