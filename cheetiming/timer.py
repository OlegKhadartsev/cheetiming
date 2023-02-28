import timeit


_instances = {}


def timing(name, n_iter=1):
    if name not in _instances:
        timer = MyIter(n_iter)
        _instances[name] = timer
    else:
        timer = _instances[name]
        timer.reset()
    return timer


def timing_data():
    return dict((k, {'calls': v._calls, 'elapsed': v._elapsed}) for (k, v) in _instances.items())


def timing_report():
    s = ''
    for (k, v) in _instances.items():
        s += f'{k}: calls:{v._calls}, total_time:{v._elapsed:.6f}\n'
    return s


class MyIter:
    def __init__(self, n_iter=1):
        if n_iter <= 0:
            raise ValueError('n_iter must be greater than 0.')
        self._n_iter = n_iter
        self._calls = 0

    def reset(self, n_iter):
        self._n_iter += n_iter

    def __iter__(self):
        self._start = timeit.default_timer()
        return self

    def __next__(self):
        if self._calls < self._n_iter:
            self._calls += 1
            return self._calls - 1
        else:
            self._elapsed = timeit.default_timer() - self._start
            raise StopIteration

    @classmethod
    def preport(cls):
        s = ''
        for (k, v) in cls._instances.items():
            s += f'{k}: calls:{v._calls}, total_time:{v._elapsed:.6f}\n'
        return s


for x in timing('timer1', 50000):
    pass

for x in timing('timer2', 100000):
    pass

for x in timing('timer1', 50000):
    pass


print(timing_report())

