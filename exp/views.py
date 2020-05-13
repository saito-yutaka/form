from django.shortcuts import render, redirect
from user.models import Profile
from .forms import UseExpForm
from django.views.generic import TemplateView


def form1(request):

    A = Profile.objects.get(pk=1)
    B = Profile.objects.get(pk=2)
    A_exp = A.exp_total
    B_exp = B.exp_total

    if request.method == 'POST':
        form = UseExpForm(request.POST)
        if form.is_valid():
            use_exp = form.cleaned_data['use_exp']
            print(use_exp)
            A_exp -= use_exp
            B_exp += use_exp
            print(A_exp)
            print(B_exp)

    form = UseExpForm()
    return render(request, 'exp/form1.html', {'form': form, 'A_exp': A_exp, 'B_exp': B_exp})
