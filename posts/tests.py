from django.test import TestCase
from django.urls import reverse
from .models import Post
from datetime import datetime, timedelta

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        # This method is run before each test.
        self.post = Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_creation(self):
        """Test if a post is created successfully"""
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')
        self.assertIsNotNone(post.slug)

    def test_slug_generation(self):
        """Test if the slug is generated from the title"""
        self.assertEqual(self.post.slug, 'test-post')

class HomeViewTest(TestCase):

    def test_home_view_status_code(self):
        """Test if home view returns 200 status code"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        """Test if home view uses the correct template"""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'posts/index.html')

class PostsViewTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='This is a test post.')

    def test_posts_view_status_code(self):
        """Test if posts view returns 200 status code"""
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_posts_list_in_context(self):
        """Test if posts are passed in the context"""
        response = self.client.get(reverse('posts'))
        self.assertIn(self.post, response.context['posts'])

class PostDetailViewTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_detail_view_status_code(self):
        """Test if post detail view returns 200 status code"""
        response = self.client.get(reverse('post-detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_template_used(self):
        """Test if post detail view uses the correct template"""
        response = self.client.get(reverse('post-detail', kwargs={'slug': self.post.slug}))
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    def test_post_detail_context(self):
        """Test if the post is in the context"""
        response = self.client.get(reverse('post-detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.context['post'], self.post)
