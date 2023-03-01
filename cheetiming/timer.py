import timeit


def create_timer(timer_name: str):
    """
    While timer_name is not checked to be unique in this package,
    it's highly recommended to create timers with unique names.


    :param timer_name:
    :type timer_name:
    :return:
    :rtype:
    """
    return TimerManager(timer_name)


class TimerManager:
    """
    this instance is typically created one per module
    """
    def __init__(self, timer_name: str):
        self._instances = {}
        self._name = timer_name

    def timing(self, code_block_name: str, n_iter: int = 1):
        if n_iter <= 0:
            raise ValueError('n_iter must be greater than zero.')
        if code_block_name not in self._instances:
            timer = Timer(code_block_name, n_iter)
            self._instances[code_block_name] = timer
        else:
            timer = self._instances[code_block_name]
            timer.reset(n_iter)
        for x in timer.generate_loop():
            # print(x, 'in timer')
            yield x

    @property
    def timing_data(self):
        return dict((k, {'calls': v._calls, 'elapsed': v._elapsed}) for (k, v) in self._instances.items())

    def timing_report(self):
        s = ''
        for (k, v) in self._instances.items():
            s += f'{k}: calls:{v._calls}, total_time:{v._elapsed:.6f}\n'
        return s


class Timer:
    def __init__(self, name: str, n_iter=1):
        if n_iter <= 0:
            raise ValueError('n_iter must be greater than 0.')
        self._name = name
        self._n_iter = n_iter
        self._calls = 0
        self._elapsed = 0

    def __str__(self):
        return f'timer {self._name}:  calls:{self._calls}, total_time:{self._elapsed:.6f}\n'

    def reset(self, n_iter):
        self._n_iter += n_iter

    def generate_loop(self):
        self._start = timeit.default_timer()
        for i in range(self._calls, self._n_iter):
            yield i
        self._elapsed += timeit.default_timer() - self._start
        self._calls = self._n_iter





