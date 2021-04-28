#!/usr/bin/env python3

import click


@click.command()
@click.argument(
    "name",
    default="World",
)
@click.option(
    "-f",
    "--formal",
    is_flag=True,
    help="Increase the formality of the greeting",
)
def main(name, formal):  # pragma: no cover
    """Greet a person or entity by NAME

    NAME is the name of the persom or entity you wish to greet. If not provided
    we'll greet the whole world!"""
    print(make_greeting(name, formal))


def make_greeting(name, formality):
    return (
        "Greetings and felicitations, {}!".format(name)
        if formality
        else "Hello, {}!".format(name)
    )


if __name__ == "__main__":
    # Ignored missing parameter lint, since the click library passes the
    # arguments in from the command line for us
    main() # pylint:disable=no-value-for-parameter
