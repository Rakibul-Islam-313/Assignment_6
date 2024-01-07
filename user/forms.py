from django import forms
from . models import GENDER_TYPE, ACCOUNT_TYPE
from . models import UserBankAccount,UserAddress
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField( choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length = 100)

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name','email','password1','password2','account_type','birth_date','gender','postal_code','city','street_address','country']
    
    def save(self,commit=True):
        my_user = super().save(commit=False)
        if commit == True:
            my_user.save()
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')

            UserBankAccount.objects.create(
                user = my_user,
                account_type = account_type,
                gender = gender,
                birth_date = birth_date,
                account_no = 1000+my_user.id
            )

            UserAddress.objects.create(
                user = my_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address
            )
        return my_user
