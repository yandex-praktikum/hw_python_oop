class InfoMessage:
    """Информационное сообщение о тренировке."""
   
    
    def __init__(self,      #Определили состав класса "Cообщение" 
                training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float,
                ) -> None:
         self.training_type=training_type
         self.duration=duration
         self.distance=distance
         self.speed=speed
         self.calories=calories 
         
    def get_message(self) -> str:    #класс создан ради этого метода, который им печатает сам себя.
        return (f'Тип тренировки: {self.training_type} \n'
                f'Длительность: {self.duration} ч.\n'
                f'Дистанция: {self.distance} км\n'
                f'Ср. скорость: {self.speed} км/ч\n'
                f'Потрачено ккал: {self.calories}.\n'
                '')
         

class Training:
    """Базовый класс тренировки."""   #Класс можно было создать сразу Runing, а в Swiming и SportsWalking добавлять тоже что и добавлялось.
    
    
    LEN_STEP: float = 0.65
    TRAINING_TYPE: str = ''

    def __init__(self,
                 action: int, #число шагов, гребков, гребки почему-то не используются, хотя могли бы.
                 duration: float,
                 weight: float, #вес для расчета калорий  
                 ) -> None:
         self.action=action
         self.duration=duration
         self.weight=weight

         
    def get_distance(self) -> float:          #ниже простейшие аривметические методы
         """Получить дистанцию в км."""
         
         
         distance = self.action * self.LEN_STEP / 1000 
         return distance
     
    def get_mean_speed(self) -> float:
         """Получить среднюю скорость движения."""
        
        
         speed = self.get_distance() / self.duration
         return speed
      
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
                
        pass

    def show_training_info(self) -> InfoMessage:                        #метод создающий объект класса InfoMessage из данных, созданных выше
        """Вернуть информационное сообщение о выполненной тренировке."""
        

        info_message = InfoMessage(self.TRAINING_TYPE,      
                                   self.duration,
                                   self.get_distance(),
                                   self.get_mean_speed(),
                                   self.get_spent_calories())
        return info_message


class Running(Training):                                #ниже создание трех дочерних классов с дополнительными параметрами и расчет калорий
    """Тренировка: бег."""
    
    
    TRAINING_TYPE = 'RUN'


    def get_spent_calories(self) -> float:
        COEF_1 = 18
        COEF_2 = 20

        calories = (COEF_1 * self.get_mean_speed() - COEF_2) * self.weight / 1000 * self.duration * 60
        
        return calories
    
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    
    
    TRAINING_TYPE = 'WLK'
   
    
    def __init__(self, action, duration, weight, height: int) -> None:
        super().__init__(action, duration, weight)
        self.height = height

        
    def get_spent_calories(self) -> float:
        COEF_3 = 0.035
        COEF_4 = 0.029

        calories = (COEF_3 * self.weight + (self.get_mean_speed()**2 / self.height) * COEF_4 *self.weight) * self.duration * 60
            
        return calories
        
class Swimming(Training):
    """Тренировка: плавание."""
    
    TRAINING_TYPE = 'SWM'


    def __init__(self, action, duration, weight, lenght_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    
    def get_distance(self) -> float:
         """Получить дистанцию в км."""
         
         
         distance = (self.lenght_pool * self.count_pool) / 1000
         return distance   
    
    def get_mean_speed(self) -> float:
         """Получить среднюю скорость плавания по бассейну."""
        
        
         speed = self.get_distance() / self.duration
         return speed

    def get_spent_calories(self) -> float:

        COEF_5 = 1.1
        COEF_6 = 2
        calories = (self.get_mean_speed() + COEF_5) * COEF_6 * self.weight
            
        return calories


def read_package(workout_type: str, data: list) -> Training:       #функция принимает строку с кодом тренировки и список данных с датчика
    """Прочитать данные полученные от датчиков."""
    
    clasess_nicks = {'RUN': Running,
                    'WLK': SportsWalking,
                    'SWM': Swimming}
    
    params: list = data
    trenka = clasess_nicks[workout_type](*params)  #переменной trenka присваивается объект класса, взятого из словаря по коду
                                                   # данные датчика в скобках "разворачиваются" в соответсвующий список по команде "*"    
    return trenka 




def main(training: Training) -> None:
    """Главная функция."""
    mess = training.show_training_info() #show_training_info создает экземляр класса InfoMessage
    print(mess.get_message())            #...и он печатает сам себя своим методом get_message()



if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)  #цикл в цикле создает экземпляр дочерей класса trening с помощью read_package
        main(training)
