import requests

from django.shortcuts import render, redirect
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


def home(request):
    return render(request, 'home.html')


def lista_pizzas(request):
    pizzas = Pizza.objects.select_related('categoria').all()

    return render(
        request,
        'pizzas.html',
        {'pizzas': pizzas}
    )


def nova_pizza(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        imagem = request.FILES.get('imagem')

        criar_categoria = request.POST.get('criar_categoria')

        if criar_categoria:
            nome_categoria = request.POST.get('nome_categoria')
            descricao_categoria = request.POST.get('descricao_categoria')

            categoria, criada = Categoria.objects.get_or_create(
                nome=nome_categoria,
                defaults={
                    'descricao': descricao_categoria
                }
            )
        else:
            categoria_id = request.POST.get('categoria')
            categoria = Categoria.objects.get(id=categoria_id)

        Pizza.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            categoria=categoria,
            imagem=imagem
        )

        return redirect('lista_pizzas')

    return render(
        request,
        'nova_pizza.html',
        {'categorias': categorias}
    )


def editar_pizza(request, id):
    pizza = Pizza.objects.get(id=id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        pizza.nome = request.POST.get('nome')
        pizza.descricao = request.POST.get('descricao')
        pizza.preco = request.POST.get('preco')

        categoria_id = request.POST.get('categoria')
        pizza.categoria = Categoria.objects.get(id=categoria_id)

        # Verifica se o usuário marcou para remover a imagem
        remover_imagem = request.POST.get('remover_imagem')

        if remover_imagem:
            if pizza.imagem:
                pizza.imagem.delete(save=False)

            pizza.imagem = None

        # Verifica se o usuário escolheu uma nova imagem
        imagem = request.FILES.get('imagem')

        if imagem:
            # Remove a imagem antiga antes de colocar a nova
            if pizza.imagem:
                pizza.imagem.delete(save=False)

            pizza.imagem = imagem

        pizza.save()

        return redirect('lista_pizzas')

    return render(
        request,
        'editar_pizza.html',
        {
            'pizza': pizza,
            'categorias': categorias
        }
    )




def excluir_pizza(request, id):
    pizza = Pizza.objects.get(id=id)

    if request.method == 'POST':
        pizza.delete()
        return redirect('lista_pizzas')

    return render(
        request,
        'confirmar_exclusao.html',
        {'pizza': pizza}
    )


def pagina_consultar_cep(request):
    dados = None
    erro = None

    if request.method == 'POST':
        cep = request.POST.get('cep', '').replace('-', '').replace('.', '').strip()

        if len(cep) != 8 or not cep.isdigit():
            erro = "Digite um CEP válido com 8 números."
        else:
            try:
                url = f"https://viacep.com.br/ws/{cep}/json/"
                resposta = requests.get(url, timeout=5)

                if resposta.status_code != 200:
                    erro = "Não foi possível consultar o CEP."
                else:
                    resultado = resposta.json()

                    if resultado.get("erro"):
                        erro = "CEP não encontrado."
                    else:
                        dados = resultado

            except requests.RequestException:
                erro = "Erro ao acessar o serviço de CEP."

    return render(
        request,
        'consultar_cep.html',
        {
            'dados': dados,
            'erro': erro
        }
    )

def lista_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        'categorias.html',
        {'categorias': categorias}
    )


def nova_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        Categoria.objects.create(
            nome=nome,
            descricao=descricao
        )

        return redirect('lista_categorias')

    return render(request, 'nova_categoria.html')


def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.nome = request.POST.get('nome')
        categoria.descricao = request.POST.get('descricao')
        categoria.save()

        return redirect('lista_categorias')

    return render(
        request,
        'editar_categoria.html',
        {'categoria': categoria}
    )


def excluir_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(
        request,
        'confirmar_exclusao_categoria.html',
        {'categoria': categoria}
    )

def lista_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        'categorias.html',
        {'categorias': categorias}
    )


def nova_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        Categoria.objects.create(
            nome=nome,
            descricao=descricao
        )

        return redirect('lista_categorias')

    return render(request, 'nova_categoria.html')


def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.nome = request.POST.get('nome')
        categoria.descricao = request.POST.get('descricao')

        categoria.save()

        return redirect('lista_categorias')

    return render(
        request,
        'editar_categoria.html',
        {'categoria': categoria}
    )


def excluir_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(
        request,
        'confirmar_exclusao_categoria.html',
        {'categoria': categoria}
    )
