from django.test import TestCase
from django.urls import reverse


class TestSearch(TestCase):
    def test_index_page(self):
        assert reverse("public:index") == "/"
