# -*- coding: utf-8 -*-
import os
import codecs
os.environ['DJANGO_SETTINGS_MODULE'] = 'shuttle.local_settings'
import django
django.setup()
from shuttle.models import Node, Route, Time
from django.core.files.base import ContentFile
from slugify import slugify

'''
    Update database with text file (to see the format please check "raw.txt").
    -- DEBUG purpose only --
    This file will do the same thing with "/upload".
'''

def initialize():
    with codecs.open('raw.txt', 'r', 'utf-8') as f:
        data = f.readlines()
    f.closed

    index = data.index("--DATA--\n")
    images = data[:index]
    data = data[index+1:]
    image_table = dict(x.rstrip().split(":") for x in images)

    for i in range(0, len(data), 2):
        clean_d = data[i][:-1]
        formated_d = clean_d.split(" - ")
        start_node, created = Node.objects.get_or_create(name=unicode(formated_d[0]))
        dest_node, created = Node.objects.get_or_create(name=unicode(formated_d[1]))
        clean_t = data[i+1][:-1]
        obj, created = Route.objects.get_or_create(start=start_node, destination=dest_node)
        obj.raw_data = clean_t
        obj.save()
        print "[\033[1m\033[92mOK\033[0m]\033[94m", obj.start, obj.destination, "\033[0mis saved in to the database"

    all_nodes = Node.objects.all()
    for n in all_nodes:
        f = open(image_table[n.name], 'rb')
        s_name = slugify(n.name)
        n.query_name = s_name
        n.image.save(s_name + ".png", ContentFile(f.read()), True)

    print "[\xF0\x9F\x8F\x86 ] \x1b[37;44m\033[1m DONE without any error \x1b[0m"


if __name__ == '__main__':
    initialize()
