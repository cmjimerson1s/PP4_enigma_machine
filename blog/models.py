from django.db import models
from cloudinary.models import CloudinaryField 


class BlogPost(models.Model):
    TAGS = [
        ('Blog','Blog'),
        ('Promotion','Promotion'),
        ('Sale','Sale'),
        ('News', 'News'),
        ('Partner Advert', 'Partner Advert'),
        ('Holiday', 'Holiday'),
        ('B.T.S', 'B.T.S'),
        ('Meet the Staff', 'Meet the Staff')
    ]

    blog_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = models.CharField(max_length=200, choices=TAGS, null=True)
    blog_image = CloudinaryField('detail image', default='placeholder')
    blog_small_image = CloudinaryField('thumbnail', default='placeholder')
    blog_blurb = models.TextField(blank=True)
    blog_content = models.TextField()
    posted_date = models.DateField(auto_now=False)
    meta_tags = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return self.blog_title