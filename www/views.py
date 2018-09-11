from django.shortcuts import render


def inicio(request):

    return render(request, '01_base/base-application.html')