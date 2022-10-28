import click
from pizza import Pepperoni, Margherita, Hawaiian
from random import randint


def log(string='Выполнено за {}с!'):
    """
    Декоратор для вывода времени выполнения операции.
    В данном случае выдает случайное число от 1 до 30.
    """
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(string.format(randint(1, 30)))
        return wrapper
    return log_decorator


@log('🔥Приготовили за {}c!🔥')
def bake(pizza):
    """
    Тут должна быть внутренняя логика приготовления.
    """
    pass


@log('🛵Доставили за {}с!🛵')
def deliver(pizza):
    """
    Тут должна быть внутренняя логика доставки.
    """
    pass


@log('👜Забрали за {}с!👜')
def pickup(pizza):
    """
    Тут должна быть внутренняя логика самовывоза.
    """
    pass


@click.group()
def cli():
    pass


PIZZA_NAMES = {
    'pepperoni': Pepperoni,
    'margherita': Margherita,
    'hawaiian': Hawaiian
}


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--bigger', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, bigger: bool):
    """
    Подфункция для независимой работы click-интерфейса и самой функции.
    Для рассмотрения функционала см. order_base.
    Флаг --delivery заказывает доставку.
    Флаг --bigger заказывает пиццу XL размера.
    pizza принимает один из трех аргуументов:
    pepperoni, margherita, hawaiian.
    """
    order_base(pizza, delivery, bigger)


def order_base(pizza: str, delivery: bool, bigger: bool):
    """Готовит и доставляет пиццу"""
    size = 'XL' if bigger else 'L'
    try:
        pizza_order = PIZZA_NAMES[pizza.lower()](size)
    except KeyError:
        print('У нас нет такой пиццы, пожалуйста, выберите пиццу из меню.')
        return
    print(f'🍕Заказ принят. {pizza_order.name} размера {pizza_order.size}.🍕')
    bake(pizza_order)
    if delivery:
        deliver(pizza_order)
    else:
        pickup(pizza_order)


@cli.command()
def menu():
    """
    Подфункция для независимой работы click-интерфейса и самой функции.
    Для рассмотрения функционала см. menu_base.
    """
    menu_base()


def menu_base():
    """Выводит меню"""
    for pizza in [Margherita(), Pepperoni(), Hawaiian()]:
        pizza.fancy_print()


if __name__ == '__main__':
    cli()
