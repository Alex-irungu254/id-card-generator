from django.shortcuts import get_object_or_404, redirect, render
from .forms import IDCardForm
from .models import IDCard
from .utils import generate_id_card
import qrcode

def create_card(request):
    if request.method == 'POST':
        form = IDCardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save()
            generate_id_card(card)
            return redirect('card-detail', pk=card.pk)
    else:
        form = IDCardForm()
    return render(request, 'form.html', {'form': form, 'title': 'Create ID Card'})


def edit_card(request, pk):
    card = get_object_or_404(IDCard, pk=pk)
    if request.method == 'POST':
        form = IDCardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            card = form.save()
            generate_id_card(card)
            return redirect('card-detail', pk=card.pk)
    else:
        form = IDCardForm(instance=card)
    return render(request, 'form.html', {'form': form, 'title': 'Edit ID Card', 'card': card})


def card_detail(request, pk):
    card = get_object_or_404(IDCard, pk=pk)
    return render(request, 'card_detail.html', {'card': card})


def verify_card(request, code):
    card = get_object_or_404(IDCard, verification_code=code)
    return render(request, 'verify.html', {'card': card})

def generate_qr(code):
    url = f"http://yourdomain.com/verify/{code}"
    qr = qrcode.make(url)
    qr.save("qr.png")