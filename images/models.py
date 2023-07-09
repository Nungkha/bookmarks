from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Images(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self) -> str:
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# slug can also be self populated from admin.py file while registering model in Admin site 
# using "prepopulated_fields" attribute
# but that is just for the Admin Interface

# save() method is overridden for user Input

    def get_absolute_url(self):
        return reverse("images:detail", args=[self.id, self.slug])
    