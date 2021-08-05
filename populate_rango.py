import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Area, Munro 

def populate():

    fort_william_munros = [
        {'name' : 'Ben Nevis',
        'difficulty' : 1,
        'elevation': 1345,
        'coordinates': '56.7969° N, 5.0036° W',
        'description': 'Ben Nevis is the highest mountain of the British Isles. It is situated in the Highland council area, Scotland. Its summit, reaching an elevation of 4,406 feet (1,343 metres), is a plateau of about 100 acres (40 hectares), with a slight slope to the south and a sheer face to the northeast',
        'image_1' : 'Ben_Nevis_1.jpg',
        'image_2' : 'Ben_Nevis_2.jpg',
        'image_3' : 'Ben_Nevis_3.jpg',
        }
    ]

    cairngorms_munros = [
        { 'name' : 'Ben Macdui',
        'difficulty' : 2,
        'elevation': 1309,
        'coordinates': '57.0704° N, 3.6691° W',
        'description': 'Ben Macdui is the second highest mountain in Scotland (and all of the British Isles) after Ben Nevis, and the highest in the Cairngorm Mountains and the wider Cairngorms National Park. The summit elevation is 1,309 metres. Ben Macdui lies on the southern edge of the Cairngorm plateau, on the boundary between the historic counties of Aberdeenshire and Banffshire.',
        'image_1' : 'Ben_Macdui_1.jpeg',
        'image_2' : 'Ben_Macdui_2.jpeg',
        'image_3' : 'Ben_Macdui_3.jpeg',
        }
    ]

    loch_lomond_munros = [
        {'name' : 'Ben Lomond',
        'difficulty' : 5,
        'elevation': 974,
        'coordinates': '56.7969° N, 5.0036° W',
        'description': 'Ben Lomonond is situated on the eastern shore of Loch Lomond, it is the most southerly of the Munros. Ben Lomond lies within the Ben Lomond National Memorial Park and the Loch Lomond and The Trossachs National Park, property of the National Trust for Scotland.Its accessibility from Glasgow and elsewhere in central Scotland, together with the relative ease of ascent from Rowardennan, makes it one of the most popular of all the Munros.',
        'image_1' : 'Ben_Lomond_1.jpg',
        'image_2' : 'Ben_Lomond_2.jpg',
        'image_3' : 'Ben_Lomond_3.jpg',
        },

        {'name' : 'Ben Vane',
        'difficulty' : 4,
        'elevation': 915,
        'coordinates': '56.2499° N, 4.7817° W',
        'description': 'Ben Vane is situated in the southern Highlands. It is one of the Arrochar Alps and stands slightly separate from the other mountains of the group being connected on its western side to the neighbouring Beinn Ìme. Ben Vane itself just qualifies as a Munro reaching a height of 915 metresand is characterised by steep and rugged slopes which fall away to the Inveruglas Water to the east and the Allt Coiregroigan to the south.',
        'image_1' : 'Ben_Vane_1.jpg',
        'image_2' : 'Ben_Vane_2.jpg',
        'image_3' : 'Ben_Vane_3.jpg',
        }
    ]

    areas = {'Fort William' : {'munros': fort_william_munros}, 
            'Cairngorms' : {'munros': cairngorms_munros},
            'Loch Lomond' : {'munros': loch_lomond_munros}}


    for area, area_data in areas.items():
        a = add_area(area)
        for m in area_data['munros']:
            add_munro(a, m['name'], m['difficulty'], m['elevation'], m['coordinates'], m['description'], m['image_1'], m['image_2'], m['image_3'])

    for a in Area.objects.all():
        for m in Munro.objects.filter(area=a):
            print(f'- {a}: {m}')

def add_munro(area, name, diff, ele, coords, desc, img1, img2, img3):
    m = Munro.objects.get_or_create(area = area, name=name)[0] 
    m.difficulty = diff
    m.elevation = ele
    m.coordinates = coords
    m.description = desc
    m.image_1 = img1
    m.image_2 = img2
    m.image_3 = img3
    m.save()
    return m

def add_area(name):
    a = Area.objects.get_or_create(name=name)[0]
    a.save()
    return a

if __name__=='__main__':
    print('Starting Rango Population Script...')
    populate()