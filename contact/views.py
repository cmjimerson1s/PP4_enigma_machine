from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUsForm
from django.views import View


# Create your views here.
def ContactUs(request):
    template = "contact/contact.html"
    form = ContactUsForm()

    context = {"form": form}

    return render(request, template, context)


class ContactUsPost(View):
    def get(self, request):
        template = "contact/contact.html"
        form = ContactUsForm()

        context = {"form": form}

        return render(request, template, context)

    def post(self, request):
        new_form = ContactUsForm()
        contact_form = ContactUsForm(data=request.POST)
        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            form.save()
            messages.success(request, "Message has been sent")
            return render(request, "contact/contact.html", {"form": new_form})
        else:
            new_form = ContactUsForm()
            messages.error(request, "Error: Please try again")
            return render(request, "contact/contact.html", {"form": new_form})
