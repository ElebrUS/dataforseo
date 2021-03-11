from django.shortcuts import redirect
from .models import Location
from .models import Country
import json


def update_loc(request):
    cy = Country.objects.filter(iso_code='DE')[0]
    with open('de.json', 'r') as file:
        pre = json.load(file)
    for obj in pre:
        if len(Location.objects.filter(code=obj['location_code'])) == 0:
            f = Location()
            setattr(f, 'country', cy)
            setattr(f, 'code', obj['location_code'])
            setattr(f, 'name', obj['location_name'].split(',')[0])
            setattr(f, 'parent_code', obj['location_code_parent'])
            setattr(f, 'type', obj['location_type'])
            f.save()
    return redirect('/')
