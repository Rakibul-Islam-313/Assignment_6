from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import DepositForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template,{
        'user': user, 
        'amount': amount
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

@method_decorator(login_required, name='dispatch')
class DepositFormView(FormView):
    template_name = 'deposit.html'
    form_class = DepositForm

    def get(self,request,*args, **kwargs):
        deposit_form = self.form_class()
        return render(request, self.template_name, {'form':deposit_form})
    
    def post(self,request,*args, **kwargs):
        deposit_form = self.form_class(request.POST)
        if deposit_form.is_valid():
            amount = deposit_form.cleaned_data.get('amount')
            account = self.request.user.account
            account.balance += amount
            account.save(update_fields=['balance'])

            messages.success(
                request,
                f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
            )

            send_transaction_email(self.request.user,amount,"Money Deposit Messages",'deposit_mail.html')

            return redirect('home_page')
        return render(request, self.template_name, {'form':deposit_form})
    