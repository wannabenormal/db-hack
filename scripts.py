import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Commendation


def fix_marks(schoolkid):
    schoolkid.mark_set.filter(points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    schoolkid.chastisement_set.all().delete()


def create_commendation(kid_name, subject):
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

    try:
        schoolkid = Schoolkid.objects.filter(
            full_name__contains=kid_name
        ).get()
    except ObjectDoesNotExist:
        print('Ученик с таким именем не найден:', kid_name)
        return
    except MultipleObjectsReturned:
        print('Найдено несколько учеников с таким именем:', kid_name)
        return

    last_lesson = Lesson.objects.filter(
        subject__title=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    ).order_by('-date').first()

    if not last_lesson:
        print('Предмета с таким названием не найдено:', subject)

    Commendation.objects.create(
        text=random.choice(commendation_options),
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )
