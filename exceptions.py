"""Кастомные исключения, генерируемые приложением"""


class NotCorrectMessage(Exception):
    """Некорректное сообщение в бот, которое не удалось распарсить"""
    pass


class NotCorrectScenarioFile(Exception):
    """Некорректный файл сценария"""
    pass


class NotCorrectScenarioLinks(Exception):
    """Некорректная ссылка в сценарии"""
    pass
