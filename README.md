### Практическое №1. Задание.
Напишите код программы на Python, которая будет в реальном времени (с максимально возможной скоростью) считывать текущую цену фьючерса XRP/USDT на бирже Binance. 
В случае, если цена упала на 1% от максимальной цены за последний час, программа должна вывести сообщение в консоль. 
При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.
#### Решение.
Запустить скрипт данной программы можно просто обычной командой в консоли python app.py.

### Практическое №2. 
Опишите, как бы вы доработали данную программу, чтобы она обрабатывала все пары, а не только XRP/USDT (код писать не нужно, просто текстом)
#### Решение.
Можно было бы попытаться создать отдельную функцию для получения всех торгующихся на binance пар с помощью binance.client и функции get_exchange_info().
Далее, с помощью цикла for возвращать по одной торговой паре и соответственно пробовать передавать результат функции в написанную мною функцию **async def stream_kline** на место параметра symbol. Аналогично можно было бы попробовать сделать для функции, получающей текущую цену актива **get_current_price** (имеется ввиду, в key = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT" пару фьючерсов заменить результатом выполнения новой функции).
