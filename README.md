# Проект Pizza

Этот проект на Python реализует интерфейс командной строки (CLI) для заказа пиццы. Он позволяет пользователям просматривать доступное меню, сделать заказ и забрать его самостоятельно или с помощью курьера.

## Использование

### Просмотр меню

Для просмотра доступных видов пицц и их ингредиентов выполните команду:

```bash
python pizza.py menu
```
```
Output:
- Margherita 🍅🧀: tomato sauce, mozzarella, tomatoes
- Pepperoni 🍅🧀🍕: tomato sauce, mozzarella, pepperoni
- Hawaiian 🍅🧀🍗🍍: tomato sauce, mozzarella, chicken, pineapple
```

### Заказ пиццы

Для заказа используйте следующий формат команды:

```bash
python pizza.py order <pizza_type> <size> [--delivery]
```

Пример:

```bash
python pizza.py order Margherita L --delivery
```
```
Output:
👩‍🍳 Cooked in 53 min!
🚗 Delivered in 52 min!
```

- Замените `<pizza_type>` на выбранный вид пиццы (`Margherita`, `Pepperoni`, `Hawaiian`).
- Замените `<size>` на предпочтительный размер (`L` или `XL`). По умолчанию можно заказать пиццу размером `L`.
- Добавьте флаг `--delivery` в конце, чтобы запросить доставку курьером (необязательно).