from django.db import models
from django.urls import reverse

MATCHS = [
    ('H', 'Home'),
    ('A', 'Away'),
    ('P', 'Postpone')
]

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})

    class Meta:
        ordering = ['id']


class Match(models.Model):
    date = models.DateField('match date')
    match = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MATCHS,
        # set the default value for match to be 'H'
        default=MATCHS[0][0]
    )

    # Create a player_id FK
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the firendly value of a Field.choice
        return f"{self.get_match_display()} on {self.date}"

    # change the default sort 
    class Meta:
        ordering = ['-date']
