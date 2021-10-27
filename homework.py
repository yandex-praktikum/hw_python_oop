from typing import Union


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {workout_type}; Длительность: {self.duration:.3f}; ч.; '
                f'Дистанция: {self.distance:.3f} км; Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}'
                )


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.len_step = 0.65
        self.m_in_km = 1000

    def info(self):
        print(self.weight)

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return (self.action * self.len_step
                / self.m_in_km)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.action * self.len_step
                / self.m_in_km
                / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        return InfoMessage('qwe', self.duration, self.get_distance(),
                           self.get_mean_speed(), self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        v_mid = self.get_mean_speed()
        w = self.weight
        t = self.duration*60
        return (18*v_mid-20)*w/self.m_in_km*t


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = 160  # Откуда 160?

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        a1 = 0.035
        a2 = 0.029
        w = self.weight
        h = self.height
        v_mid = self.get_mean_speed()
        t = self.duration*60
        return (a1 * w + (v_mid**2 // h) * a2 * w) * t


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.len_step = 1.38
        self.lenght_pool = 5
        self.count_pool = 4

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.lenght_pool
                * self.count_pool
                / self.m_in_km
                / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        v_mid = self.get_mean_speed()
        w = self.weight
        a1 = 1.1
        return (v_mid + a1) * 2 * w


def read_package(workout_type: str, data: list) -> Union[Running, SportsWalking, Swimming]:
    """Прочитать данные полученные от датчиков."""
    training_type_dict: dict = {'SWM': Swimming,
                                'RUN': Running,
                                'WLK': SportsWalking
                                }

    if workout_type == 'RUN':
        running_class = training_type_dict[workout_type]
        action, duration, weight = data
        training_object = running_class(action, duration, weight)
        training_object.training_type = workout_type  # +
    elif workout_type == 'WLK':
        walking_class = training_type_dict[workout_type]
        action, duration, weight, height = data
        training_object = walking_class(action, duration, weight, height)
        training_object.training_type = workout_type
    elif workout_type == 'SWM':
        swimming_class = training_type_dict[workout_type]
        action, duration, weight, length_pool, count_pool = data
        training_object = swimming_class(action, duration, weight, length_pool, count_pool)
        training_object.training_type = workout_type
    else:
        raise RuntimeError('Неизвестный тип тренировки.')

    return training_object


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(InfoMessage.get_message(info))


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

