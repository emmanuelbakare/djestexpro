from django.db import models
from django.utils.translation import ugettext_lazy as _
from estate.models import Estate
from django.contrib.auth import get_user_model

# Create your models here.
class Resident(models.Model):
    user=models.ForeignKey(get_user_model(), verbose_name=_("user"),related_name="resident", on_delete=models.CASCADE)
    estate = models.ManyToManyField(Estate, verbose_name=_("estate"), related_name="residents")
    house_address = models.CharField(_("house address"), max_length=100)
    active = models.BooleanField(_("active resident"), default=False) # this 
    priv = models.IntegerField(_("priviledges"), default=0) # priviledge to access different sections
    # if registering an estate admin will be True if Joining an estate is_admin will be False
    # i.e you can only be an admin if you are the one that register the estate
    is_admin = models.BooleanField(_("is Admin"), default=False) 
    created_date= models.DateTimeField(_("created date"),auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} ({self.house_address})'