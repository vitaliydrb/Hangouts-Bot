import xml.etree.ElementTree as ET
import httplib2
from ctf import CTF


#This function getting rss from list in settings.py
def get_events_from_rss(link):
    req = httplib2.Http()
    (headers, content) = req.request('{}'.format(link), 'GET')
    if headers['status'] == '200':
        xml = parse_rss(content)
        root = ET.fromstring(xml)
        return get_ctf_list(root)


#This function removes unreadable html symbols
def parse_rss(content):
    content.replace('&lt;', '<')
    content.replace('&gt;','>')
    content.replace('&amp;','&')
    content.replace('mdash;','-')
    content.replace('ndash;','-')
    content.replace('&nbsp;',' ')
    return content



def get_ctf_list(xml):
    events=[]
    for item in xml[0].findall('item'):
        title = item.find('title').text
        link = item.find('url').text
        beggining = item.find('start_date').text
        event = CTF(title, link, beggining)
        if event.get_eta():
            events.append(event)
    return events