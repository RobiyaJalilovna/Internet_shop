from django.urls import path
from . import views

urlpatterns = [
    path('buyurtmalar/', views.buyurtma_list, name='buyurtma_list'),
    path('chegirmalar/', views.chegirma_list, name='chegirma_list'),
]
