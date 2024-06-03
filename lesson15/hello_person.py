import argparse


def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }

    message = f"{greetings[lang]} {name}"
    print(message)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", dest="firstname",
        required=True, help="The name of the person"
    )

    parser.add_argument(
        "-l", "--lang", metavar="lang", dest="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting"
    )

    args = parser.parse_args()
    hello(args.firstname, args.language)


if __name__ == "__main__":
    parse_args()
