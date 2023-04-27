from cheetiming import timing, timing_session, timing_report, iterate_with_timer, range_with_timer, run_with_timer, \
    timers


def print_last_timer():
    print(f'{timing_session.calls} calls')
    print(f'{timing_session.elapsed} seconds')

def print_named_timer(timer_name):
    print(f'timer: {timer_name}\n'
          f'{timers[timer_name]}')
    print(f'{timers[timer_name][-1].calls} calls')
    print(f'{timers[timer_name][-1].elapsed} elapsed')


print('Using as context manager:')
with timing() as t:
    print('...executing my unnamed code block')
print('printing the timer as string:')
print(t)
print('printing the timer in custom format:')
print(f'Elapsed: {t.elapsed} seconds')


print('\nUsing as "named" context manager:\n'
      'Timing stats can be retrieved by code block\'s name')
with timing('my code block #1') as t:
    print('...executing my code block #1')
print('printing the timer as string:')
print(t)
print('printing the timer in custom format:')
print(f'Timer: {t.name} elapsed: {t.elapsed} seconds')

print('\nReusing a "named" context manager:')
with timing('my code block #1') as t:
    print('...executing my code block #1 again...')
print('printing the timer as string:')
print(t)
print('printing the timer in custom format:')
print(f'Timer: {t.name} elapsed: {t.elapsed} seconds')
print('Timing report:')
print(timing_report(t.name))


print('Using in for loop:\n'
      'After the loop timing report is available for the last `iterate_with_timer` call')
my_list = [2, 4, 6, 7]
for item in iterate_with_timer(my_list):
    print('...retrieving item', item)
print_last_timer()


print('\nUsing in "named" "for" loop with name:\n '
      'After the loop the `timing_report` is available for the last `iterate_with_timer` call\n'
      'Timing stats can be retrieved by timer\'s name')
my_list = [2, 4, 6, 7]

timer_name = 'my_list_timer'
for item in iterate_with_timer(my_list, timer_name):
    print('...retrieving item', item)
print_last_timer()
print_named_timer(timer_name)
print(timing_report(timer_name))

print('\nUsing in "for" loop to repeat code block `n` times')
for i in range_with_timer(5):
    print(f'...executing my code block, run #{i}')
print_last_timer()

print('\nUsing in a "named" "for" loop to repeat code block `n` times\n'
      'Timing stats can be retrieved by timer\'s name')
timer_name = "my_range_timer"
for i in range_with_timer(5, timer_name):
    print(f'...executing my code block, run #{i}')
print_last_timer()
print_named_timer(timer_name)


print('\nUsing in a "named" pseudo-"for" loop to run a code block only once:\n'
      'This method has lower overhead than using a context manager!\n'
      'Timing stats can be retrieved by timer\'s name')
timer_name = "my_pseudo_range_timer"
for _ in run_with_timer(timer_name):  # equivalent to range_with_timer(1)
    print(f'executing my code block in pseudo-loop (equivalent to `range_with_timer(1)`)')
print_last_timer()
print_named_timer(timer_name)

'\nTiming report (all named timers):'
print(timing_report())