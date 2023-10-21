pyaiogoogletrans
===========

[en](/README.rst) ru

pyaiogoogletrans - является форком [googletrans](https://github.com/ssut/py-googletrans), отличие заключается в том, что массовая загрузка выполняется асихронно. А также добавлены ассихронные функции перевода. 
Онована на версии `4.0.0-rc1`.

Основное использование
---------

Например, такой пример в обычном сихронном варианте занимает 7 секунд, когда как в ассихронном 0.5 сек.

```python
from aiogoogletrans import Translator
translator = Translator()
text_list = ['안녕하세요.'] * 30
translations = translator.translate(text_list, dest='ru')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
>> 안녕하세요 -> привет.
   안녕하세요 -> привет.
   ...
```

Одиночный вариант также корректен: 

```python
text = 'hello world'
text_ru = translator.translate(text, src='en', dest='ru')
print(text_ru.text)
>> Привет, мир
```

Также есть ассихронный вариант функции:

```python
import asyncio
from aiogoogletrans import Translator

loop = asyncio.get_event_loop()
text_ru = loop.run_until_complete(translator.async_translate('안녕하세요.', src='en', dest='ru'))
print(text_ru.text)
>> Привет, мир
```

