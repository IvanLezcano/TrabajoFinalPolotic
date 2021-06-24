import json

class Producto:
    def __init__(self,nombre,url):
        self.nombre = nombre
        self.url = url

class ProductoEncoder(json.JSONEncoder):
   def default(self, object):

        if isinstance(object, Producto):

            return object.__dict__

        else:


            return json.JSONEncoder.default(self, object)

