"""
Status Page Module
"""

# local Django
from app.modules.util.helpers import Helpers


class Status_Page():

    __helpers = None
    __logger = None

    def __init__(self):
        self.__helpers = Helpers()
        self.__logger = self.__helpers.get_logger(__name__)

    def get_system_status(self):
        return "operational"

    def get_about_site(self):
        return ""

    def get_incident_by_uri(self, uri):
        return {
            "headline": "Facebook Integration Issue",
            "headline_class": "text-danger",
            "sub_headline": "Incident Report for Silverback",
            "affected_components": ", ".join(["Cloud API", "Bmp API"]),
            "updates": [
                {
                    "type": "Resolved",
                    "body": "we began to see interruptions to Facebook integrations",
                    "date": "Feb 01, 2019 - 22:43 UTC"
                }
            ]
        }

    def get_incidents_for_period(self, period):
        return {
            "period": "May 2019 - July 2019",
            "incidents": [
                {
                    "date": "March 2019",
                    "incidents": [
                        {
                            "uri": "123",
                            "subject": "Partial network outage at one of our network suppliers",
                            "class": "text-danger",
                            "final_update": "This incident has been resolved.",
                            "period": "March 7, 08:56 CET - March 8, 2:56 CET"
                        },
                        {
                            "uri": "123",
                            "subject": "Partial network outage at one of our network suppliers",
                            "class": "text-danger",
                            "final_update": "This incident has been resolved.",
                            "period": "March 7, 08:56 CET - March 8, 2:56 CET"
                        },
                    ]
                },
                {
                    "date": "February 2019",
                    "incidents": []
                },
                {
                    "date": "January 2019",
                    "incidents": []
                }
            ]
        }

    def get_past_incidents(self, days):
        return [
            {
                "date": "March 8, 2019",
                "incidents": [
                    {
                        "uri": "123",
                        "subject": "Partial network outage at one of our network suppliers",
                        "class": "text-danger",
                        "updates": [
                            {
                                "type": "Resolved",
                                "date": "March 7, 08:56 CET",
                                "body": "we had a partial network outage at one of our network suppliers."
                            },
                            {
                                "type": "Update",
                                "date": "March 7, 08:56 CET",
                                "body": "we had a partial network outage at one of our network suppliers."
                            },
                        ]
                    },
                    {
                        "uri": "123",
                        "subject": "Partial network outage at one of our network suppliers",
                        "class": "text-danger",
                        "updates": [
                            {
                                "type": "Resolved",
                                "date": "March 7, 08:56 CET",
                                "body": "we had a partial network outage at one of our network suppliers."
                            },
                            {
                                "type": "Update",
                                "date": "March 7, 08:56 CET",
                                "body": "we had a partial network outage at one of our network suppliers."
                            },
                        ]
                    },
                ]
            },
            {
                "date": "March 7, 2019",
                "incidents": []
            },
            {
                "date": "March 6, 2019",
                "incidents": []
            },
            {
                "date": "March 5, 2019",
                "incidents": []
            },
            {
                "date": "March 4, 2019",
                "incidents": []
            },
            {
                "date": "March 3, 2019",
                "incidents": [
                    {
                        "uri": "123",
                        "subject": "Partial network outage at one of our network suppliers",
                        "class": "text-danger",
                        "updates": [
                            {
                                "type": "Resolved",
                                "date": "March 7, 08:56 CET",
                                "body": "we had a partial network outage at one of our network suppliers."
                            },
                            {
                                "type": "Update",
                                "date": "March 7, 08:56 CET",
                                "body": "we had a partial network outage at one of our network suppliers."
                            },
                        ]
                    }
                ]
            }
        ]

    def get_system_metrics(self):
        return [
            {
                "id": "container",
                "title": "Website Dashboard - Average response time",
                "xtitle": "Date",
                "ytitle": "Time (m)",
                "day_data": [
                    {"timestamp": 1554858060000, "value": 0.70},
                    {"timestamp": 1554858120000, "value": 0.80},
                    {"timestamp": 1554858180000, "value": 0.90},
                    {"timestamp": 1554858240000, "value": 0.95}
                ],
                "week_data": [
                    {"timestamp": 1554858060000, "value": 0.75},
                    {"timestamp": 1554858120000, "value": 0.85},
                    {"timestamp": 1554858180000, "value": 0.95},
                    {"timestamp": 1554858240000, "value": 0.98}
                ],
                "month_data": [
                    {"timestamp": 1554858060000, "value": 0.95},
                    {"timestamp": 1554858120000, "value": 0.76},
                    {"timestamp": 1554858180000, "value": 0.43},
                    {"timestamp": 1554858240000, "value": 0.78}
                ],
            }
        ]

    def get_services(self):
        return [
            {
                "name": "SMS & MMS REST API (HTTPS)",
                "description": "Email and In app Messages",
                "current_status": "Operational",
                "current_status_class": "bg-green",
                "uptime_chart": [],
                "sub_services": []
            },
            {
                "name": "SMS & MMS REST API (HTTPS)",
                "description": "Email and In app Messages",
                "current_status": "Operational",
                "current_status_class": "bg-warning",
                "uptime_chart": [
                    {
                        "x": 0,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#ffad62",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 5,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#ffad62",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 10,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 15,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 20,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 25,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 30,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 35,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 40,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 45,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 50,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 55,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 60,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 65,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 70,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 75,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 80,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 85,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 90,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 95,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 100,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 105,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 110,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 115,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 120,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 125,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 130,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 135,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 140,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 145,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 150,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 155,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 160,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 165,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 170,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 175,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 180,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 185,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 190,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 195,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 200,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 205,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 210,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 215,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 220,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 225,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 230,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 235,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 240,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 245,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 250,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 255,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 260,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 265,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 270,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 275,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 280,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 285,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 290,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 295,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 300,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 305,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 310,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 315,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 320,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 325,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 330,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 335,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 340,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 345,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 350,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 355,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 360,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 365,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 370,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 375,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 380,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 385,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 390,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 395,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 400,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 405,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 410,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 415,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 420,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 425,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 430,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 435,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 440,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    },
                    {
                        "x": 445,
                        "y": 0,
                        "height": "34",
                        "width": "3",
                        "fill": "#00eb8b",
                        "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                    }
                ],
                "sub_services": [
                    {
                        "name": "SMS & MMS REST API (HTTPS)",
                        "description": "Email and In app Messages",
                        "current_status": "Operational",
                        "current_status_class": "bg-red",
                        "uptime_chart": [
                            {
                                "x": 0,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#ffad62",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 5,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#ffad62",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 10,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 15,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 20,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 25,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 30,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 35,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 40,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 45,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 50,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 55,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 60,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 65,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 70,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 75,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 80,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 85,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 90,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 95,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 100,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 105,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 110,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 115,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 120,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 125,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 130,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 135,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 140,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 145,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 150,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 155,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 160,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 165,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 170,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 175,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 180,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 185,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 190,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 195,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 200,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 205,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 210,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 215,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 220,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 225,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 230,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 235,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 240,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 245,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 250,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 255,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 260,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 265,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 270,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 275,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 280,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 285,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 290,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 295,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 300,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 305,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 310,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 315,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 320,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 325,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 330,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 335,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 340,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 345,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 350,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 355,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 360,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 365,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 370,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 375,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 380,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 385,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 390,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 395,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 400,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 405,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 410,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 415,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 420,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 425,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 430,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 435,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 440,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            },
                            {
                                "x": 445,
                                "y": 0,
                                "height": "34",
                                "width": "3",
                                "fill": "#00eb8b",
                                "content": "<strong>29 Dec 2018</strong><br/>No downtime recorded on this day."
                            }

                        ]
                    }
                ]
            }
        ]
