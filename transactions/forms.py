from django import forms 
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount< min_deposit_amount:
            raise forms.ValidationError(
                f"You need to deposit at least {min_deposit_amount}" 
            )
        return amount 