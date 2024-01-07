from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,DetailView
from user.models import UserBankAccount
from . import forms 
from . models import Borrow,Books
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# Create your views here.

# def send_transaction_email(user, amount, subject, template):
#     message = render_to_string(template,{
#         'user': user, 
#         'amount': amount
#     })
#     send_email = EmailMultiAlternatives(subject, '', to=[user.email])
#     send_email.attach_alternative(message, "text/html")
#     send_email.send()

class Book_post(CreateView):
    model = Books
    form_class = forms.BookForm
    template_name = 'home.html'
    success_url = reverse_lazy('home.html')
    def form_valid(self, form):
        return super().form_valid(form)
    
class BookDetailsPost(DetailView):
    model = Books
    template_name = 'book_details.html'
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
            comment_form = forms.CommentForm(data=self.request.POST)
            post = self.get_object()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post 
                new_comment.save()
            return self.get(self, *args, **kwargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context 
    
def BorrowBook(request,id):
    book = get_object_or_404(Books, pk=id)
    user_profile, created = UserBankAccount.objects.get_or_create(user=request.user)

    if book.quantity > 0:
            if user_profile.balance > 100:
                borrow = Borrow.objects.create(user=request.user, book=book)
                borrow.save()

                book.quantity -= 1
                book.save()

                user_account = user_profile[0] if created else user_profile

                user_account.balance -= book.price
                user_account.save()

                messages.success(request, 'You borrow book Successfully')
                return redirect('profile_page')
            else:
                messages.error(request, 'Insufficient balance to borrow this book')
                return redirect('deposit_page')
    else:
            messages.success(request, 'This book out of stock')
            return redirect('home_page')
    return render(request,'profile.html',{'book':book})

def ReturnBook(request, id):
    borrow = get_object_or_404(Borrow, pk=id)
    book = borrow.book
    user_profile = UserBankAccount.objects.get_or_create(user=request.user)[0]
    if borrow.user == request.user:
        borrow.delete() 

        book.quantity += 1
        book.save()

        user_profile.balance += book.price 
        user_profile.save()

        messages.success(request, 'You returned the book successfully')
    else:
        messages.error(request, 'You are not authorized to return this book')

    return redirect('profile_page')