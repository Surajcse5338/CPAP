#!/usr/bin/env python2

import urllib2

LOGIN = 'schedutron'
PASSWD = 'somerandomstuff'
URL = 'http://localhost'
REALM = 'Secure Archive'

def handler_version(url):
    from urlparse import urlparse
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urlparse(url)[1], LOGIN, PASSWD)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url


def request_version(url):
    from base64 import encodestring
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
    req.add_header("Authorization", "Basic %s" % b64str)
    return req


for func_type in ('handler', 'request'):
    print "*** Using %s:" % func_type.upper()
    url = eval("%s_version" % func_type)(URL)
    f = urllib2.urlopen(url)
    print f.readline()
    f.close()
