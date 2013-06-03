import cherrypy
from pypi_redirect.handler._exception import HandlerException


class Root(object):
    def __init__(
            self,
            handlers,
            invalid_path_handler):
        self.handlers = handlers
        self.invalid_path_handler = invalid_path_handler

    @cherrypy.expose
    def default(self, *path):
        try:
            return self.handlers[len(path)].handle(
                path=path,
                request=cherrypy.request,
                response=cherrypy.response)

        except IndexError:
            return self.invalid_path_handler.handle(
                path=path,
                request=cherrypy.request,
                response=cherrypy.response)

        except HandlerException as e:
            e.raise_wrapped()
