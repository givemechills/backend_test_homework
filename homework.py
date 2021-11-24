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
    """Возвращает строку сообщения."""
    return (f'Тип тренировки: {self.training_type}; '
            f'Длительность: {self.duration} ч.; '
            f'Дистанция: {self.distance} км; '
            f'Ср. скорость: {self.speed} км/ч; '
            f'Потрачено ккал: {self.calories}'
            )


class Training:
    """Базовый класс с основными свойствами и методами."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    hour_min = 60

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
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance = self.get_distance
        mean_speed = distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить число потраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Класс беговой тренировки."""
    coeff_cal_1 = 18
    coeff_cal_2 = 20

    def get_spent_calories(self) -> float:
        cal_1 = self.coeff_cal_1 * self.get_mean_speed() - self.coeff_cal_2
        cal_2 = cal_1 * self.weight / self.M_IN_KM
        spent_calories = cal_2 * self.duration * self.hour_min
        print(self.get_mean_speed(), cal_1, cal_2, self.weight, spent_calories)
        return spent_calories


class SportsWalking(Training):
    """Класс спортивной ходьбы."""
    coeff_cal_3 = 0.035
    coeff_cal_4 = 0.029
    coeff = 2

    def __init__(self,
                 height: float,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        cal_3 = self.coeff_cal_3 * self.weight
        cal_4 = self.get_mean_speed() ** self.coeff // self.height
        cal_5 = cal_4 * self.coeff_cal_4 * self.weight
        spent_calories = (cal_3 + cal_5) * self.duration * Training.hour_min
        return spent_calories


class Swimming(Training):
    """Класс тренировки в бассейне."""
    calorie_1 = 1.1
    calorie_2 = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38

    def get_mean_speed(self) -> float:
        speed = self.length_pool * self.count_pool
        average_speed = speed / Training.M_IN_KM / self.duration
        return average_speed

    def get_spent_calories(self) -> float:
        calories = self.get_mean_speed() + self.calorie_1
        spent_calories = calories * self.calorie_2 * self.weight
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать принятые пакеты."""
    dict_training = {'WLK': SportsWalking,
                     'RUN': Running,
                     'SWM': Swimming}
    if workout_type in dict_training.keys():
        return dict_training[workout_type](*data)
    else:
        print('There is no such workout')


def main(training) -> Training:
    """Главная функция."""
    info = training.show_training_info()
    return info
