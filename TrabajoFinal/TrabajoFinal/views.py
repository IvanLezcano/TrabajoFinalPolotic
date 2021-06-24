import json
from json import encoder
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render





def Saludo(request):

    return HttpResponse([1,2,3,4,5])



def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento=""" <html><body> <h1> fecha y hora actuales %s </h1> </body> </html>""" %fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,anio):
    periodo=anio-2019
    edadFutura=edad+periodo
    documento=""" <html><body> <h1> en el año %s tendras %s años</h1> </body> </html>""" %(anio,edadFutura)
    return HttpResponse(documento)

def index(request):
    return render(request, 'index.html')




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




def productos(request):
    # data= [{
    #   "nombre": "lavadora",
    #   "url": "https://picsum.photos/210/302",
    # }, {
    #   "nombre": "tostadora",
    #   "url": "https://picsum.photos/210/302",
    # }, {
    #   "nombre": "Cocina",
    #   "url": "https://picsum.photos/210/302",
    # }]
    heladera = Producto("heladera","https://picsum.photos/210/305")
    tetera = Producto("tetera","https://picsum.photos/210/301")
    freezer = Producto("freezer","https://picsum.photos/210/302")
    lista = [heladera,tetera,freezer]
    encoder = ProductoEncoder() 
    data = list(map(lambda producto: producto.__dict__,lista))
    print(data)


    return HttpResponse(json.dumps(data))