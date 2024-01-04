from project.pokemon import Pokemon
from typing import List
class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List = []

    def add_pokemon(self, pokemon: Pokemon):
        if  pokemon.name in [pokemon.name for pokemon in self.pokemons]:
            return f'This is pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        for pokemon_name in self.pokemons:
            if pokemon_name == pokemon_name:
                self.pokemons.remove(pokemon_name)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        info = [f'Pokemon Trainer {self.name}', f'Pokemon count {len(self.pokemons)}']
        for pokemon in self.pokemons:
