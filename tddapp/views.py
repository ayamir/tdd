from django.http import HttpResponse
from django.shortcuts import render, redirect
from tddapp.models import Item


# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def test_can_save_a_POST_request(self):
    response = self.client.post('/', data={'item_text': 'A new list item'})

    self.assertEqual(Item.objects.count(), 1)
    new_item = Item.objects.first()
    self.assertEqual(new_item.text, 'A new list item')

    self.assertIn('A new list item', response.content.decode())
    self.assertTemplateUsed(response, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'item': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')