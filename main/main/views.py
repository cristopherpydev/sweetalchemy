from django.shortcuts import render

def homepage(request):
    return render(request, 'documents/index.html', {})
def about_us(request):
    return render(request, 'documents/about_us.html', {})
def traditional_baking(request):
    return render(request, 'documents/traditional_baking.html', {})