import pyttsx3
import sounddevice as sd
from app.global_code.helpful_functions import create_logger_error, log_it, benchmark_and_log_exceptions


def get_output_device_index(device_name: str | None) -> int | None:
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['name'] == device_name:
            return i
    return None


@benchmark_and_log_exceptions
def speak(text: str, device_name: str | None = None):
    engine = pyttsx3.init()
    output_device_index: int | None = get_output_device_index(device_name)
    print(output_device_index)
    if output_device_index is not None:
        engine.setProperty('driverName', 'sounddevice')
        engine.setProperty('audioOutput', output_device_index)

    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    speak("Hello, my name is Alex", "Pebble Speakers (High Definitio")
# Specify the desired device name
# device_name = "Pebble Speakers (High Definitio"
#
# # List available sound devices
# print(sd.query_devices())
#
# speak("Hello, my name is Alex", device_name)
