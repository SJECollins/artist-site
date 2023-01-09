from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Collection, Piece


class GalleryView(View):
    def get(self, request):
        collections = Collection.objects.all()
        pieces = Piece.objects.all()
        template_name = 'gallery/gallery.html'
        context = {
            'collections': collections,
            'pieces': pieces,
        }
        return render(request, template_name, context)


class CollectionView(View):
    def get(self, request, slug):
        collection = get_object_or_404(Collection, slug=slug)
        pieces = Piece.objects.filter(collection__slug=slug).order_by('-date_added')
        template_name = 'gallery/collection.html'
        context = {
            'collection': collection,
            'pieces': pieces,
        }
        return render(request, template_name, context)


class PieceView(View):
    def get(self, request, slug):
        piece = get_object_or_404(Piece, slug=slug)
        template_name = 'gallery/piece.html'
        context = {
            'piece': piece,
        }
        return render(request, template_name, context)


class EnquiryView(View):
    def get(self, request, slug):
        piece = get_object_or_404(Piece, slug=slug)
        template_name = 'gallery/enquiry.html'
        context = {
            'piece': piece,
        }
        return render(request, template_name, context)
