from django.shortcuts import render, HttpResponse

# Create your views here.
def accounts_views(request):
    return render(request, 'accounts/accounts.html')