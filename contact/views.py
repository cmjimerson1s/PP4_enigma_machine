from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUsForm
from django.views import View


# Collects the form and renders it to the user


def ContactUs(request):
    template = "contact/contact.html"
    form = ContactUsForm()

    context = {"form": form}

    return render(request, template, context)

# When the user submits via post the post function
# checks if the form is valid, and if it is the database
# is updated, if not it errors and redirects back to the form
# and alerts user of failure


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
