"""Free Google Translate API for Python. Translates totally free of charge."""
__all__ = 'Translator', 'AsyncTranslator',
__version__ = '4.0.0'


from aiogoogletrans.client import Translator, AsyncTranslator
from aiogoogletrans.constants import LANGCODES, LANGUAGES  # noqa
