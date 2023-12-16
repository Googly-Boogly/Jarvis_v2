from app.utils.speech_input_loop import main
from app.utils.chatgpt_api.chatgpt_api_calls import call_gpt
import asyncio
from app.database_scanner.loop import run_database_loop_asynchronous
from app.global_code.helpful_functions import log_exceptions, benchmark_function, benchmark_and_log_exceptions


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
    # call_gpt('lights on')
    call_gpt('I have a meeting tomorrow at 3pm add it to my calendar')
    # call_gpt('Lights brightness up')
    # run_database_loop_synchronous()




if __name__ == "__main__":
    # print('hi')
    # loop = asyncio.get_event_loop()
    # tasks = [run_database_loop_asynchronous()]
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(count_lines_of_code(r'F:\Coding\Iris_V2\app'))
    # they_loop()
    single_test()