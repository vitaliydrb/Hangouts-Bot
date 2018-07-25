import xml.etree.ElementTree as ET
import requests
import httplib2


def get_rss():
    req = httplib2.Http()
    (headers, content) = req.request('https://ctftime.org/event/list/upcoming/rss/', 'GET')
    if headers['status'] == '200':
        xml = parse_rss()


def parse_rss(content):
    content.replace('&lt;', '<')
    content.replace('&gt;','>')
    content.replace('&amp;','&')
    content.replace('mdash;','—')
    content.replace('ndash;','–')
    content.replace('&nbsp;',' ')
    return content

if __name__ == '__main__':
    get_rss()
