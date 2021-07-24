from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    phone = models.CharField(_("phone number"),null=True, blank=True,max_length=50)
    profile_pic = models.ImageField(_("profile picture"), 
                                        upload_to="profile_pix", 
                                        default="defaultUser.png")

    def __str__(self):
        return f"{self.user.email}"
    