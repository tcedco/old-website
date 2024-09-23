from django_distill import distill

def get_urls():
    return [
        ('/', 'index'),
        ('/about/', 'about'),
        ('/posts/', 'posts'),
        # For post detail, you need to specify slugs
        ('/posts/<slug:slug>/', 'post-detail'),
    ]

DISTILLATION = {
    'default': get_urls,
}
