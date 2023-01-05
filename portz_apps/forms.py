from django.forms import ModelForm
from django import forms
from .models import *


class LokasiForm(ModelForm):
    class Meta:
        model=Lokasi
        fields='__all__'

        widgets={
            'nama': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Pelabuhan'}),
            'alamat': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Alamat Pelabuhan'}),
            'wpp': forms.TextInput(attrs={'class':'form-control', 'placeholder':'WPP Pelabuhan'}),
            'provinsi': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Provinsi Pelabuhan'}),
            'golongan': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Golongan Pelabuhan'})
        }

class LocationForm(ModelForm):
    class Meta:
        model=Location
        fields='__all__'

        # widgets={
        #     'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Lokasi'}),
        #     'desc': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi Lokasi'}),
        #     'prov': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Provinsi'}),
        #     'pict': forms.URLField(attrs={'class':'form-control'}),
        # }