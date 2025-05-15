import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # ← 설정 경로
django.setup()

from blog.models import Post

post = Post.objects.get(id=3)
print(post.get_absolute_url())