from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import Frm_login, FormCompany
from .models import Company


def Vw_login(request):     # login
    form_data = request.POST
    form = Frm_login(form_data)
    if form.is_valid():

        try:
            user_obj = User.objects.get(username=request.POST["username"])
        except User.DoesNotExist:
            user_obj =None
        if user_obj != None:
            user = form.login(request)
            if user_obj.is_active == True:
                if user:
                    # login(user=user)
                    login(request, user)
                    return redirect('http://grafana.monitoring.bfsgodirect.com:3000/login ')
                else:
                    messages.success(request, "Enter Valid User Name and Password.")
                    return render(request, 'login.html', {'form': form})
            else:
                messages.success(request,"This user is blocked, Please contact to admin.")
                return render(request, 'login.html', {'form': form})
        else:
            messages.success(request, "Enter Valid User Name and Password.")
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})


@login_required
def switch_comapny(request):
    form = FormCompany()
    if request.POST:
        company = request.POST['company']
        obj = Company.objects.get(pk=company)
        request.session['login_company'] = obj.name
        return redirect('sre:project_dashboard')
    else:
        return render(request, 'dashboard.html', {'form': form})


@login_required
def project_dashbaord(request):
    form = FormCompany()
    login_company = request.session.get('login_company', '')
    return render(request, 'project_dashboard.html', {'form': form, 'login_company': login_company})