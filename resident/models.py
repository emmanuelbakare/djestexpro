from django.db import models
from django.utils.translation import ugettext_lazy as _
from estate.models import Estate
from django.contrib.auth import get_user_model

# Create your models here.
class Resident(models.Model):
    user=models.ForeignKey(get_user_model(), verbose_name=_("user"),related_name="resident", on_delete=models.CASCADE)
    # estate = models.ManyToManyField(Estate, verbose_name=_("estate"), related_name="residents")
    estate = models.ForeignKey(Estate, verbose_name=_("Estate"), on_delete=models.CASCADE, related_name="residents")
    house_address = models.CharField(_("house address"), max_length=100)
    # user is inactive until admin accepts him into the estate.
    # status = models.BooleanField(_("active resident"), default=False) 
    status=models.IntegerField(_("status"), default=0) #0. Inactive, 1. Active, 2. suspended, 3. Processing
    # priv = models.IntegerField(_("priviledges"), default=0) # priviledge to access different sections
    # if registering an estate admin will be True if Joining an estate is_admin will be False
    # i.e you can only be an admin if you are the one that register the estate
    # is_admin = models.BooleanField(_("foris Admin"), default=False) 
    created_date= models.DateTimeField(_("created date"),auto_now_add=True)
    comment = models.TextField(_("Comment"))

    def __str__(self):
        return f'{self.user.email} ({self.house_address})'