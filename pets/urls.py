from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('add-pet/', views.add_pet, name='add_pet'),

    path(
        'my-pet/<uuid:pet_id>/',
        views.pet_detail,
        name='pet_detail'
    ),

    path(
        'my-pet/<uuid:pet_id>/edit/',
        views.edit_pet,
        name='edit_pet'
    ),

    path(
        'my-pet/<uuid:pet_id>/delete/',
        views.delete_pet,
        name='delete_pet'
    ),

    path(
        'my-pet/<uuid:pet_id>/missing/',
        views.report_missing,
        name='report_missing'
    ),

    path(
        'my-pet/<uuid:pet_id>/safe/',
        views.mark_safe,
        name='mark_safe'
    ),

    path(
        'my-pet/<uuid:pet_id>/qr/',
        views.qr_tag,
        name='qr_tag'
    ),

    path(
        'my-pet/<uuid:pet_id>/qr/download/',
        views.download_qr,
        name='download_qr'
    ),

    path(
        'pet/<uuid:pet_id>/',
        views.public_pet,
        name='public_pet'
    ),
]