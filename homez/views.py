from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NyumbaniForm, UpdateProfileForm
from .models import  Likes, Nyumbani

# Create your views here.
@login_required
def homepage(request):
    return render(request, 'index.html')

@login_required
def homes(request):
    all_homes = Nyumbani.objects.all()
    all_homes = all_homes[::-1]
    params = {
        'all_homes': all_homes,
    }
    return render(request, 'nyumbani.html', params)

@login_required
def create_home(request):
    if request.method == 'POST':
        form = NyumbaniForm(request.POST, request.FILES)
        if form.is_valid():
            homes = form.save(commit=False)
            homes.admin = request.user.profile
            homes.save()
            return redirect('nyumbani')
    else:
        form = NyumbaniForm()
    return render(request, 'new_nyumbani.html', {'form': form})

def profile(request, username):
    return render(request, 'profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

def like_image(request, nyumbani_id):
    nyumbani = get_object_or_404(Nyumbani,id = nyumbani_id)
    like = Likes.objects.filter(nyumbani = nyumbani ,user = request.user).first()
    if like is None:
        like = Likes()
        like.image = nyumbani
        like.user = request.user
        like.save()
    else:
        like.delete()
    return redirect('landing')

