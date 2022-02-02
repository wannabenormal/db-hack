import random

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

    schoolkid = Schoolkid.objects.filter(full_name__contains=kid_name)[0]
    last_lesson = Lesson.objects.filter(
        subject__title=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    ).order_by('-date').first()

    Commendation.objects.create(
        text=random.choice(commendation_options),
        created=last_lesson.date,
        schoolkid=schoolkid,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )
