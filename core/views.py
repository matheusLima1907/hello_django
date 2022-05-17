from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, age):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'
                        .format(nome, age))


def soma(request, n1, n2):

    return HttpResponse('A soma de {} e {} e {}'
                        .format(n1, n2, n1+n2))


def sub(request, n1, n2):

    return HttpResponse('A subtração de {} e {} e {}'
                        .format(n1, n2, n1-n2))


def mult(request, n1, n2):

    return HttpResponse('A multiplicação de {} e {} e {}'
                        .format(n1, n2, n1*n2))


def div(request, n1, n2):

    return HttpResponse('A divisão de {} e {} e {}'
                        .format(n1, n2, n1/n2))
