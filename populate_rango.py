import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Area, Image, Munro 

#this .py fills the database with sample values, which could be easily expanded on for a full system
def populate():

    lochaber_munros = [#those munros with the area of lochaber
        {'name' : 'Ben Nevis',#munro name
        'difficulty' : 3, #difficulty of the Munro/5
        'elevation': 1345, #elevation of munro in metres
        'coordinates': '56.7969° N, 5.0036° W', #latitude and longitude of munro peak
        'duration' : '5 - 8 hours', #length of walk in hours 
        'length' : 17, #length of walk in km

        #text description of the munro
        'description': 'Ben Nevis is the highest mountain of the British Isles. It is situated in the Highland council area, Scotland. Its summit, reaching an elevation of 4,406 feet (1,343 metres), is a plateau of about 100 acres (40 hectares), with a slight slope to the south and a sheer face to the northeast',
        #the url section used to create iframe for the munros map
        'url' : 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d69913.5805281933!2d-5.071528499252209!3d56.79791289676395!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x488932978af1e5f3%3A0x6e948b77ffad9a71!2sBen%20Nevis!5e0!3m2!1sen!2skr!4v1628144434805!5m2!1sen!2skr',
        'views' : 200, #views of the munro (set to arbitary value for presentation)
        'likes' : 100, #likes of munro (set to arbitary value for presentation)
        }
    ]

    cairngorms_munros = [
        { 'name' : 'Ben Macdui',
        'difficulty' : 5,
        'elevation': 1309,
        'coordinates': '57.0704° N, 3.6691° W',
        'duration' : '6 - 7 hours',
        'length' : 17.5,
        'description': 'Ben Macdui is the second highest mountain in Scotland (and all of the British Isles) after Ben Nevis, and the highest in the Cairngorm Mountains and the wider Cairngorms National Park. The summit elevation is 1,309 metres. Ben Macdui lies on the southern edge of the Cairngorm plateau, on the boundary between the historic counties of Aberdeenshire and Banffshire.',
        'url' : "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d34702.29234376064!2d-3.7047309290042474!3d57.070476024862074!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4885f0c82878e349%3A0x1d0c681aff302730!2sBen%20Macdui!5e0!3m2!1sen!2skr!4v1628151939885!5m2!1sen!2skr",
        'views' : 25,
        'likes' : 10,
        }
    ]

    loch_lomond_munros = [
        {'name' : 'Ben Lomond',
        'difficulty' : 3,
        'elevation': 974,
        'coordinates': '56.7969° N, 5.0036° W',
        'duration' : '4.5 - 5.5 hours',
        'length' : 12,
        'description': 'Ben Lomond is situated on the eastern shore of Loch Lomond, it is the most southerly of the Munros. Ben Lomond lies within the Ben Lomond National Memorial Park and the Loch Lomond and The Trossachs National Park, property of the National Trust for Scotland.Its accessibility from Glasgow and elsewhere in central Scotland, together with the relative ease of ascent from Rowardennan, makes it one of the most popular of all the Munros.',
        'url' : 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d284444.32260357623!2d-4.785733625084698!3d56.153278769271694!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4888fe1e7dc8913d%3A0xb0349002fcb683b2!2sBen%20Lomond!5e0!3m2!1sen!2skr!4v1628152179964!5m2!1sen!2skr',
        'views' : 100,
        'likes' : 50,
        },

        {'name' : 'Ben Vane',
        'difficulty' : 3,
        'elevation': 915,
        'coordinates': '56.2499° N, 4.7817° W',
        'duration' : '4.5 - 6.5 hours',
        'length' : 11,
        'description': 'Ben Vane is situated in the southern Highlands. It is one of the Arrochar Alps and stands slightly separate from the other mountains of the group being connected on its western side to the neighbouring Beinn Ìme. Ben Vane itself just qualifies as a Munro reaching a height of 915 metresand is characterised by steep and rugged slopes which fall away to the Inveruglas Water to the east and the Allt Coiregroigan to the south.',
        'url' : "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d8866.521374988151!2d-4.790489858935455!3d56.24989551234191!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4889048775bea013%3A0xa769f749a02d3d98!2sBen%20Vane!5e0!3m2!1sen!2skr!4v1628152049636!5m2!1sen!2skr",
        'views' : 50,
        'likes' : 25,
        }
    ]

    #here the sample areas are defined, simply name of area, views and likes
    areas = {'Lochaber' : {'munros': lochaber_munros, 'views': 200,'likes':100}, 
            'Cairngorms' : {'munros': cairngorms_munros, 'views': 50,'likes':25},
            'Loch Lomond' : {'munros': loch_lomond_munros, 'views': 100,'likes':50}}

    #_images, specify what image should be displayed for what munro, with a description of the pic
    ben_nevis_images = [
        {'name' : 'Ben_Nevis_1.jpg',
        'title' : 'Ben Nevis',
        'description' : 'Ben Nevis seen from the valley below.',
        'likes' : 30,
        },

        {'name' : 'Ben_Nevis_2.jpg',
        'title' : 'Ben Nevis',
        'description' : 'Looking down on the valley situated to the base of Ben Nevis.',
        'likes' : 20,
        },

        {'name' : 'Ben_Nevis_3.jpg',
        'title' : 'Ben Nevis',
        'description' : 'Ben Nevis with dramatic cloud cover.',
        'likes' : 10,
        },
    ]

    ben_macdui_images = [
        {'name' : 'Ben_Macdui_1.jpeg',
        'title' : 'Ben Macdui',
        'description' : 'A lone hiker makes his way across the rocky summit.',
        'likes' : 29,
        },

        {'name' : 'Ben_Macdui_2.jpeg',
        'title' : 'Ben Macdui',
        'description' : 'Long, winding path through the valley below.',
        'likes' : 19,
        },

        {'name' : 'Ben_Macdui_3.jpeg',
        'title' : 'Ben Macdui',
        'description' : 'A unique beauty spot beloved by wild campers in the area.',
        'likes' : 9,
        },
    ]


    ben_lomond_images = [
        {'name' : 'Ben_Lomond_1.jpg',
        'title' : 'Ben Lomond',
        'description' : 'Ben Lomond seen from the loch that shares its name.',
        'likes' : 31,
        },

        {'name' : 'Ben_Lomond_2.jpg',
        'title' : 'Ben Lomond',
        'description' : 'Looking down from the peak at what appears to be a sea of cloud cover.',
        'likes' : 21,
        },

        {'name' : 'Ben_Lomond_3.jpg',
        'title' : 'Ben Lomond',
        'description' : 'Route to the summit as seen by drone.',
        'likes' : 11,
        },
    ]

    ben_vane_images = [
        {'name' : 'Ben_Vane_1.jpg',
        'title' : 'Ben Vane',
        'description' : 'Walkers ascend the craggy summit.',
        'likes' : 24,
        },

        {'name' : 'Ben_Vane_2.jpg',
        'title' : 'Ben Vane',
        'description' : 'Hiker celebrates now being able to update their profile on our website.',
        'likes' : 12,
        },

        {'name' : 'Ben_Vane_3.jpg',
        'title' : 'Ben Vane',
        'description' : 'Ben Vane seen from below.',
        'likes' : 3,
        },
    ]

    munro_images = {'Ben Nevis' : {'images': ben_nevis_images}, 
        'Ben Macdui' : {'images' : ben_macdui_images},
        'Ben Lomond' : {'images': ben_lomond_images},
        'Ben Vane' : {'images': ben_vane_images}}

    #iterate throught each area and create areas
    for area, area_data in areas.items():
        a = add_area(area, views = area_data['views'], likes = area_data['likes'])#area w/ name, views, likes
        #create all munros associated with an area
        for m in area_data['munros']:
            mun = add_munro(a, m['name'], m['difficulty'], m['elevation'], m['coordinates'], m['duration'], m['length'], m['description'], m['views'], m['likes'],m['url'],)
            #all pictures associated with munros
            for munro, image_data in munro_images.items(): 
                for i in image_data['images']:
                    if munro == m['name']:
                        add_image(i['name'], i['title'], i['description'], mun, i['likes']) 

    #script populate terminal display
    for a in Area.objects.all():
        for m in Munro.objects.filter(area=a):
            for i in Image.objects.filter(munro=m):
                print(f'- {a}: {m}: {i}')

#method for creating image object
def add_image(name, title, desc, munro, likes):
    i = Image.objects.get_or_create(munro = munro, name = name)[0]
    i.title = title
    i.description = desc
    i.likes = likes
    i.save()
    return i

#method for creating munro object
def add_munro(area, name, diff, ele, coords, dur, len, desc, views, likes, link):
    m = Munro.objects.get_or_create(area = area, name=name)[0] 
    m.difficulty = diff
    m.elevation = ele
    m.coordinates = coords
    m.duration = dur
    m.length = len
    m.description = desc
    m.views = views
    m.likes = likes
    m.mapslink = link
    m.save()
    return m

#method for creating area object
def add_area(name, views, likes):
    a = Area.objects.get_or_create(name=name)[0]
    a.views = views
    a.likes = likes
    a.save()
    return a

#main method
if __name__=='__main__':
    print('Starting Rango Population Script...')
    populate()