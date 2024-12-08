from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContentForm
from .models import Content

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContentForm
from .models import Content

def content_list(request):
    """List all content entries."""
    contents = Content.objects.all()
    return render(request, 'cms/content_list.html', {'contents': contents})

def content_upload(request):
    """Upload new content."""
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('content_list')
    else:
        form = ContentForm()
    return render(request, 'cms/content_upload.html', {'form': form})

def content_edit(request, pk):
    """Edit an existing content entry."""
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            return redirect('content_list')
    else:
        form = ContentForm(instance=content)
    return render(request, 'cms/content_edit.html', {'form': form, 'content': content})

def content_delete(request, pk):
    """Delete a content entry."""
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        content.delete()
        return redirect('content_list')
    return render(request, 'cms/content_delete.html', {'content': content})