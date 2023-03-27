from Include.PyTg import Tg
from creds import TOKEN


if __name__ == "__main__":
    inlinekeyboard = {
        "inline_keyboard": [[{"text": "TESTO", "url": "www.google.it/sen&"}]]
    }
    App = Tg(TOKEN)

    chat_id = input("Inserisci la chat Telegram (es: @nome_canale): ")
    txt = input("Inserisci il testo del messaggio: ")
    res = App.sendMessage(chat_id=chat_id, message=txt, inlinekeyboard=inlinekeyboard)
    print(res)
