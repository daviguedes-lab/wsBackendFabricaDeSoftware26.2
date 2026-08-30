import requests

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Categoria, Pizza
from .serializers import CategoriaSerializer, PizzaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


@api_view(['GET'])
def consultar_cep(request, cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url, timeout=5)

        if resposta.status_code != 200:
            return Response(
                {"erro": "Não foi possível consultar o CEP."},
                status=status.HTTP_502_BAD_GATEWAY
            )

        dados = resposta.json()

        if dados.get("erro"):
            return Response(
                {"erro": "CEP não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(dados, status=status.HTTP_200_OK)

    except requests.RequestException:
        return Response(
            {"erro": "Erro ao acessar o serviço de CEP."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )