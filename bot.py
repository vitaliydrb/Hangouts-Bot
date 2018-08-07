#!/usr/local/bin/python3
from httplib2 import Http
from json import dumps, loads
from settings import hook, rss_list
from xml_parser import get_events_from_rss
from database import add_item, get_upcoming_events, is_unique
import time


def send_message(event):
    #This is message constructor.
    bot_message = {
    "cards": [
    {
        "header": {
            "title": "CTF bot for hangouts",
            "subtitle": "vim@underdefense.com",
            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSg0-dyErI37wFNzHw_V6mtPiVy07TS4a77Toh9rSqpR10KCWzr"
      },
        "sections": [
        {
            "widgets": [
                {
                    "keyValue": {
                        "topLabel": "Event name",
                        "content": "{}".format(event.name)
                    }
                },
                {
                    "keyValue": {
                        "topLabel": "Beggining date:",
                        "content": "{}".format(event.date)
                    }
                }
            ]
        },
        {
            "widgets": [
                {
                    "buttons": [
                    {
                        "textButton": {
                            "text": "Open website",
                            "onClick": {
                                "openLink": {
                                    "url": "{}".format(event.link)
                                }
                            }
                        }
                    }
                    ]
                }
            ]
        }
        ]
    }
    ]
}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=hook,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    if response[0]['status'] == "200":
        return loads(response[1])['thread']["name"]


def remind_about_event(thread):
    bot_message = {
        'text' : 'Reminder. This event will begin soon!',
    }
    bot_message['thread'] = {"name" : thread}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=hook,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    if response[0]['status'] == '200':
        return True


if __name__ == '__main__':
    while True:
        for link in rss_list:
            events = get_events_from_rss(link)
            for event in events:
                if is_unique(event.name):
                    thread = send_message(event)
                    if thread:
                        add_item(event, thread)
        for item in get_upcoming_events():
            if item.thread:
                remind_about_event(item.thread)
    #24 hours
        time.sleep(60*60*24)