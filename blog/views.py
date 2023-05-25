from django.shortcuts import render,get_object_or_404
from .models import BlogPost
from django.views import generic, View 


class BlogListView(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.all()
    template_name = 'blog_posts.html'


class BlogDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.all()
        blog = get_object_or_404(queryset, slug=slug)
        content = blog.blog_content
        content_parts = content.split('\n')
        template = 'blog_post_detail.html'
        context = {
            'blog': blog,
            'content_parts': content_parts,
            'blog_list': queryset,
        }
        return render(request, template, context)
    
    def post(self, request, slug, *args, **kwargs):
        template = 'blog_post_detail.html'
        return render(request, template)
