from swampdragon import route_handler
from swampdragon.route_handler import ModelPublisherRouter
from .serializers import FooSerializer
from .models import Foo


class FooRouter(ModelPublisherRouter):
    serializer_class = FooSerializer
    model = Foo
    route_name = 'foo'

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.all()


route_handler.register(FooRouter)
