from django.shortcuts import render
from django.views import View

class HomeList(View):
    def get(self, request):
        return render(request, 'home/main.html')
