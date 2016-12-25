from django.shortcuts import render

def localization(request):
    return render(request, 'localization/localization.html')
