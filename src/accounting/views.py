from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class IndexView(ListView):
    """
    Главная страница
    """
    model = models.Transaction

    def get_queryset(self):
        """Возвращает транзакции и фильтрует их
        в зависимости от параметров запроса к этой вьюшке"""
        list_filters = (
            'status__pk',
            'type__pk',
            'category__pk',
            'subcategory__pk',
            'created_at__gte',
            'created_at__lte',
        )

        transactions = self.model.objects.all()
        for filter in list_filters:
            f = self.request.GET.get(filter)
            if f is not '' and f is not None:
                transactions = transactions.filter(**{filter: f})
        return transactions

    def get_context_data(self, **kwargs):
        """Добавляет данные для выставления фильтров"""
        context = super().get_context_data(**kwargs)
        context['states'] = models.Status.objects.all()
        context['types'] = models.Type.objects.all()
        context['categories'] = models.Category.objects.all()
        context['subcategories'] = models.SubCategory.objects.all()
        return context


class ReferencesView(ListView):
    """
    Страница управления справочниками
    статусы, типы, категории, подкатегории
    """
    model = models.Status
    context_object_name = 'status'
    template_name = 'accounting/references.html'

    def get_context_data(self, **kwargs):
        """Добавляет данные с других моделей
        для отображения всех их на 1 странице"""
        context = super().get_context_data(**kwargs)
        context['type'] = models.Type.objects.all()
        context['category'] = models.Category.objects.all()
        context['subcategory'] = models.SubCategory.objects.all()
        return context


class CreateUpdateViewMixin:
    """
    Mixin for `CreateView` and `UpdateView` classes
    sets `template_name` and `fields` attributes to View
    also adds model's `verbose_name` to context
    """
    template_name = 'accounting/details.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['verbose_name_pos'] = self.model.verbose_name_pos()
        return context


class TransactionCreateView(CreateUpdateViewMixin, CreateView):
    model = models.Transaction
    form_class = forms.TransactionForm
    fields = None


class TransactionUpdateView(CreateUpdateViewMixin, UpdateView):
    model = models.Transaction
    form_class = forms.TransactionForm
    fields = None


def create_reference_views_factory(users_mdoel):
    class ModelCreateView(CreateUpdateViewMixin, CreateView):
        model = users_mdoel
    return ModelCreateView.as_view()


def update_reference_views_factory(users_model):
    class ModelUpdateView(CreateUpdateViewMixin, UpdateView):
        model = users_model
    return ModelUpdateView.as_view()


def delete_views_factory(users_model, url='references'):
    class ModelDeleteView(DeleteView):
        template_name = 'accounting/confirm_delete.html'
        success_url = reverse_lazy(url)
        model = users_model
    return ModelDeleteView.as_view()
