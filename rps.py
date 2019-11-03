import random
instructions = """
Welcome to Rock, Paper, Scissors, Lizard, Spock.
First, you will choose players 1 and 2,
then you will select the number of rounds to play.
You may choose from the following players:
  Human: Are you a human? then you should control the moves, eh?
  Rocker: a computer that believes that rocks are the best.
  Randomizer: a computer who can randomly defeat you (or not?)
  Reflecter: a computer who copies your moves.
  Cycler: a computer who cycles through
  rock, paper, scissors, lizard, and spock in order.
  You can type \'q\' or press ctrl+C to quit the game anytime."""
moves = ('rock', 'paper', 'scissors', 'lizard', 'spock')

# defining classes:


class Player:
    def __init__(self):
        self.score = 0
        self.my_move = Player.move(self)
        self.their_move = Player.move(self)

    def move(self):
        pass
        return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RockerPlayer(Player):
    def move(self):
        return moves[0]


class RandomPlayer(Player):
    def move(self):
        return moves[random.randint(0, 4)]


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        index = moves.index(self.my_move) + 1
        if index >= len(moves):
            index = 0
        self.my_move = moves[index]
        return self.my_move


class HumanPlayer(Player):
    def move(self):
        human_move = verify_input(
            """Please choose your move.
            What\'s your move?
            rock, paper, scissors, lizard, or spock?
            Press enter to proceed.""",
            moves,
            0)
        return human_move


def beats(one, two):
    return ((one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'rock' and two == 'lizard') or
            (one == 'lizard' and two == 'spock') or
            (one == 'spock' and two == 'scissors') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'lizard' and two == 'paper') or
            (one == 'paper' and two == 'spock') or
            (one == 'spock' and two == 'rock') or
            (one == 'rock' and two == 'scissors'))


def verify_input(message, list, string_or_int):
    # input function with KeyboardInturrupt error handling.
    entry = None
    # string_or_int takes 0 for strings, 1 for integers.
    while True:
        try:
            if string_or_int == 0:
                entry = input(message).lower()
                if entry == 'q':
                            print('Thanks for playing')
                            exit()
                elif entry not in list:
                        print('Oops! Try again.')
                        continue
                break
            elif string_or_int == 1:
                try:
                    entry = int(input(message))
                    if entry == 0:
                        print('Thanks for playing')
                        exit()
                    break
                except ValueError:
                        print('Envalid number. Please try again.')
                        continue
        except KeyboardInterrupt:
            print('Thanks for playing.')
            exit()
    return entry


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_match(self):
        rounds = verify_input("""Enter the number of rounds you want to play,
        or enter 0 to exit.""", None, 1)
        for round in range(1, rounds + 1):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(
                f"""Player 1 Won!
        Final score:
        Player 1 | Player 2
           {self.p1.score}          {self.p2.score}""")
        elif self.p2.score > self.p1.score:
            print(
                f"""Player 2 won!
                Final Score:
        Player 1 | Player 2
           {self.p1.score}          {self.p2.score}""")
        else:
            print(
                f"""It\'s a draw,
                no one won this time.
                Final Score:
        Player 1 | Player 2
           {self.p1.score}          {self.p2.score}""")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 played {move1},\nplayer 2 played {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            motivate = game.motivate('p1')
            print(motivate)
        elif beats(move2, move1):
            self.p2.score += 1
            motivate = game.motivate('p2')
            print(motivate)
        else:
            print('Draw!')
        print(f"""Score:
        Player 1 | Player 2
           {self.p1.score}          {self.p2.score}""")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    @classmethod
    def motivate(cls, player):
        index = 0
        if player is 'p1':
            list = (
                """Player 2 is so angry that he\'s smashing his computer
                screen. But alas, he will never catch you""",
                'Oh yea, that\'s what I\'m talking about player 1!',
                'You are the greatest player on earth my friend!',
                """I hear some screaming!
                Perhaps it\'s player 2\'s angry shouts?""",
                'Man! YOU ROCK!',
                """I love when you win!
                Here\'s to some more  winnings in your future""")
        elif player is 'p2':
            list = (
                'Are you gonna continue losing like that?',
                """Fine, keep this up,
                and you will never get invited to play internationally""",
                """I wish that I have bet on you losing,
                cause I was gonna get a lot of money!""",
                'More losses, YEAY',
                'You will never win if you continued playing like that!')
        index = random.randint(0, len(list) - 1)
        return list[index]


if __name__ == '__main__':
    print(instructions)
    p1 = {
        'human': HumanPlayer(),
        'rocker': RockerPlayer(),
        'randomizer': RandomPlayer(),
        'reflecter': ReflectPlayer(),
        'cycler': CyclePlayer()}
    p2 = {
        'human': HumanPlayer(),
        'rocker': RockerPlayer(),
        'randomizer': RandomPlayer(),
        'reflecter': ReflectPlayer(),
        'cycler': CyclePlayer()}
    player1 = verify_input('Who is player 1?', p1, 0)
    player2 = verify_input('Who is player 2?', p2, 0)
    player1 = p1[player1]
    player2 = p2[player2]
    game = Game(player1, player2)
    game.play_match()
