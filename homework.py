class InfoMessage:
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')
    """Информационное сообщение о тренировке."""
    pass


class Training:
    LEN_STEP = 0.65
    M_IN_KM = 1000
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.LEN_STEP = 0.65
        self.action = action
        self.duration = duration
        self.weight = weight
        self.M_IN_KM = 1000
        pass

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM
        """Получить дистанцию в км."""
        pass

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
        """Получить среднюю скорость движения."""
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)
        self.LEN_STEP = 0.65
        self.coeff_calorie_1 = 18
        self.coeff_calorie_2 = 20
        self.M_IN_KM = 1000
        self.minut = 60

    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.get_mean_speed()
                - self.coeff_calorie_2) * self.weight / self.M_IN_KM
                * self.duration * self.minut)
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: float):
        super().__init__(action, duration, weight)
        self.height = height
        self.weight = weight
        self.LEN_STEP = 0.65
        self.coeff_calorie_1 = 0.035
        self.coeff_calorie_2 = 0.029

    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.weight
                 + (self.get_mean_speed() ** 2 // self.height)
                 * 0.029 * self.weight) * self.duration * 60)
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    LEN_STEP = 1.38

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.weight = weight
        self.M_IN_KM = 1000
        self.coeff_calorie_1 = 1.1
        self.coeff_calorie_2 = 2
        self.LEN_STEP = 1.38

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.coeff_calorie_1)
                * self.coeff_calorie_2 * self.weight)
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    Dikt = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    return Dikt[workout_type](*data)
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    info = training.show_training_info()
    print(info.get_message())
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
