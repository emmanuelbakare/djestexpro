from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.




# class EstateAddress(models.Model):
#     street1 = models.CharField(_("street 1"), max_length=100)
#     street2 = models.CharField(_("street 2"), max_length=100)
#     city = models.CharField(_("city"), max_length=20)
#     state_region = models.CharField(_("state or region"), max_length=100)
#     zip_code = models.CharField(_("zip code"), max_length=100)
#     country = models.CharField(_("country"), max_length=100)

#     def __str__(self):
#         return  self.street1 





class Estate(models.Model):
    name= models.CharField(_("estate name"), max_length=50)
    total_house = models.IntegerField(_("total house"), null=True, blank=True)

    street1 = models.CharField(_("street 1"), max_length=150)
    city = models.CharField(_("city"), max_length=20)
    state_region = models.CharField(_("state or region"), max_length=100)
    country = models.CharField(_("country"), max_length=100)
    # address= models.OneToOneField(EstateAddress, blank=True, null=True, on_delete=models.CASCADE)
    # admin=models.ManyToManyField(User, verbose_name=_("admin"))
    comment=models.TextField(_("comment"), null=True, blank=True)
    created_date= models.DateTimeField(_("Created Date"),auto_now_add=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return  f'{self.name} -  {self.city}, {self.country}'

class EstateAdmin(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    estate=models.ForeignKey(Estate, verbose_name=_("Estate"), on_delete=models.CASCADE, related_name="admin")
    perms = models.IntegerField(_("permission"), null=True, blank=True)

    class Meta:
        unique_together=['user','estate']



   




