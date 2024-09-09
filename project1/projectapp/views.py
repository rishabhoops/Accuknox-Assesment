from django.http import HttpResponse
from .models import MyModel

def test_signal_view(request):
    print("Before creating MyModel instance...")
    obj = MyModel.objects.create(name="Test")
    print("After creating MyModel instance...")
    return HttpResponse("Check your console for the output")