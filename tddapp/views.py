from django.http import HttpResponse
from django.shortcuts import render, redirect
from tddapp.models import Item

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})


def test_can_save_a_POST_request(self):
    response = self.client.post('/', data={'item_text': 'A new list item'})

    self.assertEqual(Item.objects.count(), 1)
    new_item = Item.objects.first()
    self.assertEqual(new_item.text, 'A new list item')

    self.assertIn('A new list item', response.content.decode())
    self.assertTemplateUsed(response, 'home.html')
