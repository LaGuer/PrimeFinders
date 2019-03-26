# -*- coding: utf-8 -*-
"""
Created on Tue Mar  26 17:16:46 2019
@author: LaGuer
"""

import os
import multiprocessing
import time
import random                       # for coming up with random numbers
from multiprocessing import Pool    # for pooling answers

def getResult():
    test = -1

    try:
        n = input("Give:")      # asks user for the number n
        if n < 0:
            print "Please give a positive input."
            SystemExit(-3)
    except Exception as e:
        print "Input not accepted."
        print e.message
        SystemExit(-2)
    print "You gave:", n

    start_time = time.time()

    step = 1

    if n < 10000:
        for a in range(2, n, step):     # for numbers <100000 single-threading is pretty decent

            test = ((a ** (n - 1)) % n)
            if test != 1:
                break

        if test != 1:
            print "This number is not prime!"
        elif test == 1:
            print "This number is prime!"
        elapsed_time = time.time() - start_time
        print "Realtime elapsed:", elapsed_time, "sec"
        return 0

    else:                               # code for >=100000 numbers
        test = calculate(n)             # Calls function for parallel calculation of the result
        if test != 1:
            print "This number is not prime!"
        elif test == 1:
            print "This number is probably prime!"
        elapsed_time = time.time() - start_time
        print "Realtime elapsed:", elapsed_time, "sec"
        return 1


