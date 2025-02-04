"""
Activities API Endpoint
"""

# Third Party Library
from django.views import View
from pyvalitron.form import Form
from django.http import JsonResponse

# Local Library
from app.modules.util.helpers import Helpers
from app.modules.core.request import Request
from app.modules.core.response import Response
from app.modules.validation.extension import ExtraRules
from app.modules.core.decorators import allow_if_authenticated
from app.modules.core.activity import Activity as ActivityModule


class Activities(View):

    __request = None
    __response = None
    __helpers = None
    __form = None
    __logger = None
    __user_id = None
    __activity = None
    __correlation_id = None

    def __init__(self):
        self.__request = Request()
        self.__response = Response()
        self.__helpers = Helpers()
        self.__form = Form()
        self.__activity = ActivityModule()
        self.__logger = self.__helpers.get_logger(__name__)
        self.__form.add_validator(ExtraRules())

    @allow_if_authenticated
    def get(self, request):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__user_id = request.user.id
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
            'activities': self.__format_activities(self.__activity.get(self.__user_id, offset, limit)),
            'metadata': {
                'offset': offset,
                'limit': limit,
                'count': self.__activity.count(self.__user_id)
            }
        }, self.__correlation_id))

    def __format_activities(self, activities):
        activities_list = []

        for activity in activities:
            activities_list.append({
                "id": activity.id,
                "activity": activity.activity,
                "created_at": activity.created_at.strftime("%b %d %Y %H:%M:%S")
            })

        return activities_list
