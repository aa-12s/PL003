
# Способы вызова функции& Задача "Рассылка писем"


def send_email(message, recipient, sender='university.help@gmail.com'):
    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        list_ = ('.com', '.ru', '.net')
        if not recipient.endswith(list_) or not sender.endswith(list_):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('message', 'vasyok1337@gmail.com')
send_email('message', 'urban.fan@mail.ru')
send_email('message', 'urban.student@mail.ru')
send_email('message', 'university.help@gmail.com')










