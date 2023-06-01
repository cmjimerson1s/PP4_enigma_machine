from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import BlogPost
from . import views


class BlogPostListViewTest(TestCase):

    def setUp(self):
        self.blogpost1 = BlogPost.objects.create(
            blog_title="Blog Post 1",
            slug="blog-post-1",
            blog_image="test.jpg",
            blog_blurb="Blurb for Blog Post 1",
            blog_content="Content for Blog Post 1",
            posted_date=timezone.now(),
        )
        self.blogpost2 = BlogPost.objects.create(
            blog_title="Blog Post 2",
            slug="blog-post-2",
            blog_image="test.jpg",
            blog_blurb="Blurb for Blog Post 2",
            blog_content="Content for Blog Post 2",
            posted_date=timezone.now(),
        )

    def test_blogpost_list_view(self):
        # Make a GET request to the blog list view URL and
        # store the response in a variable
        response = self.client.get(reverse("blog-post-list"))
        # Assert that the status code of the response is 200,
        # which means that the request was successful
        self.assertEqual(response.status_code, 200)
        # Assert that that template and content reponses match expected values
        self.assertTemplateUsed(response, "blog/blog_posts.html")
        self.assertContains(response, self.blogpost1.blog_title)
        self.assertContains(response, self.blogpost2.blog_title)
        self.assertContains(response, self.blogpost1.blog_blurb)
        self.assertContains(response, self.blogpost2.blog_blurb)
        # Assert that the queryset of blog posts passed to the template is
        # equal to a list of BlogPost objects as string representations
        self.assertQuerysetEqual(
            response.context["object_list"],
            [
                f"<BlogPost: {self.blogpost2.blog_title}>",
                f"<BlogPost: {self.blogpost1.blog_title}>",
            ],
            None,
            False,
        )


class BlogPostDetailViewTest(TestCase):
    def setUp(self):
        self.blogpost = BlogPost.objects.create(
            blog_title="Blog Post",
            slug="blog-post",
            blog_image="test.jpg",
            blog_blurb="Blurb for Blog Post",
            blog_content="Content for Blog Post",
            posted_date=timezone.now(),
        )

    def test_blogpost_detail_view_short_post(self):
        response = self.client.get(
            reverse("detail_view", args=[self.blogpost.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_post_detail.html")
        self.assertContains(response, self.blogpost.blog_title)
        # Assert blurb not rendered because blogpost is too short
        self.assertNotContains(response, self.blogpost.blog_blurb)
        self.assertContains(response, self.blogpost.blog_content)

    def test_blogpost_detail_view_long_post(self):
        multiline_blog_post = (
            "Content1\nContent2\nContent3\nContent4\nContent5"
        )
        contents = multiline_blog_post.split("\n")
        BlogPost.objects.filter(slug=self.blogpost.slug).update(
            blog_content=multiline_blog_post
        )
        response = self.client.get(
            reverse("detail_view", args=[self.blogpost.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_post_detail.html")
        self.assertContains(response, self.blogpost.blog_title)
        # Assert that the blurb is rendered because the blogpost is
        # long enough for a blockquote
        self.assertContains(response, self.blogpost.blog_blurb)
        # Assert all parts of the blog content is rendered
        self.assertContains(response, contents[0])
        self.assertContains(response, contents[1])
        self.assertContains(response, contents[2])
        self.assertContains(response, contents[3])
        self.assertContains(response, contents[4])

    def test_post(self):
        response = self.client.post(
            reverse("detail_view", args=[self.blogpost.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog_post_detail.html")
