from project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player) -> str:
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str) -> str:
        for index, player in enumerate(self.__players):
            if player.name == player_name:
                current_player = self.__players.pop(index)
                return current_player
        return f"Player {player_name} not found"