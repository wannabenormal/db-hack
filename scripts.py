import random

from datacenter.models import Schoolkid, Lesson, Commendation


def fix_marks(schoolkid):
    schoolkid.mark_set.filter(points__in=[2, 3]).update(points=5)
