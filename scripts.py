import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Commendation


def get_schoolkid_by_name(kid_name):
    if not kid_name:
        print('Не указано имя')
        return None

    try:
        schoolkid = Schoolkid.objects.filter(
            full_name__contains=kid_name
        ).get()
    except ObjectDoesNotExist:
        print(f'Ученик с таким именем не найден: {kid_name}')
        return None
    except MultipleObjectsReturned:
        print(f'Найдено несколько учеников с таким именем: {kid_name}')
        return None
    else:
        return schoolkid


def fix_marks(schoolkid):
    if not schoolkid:
        print('Не передан объект ученика')

    schoolkid.mark_set.filter(points__in=[2, 3]).update(points=5)
    print('Все плохие оценки заменены на 5')


def remove_chastisements(schoolkid):
    if not schoolkid:
        print('Не передан объект ученика')

    schoolkid.chastisement_set.all().delete()
    print('Все замечания удалены')


def create_commendation(schoolkid, subject):
    commendation_options = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!'
    ]

    commendation_text = random.choice(commendation_options)

    last_lesson = Lesson.objects.filter(
        subject__title=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    ).order_by('-date').first()

    if not last_lesson:
        print('Предмет с таким названием не найден:', subject)
        return

    Commendation.objects.create(
        text=commendation_text,
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )
    print(
        f'Создана похвала для {schoolkid.full_name}\n'
        f'По предмету {subject}\n'
        f'С текстом: {commendation_text}'
    )
