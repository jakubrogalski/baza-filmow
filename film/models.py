from django.db import models
from django.core.urlresolvers import reverse

class Film(models.Model):

    CHOICE_GENRE = (
        ('Akcja', 'Akcja'),
        ('Animowany', 'Animowany'),
        ('Biograficzny', 'Biograficzny'),
        ('Dokumentalny', 'Dokumentalny'),
        ('Dramat', 'Dramat'),
        ('Familijny', 'Familijny'),
        ('Fantasy', 'Fantasy'),
        ('Gangsterski', 'Gangsterski'),
        ('Historyczny', 'Historyczny'),
        ('Horror', 'Horror'),
        ('Katastroficzny', 'Katastroficzny'),
        ('Komedia', 'Komedia'),
        ('Kryminal', 'Kryminal'),
        ('Melodramat', 'Melodramat'),
        ('Muzyczny', 'Muzyczny'),
        ('Obyczajowy', 'Obyczajowy'),
        ('Polityczny', 'Polityczny'),
        ('Prawniczy', 'Prawniczy'),
        ('Przygodowy', 'Przygodowy'),
        ('Psychologiczny', 'Psychologiczny'),
        ('Science fiction', 'Science fiction'),
        ('Sensacyjny', 'Sensacyjny'),
        ('Sportowy', 'Sportowy'),
        ('Szpiegowski', 'Szpiegowski'),
        ('Sztuki walki', 'Sztuki walki'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),
        ('Wojenny', 'Wojenny'),
    )

    CHOICE_GENRE2 = (
        ('---------', '---------'),
        ('Akcja', 'Akcja'),
        ('Animowany', 'Animowany'),
        ('Biograficzny', 'Biograficzny'),
        ('Dokumentalny', 'Dokumentalny'),
        ('Dramat', 'Dramat'),
        ('Familijny', 'Familijny'),
        ('Fantasy', 'Fantasy'),
        ('Gangsterski', 'Gangsterski'),
        ('Historyczny', 'Historyczny'),
        ('Horror', 'Horror'),
        ('Katastroficzny', 'Katastroficzny'),
        ('Komedia', 'Komedia'),
        ('Kryminal', 'Kryminal'),
        ('Melodramat', 'Melodramat'),
        ('Muzyczny', 'Muzyczny'),
        ('Obyczajowy', 'Obyczajowy'),
        ('Polityczny', 'Polityczny'),
        ('Prawniczy', 'Prawniczy'),
        ('Przygodowy', 'Przygodowy'),
        ('Psychologiczny', 'Psychologiczny'),
        ('Science fiction', 'Science fiction'),
        ('Sensacyjny', 'Sensacyjny'),
        ('Sportowy', 'Sportowy'),
        ('Szpiegowski', 'Szpiegowski'),
        ('Sztuki walki', 'Sztuki walki'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),
        ('Wojenny', 'Wojenny'),
    )

    CHOICE_WHERE = (
        ('Dysk', 'Dysk'),
        ('Netflix', 'Netflix'),
    )

    tytul = models.CharField(max_length=500)
    gatunek = models.CharField(max_length=20, choices=CHOICE_GENRE)
    gatunek2 = models.CharField(max_length=20, choices=CHOICE_GENRE2, default='1')
    gatunek3 = models.CharField(max_length=20, choices=CHOICE_GENRE2, default='1')
    rok = models.IntegerField(null=True, default=2000)
    nota = models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=10, default=7.5)
    gdzie = models.CharField(max_length=8, choices=CHOICE_WHERE, default=1)

    def get_absolute_url(self):
        return reverse('film:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.tytul + " - " + self.gatunek + " - " + self.gdzie