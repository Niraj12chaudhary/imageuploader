from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = Image.objects.all()
            return render(request, 'home.html', {'form': ImageForm(), 'success': 'Image uploaded successfully!', 'img': img})
    else:
        form = ImageForm()
        img = Image.objects.all()
    return render(request, 'home.html', {'img': img, 'form': form})
