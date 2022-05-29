class InfoMessage:
    """Информационное сообщение о тренировке."""
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
              f'Длительность: {self.duration} ч.; '
              f'Дистанция: {self.distance} км; '
              f'Ср. скорость: {self.speed} км/ч; '
              f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65 
    M_IN_KM = 1000
    Min_IN_Hours: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM 

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        informational_message = InfoMessage(self.__class__.__name__,
        self.duration,
        self.get_distance(),
        self.get_mean_speed(),
        self.get_spent_calories())
        return informational_message


class Running(Training):
    """Тренировка: бег."""
    coeff_cal_run1: int = 18
    coeff_cal_run2: int = 20

    def __init_(self,
                action: int,
                duration: float,
                weight: float) -> None:
        super().__init__(action, duration, weight) 


    def get_spent_calories(self) -> float:
        return ((self.coeff_cal_run1 * self.get_mean_speed() 
                - self.coeff_cal_run2) * self.weight / self.M_IN_KM 
                * self.duration * self.Min_IN_Hours) 



class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_cal_1: float = 0.035
    coeff_cal_2: float = 0.029

    def _init_(self,
               action: int,
               duration: float,
               weight: float,
               height: float
               ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return((self.coeff_cal_1 * self.weight + (self.get_mean_speed()
               **2 // self.height) * self.coeff_cal_2 * self.weight)
               * self.duration *self.Min_IN_Hours)



class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    coeff_cal_1: float = 1.1
    coeff_cal_2: float = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float, 
                 length_pool: float,
                 count_pool: float) -> None:  
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool 
				* self.count_pool 
				/ self.M_IN_KM /self.duration) 

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed()
                + self.coeff_cal_1) * self.coeff_cal_2 
                * self.weight) 


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    class_name = {
        'RUN': Running,
        'SWM': Swimming,
        'WLK': SportsWalking
    }
    return class_name.get(workout_type, data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message()) 

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)  
