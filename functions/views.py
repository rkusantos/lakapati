from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

from .forms import *
from .models import *

# Create your views here.
class InputFarmView(LoginRequiredMixin, CreateView):
    template_name = 'functions/input_farm.html'

    def get(self, request, *args, **kwargs):
        
        form = InputFarmForm()
        result = Farm.objects.filter(user=request.user)
        return render(request, self.template_name, {'form':form, 'result':result})
    
    def post(self, request, *args, **kwargs):
        form = InputFarmForm(request.POST or None)

        if form.is_valid():
            print('FORM IS VALID')
            self.farm_name = form.cleaned_data['farm_name']
            self.longitude = form.cleaned_data['longitude']
            self.latitude = form.cleaned_data['latitude']
            error_message = ''
            success_message=  ''
            
            try:

                insert_farm = Farm(user=request.user, 
                farm_name=self.farm_name, 
                longitude=self.longitude, 
                latitude=self.latitude)
                insert_farm.save()
                success_message = 'Data Successfully Inserted!'
            except Exception as e:
                error_message = 'Error Inserting Data'

            result = Farm.objects.filter(user=request.user)

        return render(request, self.template_name, {'form': form, 
        'error_message': error_message, 
        'success_message' : success_message,
        'result': result
        })


class CheckFarmView(LoginRequiredMixin, CreateView):
    template_name = 'functions/check_farm.html'

    def get(self, request, *args, **kwargs):
        
        form = CheckFarmForm(request=request)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = CheckFarmForm(request.POST or None, request=request)
        
        error_message = ''
        success_message=  ''

        if form.is_valid():
            print('FORM IS VALID')
            self.date = form.cleaned_data['date']
            self.farm = form.cleaned_data['farm']

            
            
            try:
                result = FarmDetails.objects.filter(user=request.user, 
                date=self.date, 
                farm_name=self.farm)
            except Exception as e:
                error_message = 'Error Inserting Data'

            print(result)

        return render(request, self.template_name, {'form': form, 
        'error_message': error_message, 
        'success_message' : success_message,
        'result': result
        })


class AnalysisView(LoginRequiredMixin, CreateView):
    template_name = 'functions/analysis.html'

    def get(self, request, *args, **kwargs):
        result = FarmDetails.objects.filter(user=request.user)
        return render(request, self.template_name, {'result':result})