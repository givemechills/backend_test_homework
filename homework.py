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

def get_message(self) -> InfoMessage:
    """Возвращает строку сообщения."""
    return (f'Тип тренировки: {self.training_type}; '
    f'Длительность: {self.duration} ч.; '
    f'Дистанция: {self.distance} км; '
    f'Ср. скорость: {self.speed} км/ч; '
    f'Потрачено ккал: {self.calories}'
    )

class Training:
    """Базовый класс с основными свойствами и методами."""

    def __init__(self,
        action: int,
        duration: float,
        weight: float,
        training_type: str) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.training_type = training_type

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        LEN_STEP = 0.65
        M_IN_KM = 1000
        distance = self.action * LEN_STEP / M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance
        mean_speed = distance()/self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить число потраченных калорий."""
        pass 

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage (type(self).__name__,
        self.duration,
        self.get_distance(),
        self.get_mean_speed(),
        self.get_spent_calories()
        )

class Running(Training):
    """Класс беговой тренировки."""
    def get_spent_calories(self,
    weight: float,
    duration: float,
    ) -> float:
        super().__get_spent_calories__(self)
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        spent_calories = (18 * self.mean_speed - 20) * self.weight / self.M_IN_KM * self.duration
        return spent_calories()


class SportsWalking:
    """Класс спортивной ходьбы."""
    def __init__(self,
    height: float,
    action: int,
    duration: float,
    weight: float,
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> str:
        coeff_calorie_3 = 0.035
        coeff_calorie_4 = 0.029
        spent_calories = (0.035 * self.weight + (self.speed ** 2 // self.height) * 0.029 * self.weight) * self.duration
        return spent_calories


class Swimming:
    """Класс тренировки в бассейне."""
    def __init__(self, 
        lenght_pool: float,
        count_pool: int) -> None:
        super().__init__(self)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38

    def get_mean_speed(self) -> str:
        average_speed = self.lenght_pool * self.count_pool / self.M_IN_KM / self.duration
        return average_speed

    def get_spent_calories(self) -> str:
        spent_calories = (self.speed + 1.1) * 2 * self.weight
        return spent_calories

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать принятые пакеты."""
    dict_training = {'WLK' : SportsWalking,
                    'RUN' : Running,
                    'SWM' : Swimming}
    if workout_type in dict_training.keys():
        training = dict_training[workout_type](*data)
        return dict_training[workout_type]
    else:
        print('There is no such workout')

def main(training) -> Training:
    """Главная функция."""
    info = InfoMessage.show_training_info(training)
    return info
    