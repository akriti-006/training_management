# shared_app/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ProgrammingLanguage  # or any other model you want to use
import os

@receiver(post_save, sender=ProgrammingLanguage)
def after_car_saved(sender, instance, created, **kwargs):
    if created:
        print(f"🚗 ProgrammingLanguage created: {instance.name}")
    else:
        print(f"✏️ ProgrammingLanguage updated: {instance.name}")

# @receiver(post_delete, sender=ProgrammingLanguage)
# def after_car_deleted(sender, instance, **kwargs):
#     if instance.photo:
#         if os.path.isfile(instance.photo.path):
#             os.remove(instance.photo.path)
#             print(f"🗑️ Deleted photo: {instance.photo.path}")
