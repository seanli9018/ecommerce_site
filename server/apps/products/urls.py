from django.urls import path
from .views import ProductCategoryView

app_name = 'products'

urlpatterns = [
    path('product-categories/<int:parent_category_id>/', ProductCategoryView.as_view(), name='product-categories'),
]