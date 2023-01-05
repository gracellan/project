from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic.base import TemplateView

class Locations(TemplateView):
    template_name = 'locations.html'

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(*args, **kwargs)
        context['locations'] = Location.objects.all()
        return context 

def add_loc(request, *args, **kwargs):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    form=LocationForm()
    context={
        'form':form,
    }
    return render(request, 'add.html', context)


@login_required(login_url='login')
def HomePage(request):
    
    data=Lokasi.objects.all()
    data1=Location.objects.all()

    form=LokasiForm()
    form1=LocationForm()
    if request.method=='POST':
        form=LokasiForm(request.POST)
        form=LocationForm(request.POST)
        form.save()
        form=LokasiForm()
        form=LocationForm()

    context={
        'form':form,
        'data':data,
        'data1':data,
        'form1':form,
    }
    
    return render (request, 'home.html', context)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('Password Tidak Cocok')
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        # print(uname,email,pass1,pass2)

    return render (request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username atau Password salah")

    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def UpdatePage(request):
    data=Lokasi.objects.all()

    form=LokasiForm()
    if request.method=='POST':
        form=LokasiForm(request.POST)
        form.save()
        form=LokasiForm()
        return redirect('home')

    context={
        'form':form,
        'data':data,
        'pesan': 'Data berhasil ditambahkan',
    }
    return render (request, 'update.html', context)

# Delete 
def Delete_record(request,id):
    a=Lokasi.objects.get(pk=id)
    a.delete()
    return redirect('home')

# Edit
def Edit_Record(request,id):
    data=Lokasi.objects.get(pk=id)
    if request.method=='POST':
       form=LokasiForm(request.POST,instance=data)
       if form.is_valid():
        form.save()
        return redirect('home')
    else:
        data=Lokasi.objects.get(pk=id)
        form=LokasiForm(instance=data)
        template= 'edit.html'
    context={
        'form':form,
        'data': data,
    }
    return render(request, template, context)
    

# def Edit_Record(request, id):
#     data = Lokasi.objects.get(pk=id)

#     if request.POST:
#         form = LokasiForm(request.POST)
#         if form.is_valid():
#             form.save()
#             pesan = 'Data berhasil diupdate'
#             context={
#                 'pesan': pesan,
#                 'form': form,
#                 'data': data,
#             }
#             return render(request, 'edit.html', context)
#     else: 
#         form = LokasiForm()
#         context={
#             'form': form,
#         }

#     return render(request, 'edit.html', context)




