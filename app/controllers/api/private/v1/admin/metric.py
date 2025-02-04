"""
Metrics API Endpoint
"""

# Third Party Library
from django.views import View
from django.urls import reverse
from pyvalitron.form import Form
from django.http import JsonResponse
from django.utils.translation import gettext as _

# Local Library
from app.modules.util.helpers import Helpers
from app.modules.core.request import Request
from app.modules.core.response import Response
from app.modules.validation.extension import ExtraRules
from app.modules.core.metric import Metric as MetricModule
from app.modules.core.decorators import allow_if_authenticated


class Metrics(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __metric = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__metric = MetricModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def post(self, request):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__request.set_request(request)

        request_data = self.__request.get_request_data("post", {
            "title": "",
            "description": "",
            "source": "",
            "application": "",
            "metric": "",
            "x_axis": "",
            "y_axis": ""
        })

        self.__form.add_inputs({
            'title': {
                'value': request_data["title"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'description': {
                'value': request_data["description"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'source': {
                'value': request_data["source"],
                'validate': {
                    'any_of': {
                        'param': [["newrelic"]],
                        'error': _('Error! Source is invalid.')
                    }
                }
            },
            'application': {
                'value': request_data["application"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'metric': {
                'value': request_data["metric"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'x_axis': {
                'value': request_data["x_axis"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'y_axis': {
                'value': request_data["y_axis"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_errors_failure(self.__form.get_errors(), {}, self.__correlation_id))

        result = self.__metric.insert_one({
            "title": self.__form.get_sinput("title"),
            "description": self.__form.get_sinput("description"),
            "source": self.__form.get_sinput("source"),
            "x_axis": self.__form.get_sinput("x_axis"),
            "y_axis": self.__form.get_sinput("y_axis"),
            "data": '{"application":"%s", "metric":"%s"}' % (
                self.__form.get_sinput("application"),
                self.__form.get_sinput("metric")
            )
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Metric created successfully.")
            }], {}, self.__correlation_id))
        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while creating metric.")
            }], {}, self.__correlation_id))

    @allow_if_authenticated
    def get(self, request):

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
            'metrics': self.__format_metrics(self.__metric.get_all(offset, limit)),
            'metadata': {
                'offset': offset,
                'limit': limit,
                'count': self.__metric.count_all()
            }
        }, self.__correlation_id))

    def __format_metrics(self, metrics):
        metrics_list = []

        for metric in metrics:
            metrics_list.append({
                "id": metric.id,
                "title": metric.title,
                "source": metric.source.title(),
                "created_at": metric.created_at.strftime("%b %d %Y %H:%M:%S"),
                "edit_url": reverse("app.web.admin.metric.edit", kwargs={'metric_id': metric.id}),
                "delete_url": reverse("app.api.private.v1.admin.metric.endpoint", kwargs={'metric_id': metric.id})
            })

        return metrics_list


class Metric(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __metric = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__metric = MetricModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def post(self, request, metric_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__request.set_request(request)

        request_data = self.__request.get_request_data("post", {
            "title": "",
            "description": "",
            "source": "",
            "application": "",
            "metric": "",
            "x_axis": "",
            "y_axis": ""
        })

        self.__form.add_inputs({
            'title': {
                'value': request_data["title"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'description': {
                'value': request_data["description"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'source': {
                'value': request_data["source"],
                'validate': {
                    'any_of': {
                        'param': [["newrelic"]],
                        'error': _('Error! Source is invalid.')
                    }
                }
            },
            'application': {
                'value': request_data["application"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'metric': {
                'value': request_data["metric"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'x_axis': {
                'value': request_data["x_axis"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            },
            'y_axis': {
                'value': request_data["y_axis"],
                'sanitize': {
                    'strip': {}
                },
                'validate': {}
            }
        })

        self.__form.process()

        if not self.__form.is_passed():
            return JsonResponse(self.__response.send_errors_failure(self.__form.get_errors(), {}, self.__correlation_id))

        result = self.__metric.update_one_by_id(metric_id, {
            "title": self.__form.get_sinput("title"),
            "description": self.__form.get_sinput("description"),
            "source": self.__form.get_sinput("source"),
            "x_axis": self.__form.get_sinput("x_axis"),
            "y_axis": self.__form.get_sinput("y_axis"),
            "data": '{"application":"%s", "metric":"%s"}' % (
                self.__form.get_sinput("application"),
                self.__form.get_sinput("metric")
            )
        })

        if result:
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Metric updated successfully.")
            }], {}, self.__correlation_id))
        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while updating metric.")
            }], {}, self.__correlation_id))

    @allow_if_authenticated
    def delete(self, request, metric_id):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__user_id = request.user.id

        if self.__metric.delete_one_by_id(metric_id):
            return JsonResponse(self.__response.send_private_success([{
                "type": "success",
                "message": _("Metric deleted successfully.")
            }], {}, self.__correlation_id))

        else:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Something goes wrong while deleting metric.")
            }], {}, self.__correlation_id))


class NewRelicApps(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __metric = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__metric = MetricModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def get(self, request):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""

        result = False
        try:
            result = self.__metric.get_new_relic_apps()
        except Exception as e:
            self.__logger.error(_("Error while listing newrelic applications: %(error)s {'correlationId':'%(correlationId)s'}") % {
                "error": str(e),
                "correlationId": self.__correlation_id
            })

        if result is False:
            return JsonResponse(self.__response.send_private_failure([{
                "type": "error",
                "message": _("Error! Connecting to New Relic.")
            }], {}, self.__correlation_id))

        return JsonResponse(self.__response.send_private_success([], {
            'apps': result
        }, self.__correlation_id))
