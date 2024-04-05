from django.shortcuts import render

def inicio(request):

    return render(request, 'index.html', {})

def categorias(request):

    return render(request, 'categorias.html', {})

def documentos(request):

    return render(request, 'documentos.html', {})

def contacto(request):

    return render(request, 'contacto.html', {})



