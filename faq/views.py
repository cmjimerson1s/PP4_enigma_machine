from django.shortcuts import render
from .models import Faq

# Collects all of the Faq items from the database
# to render to the template


def FaqList(request):
    template = "faq/faq.html"
    queryset = Faq.objects.all()

    return render(request, template, {'faq': queryset})
