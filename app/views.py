from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from app.models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count
        al = Auto.objects.all()
        ctx = {'make_count': mc, 'auto_list': al}

        return render(request, 'app/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'app/make_list.html', ctx)


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    success_url = reverse_lazy('app:all')
    fields = '__all__'


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    success_url = reverse_lazy('app:all')
    fields = '__all__'


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    success_url = reverse_lazy('app:all')
    fields = '__all__'


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('app:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('app:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('app:all')
