from django.urls import path
from . import views

urlpatterns = [
    path('apply-loan/<int:farmer_id>/', views.apply_for_loan, name='apply-loan'),
]

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loan/', include('loan_scoring.urls')),
]
