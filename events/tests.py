from django.shortcuts import reverse
from rest_framework import status
from events.factories import EventFactory
from django_drf_ci import base_tests
import json
# Create your tests here.


class EventTests(base_tests.BaseApiTest):

    def test_events_list(self):
        EventFactory(name="New event")

        response = self.client.get(reverse('events:event-list-create'))

        self.assertEqual('New event', response.data[0]['name'])

    def test_event_create(self):
        data = json.dumps({"name": "Event 1"})

        response = self.client.post(reverse('events:event-list-create'), data, content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
