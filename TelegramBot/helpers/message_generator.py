import random
from TelegramBot.logging import LOGGER

MESSAGES = [
  "GPT-4o уже пишет код, тестирует и увольняет — вы уже подали резюме в службу поддержки AI?",
  "AI теперь не только пишет баги, но и объясняет, почему это фича — кто сталкивался?",
  "Нейросети стали настолько умными, что начали жаловаться на дедлайны — вы видели это в проде?",
  "Кто уже заменил своего тимлида на LLM?",
  "AI везде: в коде, в кофе, в холодильнике — что ещё осталось людям?",
  "Хакеры используют AI для атак — вы уже защищаетесь AI от AI?",
  "Ransomware-as-a-Service — кто уже получил первый инвойс?",
  "Вам тоже пришло фишинговое письмо, идеально написанное GPT?",
  "Безопасность — это ещё про код или уже про эзотерику?",
  "Кто до сих пор использует пароль '123456' в 2025-м?",
  "Ваше облако тоже стало таким тяжёлым, что не помещается в бюджет?",
  "Сервер упал — это плановая медитация или незапланированная катастрофа?",
  "Вы когда-нибудь чувствовали себя и DevOps, и поджигателем одновременно?",
  "CI/CD когда-нибудь обновлял прод без вашего ведома?",
  "Вы тоже подозреваете, что \"облако\" — это просто чей-то старый ноутбук?",
  "Код может быть зелёным в плане экологии — вы уже пробовали?",
  "Серверы греют офис — это инновация или отчаяние?",
  "Ваш код когда-нибудь спасал деревья или только нервы?",
  "Вы пробовали заменить кофе на солнечную энергию?",
  "Ваш код настолько чистый, что его можно компостировать?",
  "Инженеры AI стали пессимистами — у вас на работе тоже так?",
  "Вы уже учитесь у AI, который учится у вас?",
  "Получали ли вы сертификацию от AI, который вас потом собеседовал?",
  "Кто-нибудь понял, как выбраться из замкнутого цикла обучения AI?",
  "Карьера в IT от джуна до ассистента AI за 3 месяца — это реально?",
  "TikTok знает о вас больше, чем вы — кто ещё почувствовал это?",
  "Алгоритмы рекомендуют отдых от самих себя — вы послушались?",
  "Ваши посты в соцсетях лайкают боты — это уже норма?",
  "Сравниваете ли вы свою жизнь с чужой постановкой в LinkedIn?",
  "Пробовали цифровую детоксикацию — как ощущения без Wi-Fi?",
  "Код — это поэзия? Тогда кто наш Бунин?",
  "Баг — это фича или просто плохой PR?",
  "Когда последний раз у вас тесты проходили с первого раза?",
  "Вы когда-нибудь успевали понять систему до того, как её обновили?",
  "Решали ли вы когда-нибудь несуществующие проблемы с нестабильными решениями?",
  "Вы когда-нибудь ломали систему, чтобы её понять?",
  "Если работает — стоит ли вообще признавать, что вы трогали?",
  "Вы тоже заметили, что 'временно' — это самый надёжный план?",
  "Говорили ли вы \"легкий баг\" вслух и потом жалели?",
  "Вы когда-нибудь чувствовали себя в IT как шаман с ноутбуком?"
]

async def generate_message() -> str:
    """
    Генерирует случайное сообщение из предустановленного списка.
    """
    try:
        message = random.choice(MESSAGES)
        LOGGER(__name__).info(f"Сгенерировано сообщение: {message}")
        return message
    except Exception as e:
        LOGGER(__name__).error(f"Ошибка при генерации сообщения: {e}")
        return "Эй, народ! Давайте пообщаемся! 🤖" 
