from pyaiogoogletrans import Translator
import time

start = time.time()
translator = Translator()
text = '안녕하세요.'
text_ru = translator.translate(text, dest='ru')
print(text_ru.text, text_ru.origin)
print(f'{time.time() - start}s')
