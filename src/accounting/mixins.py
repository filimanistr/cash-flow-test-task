from django.urls import reverse_lazy
from .models import Transaction
from . import forms


class TransactionModelSuccessMixin:
    """Specifies `model` and `success_url`"""
    model = Transaction
    success_url = reverse_lazy('index')


class ReferenceSuccessMixin:
    """Specifies `success_url`"""
    success_url = reverse_lazy('references')


class TemplateContextMixin:
    """
    Specifies `template_name` for any model's creation and update,
    adds model's `verbose_name` to context
    """
    template_name = 'accounting/details.html'
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['verbose_name_pos'] = self.model.verbose_name_pos()
        return context

    def form_valid(self, form):
        # there are two submit buttons in one form
        # submit only if `final` button was pressed
        if 'final_submit' in self.request.POST:
            return super().form_valid(form)
        return self.form_invalid(form)


class TransactionTemplateContextFormMixin(TemplateContextMixin):
    """
    Specifies `template_name` and `form_class`
    for `Template` creation and update,
    adds model's `verbose_name` to context
    """
    form_class = forms.TransactionForm
    fields = None  # can't set fields and form_class at the same time
