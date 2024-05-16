from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

# listings/views.py

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def about(request):
    listings = Listing.objects.all()
    return render(request, 'listings/about.html', {'listings': listings})


def listitings(request):
    listingss = Listing.objects.all()
    return render(request, 'listings/listings.html', {'saucissedemorto': listingss})

def contact(request):
    return render(request, 'listings/contact.html')

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit