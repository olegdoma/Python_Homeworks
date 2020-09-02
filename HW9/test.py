class NotNameError(Exception):
    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


class NotEmailError(Exception):
    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


def chek_line(line):
    # print(f'Читаем строку {line}', flush=True)
    name, email, age = line.split(' ')
    # name = str(name)
    # email = str(email)
    age = int(age)
    if len(line) < 3:
        print(f'Не хватает данных в строке {line}')
    elif not name.isalpha():
        raise NotNameError(f'Ошибка в имени в строке {line}')
    elif not email.__contains__('@') or not email.__contains__('.'):
        raise NotEmailError(f'Неверный формат email в строке {line}')
    elif not 10 < age < 99:
        print(f'Возраст указан неверно в строке {line}')
    else:
        return True


with open('test.txt', "r", encoding="utf-8") as file:
    for line in file:
        try:
            if chek_line(line):
                with open('registrations_good.log', "a", encoding="utf-8") as file2:
                    file2.write(line)
            else:
                with open('registrations_bad.log', "a", encoding="utf-8") as file2:
                    file2.write(line)
        except (ValueError, NotNameError, NotEmailError):
            with open('registrations_bad.log', "a", encoding="utf-8") as file2:
                file2.write(line)
                print('Ошибка данных')