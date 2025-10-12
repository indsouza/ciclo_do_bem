"""
URL configuration for projeto_ciclo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# gerenciador/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import index,saiba_mais

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estabelecimentos/', include(('estabelecimentos.urls', 'estabelecimentos'), namespace='estabelecimentos')),
    path('instituicoes/', include(('instituicoes.urls', 'instituicoes'), namespace='instituicoes')),
    path('ofertas/', include(('ofertas.urls', 'ofertas'), namespace='ofertas')),
    path('', index, name='index'),
    path('saiba_mais/',saiba_mais, name='saiba_mais'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
