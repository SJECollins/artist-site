from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        template_name = 'home/index.html'
        return render(request, template_name)


class AboutView(View):
    def get(self, request):
        template_name = 'home/about.html'
        return render(request, template_name)


class ContactView(View):
    def get(self, request):
        template_name = 'home/contact.html'
        return render(request, template_name)
