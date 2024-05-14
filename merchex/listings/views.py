from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    listings = Listing.objects.all()
    return render(request, 'listings/about.html', {'listings': listings})


def listitings(request):
    listingss = Listing.objects.all()
    return render(request, 'listings/listings.html', {'saucissedemorto': listingss})

def contact(request):
    return render(request, 'listings/contact.html')