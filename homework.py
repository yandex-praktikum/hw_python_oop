from statistics import mean
from tokenize import Floatnumber


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = round(duration, 3)
        self.distance = round(distance, 3)
        self.speed = round(speed, 3)
        self.calories = round(calories, 3)

    def get_message(self) -> str:
        message = (f"Тип тренировки: {self.training_type}; "
                   f"Длительность: {self.duration}; "
                   f"Дистанция: {self.distance}; "
                   f"Ср. скорость: {self.speed} км/ч; "
                   f"Потрачено ккал: {self.calories}.")
        return message


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
        self.M_IN_KM: int = 1000
        self.LEN_STEP: float = 0.65

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        self.distance = distance
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.distance / self.duration
        self.mean_speed = mean_speed
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
    
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        spent_calories = ((coeff_calorie_1 * self.mean_speed - coeff_calorie_2) * 
                            self.weight / self.M_IN_KM * self.duration)
        self.spent_calories = spent_calories
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
    
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        spent_calories = ((coeff_calorie_1 * self.weight + (self.mean_speed ** 2 // self.height)
                            * coeff_calorie_2 * self.weight) * self.duration)
        self.spent_calories = spent_calories
        return spent_calories

    


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float,
                 lenght_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38
    
    def get_mean_speed(self) -> float:
        mean_speed = (self.lenght_pool * self.count_pool / self.M_IN_KM
                        / self.duration)
        self.mean_speed = mean_speed
        return mean_speed
    
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        spent_calories = (self.mean_speed + 1.1) * 2 * self.weight
        self.spent_calories = spent_calories
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
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
