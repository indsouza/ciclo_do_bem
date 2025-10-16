from django.contrib import admin
from django.urls import path, include
from .views import index, saiba_mais
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps
    path('estabelecimentos/', include(('estabelecimentos.urls', 'estabelecimentos'), namespace='estabelecimentos')),
    path('instituicoes/', include(('instituicoes.urls', 'instituicoes'), namespace='instituicoes')),
    path('ofertas/', include(('ofertas.urls', 'ofertas'), namespace='ofertas')),

    # Core / Home
    path('', index, name='index'),
    path('saiba_mais/', saiba_mais, name='saiba_mais'),
]

# Servir arquivos de mídia durante desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
