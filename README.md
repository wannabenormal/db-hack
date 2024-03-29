# Взлом электронного дневника
Эти скрипты позволяют исправить в базе данных оценки, удалить замечания или же добавить похвалу для учеников.

## Подготовка
Файл `scripts.py` необходимо поместить в корневую директорию [электронного дневника](https://github.com/devmanorg/e-diary).

Далее необходимо зайти в Shell-интерфейс с помощью команды:
```
python manage.py shell
```
После этого необходимо выполнить:
```Python
from scripts import get_schoolkid_by_name, fix_marks, remove_chastisements, create_commendation
```

## Использование
Для всех команд необходимо будет передать объект ученика. Для получения объекта необходимо выполнить следующее:
```Python
kid = get_schoolkid_by_name('ФИО ученика')
```
Если ученик не найден или найдено несколько учеников, то выведется соответствующее сообщение.
После этого команду надо выполнить `заново` с корректными данными.

### Исправление оценок
Скрипт найдет все плохие оценки (2 и 3) и заменит их на 5.
Пример использования:
```Python
fix_marks(kid)
```
Если все выполнено корректно, скрипт выведет соответсвующее сообщение.

### Удаление замечаний
Скрипт найдет все замечания для ученика и удалит их.
Пример использования:
```Python
remove_chastisements(kid)
```
Если все выполнено корректно, скрипт выведет соответсвующее сообщение.

### Добавление похвалы
Скрипт создаст похвалу для ученика по последнему уроку выбранного предмета.
Пример использования:
```Python
create_commendation(kid, 'Математика')
```
Если все выполнено корректно, скрипт выведет соответсвующее сообщение.
Если скрипту не удастся найти указанный предмет, он сообщит об этом в консоль.