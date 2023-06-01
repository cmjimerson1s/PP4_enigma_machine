from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.views import generic, View

# Collects all the BlogPost items from database
# to render to the template


class BlogListView(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.all()
    template_name = "blog/blog_posts.html"

# When user selects one blogpost the slug is used
# to query the database and collect the additional
# information for said blogpost, while also sending
# the current blog items to render as a side window


class BlogDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.all()
        blog = get_object_or_404(queryset, slug=slug)
        content = blog.blog_content
        content_parts = content.split("\n")
        template = "blog/blog_post_detail.html"
        context = {
            "blog": blog,
            "content_parts": content_parts,
            "blog_list": queryset,
        }
        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        template = "blog/blog_post_detail.html"
        return render(request, template)
