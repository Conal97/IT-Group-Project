import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Area, Munro 
def populate():

    fort_william_munros = [
        {'area' : 'Fort William',
        'name' : 'Ben Nevis',
        'difficulty' : 1,
        'elevation': 1345,
        'coordinates': '56.7969° N, 5.0036° W'},
    ]

    cairngorms_munros = [
        {'area' : 'Cairngorms',
        'name' : 'Ben Macdui',
        'difficulty' : 2,
        'elevation': 1309,
        'coordinates': '57.0704° N, 3.6691° W'},

    ]

    loch_lomond_munros = [
        {'area' : 'Loch Lomond',
        'name' : 'Ben Lomond',
        'difficulty' : 5,
        'elevation': 974,
        'coordinates': '56.7969° N, 5.0036° W'},

        {'name' : 'Ben Vane',
        'difficulty' : 4,
        'elevation': 915,
        'coordinates': '56.2499° N, 4.7817° W'},
    ]

    areas = {'Fort William' : {'munros': fort_william_munros,}, 
            'Cairngorms' : {'munros': cairngorms_munros,},
            'Loch Lomond' : {'munros': loch_lomond_munros,},
            }


    for area in areas.items():
        a = add_area(area)
        for m in 'munros':
            add_munro(m['area'], m['name'], m['difficulty'], m['elevation'], m['coordinates'],)

    for a in Area.objects.all():
        for m in Munro.objects.filter(area=a):
            print(f'- {a}: {m}')

def add_munro(area, name, diff, ele, coords):
    m = Munro.objects.get_or_create(munroarea = area, name=name)[0]
    m.difficulty = diff
    m.elevation = ele
    m.coordinates = coords
    m.save()
    return m

def add_area(name):
    a = Area.objects.get_or_create(name=name) [0]
    a.save()
    return a

if __name__=='__main__':
    print('Starting Rango Population Script...')
    populate()