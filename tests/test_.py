import time
import pytest
from cheetiming import create_timer


@pytest.fixture
def timer():
    return create_timer(__file__)


def test_single_calls_count(timer):
    for _ in timer.timing('my_name'):
        pass
    assert timer.timing_data['my_name']['calls'] == 1


def test_recreate_timer_calls_count(timer):
    for _ in timer.timing('my_name1'):
        pass
    for _ in timer.timing('my_name2', 1000):
        pass
    for _ in timer.timing('my_name1', 1000):
        pass
    assert timer.timing_data['my_name1']['calls'] == 1001
    assert timer.timing_data['my_name2']['calls'] == 1000


def test_recreate_timer_calls_count_time(timer):
    for _ in timer.timing('my_name1'):
        time.sleep(1.1)
    for _ in timer.timing('my_name2', 4):
        time.sleep(.3)
    for _ in timer.timing('my_name1', 2):
        time.sleep(1.1)
    assert timer.timing_data['my_name1']['calls'] == 3
    assert timer.timing_data['my_name2']['calls'] == 4

    assert 3 < timer.timing_data['my_name1']['elapsed'] < 4
    assert 1 < timer.timing_data['my_name2']['elapsed'] < 2


