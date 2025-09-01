from . import models


def list_transactions(request):
    list_filters = (
        'status__pk',
        'type__pk',
        'category__pk',
        'subcategory__pk',
        'created_at__gte',
        'created_at__lte',
    )

    transactions = models.Transaction.objects.all()
    for filter in list_filters:
        f = request.GET.get(filter)
        if f is not '' and f is not None:
            transactions = transactions.filter(**{filter: f})
    return transactions


def list_filters_options(context: dict) -> dict:
    context['states'] = models.Status.objects.all()
    context['types'] = models.Type.objects.all()
    context['categories'] = models.Category.objects.all()
    context['subcategories'] = models.SubCategory.objects.all()
    return context


def list_references(context: dict) -> dict:
    context['type'] = models.Type.objects.all()
    context['category'] = models.Category.objects.all()
    context['subcategory'] = models.SubCategory.objects.all()
    return context
