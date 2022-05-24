from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View

from .forms import PassengerForm

# Create your views here.


class ReserveCreateView(View):
    form_class = PassengerForm
    template_name = "passengers/reserve.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.save(commit=False)
            cd.reserver = request.user
            cd.fly_code = request.POST.get("fly_code")
            cd.save()
            messages.success(request, "", "success")
            return redirect()
        else:
            messages.error(request, "", "danger")
        return render(request, self.template_name, {"form": form})
