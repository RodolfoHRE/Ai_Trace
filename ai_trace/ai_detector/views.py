from django.shortcuts import render, redirect
import random

def index(request):
    if request.method == 'GET':
        request.session.pop('image', None)
        request.session.pop('image_name', None)
        return render(request, 'inicio.html')

    if request.method == 'POST':
        image = request.FILES.get('image')
        if image and image.size <= 2 * 1024 * 1024:  # 2MB
            request.session['image_name'] = image.name
            return render(request, 'inicio.html', {
                'file_uploaded': True,
                'image_name': image.name,
            })
        else:
            return render(request, 'inicio.html', {
                'error': 'Arquivo muito grande! Máximo 2MB.'
            })