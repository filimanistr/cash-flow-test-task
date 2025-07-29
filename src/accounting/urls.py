from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('references/', views.ReferencesView.as_view(), name='references'),

    path('transactions/create/', views.TransactionCreateView.as_view()),
    path('references/states/create/', views.create_reference_views_factory(models.Status)),
    path('references/types/create/', views.create_reference_views_factory(models.Type)),
    path('references/categories/create/', views.create_reference_views_factory(models.Category)),
    path('references/subcategories/create/', views.create_reference_views_factory(models.SubCategory)),

    path('transactions/update/<int:pk>/', views.TransactionUpdateView.as_view()),
    path('references/states/update/<int:pk>/', views.update_reference_views_factory(models.Status)),
    path('references/types/update/<int:pk>/', views.update_reference_views_factory(models.Type)),
    path('references/categories/update/<int:pk>/', views.update_reference_views_factory(models.Category)),
    path('references/subcategories/update/<int:pk>/', views.update_reference_views_factory(models.SubCategory)),

    path('transactions/remove/<int:pk>/', views.delete_views_factory(models.Transaction, 'index')),
    path('references/states/remove/<int:pk>/', views.delete_views_factory(models.Status)),
    path('references/types/remove/<int:pk>/', views.delete_views_factory(models.Type)),
    path('references/categories/remove/<int:pk>/', views.delete_views_factory(models.Category)),
    path('references/subcategories/remove/<int:pk>/', views.delete_views_factory(models.SubCategory)),
]

