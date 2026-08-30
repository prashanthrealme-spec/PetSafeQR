from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Pet
from .forms import PetForm

import qrcode
import base64
from django.urls import reverse

from io import BytesIO


# ---------------------------------------
# HOME
# ---------------------------------------

def home(request):

    return render(
        request,
        'pets/home.html'
    )


# ---------------------------------------
# DASHBOARD
# ---------------------------------------

@login_required
def dashboard(request):

    pets = Pet.objects.filter(
        owner=request.user
    ).order_by('-created_at')

    return render(
        request,
        'pets/dashboard.html',
        {
            'pets': pets
        }
    )


# ---------------------------------------
# ADD PET
# ---------------------------------------

@login_required
def add_pet(request):

    if request.method == 'POST':

        form = PetForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            pet = form.save(
                commit=False
            )

            pet.owner = request.user

            pet.save()

            return redirect(
                'dashboard'
            )

    else:

        form = PetForm()

    return render(
        request,
        'pets/add_pet.html',
        {
            'form': form
        }
    )


# ---------------------------------------
# PET DETAIL
# ---------------------------------------

@login_required
def pet_detail(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id,
        owner=request.user
    )

    return render(
        request,
        'pets/pet_detail.html',
        {
            'pet': pet
        }
    )


# ---------------------------------------
# EDIT PET
# ---------------------------------------

@login_required
def edit_pet(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id,
        owner=request.user
    )

    if request.method == 'POST':

        form = PetForm(
            request.POST,
            request.FILES,
            instance=pet
        )

        if form.is_valid():

            form.save()

            return redirect(
                'pet_detail',
                pet_id=pet.pet_id
            )

    else:

        form = PetForm(
            instance=pet
        )

    return render(
        request,
        'pets/edit_pet.html',
        {
            'form': form,
            'pet': pet
        }
    )


# ---------------------------------------
# DELETE PET
# ---------------------------------------

@login_required
def delete_pet(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id,
        owner=request.user
    )

    if request.method == 'POST':

        pet.delete()

        return redirect(
            'dashboard'
        )

    return render(
        request,
        'pets/delete_pet.html',
        {
            'pet': pet
        }
    )


# ---------------------------------------
# REPORT PET MISSING
# ---------------------------------------

@login_required
def report_missing(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id,
        owner=request.user
    )

    if request.method == 'POST':

        pet.status = 'MISSING'

        pet.save()

        return redirect(
            'pet_detail',
            pet_id=pet.pet_id
        )

    return render(
        request,
        'pets/report_missing.html',
        {
            'pet': pet
        }
    )


# ---------------------------------------
# MARK PET SAFE
# ---------------------------------------

@login_required
def mark_safe(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id,
        owner=request.user
    )

    if request.method == 'POST':

        pet.status = 'SAFE'

        pet.save(
            update_fields=[
                'status',
                'updated_at'
            ]
        )

        return redirect(
            'pet_detail',
            pet_id=pet.pet_id
        )

    return render(
        request,
        'pets/mark_safe.html',
        {
            'pet': pet
        }
    )
# ---------------------------------------
# PUBLIC PET PAGE
# ---------------------------------------

def public_pet(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id
    )

    return render(
        request,
        'pets/public_pet.html',
        {
            'pet': pet
        }
    )
# ---------------------------------------
# DOWNLOAD QR
# ---------------------------------------

@login_required
def download_qr(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id,
        owner=request.user
    )

    qr_url = request.build_absolute_uri(
        reverse(
            'public_pet',
            kwargs={'pet_id': pet.pet_id}
        )
    )

    qr = qrcode.make(qr_url)

    buffer = BytesIO()

    qr.save(
        buffer,
        format='PNG'
    )

    response = HttpResponse(
        buffer.getvalue(),
        content_type='image/png'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="{pet.name}_PetSafe_QR.png"'
    )

    return response

# ---------------------------------------
# QR TAG
# ---------------------------------------

@login_required
def qr_tag(request, pet_id):

    pet = get_object_or_404(
        Pet,
        pet_id=pet_id,
        owner=request.user
    )

    qr_url = request.build_absolute_uri(
        reverse(
            'public_pet',
            kwargs={'pet_id': pet.pet_id}
        )
    )

    qr = qrcode.make(qr_url)

    buffer = BytesIO()

    qr.save(
        buffer,
        format='PNG'
    )

    qr_code = base64.b64encode(
        buffer.getvalue()
    ).decode()

    return render(
        request,
        'pets/qr_tag.html',
        {
            'pet': pet,
            'qr_code': qr_code
        }
    )