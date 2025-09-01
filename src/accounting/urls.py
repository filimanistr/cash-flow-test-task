from django.urls import path, include
from . import views, models

"""
I'd rather define the REST API here
and have the client pass model names
in the request body; What you see here
is the consequence of using templates
"""

status_patterns = [
    path('states/create/', views.ReferenceCreateView.as_view(model=models.Status)),
    path('states/update/<int:pk>/', views.ReferenceUpdateView.as_view(model=models.Status)),
    path('states/remove/<int:pk>/', views.ReferenceDeleteView.as_view(model=models.Status)),
]

type_patterns = [
    path('types/create/', views.ReferenceCreateView.as_view(model=models.Type)),
    path('types/update/<int:pk>/', views.ReferenceUpdateView.as_view(model=models.Type)),
    path('types/remove/<int:pk>/', views.ReferenceDeleteView.as_view(model=models.Type)),
]

category_patterns = [
    path('categories/create/', views.ReferenceCreateView.as_view(model=models.Category)),
    path('categories/update/<int:pk>/', views.ReferenceUpdateView.as_view(model=models.Category)),
    path('categories/remove/<int:pk>/', views.ReferenceDeleteView.as_view(model=models.Category)),
]

subcategory_pattern = [
    path('subcategories/create/', views.ReferenceCreateView.as_view(model=models.SubCategory)),
    path('subcategories/update/<int:pk>/', views.ReferenceUpdateView.as_view(model=models.SubCategory)),
    path('subcategories/remove/<int:pk>/', views.ReferenceDeleteView.as_view(model=models.SubCategory)),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('transactions/create/', views.TransactionCreateView.as_view()),
    path('transactions/update/<int:pk>/', views.TransactionUpdateView.as_view()),
    path('transactions/remove/<int:pk>/', views.TransactionDeleteView.as_view()),

    path('references/', views.ReferencesView.as_view(), name='references'),
    path('references/', include((status_patterns, 'states'))),
    path('references/', include((type_patterns, 'types'))),
    path('references/', include((category_patterns, 'categories'))),
    path('references/', include((subcategory_pattern, 'subcategories'))),
]
