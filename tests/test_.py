import time

from cheetiming import timing
from cheetiming import timing_data


def test_single_calls_count():
    for _ in timing('my_name'):
        pass
    assert timing_data()['my_name']['calls'] == 1


def test_recreate_timer_calls_count():
    for _ in timing('my_name1'):
        pass
    for _ in timing('my_name2', 1000):
        pass
    for _ in timing('my_name1', 1000):
        pass
    assert timing_data()['my_name1']['calls'] == 1001
    assert timing_data()['my_name2']['calls'] == 1000


def test_recreate_timer_calls_count_time():
    for _ in timing('my_name1'):
        time.sleep(1.1)
    for _ in timing('my_name2', 4):
        time.sleep(.3)
    for _ in timing('my_name1', 2):
        time.sleep(1.1)
    assert timing_data()['my_name1']['calls'] == 3
    assert timing_data()['my_name2']['calls'] == 2

    assert 3 < timing_data()['my_name1']['elapsed'] < 4
    assert 2 < timing_data()['my_name2']['calls'] < 3


