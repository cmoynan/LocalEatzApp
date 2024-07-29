from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactQueryForm

# Create your views here.

def about(request):
    if request.method == 'POST':
        form = ContactQueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your query has been submitted successfully.')
            return redirect('about')
    else:
        form = ContactQueryForm()
    return render(request, 'about/about.html', {'form': form})
