# from collections.abc import Iterable, Iterator


class ExemploIterable():
    def __init__(self, players_names: list):
        self.players = [print(player_name) for player_name in players_names]

    def __iter__(self):
        return ExemploIterable(self.players)


class ExemploIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        try:
            result = self.iterable[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return result


ExemploIterable(['Declan Rice', 'Jude Bellingham',
                 'Kalvin Phillips', 'Jordan Henderson'])
