from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
class MyModel(models.Model):
 name = models.CharField(max_length=100)
  
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received. Handler starting...")
    post_save.disconnect(my_signal_handler, sender=MyModel)
    instance.name = instance.name + "_updated"
    instance.save()
    post_save.connect(my_signal_handler, sender=MyModel)
    print("Signal handler finished.")