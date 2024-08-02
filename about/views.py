from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactQueryForm


def about(request):
    if request.method == 'POST':
        form = ContactQueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success
            (request, 'Your query has been submitted successfully.')
            return redirect('confirmation')
    else:
        form = ContactQueryForm()
    return render(request, 'about/about.html', {'form': form})


def confirmation(request):
    return render(request, 'about/confirmation.html')
