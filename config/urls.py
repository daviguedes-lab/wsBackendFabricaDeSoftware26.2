"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from produtos.views import (
    home,
    consultar_cep,
    pagina_consultar_cep,
    lista_pizzas,
    nova_pizza,
    editar_pizza,
    excluir_pizza,
    lista_categorias,
    nova_categoria,
    editar_categoria,
    excluir_categoria,
    CategoriaViewSet,
    PizzaViewSet,
)


router = DefaultRouter()

router.register(r'categorias', CategoriaViewSet)
router.register(r'pizzas', PizzaViewSet)


urlpatterns = [
    # Página inicial
    path('', home, name='home'),

    # Admin
    path('admin/', admin.site.urls),

    # API
    path('api/', include(router.urls)),
    path('api/consultar-cep/<str:cep>/', consultar_cep),

    # Pizzas
    path('pizzas/', lista_pizzas, name='lista_pizzas'),
    path('pizzas/nova/', nova_pizza, name='nova_pizza'),
    path('pizzas/editar/<int:id>/', editar_pizza, name='editar_pizza'),
    path('pizzas/excluir/<int:id>/', excluir_pizza, name='excluir_pizza'),

    # CEP
    path('consultar-cep/', pagina_consultar_cep, name='consultar_cep'),

    # Categorias
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('categorias/nova/', nova_categoria, name='nova_categoria'),
    path('categorias/editar/<int:id>/', editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:id>/', excluir_categoria, name='excluir_categoria'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )