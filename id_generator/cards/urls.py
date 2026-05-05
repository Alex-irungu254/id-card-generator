from django.urls import path
from . import views


urlpatterns = [
  path('', views.create_card, name='create-card'),
  path('card/<int:pk>/', views.card_detail, name='card-detail'),
  path('card/<int:pk>/edit/', views.edit_card, name='edit-card'),
  path('verify/<uuid:code>/', views.verify_card, name='verify-card'),
]