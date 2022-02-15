from django.db import models
from user_data.models import UserTable


class GameModel(models.Model):
    """model to store the game history"""

    user = models.ForeignKey(UserTable, null=True, on_delete=models.CASCADE)
    player1 = models.CharField(max_length=50)
    player1_score = models.IntegerField(default=0)
    player2 = models.CharField(max_length=50)
    player2_score = models.IntegerField(default=0)
    dateTime = models.DateTimeField(auto_now_add=True)
    player1_team = models.CharField(max_length=50)
    player2_team = models.CharField(max_length=50)

    def __str__(self):
        return str(self.player1)


