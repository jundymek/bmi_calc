from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Bmi
from .forms import BmiForm

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import ColumnChart


def index(request):
    form = BmiForm()
    if request.method == 'POST':
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            bmi = weight / ((height / 100)**2)
            try:
                bmi_object = Bmi.objects.get(bmi=int(bmi))
                bmi_object.counter = int(bmi_object.counter) + 1
                bmi_object.save()
            except ObjectDoesNotExist:
                bmi_object = Bmi(bmi=int(bmi))
                bmi_object.save()
            bmi_wynik = "Twoje BMI wynosi: " + str(int(bmi))

            return render(request, 'bmi_calc/index.html', {'form': form, 'bmi_wynik': bmi_wynik})
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
