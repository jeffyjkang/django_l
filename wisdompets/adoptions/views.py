from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Pet

def home(request):
  # return HttpResponse('<p>home view</p>')
  pets = Pet.objects.all()
  return render(request, 'home.html', {
    'pets': pets,
  })

def pet_detail(request, pet_id):
  # return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')
  try:
    pet = Pet.objects.get(id=pet_id)
  except Pet.DoesNotExist:
    raise Http404('pet not found')
  return render(request, 'pet_detail.html', {
    'pet': pet,
  })
