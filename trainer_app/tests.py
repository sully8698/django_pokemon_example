from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Trainer
from pokemon_app.models import Pokemon

# Create your tests here.
class trainer_test(TestCase):

    def test_01_create_trainer_instance(self):
            # Here we will create our pokemon instance
            new_trainer = Trainer(name="Ash", age=10)
            try:
                # remember validators are not ran on our new instance until we run full_clean
                new_trainer.full_clean()
                # here we will ensure our instance is actually created
                self.assertIsNotNone(new_trainer)
            except ValidationError as e:
                # print(e.message_dict)
                #if it sends an error we want to ensure this test fails
                self.fail()

    def test_02_pokemon_relationship(self):
        new_trainer = Trainer(name="Ash", age=10)
        new_trainer.save()
        new_pokemon = Pokemon(name="Pikachu", description='Only the best electric type pokemon in the show but NOT in the games', captured=False, trainer = new_trainer)
        new_pokemon.save()

        self.assertEqual(new_trainer.pokemon_team.count(), 1)
        self.assertEqual(new_trainer.pokemon_team.first(), new_pokemon)
