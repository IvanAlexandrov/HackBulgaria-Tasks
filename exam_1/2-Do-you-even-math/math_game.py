import random
import database as db


class MathGame(object):

    NUMBERS = [x for x in range(1, 11)]

    def __init__(self):
        self.n = 0
        self.scores = 0

    def get_question(self):
        op = random.choice('+-*/')
        first_number = random.choice(MathGame.NUMBERS)
        second_number = random.choice(MathGame.NUMBERS)
        self.question = str(first_number) + op + str(second_number)
        self.n += 1

        return self.question

    def is_correct(self, answer):

        # spooky test for user cheating, because using eval function
        if self.question == answer:
            return False

        elif answer == '':
            return False

        elif eval(self.question) == eval(answer):
            return True

        return False

    def score(self, n):
        self.scores = self.n * n

    def get_scores(self):
        return self.scores


def help():
    print('\nWelcome to \'Do you even math?\' game!')
    print('Here are your options:')
    print(' - start')
    print(' - highscores')


def end_game(math):
    print('Incorrect! Ending game. Your score is: ' + str(math.get_scores()))
    main()


def main():
    help()
    db.Math()
    command = input('?>')
    player = ''
    if command == 'start':
        player = input('Enter your player name>')
        print('Welcome ' + player + '! Let the game begin!')
        n = 0
        math = MathGame()
        while True:
            n += 1
            print('Question #' + str(n) + ":")
            print()
            print('What is the answer to ' + str(math.get_question()))
            answer = input('?> ')
            if math.is_correct(answer):
                print('Correct!')
                math.score(n)
            else:
                player1 = db.Math(player_name=player,
                                  scores=math.get_scores())
                db.session.add(player1)
                db.session.commit()
                end_game(math)
                n = 0
                help()

    elif command == 'highscores':
        print('\nThis is the current TOP 10:\n')
        top_10 = db.session.query(db.Math.player_name, db.Math.scores).\
            order_by(db.Math.scores.desc()).limit(10)
        for i, one in enumerate(top_10):
            print('{}. \t{} with {} points'.
                  format(str(i+1), one.player_name, one.scores))

        main()

    else:
        exit()

if __name__ == '__main__':
    main()
