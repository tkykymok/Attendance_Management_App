from django.shortcuts import render, redirect
from app.models import Date, CheckInOut
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from datetime import datetime, date, time, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecordForm, CreateUserForm, LoginForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from .decorators import unauthenticated_user, allowed_users, admin_only

@login_required
def index(request):
    if request.method == 'GET':
        s_date = datetime(2020, 1,1).date()
        staff = User.objects.get(username=request.user)
        
    #--初期データ作成--
        for d in range(120):
            md = s_date + timedelta(days=d)
            if CheckInOut.objects.filter(staff=staff, date_worked__masterdate=md).exists():
                pass
            else:
                ad = Date.objects.get(masterdate=md)
                add_record =  CheckInOut(staff=staff, date_worked=ad)
                add_record.save()
                
    #--残業時間（分）自動登録--
        for d2 in range(120):
            md = s_date + timedelta(days=d2)
            if CheckInOut.objects.filter(staff=staff, date_worked__masterdate=md, overtime_s__isnull=True, overtime_e__isnull=True).exists():
                pass  
            else:
                t_record = CheckInOut.objects.get(staff=staff, date_worked__masterdate=md)
                os = t_record.overtime_s
                oe = t_record.overtime_e
                over_time = abs(datetime.combine(s_date, os) - datetime.combine(s_date,oe)).seconds/60
                t_record.total_overtime = over_time
                t_record.save()
                
    #--出勤退勤処理--
    if request.method == 'POST':
        staff = User.objects.get(username=request.user)
        today = date.today()
        t_record = CheckInOut.objects.get(staff=staff, date_worked__masterdate=today)
        #--出勤処理 --
        if 'button_1' in request.POST:
            record_check =  CheckInOut.objects.filter(staff=staff, date_worked__masterdate=today, check_in__isnull=True)
            if record_check.exists(): #出勤未処理
                t_record.check_in = datetime.now().time()
                t_record.save()
                messages.success(request, '出勤　{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
                return redirect('/')
            else: #出勤済の場合
                pass
                 
        #--退勤処理 --
        elif 'button_2' in request.POST:
            record_check = CheckInOut.objects.filter(staff=staff, date_worked__masterdate=today, check_out__isnull=True)
            
            if record_check.exists(): #退勤未処理
                t_record.check_out = datetime.now().time()
                t_record.save()
                messages.success(request, '退勤　{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
                return redirect('/')
            else: #退勤済の場合
                pass
            
    return render(request, 'app/index.html')

    
@login_required
def recordList(request):  #検索機能
    date_s = request.GET.get('date_s')
    date_e = request.GET.get('date_e')
    if  date_s == "" and date_e == "" or date_s == "" or date_e == "" :
        messages.success(request, '日付を入力してください')
        return redirect ('record')
    else:
        record_list = CheckInOut.objects.filter(staff=request.user, date_worked__masterdate__range=[date_s, date_e])   
        context = {'record_list':record_list, 'date_s':date_s, 'date_e':date_e}
        return render (request, 'app/record_list.html', context )
    

def datelist(request):
    date_list = Date.objects.all()
    if request.method == 'POST':
        for d in range(366):
            s_date = datetime(2020, 1, 1).date()
            md = s_date + timedelta(days=d)
            if Date.objects.filter(masterdate=md).exists():
                pass
            else:
                add_date =  Date(masterdate=md)
                add_date.save()

@login_required
@allowed_users(allowed_roles=['admin'])
def records(request):
    staff_list = User.objects.all()
    staff = request.GET.get('staff')
    date_s = request.GET.get('date_s')
    date_e = request.GET.get('date_e')
    
    if  date_s == "" and date_e == "":
        records = CheckInOut.objects.filter(staff=staff)
        context = {'staff_list':staff_list, 'records':records}
        return render(request, 'app/admin_record_list.html', context)
     
    else:
        records = CheckInOut.objects.filter(staff=staff, date_worked__masterdate__range=[date_s, date_e])
        context = {'staff_list':staff_list, 'records':records}
        return render(request, 'app/admin_record_list.html', context)
    
@login_required
@allowed_users(allowed_roles=['admin'])
def datelist(request):
    date_list = Date.objects.all()
    if request.method == 'POST':
        for d in range(366):
            s_date = datetime(2020, 1, 1).date()
            md = s_date + timedelta(days=d)
            if Date.objects.filter(masterdate=md).exists():
                pass
            else:
                add_date =  Date(masterdate=md)
                add_date.save()
            
        
    return render(request, 'app/admin_date_list.html',{'date_list':date_list})

@login_required
@allowed_users(allowed_roles=['admin'])
def staffCreate(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)
           
            
            messages.success(request, '新規登録完了' + username)
            return redirect('/')
    
    
    context = {'form':form}
    return render(request, 'app/register.html', context)



class Login(LoginView):
    form_class = LoginForm
    template_name = 'register/login.html'
    redirect_authenticated_user = 'index'
    

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'register/login.html'


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = CheckInOut
    form_class = RecordForm
    success_url = '/'
    
class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = CheckInOut
    success_url = '/record'


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更ビュー"""
    success_url = reverse_lazy('password__change__done')
    template_name = 'app/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
        context["form_name"] = "password_change"
        return context

class PasswordChangeDone(LoginRequiredMixin,PasswordChangeDoneView):
    """パスワード変更完了"""
    template_name = 'app/password_change_done.html'