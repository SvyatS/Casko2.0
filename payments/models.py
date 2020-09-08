from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Policyholder(models.Model):
    choicesstatus = (("Черновик", "Черновик"), ("Сохранено", "Сохранено"), ("Оплачено", "Оплачено"), ("Помечено на удаление", "Помечено на удаление"))

    status = models.CharField("Статус", max_length = 64, choices=choicesstatus, default="Черновик")

    first_name = models.CharField("Имя", max_length = 64)
    last_name = models.CharField("Фамилия", max_length = 64)
    father_name = models.CharField("Отчество", max_length = 64)

    driver_age = models.IntegerField("Возвраст")
    experience = models.IntegerField("Стаж")

    admin = models.ForeignKey(User, on_delete = models.CASCADE, unique=False)

    brand = models.CharField("Марка", max_length = 32)
    model = models.CharField("Модель", max_length = 64)
    number_of_drivers = models.IntegerField("Число водителей")
    kbm = models.FloatField("Кмб")

    date = models.DateTimeField(auto_now_add=True)

    car_year = models.IntegerField("Год выпуска")
    insurance_amount = models.IntegerField("Страховая сумма")
    class_master = models.IntegerField("Класс автомастерской")

    accident_caused_by_third_parties = models.BooleanField("ДТП по вине третьих лиц")
    accident_caused_by_drivers_of_the_insured_car = models.BooleanField("ДТП по вине водителей застрахованного ТС")
    damage = models.BooleanField("Механические повреждения")
    broken_glass = models.BooleanField("Бой стекол ТС")
    unlawful_actions_of_third_parties = models.BooleanField("Противоправние действия третьих лиц")
    hijacking = models.BooleanField("Хищение")
    total_damage = models.BooleanField("Только тотальный ущерб")

    number_of_payments = models.IntegerField("Количество платежей")
    insurance_period = models.IntegerField("Срок страхования", null=True, default=12)
    prize_kf = models.FloatField("Коэффициент соотношения выплат к премиям")
    anderright_kf = models.FloatField("Андреррайтерский коэффициент")

    insurance_liability = models.IntegerField("Страховая сумма")
    insurance_prize_osago = models.IntegerField("Страховая премия по ОСАГО")

    insurance_accident = models.IntegerField("Страховая сумма")
    insurance_places = models.CharField("Застрахованные посадочные места", max_length = 64)

    def __str__(self):
        return str(self.last_name + ' ' + self.first_name)

    class Meta:
        verbose_name = 'Страхователь'
        verbose_name_plural = 'Страхователи'
