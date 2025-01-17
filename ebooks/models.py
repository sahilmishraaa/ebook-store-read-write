from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Ebook(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ebooks')
    description = models.TextField()
    cover_image = models.ImageField(upload_to='ebooks/allebook/covers/')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    file = models.FileField(upload_to='ebooks/allebooks/files/')
    is_paid = models.BooleanField(default=False)
    publication_date = models.DateTimeField(auto_now_add=True)
    purchase_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20, 
        choices=[('available', 'Available'), ('unavailable', 'Unavailable')],
        default='available'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    keywords = models.CharField(max_length=500, blank=True, help_text="Comma-separated keywords")
    file_size = models.PositiveIntegerField(help_text="File size in bytes", null=True)
    review_count = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    page_count = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        help_text="Number of pages in the ebook"
    )

    class Meta:
        ordering = ['-uploaded_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['title']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.status = 'unavailable'
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
