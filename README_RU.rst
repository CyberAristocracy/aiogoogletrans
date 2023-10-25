pyaiogoogletrans
===============

.. raw:: html

   <a href="/README.rst">en</a> ru

pyaiogoogletrans - это форк [googletrans](https://github.com/ssut/py-googletrans), отличающийся тем, что массовая загрузка выполняется асинхронно. Также добавлены асинхронные функции перевода. Основан на версии `4.0.0-rc1`.

Основное использование
---------------------

Например, такой пример в обычном синхронном варианте занимает 7 секунд, в то время как в асинхронном - 0.5 секунды.

.. code-block:: python

    from aiogoogletrans import Translator
    translator = Translator()
    text_list = ['안녕하세요.'] * 30
    translations = translator.translate(text_list, dest='ru')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)
    >> 안녕하세요 -> привет.
       안녕하세요 -> привет.
       ...

Одиночный вариант также корректен:

.. code-block:: python

    text = 'hello world'
    text_ru = translator.translate(text, src='en', dest='ru')
    print(text_ru.text)
    >> Привет, мир

Также есть асинхронный вариант функции:

.. code-block:: python

    import asyncio
    from aiogoogletrans import Translator

    loop = asyncio.get_event_loop()
    text_ru = loop.run_until_complete(translator.async_translate('안녕하세요.', src='en', dest='ru'))
    print(text_ru.text)
    >> Привет, мир
