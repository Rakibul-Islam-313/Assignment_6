from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import SignupForm
from django.contrib import messages

from Books.models import Books,Borrow 
from user.models import UserBankAccount
from book_category.models import Categories
# Create your views here.

class SignUpFormView(CreateView):
    template_name = 'signup_form.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Sign up successfully')
            return redirect('login_page')
        else:
            return render(request,self.template_name,{'form':form})
    

class LoginFormView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get(self, request):
        login_form = self.form_class()
        return render(request,self.template_name,{'form':login_form})
    
    def post(self,request):
        login_form = self.form_class(request, data=request.POST)
        if login_form.is_valid():
            self.form_valid(login_form)
            messages.success(request,'Login successfully')
            return redirect('home_page')
        else:
            messages.warning(request,'login information invalid')
            return render(request,self.template_name,{'form':login_form})   


class LogoutFormView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home_page')
    

def ProfileView(request,category_slug = None):
    data = Books.objects.all()
    book_category = Categories.objects.all()
    borrow = Borrow.objects.all()

    if category_slug is not None:
        user_id = request.user.id
        category = Categories.objects.get(slug = category_slug)
        data = Books.objects.filter(categories = category)
        borrow = Borrow.objects.filter(id = user_id)

    return render(request, 'profile.html', {'data': data,'borrow': borrow, 'book_category': book_category})