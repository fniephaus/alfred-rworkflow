# The MIT License (MIT)
#
# Copyright (c) 2015 Fabio Niephaus <code@fniephaus.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import signal
import sys
import math
from time import time

from workflow import RWorkflow

# see https://projecteuler.net/overview=001
def problem1(n):
    result = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

# see https://projecteuler.net/overview=002
def problem2(n):
    result = 0
    a = 1
    b = 1
    while b < n:
        if b % 2 == 0:
            result = result + b
        tmp = a + b
        a = b
        b = tmp
    return result

# see https://projecteuler.net/overview=003
def problem3(n):
    if n % 2 == 0:
        n = n // 2
        last_factor = 2
        while n % 2 == 0:
            n = n // 2
    else:
        last_factor = 1
    factor = 3
    while n > 1:
        if n % factor == 0:
            n = n // factor
            last_factor = factor
            while n % factor == 0:
                n = n // factor
        factor = factor + 2
    return last_factor


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True


# see https://projecteuler.net/overview=010
def problem10(n):
    result = 5
    i = 5
    while i <= n:
        if is_prime(i):
            result += i
        i += 2
        if i <= n and is_prime(i):
            result += i
        i += 4
    return result


def main(args):
    start = time()
    wf = RWorkflow()

    if len(args) == 2:
        try:
            number = int(args[1])
            result1 = problem1(number)
            wf.add_item(
                title="Answer 1: %s" % result1,
                subtitle="Find the sum of all the multiples of 3 or 5 below %s." % number,
                arg=str(result1),
                valid=True
            )
            result2 = problem2(number)
            wf.add_item(
                title="Answer 2: %s" % problem2(number),
                subtitle="Find the sum of the even Fibonacci values that do not exceed %s." % number,
                arg=str(result2),
                valid=True
            )
            result3 = problem3(number)
            wf.add_item(
                title="Answer 3: %s" % problem3(number),
                subtitle="What is the largest prime factor of the number %s ?" % number,
                arg=str(result3),
                valid=True
            )
            result10 = problem10(number)
            wf.add_item(
                title="Answer 10: %s" % problem10(number),
                subtitle="The sum of all the primes below %s." % number,
                arg=str(result10),
                valid=True
            )
        except ValueError:
            wf.add_item(
                title="Invalid input" ,
                subtitle="%s is not a number." % args[1],
                valid=False
            )

    # Add execution time for benchmarking purposes
    execution_time = str((time() - start) * 1000)
    offset = execution_time.find('.') + 5
    assert offset > 0
    wf.add_item(
        title="Execution time: %sms" % execution_time[0:offset],
        icon=wf.get_icon("info")
    )

    wf.send_feedback()
    return 0


def target(driver, args):
    return main, None

if __name__ == '__main__':
    main(sys.argv)
