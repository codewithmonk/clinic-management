from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def show_options(request):
    return render(request, 'core/home.html', {})
