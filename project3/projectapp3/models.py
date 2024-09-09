from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    modified_by_signal = models.BooleanField(default=False)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    if not instance.modified_by_signal:  # Check if the instance was already modified by the signal
        print(f"Signal received for: {instance.name}")
        # Modify the instance within the signal handler
        instance.name = "Modified by Signal"
        instance.modified_by_signal = True  # Set the flag to True to prevent further modification
        instance.save()  # Save the modified instance within the same transaction

def run_transaction():
    # Start a transaction
    with transaction.atomic():
        # Create an instance of MyModel
        obj = MyModel.objects.create(name="Original")
        print(f"Name after creation: {obj.name}")

        # Perform an update within the same transaction
        obj.name = "Updated by Main Transaction"
        obj.save()  # This triggers the signal

        # Fetch the updated object to see changes
        obj.refresh_from_db()
        print(f"Name after signal handling: {obj.name}")
