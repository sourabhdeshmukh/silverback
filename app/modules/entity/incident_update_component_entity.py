"""
Incident Update Component Module
"""

# Standard Library
import datetime

# Third Party Library
import pytz
from django.utils import timezone
from django.db.models.aggregates import Count

# Local Library
from app.models import Component
from app.models import IncidentUpdate
from app.models import IncidentUpdateComponent


class IncidentUpdateComponentEntity():

    def insert_one(self, item):
        new_item = IncidentUpdateComponent()

        if "type" in item:
            new_item.type = item["type"]

        if "incident_update_id" in item:
            new_item.incident_update = None if item["incident_update_id"] is None else IncidentUpdate.objects.get(pk=item["incident_update_id"])

        if "component_id" in item:
            new_item.component = None if item["component_id"] is None else Component.objects.get(pk=item["component_id"])

        new_item.save()
        return False if new_item.pk is None else new_item

    def update_one_by_id(self, id, data):
        item = self.get_one_by_id(id)
        if item is not False:

            if "type" in data:
                item.type = data["type"]

            if "incident_update_id" in data:
                item.incident_update = None if data["incident_update_id"] is None else IncidentUpdate.objects.get(pk=data["incident_update_id"])

            if "component_id" in data:
                item.component = None if data["component_id"] is None else Component.objects.get(pk=data["component_id"])

            item.save()
            return True
        return False

    def count_all(self, incident_update_id):
        return IncidentUpdateComponent.objects.filter(incident_update_id=incident_update_id).count()

    def get_all(self, incident_update_id):
        return IncidentUpdateComponent.objects.filter(incident_update_id=incident_update_id).order_by('-created_at')

    def get_one_by_id(self, id):
        try:
            item = IncidentUpdateComponent.objects.get(id=id)
            return False if item.pk is None else item
        except Exception:
            return False

    def get_affected_components(self, days=0):
        last_x_days = timezone.now() - datetime.timedelta(days)
        return IncidentUpdateComponent.objects.filter(created_at__gte=datetime.datetime(
            last_x_days.year,
            last_x_days.month,
            last_x_days.day,
            tzinfo=pytz.UTC
        )).order_by('-created_at')

    def delete_one_by_id(self, id):
        item = self.get_one_by_id(id)
        if item is not False:
            count, deleted = item.delete()
            return True if count > 0 else False
        return False

    def count_over_days(self, days=7):
        last_x_days = timezone.now() - datetime.timedelta(days)
        return IncidentUpdateComponent.objects.filter(
            created_at__gte=last_x_days
        ).extra({"day": "date(created_at)"}).values("day").order_by('-day').annotate(count=Count("id"))
