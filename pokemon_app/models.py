# models has many different methods we will utilize when creating our Models
from django.db import models
from move_app.models import Move
from trainer_app.models import Trainer
from django.core import validators as v
from django.core.exceptions import ValidationError
from .validators import validate_name


# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Pokemon(models.Model):
    name = models.CharField(max_length=255, validators=[validate_name])

    level = models.IntegerField(default=1)

    date_encountered = models.DateField(auto_now_add=True)

    captured = models.BooleanField(default=False)

    description = models.TextField(default="Unkown", validators=[v.MinLengthValidator(25), v.MaxLengthValidator(150)])

    moves = models.ManyToManyField(Move)

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True, related_name='pokemon_team')

    # DUNDER METHOD
    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be caught'}"

    # RAISES POKEMON'S LEVEL
    def level_up(self, new_level):
        self.level = new_level
        self.save()

    # Switches Pokemon's captured status from True to False and vise versa
    def change_caught_status(self, status):
        self.captured = status
        self.save()

    # Lets ensure the clean method checks that we can only learn 4 moves
    def clean(self):
        if self.pk is None:
            return
        if self.moves.count() > 4:  # Change the maximum number of relationships as needed
            raise ValidationError("A Pokemon can have at most 4 moves.")