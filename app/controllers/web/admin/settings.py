"""
Settings Web Controller
"""

# Standard Library
import os

# Third Party Library
from django.views import View
from django.shortcuts import render
from django.utils.translation import gettext as _

# Local Library
from app.modules.core.acl import ACL
from app.modules.core.upgrade import Upgrade
from app.modules.core.context import Context
from app.modules.core.decorators import login_if_not_authenticated_or_no_permission


class Settings(View):

    template_name = 'templates/admin/settings.html'
    __context = Context()
    __upgrade = Upgrade()
    __acl = ACL()
    __correlation_id = None

    @login_if_not_authenticated_or_no_permission("manage_settings")
    def get(self, request):

        self.__correlation_id = request.META["X-Correlation-ID"] if "X-Correlation-ID" in request.META else ""
        self.__context.autoload_options()
        self.__context.autoload_user(request.user.id if request.user.is_authenticated else None)
        self.__context.load_options({
            "app_name": "",
            "app_email": "",
            "app_url": "",
            "app_description": "",
            "google_analytics_account": "",
            "reset_mails_messages_count": "",
            "reset_mails_expire_after": "",
            "access_tokens_expire_after": "",
            "prometheus_token": "",
            "newrelic_api_key": ""
        })

        self.__context.push({
            "current": self.__upgrade.get_current_version(),
            "latest": self.__upgrade.get_latest_version()
        })

        self.__context.push({
            "page_title": _("Settings · %s") % self.__context.get("app_name", os.getenv("APP_NAME", "Silverback"))
        })

        return render(request, self.template_name, self.__context.get())
