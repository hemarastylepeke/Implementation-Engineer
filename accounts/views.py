from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Landing page
def landing_page(request):
    return render(request, 'account/landing_page.html')

@login_required
def success_page(request):
    return render(request, 'account/success_page.html')