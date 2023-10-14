from utils.speech_input_loop import main
import torch
from utils.chatgpt_api.chatgpt_api_calls import call_gpt
import asyncio
from database_scanner.loop import run_database_loop_asynchronous
from global_code.helpful_functions import count_lines_of_code


def they_loop():
    loop = asyncio.get_event_loop()
    tasks = [run_database_loop_asynchronous(), main()]
    # tasks = [main()]

    try:
        loop.run_until_complete(asyncio.gather(*tasks))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()


def single_test():
    call_gpt('I need to go to the target tonight')


if __name__ == "__main__":
    # they_loop()
    single_test()