import random
import yaml
import getpass


def read_yaml_file(path: str) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def main():
    yaml_path = './guessing_game/game_config.yaml'
    config = read_yaml_file(path=yaml_path)
    range_minimun = config['range']['minimun']
    range_maximun = config['range']['maximun']
    number_guesses = config['guesses']
    game_mode = config['mode']
    solved = False

    if game_mode == 'single':
        correct_number = random.randint(range_minimun, range_maximun)
    elif game_mode == 'multi':
        correct_number = int(getpass.getpass('Player 2 please enter a number to guess: '))
    else:
        print('incorrect chosen mode!')
        exit()

    for i in range(number_guesses):
        ans = int(input('Player 1  - Guess the number: '))

        if ans < correct_number:
            print('Too low')
        elif ans > correct_number:
            print('Too high')
        else:
            print('You got it!')
            solved = True
            break

    if not solved:
        print(f"You didn't make it, the number was {correct_number}")


if __name__ == '__main__':
    main()
