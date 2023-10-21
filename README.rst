pyaiogoogletrans
===============
:ref:`Russian Version </path/to/README_RU.rst>`

pyaiogoogletrans - is a fork of `googletrans <https://github.com/ssut/py-googletrans>`_, the difference is that bulk loading is performed asynchronously. Asynchronous translation functions have also been added.
Based on version `4.0.0-rc1`.

Main Use
--------

For example, such an example in the usual synchronous version takes 7 seconds, when in the asynchronous version it takes 0.5 seconds.

.. code-block:: python

    from aiogoogletrans import Translator
    translator = Translator()
    text_list = ['안녕하세요.'] * 30
    translations = translator.translate(text_list, dest='ru')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)

    # Output:
    # >> 안녕하세요 -> привет.
    #    안녕하세요 -> привет.
    #    ...

The single option is also correct:

.. code-block:: python

    text = 'hello world'
    text_ru = translator.translate(text, src='en', dest='ru')
    print(text_ru.text)

    # Output:
    # >> Привет, мир

There is also an asynchronous version of the function:

.. code-block:: python

    import asyncio
    from aiogoogletrans import Translator

    loop = asyncio.get_event_loop()
    text_ru = loop.run_until_complete(translator.async_translate('안녕하세요.', src='en', dest='ru'))
    print(text_ru.text)

    # Output:
    # >> Привет, мир
