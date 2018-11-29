from django.db import models

from weight_management_api.users.models import User


class UserWeight(models.Model):
    """
    Model to manage user's weight
    """
    weight = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'user_weights'

    def __str__(self):
        return '{name}_{weight}'.format(name=self.user.first_name, weight=self.weight)
