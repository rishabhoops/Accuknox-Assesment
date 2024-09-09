from django.core.management.base import BaseCommand
from projectapp2.models import MyModel
import threading

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(f"Main thread ID before creating object: {threading.get_ident()}")
        obj = MyModel.objects.create(name="Test")
        print("Object created")
