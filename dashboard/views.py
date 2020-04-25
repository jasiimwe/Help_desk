from django.shortcuts import render
from account.models import Account

# Create your views here.
def index(request):
    return render(request, 'dashboard/home.html',{})
