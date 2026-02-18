from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm


class ContactView(FormView):
    template_name = "contact/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact:contact_success")

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = "contact/contact_success.html"
