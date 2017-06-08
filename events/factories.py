from factory import DjangoModelFactory
from .models import Event
import factory


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event
        django_get_or_create = ('name',)

    name = factory.Faker('name')
