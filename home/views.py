from django.shortcuts import render
from django.views import View

from .models import Event


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


class EventView(View):
    def get(self, request):
        events = Event.objects.all()
        template_name = 'home/events.html'
        context = {
            'events': events,
        }
        return render(request, template_name, context)
