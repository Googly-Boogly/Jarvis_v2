from app.global_code.helpful_functions import log_exceptions, benchmark_function, benchmark_and_log_exceptions


@benchmark_and_log_exceptions

def test2():
    x = 1/0

if __name__ == '__main__':
    test2()