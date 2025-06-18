# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from shared_app.models import (
    ProgrammingLanguage
)
from django.urls import reverse_lazy

class PlListView(LoginRequiredMixin, ListView):
    model = ProgrammingLanguage
    template_name = 'pl-list.html'
    context_object_name = 'data' 
    queryset = ProgrammingLanguage.objects.all() 
    ordering = ['-id'] 

    def handle_no_permission(self):
        messages.error(self.request, 'You must be logged in to view this page.')
        return super().handle_no_permission()

    # def get(self, request):
    #     data = ProgrammingLanguage.objects.all().order_by('-id')
    #     return super().get(request)


class PlAddView(LoginRequiredMixin, CreateView):
    model = ProgrammingLanguage
    fields = ['name', 'description']
    template_name = 'pl-add.html'
    success_url = reverse_lazy('shared-app:programming-language-list')


class PlDetailView(LoginRequiredMixin, DetailView):
    model = ProgrammingLanguage
    template_name = 'pl-detail.html'
    context_object_name = 'obj'


class PlUpdateView(LoginRequiredMixin, UpdateView):
    model = ProgrammingLanguage
    template_name = 'pl-update.html'
    context_object_name = 'obj'
    fields = ['name', 'description']
    success_url = reverse_lazy('shared-app:programming-language-list')


class PlDeleteView(LoginRequiredMixin, DeleteView):
    model = ProgrammingLanguage
    template_name = 'pl-delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('shared-app:programming-language-list')
