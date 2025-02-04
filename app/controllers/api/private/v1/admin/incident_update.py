"""
Incident Updates API Endpoint
"""

# Third Party Library
from django.views import View
from django.urls import reverse
from pyvalitron.form import Form
from django.http import JsonResponse
from django.forms.fields import DateTimeField
from django.utils.translation import gettext as _

# Local Library
from app.modules.util.helpers import Helpers
from app.modules.core.request import Request
from app.modules.core.response import Response
from app.modules.core.task import Task as Task_Module
from app.modules.validation.extension import ExtraRules
from app.modules.core.decorators import allow_if_authenticated
from app.modules.core.incident import Incident as IncidentModule
from app.modules.core.subscriber import Subscriber as SubscriberModule
from app.modules.core.notification import Notification as NotificationModule
from app.modules.core.incident_update import IncidentUpdate as IncidentUpdateModule
from app.modules.core.incident_update_component import IncidentUpdateComponent as IncidentUpdateComponentModule
from app.modules.core.incident_update_notification import IncidentUpdateNotification as IncidentUpdateNotificationModule


class IncidentUpdates(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __incident = None
    __incident_update = None
    __task = None
    __notification = None
    __subscriber = None
    __incident_update_notification = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__incident = IncidentModule()
        self.__incident_update = IncidentUpdateModule()
        self.__task = Task_Module()
        self.__notification = NotificationModule()
        self.__subscriber = SubscriberModule()
        self.__incident_update_notification = IncidentUpdateNotificationModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def post(self, request, incident_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__user_id = request.user.id
        self.__request.set_request(request)

        request_data = self.__request.get_request_data("post", {
            "status": "",
            "notify_subscribers": "",
            "message": "",
            "datetime": "",
        })

        self.__form.add_inputs({
            'message': {
                'value': request_data["message"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'datetime': {
                'value': request_data["datetime"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'status': {
                'value': request_data["status"],
                'validate': {
                    'any_of': {
                        'param': [["investigating", "identified", "monitoring", "update", "resolved"]],
                        'error': _('Error! Status is invalid.')
                    }
                }
            },
            'notify_subscribers': {
                'value': request_data["notify_subscribers"],
                'validate': {
                    'any_of': {
                        'param': [["on", "off"]],
                        'error': _('Error! Notify subscribers is invalid.')
                    }
                }
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_errors_failure(self.__form.get_errors(), {}, self.__correlation_id))

        result = self.__incident_update.insert_one({
            "notify_subscribers": self.__form.get_sinput("notify_subscribers"),
            "datetime": DateTimeField().clean(self.__form.get_sinput("datetime")),
            "total_suscribers": self.__subscriber.count_by_status(SubscriberModule.VERIFIED),
            "message": self.__form.get_sinput("message"),
            "status": self.__form.get_sinput("status"),
            "incident_id": incident_id
        })

        if self.__form.get_sinput("status") == "resolved":
            self.__incident.update_one_by_id(incident_id, {
                "status": "closed"
            })
        else:
            self.__incident.update_one_by_id(incident_id, {
                "status": "open"
            })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Incident update created successfully.")
            }], {}, self.__correlation_id))
        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating update.")
            }], {}, self.__correlation_id))

    @allow_if_authenticated
    def get(self, request, incident_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__request.set_request(request)

        request_data = self.__request.get_request_data("get", {
            "offset": "",
            "limit": ""
        })

        try:
            offset = int(request_data["offset"])
            limit = int(request_data["limit"])
        except Exception:
            offset = 0
            limit = 0

        return JsonResponse(self.__response.send_private_success([], {
            'updates': self.__format_incident_updates(self.__incident_update.get_all(incident_id, offset, limit), incident_id),
            'metadata': {
                'offset': offset,
                'limit': limit,
                'count': self.__incident_update.count_all(incident_id)
            }
        }, self.__correlation_id))

    def __format_incident_updates(self, updates, incident_id):
        updates_list = []

        for update in updates:

            notified_subscribers = self.__incident_update_notification.count_by_update_status(
                update.id,
                IncidentUpdateNotificationModule.SUCCESS
            )
            progress = int(notified_subscribers/update.total_suscribers) * 100 if update.total_suscribers > 0 else 0

            updates_list.append({
                "id": update.id,
                "status": update.status.title(),
                "notify_subscribers": update.notify_subscribers.title(),
                "datetime": update.datetime.strftime("%b %d %Y %H:%M:%S"),
                "progress": progress if progress <= 100 else 100,
                "created_at": update.created_at.strftime("%b %d %Y %H:%M:%S"),
                "view_url": reverse("app.web.admin.incident_update.view", kwargs={'incident_id': incident_id, "update_id": update.id}),
                "edit_url": reverse("app.web.admin.incident_update.edit", kwargs={'incident_id': incident_id, "update_id": update.id}),
                "delete_url": reverse("app.api.private.v1.admin.incident_update.endpoint", kwargs={'incident_id': incident_id, "update_id": update.id})
            })

        return updates_list


class IncidentUpdate(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __incident_update = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__incident_update = IncidentUpdateModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def post(self, request, incident_id, update_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__request.set_request(request)

        request_data = self.__request.get_request_data("post", {
            "status": "",
            "notify_subscribers": "",
            "message": "",
            "datetime": "",
        })

        self.__form.add_inputs({
            'message': {
                'value': request_data["message"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'datetime': {
                'value': request_data["datetime"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'status': {
                'value': request_data["status"],
                'validate': {
                    'any_of': {
                        'param': [["investigating", "identified", "monitoring", "update", "resolved"]],
                        'error': _('Error! Status is invalid.')
                    }
                }
            },
            'notify_subscribers': {
                'value': request_data["notify_subscribers"],
                'validate': {
                    'any_of': {
                        'param': [["on", "off"]],
                        'error': _('Error! Notify subscribers is invalid.')
                    }
                }
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_errors_failure(self.__form.get_errors(), {}, self.__correlation_id))

        result = self.__incident_update.update_one_by_id(update_id, {
            "notify_subscribers": self.__form.get_sinput("notify_subscribers"),
            "datetime": DateTimeField().clean(self.__form.get_sinput("datetime")),
            "message": self.__form.get_sinput("message"),
            "status": self.__form.get_sinput("status")
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Incident update updated successfully.")
            }], {}, self.__correlation_id))
        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while updating update.")
            }], {}, self.__correlation_id))

    @allow_if_authenticated
    def delete(self, request, incident_id, update_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__user_id = request.user.id

        if self.__incident_update.delete_one_by_id(update_id):
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Incident update deleted successfully.")
            }], {}, self.__correlation_id))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while deleting incident update.")
            }], {}, self.__correlation_id))


