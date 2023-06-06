from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Final
# from django.views.generic import ListView, CreateView, UpdateView
# from django.urls import reverse_lazy
# from . forms import PersonForm

from django.template.context_processors import request


# Create your views here.
# class PersonListView(ListView):
#     model = Final
#
#     context_object_name = 'people'
#
# class PersonCreateView(CreateView):
#     model = Final
#     form_class = PersonForm
#     fields = ('name', 'dob', 'age', 'gender','phone','email','address','district','branch','account','materials')
#     success_url = reverse_lazy('person_changelist')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"new.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(username=username,password=password)
                print("user created")
                user.save()
                return render(request,"login.html")
        else:
            print("password mismatch")

    return render(request,"register.html")

def new(request):
    return render(request,"new.html")
def final(request):
        if request.method == "POST":
            name = request.POST.get('name', )
            date = request.POST.get('date', )
            age = request.POST.get('age', )
            phone = request.POST.get('phone', )
            gender = request.POST.get('gender', )
            email = request.POST.get('email', )
            address = request.POST.get('address', )
            district= request.POST.get('district', )
            account = request.POST.get('account', )
            materials = request.POST.get('materials', )

            final_form = Final(name=name, date=date, age=age,phone=phone,gender=gender,email=email,address=address,district=district,account=account,materials=materials)
            final_form.save()
            return render(request,"last.html")
        return render(request,"final.html")
def logout(request):
    auth.logout(request)
    return render(request,"home.html")
# def load_cities(request):
#     district_id = request.GET.get('district')
#     branches = Branch.objects.filter(district_id=district_id).order_by('name')
#     return render(request, 'hr/branch_dropdown_list_options.html', {'branches': branches})
#