def calculate(n):
    pool = Pool()
    quantum = 120  # Time before timeout of reply-wait
    index = 40
    answer = []

    # Code for assigning parallel calculation of the results (threading)
    result1 = pool.apply_async(fermat, [n])
    result2 = pool.apply_async(fermat, [n])
    result3 = pool.apply_async(fermat, [n])
    result4 = pool.apply_async(fermat, [n])
    result5 = pool.apply_async(fermat, [n])
    result6 = pool.apply_async(fermat, [n])
    result7 = pool.apply_async(fermat, [n])
    result8 = pool.apply_async(fermat, [n])
    result9 = pool.apply_async(fermat, [n])
    result10 = pool.apply_async(fermat, [n])
    result11 = pool.apply_async(fermat, [n])
    result12 = pool.apply_async(fermat, [n])
    result13 = pool.apply_async(fermat, [n])
    result14 = pool.apply_async(fermat, [n])
    result15 = pool.apply_async(fermat, [n])
    result16 = pool.apply_async(fermat, [n])
    result17 = pool.apply_async(fermat, [n])
    result18 = pool.apply_async(fermat, [n])
    result19 = pool.apply_async(fermat, [n])
    result20 = pool.apply_async(fermat, [n])
    result21 = pool.apply_async(fermat, [n])
    result22 = pool.apply_async(fermat, [n])
    result23 = pool.apply_async(fermat, [n])
    result24 = pool.apply_async(fermat, [n])
    result25 = pool.apply_async(fermat, [n])
    result26 = pool.apply_async(fermat, [n])
    result27 = pool.apply_async(fermat, [n])
    result28 = pool.apply_async(fermat, [n])
    result29 = pool.apply_async(fermat, [n])
    result30 = pool.apply_async(fermat, [n])
    result31 = pool.apply_async(fermat, [n])
    result32 = pool.apply_async(fermat, [n])
    result33 = pool.apply_async(fermat, [n])
    result34 = pool.apply_async(fermat, [n])
    result35 = pool.apply_async(fermat, [n])
    result36 = pool.apply_async(fermat, [n])
    result37 = pool.apply_async(fermat, [n])
    result38 = pool.apply_async(fermat, [n])
    result39 = pool.apply_async(fermat, [n])
    result40 = pool.apply_async(fermat, [n])
    print "Pool filled successfully\n"

    # idx = 1
    loop_flag = True  # When this is true it is still calculating the answers
    while quantum < 600 and loop_flag:  # This allows the program to collapse after 10 minutes have passed
        try:
            print "**Progression**"
            #
            val1 = result1.get(timeout=quantum)
            answer.append(val1)
            #                                                                          # The first 21 calculations are
            val2 = result2.get(timeout=quantum)                                        # checked to see whether the
            answer.append(val2)                                                        # number turned out to be complex
            #                                                                          # (P = 0.5)
            val3 = result3.get(timeout=quantum)                                        # They are checked in groups of
            answer.append(val3)                                                        # 4 in order not to inhibit the
            #                                                                          # multithreaded processing
            val4 = result4.get(timeout=quantum)
            answer.append(val4)

            if check_complex(val1) == 0 or check_complex(val2) == 0 or check_complex(val3) == 0 or check_complex(val4) == 0:
                print "100%"
                return 0

            val5 = result5.get(timeout=quantum)
            answer.append(val5)
            #
            val6 = result6.get(timeout=quantum)
            answer.append(val6)
            #
            val7 = result7.get(timeout=quantum)
            answer.append(val7)
            #
            val8 = result8.get(timeout=quantum)
            answer.append(val8)

            if check_complex(val5) == 0 or check_complex(val6) == 0 or check_complex(val7) == 0 or check_complex(val8) == 0:
                print "100%"
                return 0

            val9 = result9.get(timeout=quantum)
            answer.append(val9)
            #
            val10 = result10.get(timeout=quantum)
            answer.append(val10)

            print "25%"

            #
            val11 = result11.get(timeout=quantum)
            answer.append(val11)
            #
            val12 = result12.get(timeout=quantum)
            answer.append(val12)

            if check_complex(val9) == 0 or check_complex(val10) == 0 or check_complex(val11) == 0 or check_complex(val12) == 0:
                print "100%"
                return 0

            val13 = result13.get(timeout=quantum)
            answer.append(val13)
            #
            val14 = result14.get(timeout=quantum)
            answer.append(val14)
            #
            val15 = result15.get(timeout=quantum)
            answer.append(val15)
            #
            val16 = result16.get(timeout=quantum)
            answer.append(val16)

            if check_complex(val13) == 0 or check_complex(val14) == 0 or check_complex(val15) == 0 or check_complex(
                    val16) == 0:
                print "100%"
                return 0

            val17 = result17.get(timeout=quantum)
            answer.append(val17)
            #
            val18 = result18.get(timeout=quantum)
            answer.append(val18)
            #
            val19 = result19.get(timeout=quantum)
            answer.append(val19)
            #
            val20 = result20.get(timeout=quantum)
            answer.append(val20)

            print "50%"

            val21 = result21.get(timeout=quantum)
            answer.append(val21)

            if check_complex(val7) == 0 or check_complex(val18) == 0 or check_complex(val19) == 0 or check_complex(
                    val20) == 0 or check_complex(val21) == 0:
                print "100%"
                return 0

            # The values are not check from now on (p=0.5)

            answer.append(result22.get(timeout=quantum))
            answer.append(result23.get(timeout=quantum))
            answer.append(result24.get(timeout=quantum))
            answer.append(result25.get(timeout=quantum))
            answer.append(result26.get(timeout=quantum))
            answer.append(result27.get(timeout=quantum))
            answer.append(result28.get(timeout=quantum))
            answer.append(result29.get(timeout=quantum))
            answer.append(result30.get(timeout=quantum))
            print "75%"
            answer.append(result31.get(timeout=quantum))
            answer.append(result32.get(timeout=quantum))
            answer.append(result33.get(timeout=quantum))
            answer.append(result34.get(timeout=quantum))
            answer.append(result35.get(timeout=quantum))
            answer.append(result36.get(timeout=quantum))
            answer.append(result37.get(timeout=quantum))
            answer.append(result38.get(timeout=quantum))
            answer.append(result39.get(timeout=quantum))
            answer.append(result40.get(timeout=quantum))
            print "100%"
            loop_flag = False  # This flag as false signals the end of the 40 calculations
        except multiprocessing.TimeoutError as e:
            print "Timeout Error.Increasing quantum...\n", e.message
            quantum += 60

    for i in range(1, index):
        if answer[i] != 1:
            return 0

    # print "All aces!"

    try:
        pool.close()
    except AssertionError as e:
        print "Failed to free Pool obj.", e.message

    return 1


def fermat(n):
    a = random.randrange(1, n - 1, 1)
    test = ((a ** (n - 1)) % n)         # This line essentially is Fermat's test
    return test                         # if this returns something else than 1, then n is not prime


def check_complex(mod):  # 1-> Could be prime | 0->NOT a prime
    if mod != 1:
        return 0
    else:
        return 1

def main():
    print "**PrimeFinders v0.0.1**"
    print 'Process Id:', os.getpid()
    print "Cores: ", multiprocessing.cpu_count()
    ex_code = getResult()
    print "EXIT CODE: ", ex_code


if __name__ == '__primefinders__':
    primefinders()
