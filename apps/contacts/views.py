from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    context = {'contacts': contacts}
    return render(request, 'contacts/index.html', context)


@login_required(login_url='login')
def add_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('contact_list')
    context = {'form': form}
    return render(request, 'contacts/add.html', context)


@login_required(login_url='login')
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('contact_list')
