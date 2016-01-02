from respite import Views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime	
from models import Node, Route, Time

class PostViews(Views):
    supported_formats = ['html', 'json', 'xml']

    def index(self, request):
        nodes = Node.objects.all()

        return self._render(
            request = request,
            template = 'bilgi/index',
            context = {
                'nodes': nodes
            },
            status = 200
        )
	
    def show(self, request, campus):
        node = Node.objects.get(query_name=campus)
        routes = Route.objects.filter(start=node)

        return self._render(
            request = request,
            template = 'bilgi/counter',
            context = {
            	'start_node':node,
                'routes': routes,
            },
            status = 200
        )	