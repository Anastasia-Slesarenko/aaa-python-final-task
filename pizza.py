import click
from log import log


class Pizza:
    ingredients = None
    emoji = None
    available_sizes = ["L", "XL"]

    def __init__(self, size: str = "L") -> None:
        if size not in self.available_sizes:
            raise ValueError(
                f"We have pizzas only: {', '.join(self.available_sizes)}"
                )
        self.size = size

    def dict(self) -> dict:
        recipe = {self.__class__.__name__: self.ingredients}
        return recipe

    @log("👩‍🍳 Cooked in {} min!")
    def bake(self):
        pass

    @log("🚗 Delivered in {} min!")
    def delivery(self):
        pass

    @log("🏃 Picked up in {} min!")
    def pickup(self):
        pass

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, self.__class__) and
            self.ingredients == other.ingredients and
            self.size == other.size
            )


class Margherita(Pizza):
    ingredients = ["tomato sauce", "mozzarella", "tomatoes"]
    emoji = "🍅🧀"


class Pepperoni(Pizza):
    ingredients = ["tomato sauce", "mozzarella", "pepperoni"]
    emoji = "🍅🧀🍕"


class Hawaiian(Pizza):
    ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapple"]
    emoji = "🍅🧀🍗🍍"


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Shows the menu"""
    for pizza in Pizza.__subclasses__():
        click.echo(
            f"- {pizza.__name__} {pizza.emoji}: {', '.join(pizza.ingredients)}"
        )


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1, default="L")
def order(pizza: str, size: str, delivery: bool):
    """Bakes and delivers the pizza"""
    pizza = pizza.capitalize()
    pizza_types = {cls.__name__: cls for cls in Pizza.__subclasses__()}
    if pizza not in pizza_types:
        click.echo(f"Sorry, we only have: {', '.join(pizza_types.keys())}")
    else:
        ordered_pizza = pizza_types[pizza](size=size)
        ordered_pizza.bake()
        if delivery:
            ordered_pizza.delivery()
        else:
            ordered_pizza.pickup()


if __name__ == "__main__":
    cli()
