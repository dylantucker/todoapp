from django.urls import reverse
# Create your tests here.

def test_index_page():
    url = reverse('index')
    assert url == '/'