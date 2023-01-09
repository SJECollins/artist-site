from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('collection/<slug>', views.CollectionView.as_view(), name='collection'),
    path('piece/<slug>', views.PieceView.as_view(), name='piece'),
    path('enquiry/<slug>', views.EnquiryView.as_view(), name='enquiry'),
]