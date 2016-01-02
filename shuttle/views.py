from respite import Views
from models import Node, Route, Time

# THOSE WERE FOR DEBUG PURPOSE AND HTML TEMPLATES ARE DELETED!
class NodeViews(Views):
    supported_formats = ['html', 'json', 'xml']

    def index(self, request):
        nodes = Node.objects.all()

        return self._render(
            request = request,
            template = 'all_nodes',
            context = {
                'nodes': nodes
            },
            status = 200
        )

    def show(self, request, id):
        node = Node.objects.get(pk=id)

        return self._render(
            request = request,
            template = 'node',
            context = {
                'node': node
            },
            status = 200
        )