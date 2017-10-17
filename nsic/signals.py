#from django.db.models.signals import pre_save
#from django.dispatch import receiver
#from .models import Year

#@receiver(pre_save, sender=NSICInfo)
#def my_callback(sender, instance, *args, **kwargs):
#    instance.detail.replace('{{ REG_FEE }}',Year.objects.get(pk=1).registration_fee)
