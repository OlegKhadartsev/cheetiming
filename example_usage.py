from functools import partial


examples = [
    ("Using as a context manager:",
     """import time
from cheetiming import timing

with timing() as t:
    time.sleep(.1)    
print(t)
print(t.elapsed)
"""),

    ("Using as a _named_ context manager:",
     """import time
from cheetiming import timing

with timing('my_named_code_block') as t:
    time.sleep(.1)    
print(t)
print(t.name, t.elapsed)
"""),
    ('Reusing a _named_ context manager:',
     """import time
from cheetiming import timing, timing_report

with timing('my_repeating_code_block') as t:
    time.sleep(.1)
print(t)
with timing('my_repeating_code_block') as t:
    time.sleep(.1)    
print(t)
# print timing_report:
print(timing_report(t.name))
"""),
    ("Using in a ___for___ loop",
     """from cheetiming import iterate_with_timer, timing_session
      
my_list = [2, 4, 6, 7]
for i, item in iterate_with_timer(my_list):
    print(f'loop {i}: retrieving item:{item}')
print(timing_session)
print(timing_session.calls, 'calls', timing_session.elapsed, 'sec') 
"""),
    ("Using in a _named_ ___for___ loop",
     """from cheetiming import iterate_with_timer, timing_session, timing_report
      
my_list = [2, 4, 6, 7]
for i, item in iterate_with_timer(my_list, 'my_loop_timer'):
    print(f'loop {i}: retrieving item:{item}')
print(timing_session)
print(timing_report('my_loop_timer'))
"""),
    ("Using as a ___range___ -like generator loop to repeat a code block _n_ times",
     """from cheetiming import range_with_timer, timing_session
      
for i in range_with_timer(5):
    print(f'loop {i}')
print(timing_session)
print(timing_session.calls, 'calls', timing_session.elapsed, 'sec')
"""),
    ("Using as a _named_ ___range___ -like generator loop to repeat a code block _n_ times",
     """from cheetiming import range_with_timer, timing_session, timing_report
      
for i in range_with_timer(5, 'my_range_timer'):
    print(f'loop {i}')
print(timing_session)
print(timing_report('my_range_timer'))
"""),
    ("Using as a pseudo- ___range___ -like generator loop to run a code block only __once__\n"
     "(it brings lower overhead than using a context manager)",
     """from cheetiming import run_with_timer, timing_session
      
for _ in run_with_timer():
    print('running my code block only once!')
print(timing_session)
"""),
    ("Using as a _named_ pseudo- ___range___ -like generator loop to run a code block only __once__\n"
     "(it brings lower overhead than using a context manager)",
     """from cheetiming import run_with_timer, timing_session, timing_report
      
for _ in run_with_timer('my_pseudo_range_timer'):
    print('running my code block only once!')
print(timing_session)
print(timing_report('my_pseudo_range_timer'))
"""),
    ("Using timing_report to print statistics for all named timers",
     """from cheetiming import timing_report

# using named timers from the examples above here ...

print(timing_report())
"""),
    ("Printing a specific timer's report",
     """from cheetiming import timing_report

# using named timers from the examples above here ...

print(timing_report('my_repeating_code_block'))
""")

]


def exec_code_with_output(title, source):
    print('- ' + title)
    print(f'```python\n{source}```\nOutput:\n```')
    exec(source)
    print('```')


with open('Usage.md', 'w', encoding='utf8') as f_usage:
    f_usage.write('')
with open('Usage.md', 'a', encoding='utf8') as f_usage:
    print = partial(print, file=f_usage)
    for example in examples:
        exec_code_with_output(*example)


