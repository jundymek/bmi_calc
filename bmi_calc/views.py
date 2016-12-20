from ipware.ip import get_ip

from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Bmi
from .forms import BmiForm
from .calculation import BmiCalculator

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import ColumnChart


def index(request):
    form = BmiForm()
    ip = get_ip(request)
    print('Your ip adress is: ' + ip)
    g = GeoIP2()
    print(g.country(str(ip)))
    if request.method == 'POST':
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            wynik = BmiCalculator(height, weight)
            bmi = wynik.count_bmi()
            print(bmi)
            print(int(round(bmi)))
            message = wynik.bmi_message()
            # bmi = weight / ((height / 100)**2)
            try:
                bmi_object = Bmi.objects.get(bmi=int(round(bmi)))
                bmi_object.counter = int(bmi_object.counter) + 1
                bmi_object.save()
            except ObjectDoesNotExist:
                bmi_object = Bmi(bmi=int(round(bmi)))
                bmi_object.save()

            return render(request, 'bmi_calc/index.html', {'form': form,
                                                           'bmi': int(round(bmi)), 'message': message[0],
                                                           'message1': message[1], 'color': message[2],
                                                           'ok': message[3],
                                                           'ip': ip})
    return render(request, 'bmi_calc/index.html', {'form': form, 'ip': ip})


def charts(request):
    data_bmi = []
    data_licznik = []
    data_all = [['bmi', 'Liczba uzyskanych wyników']]
    for object in Bmi.objects.values_list('bmi'):
        for i in object:
            print(i)
            if i > 40:
                data_bmi.append(40)
            else:
                data_bmi.append(float(i))
    for object in Bmi.objects.values_list('counter'):
        for i in object:
            data_licznik.append(float(i))
    dane = [list(i) for i in zip(data_bmi, data_licznik)]
    data_all = data_all + dane

    data_source = SimpleDataSource(data=data_all)
    chart = ColumnChart(data_source, options={'bar': {'groupWidth': '10%'},
                                              'hAxis': {'title': 'BMI',
                                                        'gridlines': {'count': 15},
                                                        'ticks': [0, 10, 20, 30, {'v': 40,
                                                                                  'f': 'pow. 40'}],
                                                        'textStyle': {'color': '#01579b',
                                                                      'bold': 'True'},
                                                        'minValue': 41},
                                              'vAxis': {'title': 'Licznik',
                                                        'gridlines': {'count': 15}}, 'title': "BMI"})
    context = {'chart': chart}
    return render(request, 'bmi_calc/charts.html', context)
