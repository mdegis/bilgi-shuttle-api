from respite import Views
from django.contrib.auth.decorators import login_required
from models import Node, Route, Time
from django.shortcuts import redirect
import codecs
from django.core.files.base import ContentFile
from slugify import slugify
from django.contrib.auth.models import User

class PostViews(Views):
    supported_formats = ['html', 'json', 'xml']

    def index(self, request):
        self.supported_formats = ['json']
        nodes = Node.objects.all()

        return self._render(
            request = request,
            context = {
                'nodes': nodes
            },
            status = 200
        )

    def show(self, request, campus):
        self.supported_formats = ['json']
        node = Node.objects.get(query_name=campus)
        routes = Route.objects.filter(start=node)

        return self._render(
            request = request,
            context = {
            	'start_node':node,
                'routes': routes,
            },
            status = 200
        )

    def upload(self, request):
        self.supported_formats = ['html']
        if request.user.is_staff:
            return self._render(
                request = request,
                template = 'upload',
                status = 200
            )
        else:
            return redirect('/admin/login/?next=/upload')

    def process_file(self, request):
        self.supported_formats = ['html']
        if request.user.is_staff:
            a = request.FILES['raw_shuttle']
            data = a.readlines()
            index = data.index("--DATA--\n")
            images = data[:index]
            data = data[index+1:]
            image_table = dict(unicode(x).rstrip().split(":") for x in images)

            for i in range(0, len(data), 2):
                clean_d = data[i][:-1]
                formated_d = clean_d.split(" - ")
                start_node, created = Node.objects.get_or_create(name=unicode(formated_d[0]))
                dest_node, created = Node.objects.get_or_create(name=unicode(formated_d[1]))
                clean_t = data[i+1][:-1]
                obj, created = Route.objects.get_or_create(start=start_node, destination=dest_node)
                obj.raw_data = clean_t
                obj.save()

            all_nodes = Node.objects.all()
            for n in all_nodes:
                f = open(image_table[n.name], 'rb')
                s_name = slugify(n.name)
                n.query_name = s_name
                n.image.save(s_name + ".png", ContentFile(f.read()), True)
        return redirect('/admin/login/?next=/upload')
