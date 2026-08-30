from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import RegisterForm
from .models import OwnerProfile
from django.contrib.auth.decorators import login_required



def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            OwnerProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                area=form.cleaned_data['area']
            )

            login(request, user)

            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Invalid username or password.'
            }
        )

    return render(
        request,
        'accounts/login.html'
    )

def logout_view(request):

    logout(request)

    return redirect('home')
@login_required
def profile(request):

    profile, created = OwnerProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'phone': '',
            'area': ''
        }
    )

    if request.method == 'POST':

        phone = request.POST.get('phone', '').strip()
        area = request.POST.get('area', '').strip()

        profile.phone = phone
        profile.area = area

        profile.save()

        return redirect('profile')

    return render(
        request,
        'accounts/profile.html',
        {
            'profile': profile
        }
    )