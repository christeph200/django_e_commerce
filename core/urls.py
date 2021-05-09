from django.urls import path
from .views import checkout,products,HomeView,ItemDetailView
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('checkout',checkout,name='check-out'),
    path('products/<slug>/',ItemDetailView.as_view(),name='products')
]
app_name="core"