from django.shortcuts import render


def faqList(request):
    template = "faq/faq.html"

    return render(request, template)
