from django import forms 
from .models import Books,Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Books 
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']