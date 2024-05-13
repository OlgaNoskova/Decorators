
from functools import wraps
import datetime


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        call_time = datetime.datetime.now()
        result = old_function(*args, **kwargs)

        with open('new.log', 'w', encoding='utf-8') as f:
            f.write(f"Функция {old_function.__name__}  вызвана {call_time}.\n"
                    f"Возвращаемое значение {result[0]} ограничена первыми элементом списка.\n")
        return result

    return new_function

