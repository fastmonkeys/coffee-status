from __future__ import print_function
from urllib2 import urlopen
import json
import datetime

response = urlopen('http://192.168.179.80:8080/api').read()
data = json.loads(response.decode('utf-8'))


# Coffee amount
cups = data['current'] / 10
brewed_at_datetime = datetime.datetime.strptime(data['brewed_at'], '%Y-%m-%d %H:%M:%S.%f')
brewed_at = brewed_at_datetime.strftime('%H:%M')
ago = int((datetime.datetime.now() - brewed_at_datetime).total_seconds()/60)
if cups > 0:
    print('%sX:coffee:%smin' % (cups, ago))
else:
    print(':x:%smin' % ago)


# Notify when new pan
filename = '/tmp/coffee_watch_already_notified_brews_list.txt'

f = open(filename, 'a+')
f.close()
f = open(filename, 'r')
notified_brews = [line.strip() for line in f.readlines()]
f.close()

try:
    from pync import Notifier
    if data['brewed_at'] not in notified_brews and brewed_at_datetime > datetime.datetime.now() - datetime.timedelta(hours=3):
        f = open(filename, 'a')
        f.write('{}\n'.format(data['brewed_at']))
        f.close()
        Notifier.notify('New pan of coffee was brewed at {}'.format(brewed_at), title='New coffee')
except ImportError:
    print('---')
    print('Install pync to get notifications of new brews')

