from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from . import models, selectors
from .mixins import TransactionModelSuccessMixin, ReferenceSuccessMixin, \
                    TemplateContextMixin, TransactionTemplateContextFormMixin


class IndexView(ListView):
    """Главная страница"""
    model = models.Transaction

    def get_queryset(self):
        """Filters transactions based on URL parameters"""
        return selectors.list_transactions(self.request)

    def get_context_data(self, **kwargs):
        """Adds select options for filters to context"""
        context = super().get_context_data(**kwargs)
        return selectors.list_filters_options(context)


class ReferencesView(ListView):
    """
    Страница управления справочниками
    статусы, типы, категории, подкатегории
    """
    model = models.Status
    context_object_name = 'status'
    template_name = 'accounting/references.html'

    def get_context_data(self, **kwargs):
        """Adds other models to list on the page"""
        context = super().get_context_data(**kwargs)
        return selectors.list_references(context)


class TransactionCreateView(TransactionModelSuccessMixin, TransactionTemplateContextFormMixin, CreateView): pass
class TransactionUpdateView(TransactionModelSuccessMixin, TransactionTemplateContextFormMixin, UpdateView): pass
class TransactionDeleteView(TransactionModelSuccessMixin, DeleteView):
    template_name = 'accounting/confirm_delete.html'


class ReferenceCreateView(ReferenceSuccessMixin, TemplateContextMixin, CreateView): pass
class ReferenceUpdateView(ReferenceSuccessMixin, TemplateContextMixin, UpdateView): pass
class ReferenceDeleteView(ReferenceSuccessMixin, DeleteView):
    template_name = 'accounting/confirm_delete.html'
