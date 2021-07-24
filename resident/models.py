from django.db import models
from django.utils.translation import ugettext_lazy as _
from estate.models import Estate
from django.contrib.auth import get_user_model

# Create your models here.
class Resident(models.Model):
    user=models.ForeignKey(get_user_model(), verbose_name=_("user"),related_name="resident", on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate, verbose_name=_("Estate"), on_delete=models.CASCADE, related_name="residents")
    house_address = models.CharField(_("house address"), max_length=100)
    # user is inactive until admin accepts him into the estate.
    # status = models.BooleanField(_("active resident"), default=False) 
    status=models.IntegerField(_("status"), default=0) #0. Inactive, 1. Active, 2. suspended, 3. Processing
    # is_admin = models.BooleanField(_("foris Admin"), default=False) 
    created_date= models.DateTimeField(_("created date"),auto_now_add=True)
    comment = models.TextField(_("Comment"), blank=True, null=True)

    class Meta:
        unique_together =  ('estate', 'user') 
        ordering = ['estate']

    def __str__(self):
        if self.user.first_name or self.user.last_name:
            return f'{self.estate.name} -{self.house_address} ({self.user.first_name} {self.user.last_name})'
        else:
            return f'{self.estate.name} -{self.house_address} ({self.user.email})'