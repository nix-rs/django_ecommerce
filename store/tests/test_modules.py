from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='django1', slug='django1')

    def test_category_model_entry0(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data),  'django1')


class TestProductModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')

    def test_product_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        self.assertEqual(url, '/django-beginners/')
        response = self.client.post(
            reverse('store:product_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.products.all()
        self.assertEqual(data.count(), 1)
