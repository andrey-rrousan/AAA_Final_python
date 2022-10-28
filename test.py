from pizza import *
from cli import *


def test_pizza_base():
    pizza = PizzaBase()
    assumed_dict_keys = ['томатный соус', 'моцарелла']
    assert list(pizza.dict().keys()) == assumed_dict_keys


def test_pepperoni():
    pizza = Pepperoni()
    assumed_dict_keys = ['томатный соус', 'моцарелла', 'пепперони']
    assert list(pizza.dict().keys()) == assumed_dict_keys


def test_margherita():
    pizza = Margherita()
    assumed_dict_keys = ['томатный соус', 'моцарелла', 'помидоры']
    assert list(pizza.dict().keys()) == assumed_dict_keys


def test_hawaiian():
    pizza = Hawaiian()
    assumed_dict_keys = ['томатный соус', 'моцарелла', 'курица', 'ананасы']
    assert list(pizza.dict().keys()) == assumed_dict_keys


def test_inequality():
    assert not Pepperoni() == Hawaiian()


def test_equality():
    assert Margherita() == Margherita()


def test_fancy_print(capsys):
    PizzaBase().fancy_print()
    out, err = capsys.readouterr()
    assert 'Основа: томатный соус🥫' in out


def test_bake(capsys):
    bake(Pepperoni())
    out, err = capsys.readouterr()
    assert '🔥Приготовили за ' in out


def test_deliver(capsys):
    deliver(Pepperoni())
    out, err = capsys.readouterr()
    assert '🛵Доставили за ' in out


def test_pickup(capsys):
    pickup(Pepperoni())
    out, err = capsys.readouterr()
    assert '👜' in out


def test_order(capsys): 
    order_base('pepperoni', False, False)
    out, err = capsys.readouterr()
    assert '🍕Заказ принят. Пепперони размера L.🍕\n' in out


def test_order_not_delivery(capsys):
    order_base('pepperoni', False, False)
    out, err = capsys.readouterr()
    assert not ('Доставили' in out)


def test_order_delivery(capsys):
    order_base('pepperoni', True, False)
    out, err = capsys.readouterr()
    assert ('Доставили' in out)


def test_order_pickup(capsys):
    order_base('pepperoni', False, True)
    out, err = capsys.readouterr()
    assert ('👜Забрали' in out)


def test_order_bigger(capsys):
    order_base('pepperoni', True, True)
    out, err = capsys.readouterr()
    assert 'Пепперони размера XL' in out


def test_order_noname(capsys):
    order_base('chicken runch', True, True)
    out, err = capsys.readouterr()
    assert 'У нас нет такой пиццы' in out


def test_menu(capsys):
    menu_base()
    out, err = capsys.readouterr()
    occurances = [string in out for string in ['Маргарита', 'Пепперони', 'Гавайская']]
    assert all(occurances)
