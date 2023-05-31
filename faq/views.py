from django.shortcuts import render
from .models import Faq


def FaqList(request):
    template = "faq/faq.html"
    queryset = Faq.objects.all()

    return render(request, template, {'faq': queryset})
