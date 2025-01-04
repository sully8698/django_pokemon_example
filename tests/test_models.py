from django.test import TestCase
from django.urls import reverse, resolve
from django.core.exceptions import ValidationError
from pokemon_app.models import Pokemon # import pokemon model
from move_app.models import Move
from pokemon_app.views import AllPokemon, SelectedPokemon
from move_app.views import AllMoves, SelectedMove
import json

# Create your tests here.
class pokemon_test(TestCase):
    
    def test_01_create_pokemon_instance(self):
        # Here we will create our pokemon instance
        new_pokemon = Pokemon(name="Pikachu", description='Only the best electric type pokemon in the show but NOT in the games', captured=False)
        try:
            # remember validators are not ran on our new instance until we run full_clean
            new_pokemon.full_clean()
            # here we will ensure our instance is actually created
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            # print(e.message_dict)
            #if it sends an error we want to ensure this test fails
            self.fail()
        
    def test_02_create_pokemon_with_incorrect_name_format(self):
        # we create an instance with an improper name
        new_pokemon = Pokemon(name='ch4r1z4 rd', description='Looks like a Dragon has wings, breathes fire.. but is not a dragon')
        try:
            new_pokemon.full_clean()
            # if our instance runs through the full clean and doesn't throw an error, than we
            # know our validator is not working correctly and we should fail this test 
            self.fail()

        except ValidationError as e:
            # print(e.message_dict)
            # we can ensure the correct message is inside our ValidationError
            self.assertTrue('Improper name format' in e.message_dict['name'])


class move_test(TestCase):

    def test_01_create_move_instance(self):
        new_move = Move(name='Psychic')
        try:
            new_move.full_clean()
            self.assertIsNotNone(new_move)
        except ValidationError as e:
            # print(e.message_dict)
            self.fail()

    def test_02_create_move_with_incorrect_name_and_PP(self):
        new_move = Move(name='wing 4ttack', maxPP=20, pp=25)
        try:
            new_move.full_clean()
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assertTrue(
                'Improper Format' in e.message_dict['name'] and "PP can't be higher than Max PP" in e.message_dict['__all__'])


class Test_views(TestCase):

    # We will need a client for every test, instead of re-writing  this
    # instance we can use the set up method to access the client on every
    # test by prepending it with self
    def setUp(self):
        Pokemon(name="Pikachu", description = 'Only the best electric type pokemon in the show but NOT in the games').save()
        Pokemon(name='ch4r1z4 rd', description = 'Looks like a Dragon has wings, breathes fire.. but is not a dragon').save()
        

    def test_001_get_all_pokemon(self):
        # client sends a get request to a url path by url name
        response = self.client.get(reverse('all_pokemon'))
        response_body =json.loads(response.content)
        self.assertEqual(len(response_body), 2)

    def test_002_get_a_pokemon(self):
        # client sends a get request to a url path by url name.
        response = self.client.get(reverse('selected_pokemon', args=['pikachu']))
        # since our URL has an integrated parameter, we can pass it's value through args
        response_body = json.loads(response.content)
        self.assertEqual(response_body["fields"]["name"], "Pikachu")

class Test_urls(TestCase):

    def test_001_all_pokemon(self):
        # we will resolve our url to access the information attached to the
        # url instead of seeing it's behavior
        url = resolve(reverse('all_pokemon'))
        # subTest allows us to run more than one assertion within a Test
        with self.subTest():
            # Here we will ensure the url path matches the url route
            self.assertEqual(url.route, 'api/v1/pokemon/')
        # Finally we will assert the correct view is corresponding to this endpoint
        self.assertTrue(url.func.view_class is AllPokemon)

class Test_move_views(TestCase):

    def setUp(self):
        Move(name='Splash', accuracy=25, maxPP=20, pp=60).save(),
        Move(name='Dig', accuracy=25, maxPP=20, pp=60).save()
    
    def test_001_all_moves(self):
        response = self.client.get(reverse('all_moves'))
        response_body = json.loads(response.content)
        self.assertEqual(len(response_body), 2)
    
    def test_oo2_select_a_move(self):
        response = self.client.get(reverse('selected_move', args=['dig']))
        response_body = json.loads(response.content)
        self.assertEqual(response_body["fields"]["name"], "Dig")

        