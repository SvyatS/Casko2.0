from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views
import payments.views as pv
import calculation.views as cv



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('home/', pv.Homepage, name = 'homepage'),
    path('payment/create/', pv.CreatePayment, name = 'CreatePayment'),
    path('payment/calculation/', cv.calculation, name = 'calculation'),
]

urlpatterns += staticfiles_urlpatterns()

router = SimpleRouter()

router.register(r'policyholder', pv.PolicyholderViewSet)

urlpatterns += router.urls