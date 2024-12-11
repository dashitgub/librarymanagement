from django.shortcuts import render, redirect
from .models import Library, Category
from .forms import LibraryForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def library_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        library = Library.objects.filter(category_id=category_id).order_by('created_at')
    else:
        library = Library.objects.all().order_by('created_at')
    
    categories = Category.objects.all()

    paginator = Paginator(library, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'analiz/task_list.html', {'library':page_obj, 'categories':categories})

def Library_add(requests):
    if requests.method == 'POST':
        form = LibraryForm(requests.POST)
        if form.is_valid():
            form.save()
            print("Library added successfully!")
            return redirect('task_list')
    else:
        form = LibraryForm
    Categories = Category.objects.all()
    return render(requests, 'analiz/task_form.html', {'form':form, 'categories' : Categories})

def library_edit(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=library)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = LibraryForm(instance=library)
    return render(request, 'analiz/task_form.html', {'form': form})

def library_delete(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        library.delete()
        return redirect('task_list')
    return render(request, 'analiz/task_confirm_delete.html', {'library': library})
