aiogoogletrans
===========

[en](/README.rst) ru

aiogoogletrans is a fork of [googletrans](https://github.com/ssut/py-googletrans), the difference is that bulk loading is performed asynchronously. Asynchronous translation functions have also been added.
Based on version `4.0.0-rc1`.

Basic Usage
---------

For example, such an example in the usual synchronous version takes 7 seconds, when in the asynchronous version it takes 0.5 seconds.

```python
from pyaiogoogletrans import Translator
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
from pyaiogoogletrans import Translator

loop = asyncio.get_event_loop()
text_ru = loop.run_until_complete(translator.async_translate('안녕하세요.', src='en', dest='ru'))
print(text_ru.text)
>> Привет, мир
```

