from django.shortcuts import render
from .models import Item
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView
# Create your views here.

def item_list(request):

    context={
        "items":Item.objects.all()
    }
    return render(request,"home-page.html",context)
def checkout(request):
    return render(request,"checkout-page.html")

def products(request):
    return render(request,"product-page.html")

class ItemDetailView(DetailView):
    model=Item
    template_name="product-page.html"
class HomeView(ListView):
    model=Item
    template_name="home-page.html"
