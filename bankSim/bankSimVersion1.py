# main.py
# Bank-Queue-Simulation
# CSCI 154

# The following program simulates a bank queue.
# Assumptions
#   1. After closing, tellers will finish helping customers that are in the process of being helped.
#   2. After closing, tellers will not help any customers still standing in line.
#   3. If a customer came too late to be helped, their wait time will still be added to the total wait time.

from queue import PriorityQueue
import heapq

class Customer:
    def __init__(self, time, work):
        self.time = time
        self.work = work

    def __lt__(self, other):
        return self.time < other.time

    def __le__(self, other):
        return self.time <= other.time

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    def __ge__(self, other):
        return self.time >= other.time

    def __gt__(self, other):
        return self.time > other.time


class Event:
    def __init__(self, type, time, index):
        self.type = type
        self.time = time
        selt.index = index

    def __lt__(self, other):
        return self.time < other.time

    def __le__(self, other):
        return self.time <= other.time

    def __eq__(self, other):
        return self.time == other.time

    def __ne__(self, other):
        return self.time != other.time

    def __ge__(self, other):
        return self.time >= other.time

    def __gt__(self, other):
        return self.time > other.time

    def getTime(self):
        return self.time


def printCustomer(Customer1, name):
    print(name, ":", Customer1.time)


def printTeller(Teller1, name):
    print(name, ":", Teller1.time)


# Maximum amount of work a customer can enter the priority queue with.
priorityQueueLimit = 15
# Stores total wait time for all standard customers.
standardCustomerWait = 0
# Stores total wait time for all priority customers.
priorityCustomerWait = 0

standardLine = PriorityQueue()  # Stores all standard customers
priorityLine = PriorityQueue()  # Stores all priority customers
eventList = PriorityQueue()    # Stores all tellers


# CUSTOMERS-------------------------------------------------------
# for i in range(10):
#     customerLine.put(Customer(i, 5))
customerLine = [Customer(2, 10),
                Customer(3, 10),
                Customer(1, 10),
                Customer(2, 10),
                Customer(9, 10),
                Customer(5, 10),
                Customer(4, 10),
                Customer(7, 10),
                Customer(9, 10),
                Customer(10, 10)]

tellers = [(1, 10), (1, 10), (1, 10)]
# Initialize Tellers


def bankSimulation():

    # Create an arrival event for each customer.
    index = 0
    for customer in customerLine:
        eventList.put(Event('a', customer.time))
        index += 1

    # Run simulation
    while not eventList.empty:

        curEvent = eventList.get()

        # If customer arrival
        if curEvent.type == 'a':
            # Check if standardLine is full
            if standardLine.empty:


                # Begin Simulation
                # run = True
                # while run:
                #     # Past closing time.
                #     if tellerLine.empty():
                #         break
                #     else:   # peek at next teller
                #         curTeller = tellerLine.queue[0]
                #     # No customers in line.
                #     if standardLine.empty() and priorityLine.empty():
                #         break
                #     if not priorityLine.empty():
                #         priorityCustomer = priorityLine.queue[0]
                #     if not standardLine.empty():
                #         standardCustomer = standardLine.queue[0]
                #     while (curTeller.time < priorityCustomer.time) and (curTeller.time < standardCustomer.time):
                #         break
                #     run = False
bankSimulation()


# print("\nCustomer:")
# i = 1
# while not customerLine.empty():
#     printCustomer(customerLine.get(), i)
#     i = i +1

# i =1
# print("\nTeller:")
# while not tellerLine.empty():
#     printCustomer(tellerLine.get(), i)
#     i = i +1
