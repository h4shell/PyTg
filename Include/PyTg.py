import requests


class Tg:
    def __init__(self, apiToken):
        """
        Summary line.

        Extended description of function.

        Parameters
        ----------

        token: str
            API Token di Telegram (BotFather)
        """
        self.apiToken = apiToken
        self.url = f"https://api.telegram.org/bot{apiToken}/"
        self.headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json",
        }

    def sendMessage(self, chat_id, message, inlinekeyboard):
        """
        Summary line.

        Extended description of function.

        Parameters
        ----------

        chat_id : str
            Canale Telegram dove scrivere es: "@nome_canale"
        message : str
            Messaggio da inviare
        arg3 : dict or None
            Bottone Telegram

        Return
        ------
        res : dict
        """

        if inlinekeyboard == None:
            payload = {
                "text": message,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
            }
        else:
            payload = {
                "text": message,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
                "reply_markup": inlinekeyboard,
            }

        res = requests.post(
            f"{self.url}sendMessage?chat_id={chat_id}",
            headers=self.headers,
            json=payload,
        )
        return res.json()
