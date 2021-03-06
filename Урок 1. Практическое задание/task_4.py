"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


class user_info:
    def __init__(self, user_id, login, password, is_activated):
        self.user_id = user_id
        self.login = login
        self.password = password
        self.is_activated = is_activated


users = [user_info(1, "login1", 'password1', False),
         user_info(2, "login2", 'password2', False),
         user_info(3, "login3", 'password3', False),
         user_info(4, "login4", 'password4', False)]

user_name_map = dict()
for user in users:
    user_name_map[user.login] = user

while True:
    while True:
        input_string = input('Введите логин пользователя > ')
        login = (input_string if input_string is not None else '').strip()
        user = user_name_map.get(login)
        if user is None:
            print(f"Пользователь '{login}' не найден")
            continue
        break
    if user.is_activated == True:
        print('Допуск к ресурсу есть')
    while True:
        if input('Введите 1 для активации > ') == '1':
            user.is_activated = True
            print(f"Пользователь '{user.login}' активирован и может войти в систему.")
            break
    while True:
        password = input('Введите пароль:')
        if password == user.password:
            print(f'Пользователь успешно авторизован')
            break
        else:
            print(f'Неверный пароль')
    break

# Сложность алгоритма - O(1)
# Очевидно выбираем алгоритм с наименее растущей функцией сложности.
