from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from shared_app.models import ProgrammingLanguage, Framework, CourseData

class PlListView(LoginRequiredMixin, ListView):
    model = ProgrammingLanguage
    template_name = 'Programming-Language/list.html'
    context_object_name = 'data'
    ordering = ['-id']

    def handle_no_permission(self):
        messages.error(self.request, 'You must be logged in to view this page.')
        return super().handle_no_permission()


class PlAddView(LoginRequiredMixin, CreateView):
    model = ProgrammingLanguage
    template_name = 'Programming-Language/add.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('shared-app:programming-language-list')

    def form_valid(self, form):
        messages.success(self.request, "Programming Language added successfully")
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page')
        return super().handle_no_permission()


class PlDetailView(LoginRequiredMixin, DetailView):
    model = ProgrammingLanguage
    template_name = 'Programming-Language/detail.html'
    context_object_name = 'obj'

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to view this page')
        return super().handle_no_permission()


class PlUpdateView(LoginRequiredMixin, UpdateView):
    model = ProgrammingLanguage
    template_name = 'Programming-Language/update.html'
    context_object_name = 'obj'
    fields = ['name', 'description']
    success_url = reverse_lazy('shared-app:programming-language-list')

    def form_valid(self, form):
        messages.success(self.request, "Programming Language updated successfully")
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to update the page')
        return super().handle_no_permission()


class PlDeleteView(LoginRequiredMixin, DeleteView):
    model = ProgrammingLanguage
    template_name = 'Programming-Language/delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('shared-app:programming-language-list')

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "Programming Language deleted successfully")
        return super().delete(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to delete this item')
        return super().handle_no_permission()
    

class FwListView(LoginRequiredMixin, ListView):
    model = Framework
    template_name = 'Framework/list.html'
    context_object_name = 'data'
    ordering = ['-id']

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()


class FwAddView(LoginRequiredMixin, CreateView):
    model = Framework
    template_name = 'Framework/add.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('shared-app:framework-list')

    def form_valid(self, form):
        messages.success(self.request, "Framework added successfully")
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page')
        return super().handle_no_permission()
    

class FwDetailView(LoginRequiredMixin, DetailView):
    model = Framework
    template_name = 'framework/detail.html'
    context_object_name = 'obj'

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to view this page')
        return super().handle_no_permission()


class FwUpdateView(LoginRequiredMixin, UpdateView):
    model = Framework
    template_name = 'Framework/update.html'
    context_object_name = 'obj'
    fields = ['name', 'description']
    success_url = reverse_lazy('shared-app:framework-list')

    def form_valid(self, form):
        messages.success(self.request, "Framework updated successfully")
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to update the page')
        return super().handle_no_permission()


class FwDeleteView(LoginRequiredMixin, DeleteView):
    model = Framework
    template_name = 'framework/delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('shared-app:framework-list')

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "Framework deleted successfully")
        return super().delete(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to delete this item')
        return super().handle_no_permission()
    

class CdListView(LoginRequiredMixin, ListView):
    model = CourseData
    template_name = 'course-data/list.html'
    context_object_name = 'data'
    ordering = ['-id']

    def handle_no_permission(self):
        messages.error(self.request, 'Please login to visit add page ')
        return super().handle_no_permission()

