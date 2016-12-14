from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Bmi
from .forms import BmiForm
from .calculation import BmiCalculator

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import ColumnChart


def index(request):
    form = BmiForm()
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
                'bmi': int(round(bmi)), 'message':message[0], 
                'message1': message[1], 'color': message[2],
                'ok': message[3],})
    return render(request, 'bmi_calc/index.html', {'form': form})


def charts(request):
    data_bmi = []
    data_licznik = []
    data_all = [['bmi', 'Liczba uzyskanych wyników']]
    for object in Bmi.objects.values_list('bmi'):
        for i in object:
            data_bmi.append(float(i))
    for object in Bmi.objects.values_list('counter'):
        for i in object:
            data_licznik.append(float(i))
    dane = [list(i) for i in zip(data_bmi, data_licznik)]
    data_all = data_all + dane

    data_source = SimpleDataSource(data=data_all)
    chart = ColumnChart(data_source, options={'bar': {'groupWidth': '10%'},
                                              'vAxis': {'gridlines': {'count': 10}},
                                              'hAxis': {'title': 'BMI', 'gridlines': {'count': 5}},
                                              'vAxis': {'title': 'Licznik', 'gridlines': {'count': 5}}, 'title': "BMI"})
    context = {'chart': chart}
    return render(request, 'bmi_calc/charts.html', context)