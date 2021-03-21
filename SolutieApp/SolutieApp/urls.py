"""SolutieApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from Application.views import get_signup
from Application.views import get_login
from Application.views import get_dashboard
from Application.views import get_forms
from Application.views import get_build
from Application.views import get_template_online_store
from Application.views import save_site
from Application.views import get_summary
from Application.views import save_product

#--- daca crapa sterge
from django.conf import settings
from django.conf.urls.static import static
#----final


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/registration/',get_signup),
    path('accounts/login/',get_login),
    path('dashboard/', get_dashboard),
    path('dashboard/site/', get_template_online_store),
    path('build/forms/', get_forms),
    path('build/', get_build),
    path('build/save/', save_site),
    path('build/product/', save_product),
    path('', get_dashboard),
    path('test/', get_summary),
]


#--- daca crapa sterge
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#----final