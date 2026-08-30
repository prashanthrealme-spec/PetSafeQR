from django.urls import path
from . import views


urlpatterns = [

    # Home
    path(
        '',
        views.home,
        name='home'
    ),

    # Owner Dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # Add Pet
    path(
        'add-pet/',
        views.add_pet,
        name='add_pet'
    ),

    # Owner Pet Details
    path(
        'my-pet/<uuid:pet_id>/',
        views.pet_detail,
        name='pet_detail'
    ),

    # Edit Pet
    path(
        'my-pet/<uuid:pet_id>/edit/',
        views.edit_pet,
        name='edit_pet'
    ),

    # Delete Pet
    path(
        'my-pet/<uuid:pet_id>/delete/',
        views.delete_pet,
        name='delete_pet'
    ),

    # Report Missing
    path(
        'my-pet/<uuid:pet_id>/missing/',
        views.report_missing,
        name='report_missing'
    ),

    # Mark Safe Confirmation
    path(
        'my-pet/<uuid:pet_id>/safe/',
        views.mark_safe,
        name='mark_safe'
    ),

    # QR Tag
    path(
        'my-pet/<uuid:pet_id>/qr/',
        views.qr_tag,
        name='qr_tag'
    ),

    # Download QR
    path(
        'my-pet/<uuid:pet_id>/qr/download/',
        views.download_qr,
        name='download_qr'
    ),

    # PUBLIC QR URL
    # This URL is accessible without login
    path(
        'pet/<uuid:pet_id>/',
        views.public_pet,
        name='public_pet'
    ),
]