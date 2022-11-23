import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Dht


# Create your views here.
def home(request) :
    return HttpResponse('Hello Everyone ! :)')


def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'tables.html', s)


class EditorChartView (TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = Dht.objects.all()
        return context


def exp_csv(request):
    obj = Dht.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'HUM'])
    studs = obj.values_list('id', 'temp', 'hum')
    for std in studs:
        writer.writerow(std)
    return response
