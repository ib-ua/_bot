import sys
from .bot import Bot


def main():
    if len(sys.argv) >= 2:
        bot = Bot(sys.argv[1])
    else:
        bot = Bot()
    bot.start()


if __name__ == "__main__":
    main()
