__author__ = 'cesar'

''' Decided to use flask .. check project vmx-server-api '''

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor


class Test(Resource):
    isLeaf = True

    http = '<h1>loco!</h1>'

    def render_GET(self, request):

        print 'Got a HTTP GET'
        for header in request.requestHeaders.getAllRawHeaders():
            print header
        print request.content.getvalue()
        return "<html><body>{0}</body></html>".format(self.http)


factory = Site(resource=Test())
reactor.listenTCP(8081, factory)
reactor.run()