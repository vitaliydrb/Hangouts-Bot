from httplib2 import Http
from json import dumps
from settings import hook, link
from xml_parser import get_events_from_rss


def send_message(event):
    #This is message constructor.
    bot_message = {
  "cards": [
    {
      "header": {
        "title": "CTF bot for hangours",
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
        return True

if __name__ == '__main__':
    #This will parse events from rss list.
    events = get_events_from_rss(link)
    for event in events:
        send_message(event)