from django.urls import path
from .import views
urlpatterns = [
    path('cart/',views.cartdetail,name='cart'),
    path('size/',views.size,name="size"),
    path('demo/',views.demo,name="demo"),
]