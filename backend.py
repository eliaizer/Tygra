import subprocess
import threading



class backendTygra():
    def __init__(self):
        self.ffmpeg_path = "ffmpeg"
        self.process = None

    def start(self, options):
        # запуск потока ffmpeg с опциям из GUI
        pass

    def kill(self):
        # обычное завершение процесса
        self.done(1)

    def done(self):
        # в случае успеха возратить статус Успеха и место результата
        # в случае неудачи возратить статус Неудачи и ошибки ffmpeg
        pass

    def get_progres(self):
        # возратить значение прогресса в процентах для GUI
        return 0

    # Установка доступных опций в графическом интерфейсе
    def get_avilable_options(self, input_file):
        if input_file.endswith(".avi"):
            print("avi")