class IncidentUpdatesNotify(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __incident_update = None
    __task = None
    __notification = None
    __subscriber = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__incident_update = IncidentUpdateModule()
        self.__task = Task_Module()
        self.__notification = NotificationModule()
        self.__subscriber = SubscriberModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def post(self, request, incident_id, update_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__user_id = request.user.id

        task = self.__task.delay("incident_update", {
            "incident_update_id": update_id,
            "user_id": self.__user_id
        }, self.__user_id)

        result = False

        if task:
            result = self.__notification.create_notification({
                "highlight": "Incident Update",
                "notification": "notifying subscribers with the incident update",
                "url": "#",
                "type": NotificationModule.PENDING,
                "delivered": False,
                "user_id": self.__user_id,
                "task_id": task.id
            })

        if task and result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Notification delivery started successfully.")
            }], {}, self.__correlation_id))
        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while starting delivery.")
            }], {}, self.__correlation_id))


class IncidentUpdatesComponents(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __incident_update = None
    __task = None
    __notification = None
    __subscriber = None
    __incident_update_component = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__incident_update = IncidentUpdateModule()
        self.__task = Task_Module()
        self.__notification = NotificationModule()
        self.__subscriber = SubscriberModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__incident_update_component = IncidentUpdateComponentModule()
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def post(self, request, incident_id, update_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__user_id = request.user.id
        self.__request.set_request(request)

        request_data = self.__request.get_request_data("post", {
            "type": "",
            "component_id": ""
        })

        self.__form.add_inputs({
            'component_id': {
                'value': request_data["component_id"],
                'validate': {
                    'sv_numeric': {
                        'error': _('Error! Component is required.')
                    }
                }
            },
            'type': {
                'value': request_data["type"],
                'validate': {
                    'any_of': {
                        'param': [["operational", "degraded_performance", "partial_outage", "major_outage", "maintenance"]],
                        'error': _('Error! Type is required.')
                    }
                }
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_errors_failure(self.__form.get_errors(), {}, self.__correlation_id))

        result = self.__incident_update_component.insert_one({
            "component_id": int(self.__form.get_sinput("component_id")),
            "type": self.__form.get_sinput("type"),
            "incident_update_id": int(update_id)
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Affected component created successfully.")
            }], {}, self.__correlation_id))
        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating affected component.")
            }], {}, self.__correlation_id))


class IncidentUpdatesComponent(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __incident_update_component = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__incident_update_component = IncidentUpdateComponentModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def delete(self, request, incident_id, update_id, item_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__user_id = request.user.id

        if self.__incident_update_component.delete_one_by_id(item_id):
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Affected component deleted successfully.")
            }], {}, self.__correlation_id))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while deleting affected component.")
            }], {}, self.__correlation_id))
