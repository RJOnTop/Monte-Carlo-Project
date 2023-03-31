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
import copy

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


class Teller:
    def __init__(self, time, workRate):
        self.time = time
        self.workRate = workRate

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

    def __lt__(self, other):
        return self.time < other.time


def printCustomer(Customer1, name):
    print(name, ":", Customer1.time)


def printTeller(Teller1, name):
    print(name, ":", Teller1.time)


def printMetrics():

    print("Standard Customers Count:  ", stanCustomerCount)
    print("Standard Customers Served: ", stanCustomerServed)
    print("Standard Customers Wait:   ", stanCustomerWait, "\n")

    print("Priority Customers Count:  ", priCustomerCount)
    print("Priority Customers Served: ", priCustomerServed)
    print("Priority Customers Wait:   ", priCustomerWait)


# Global Variables
priLineWorkLimit = 10           # work limit for priority line

stanCustomerCount = 5           # Total number of standard customers.
# Total number of standard customers that were helped by tellers.
stanCustomerServed = 0
# Stores total wait time for all standard customers.
stanCustomerWait = 0

priCustomerCount = 5    # Total number of priority customers.
# Total number of priority customers that were helped by tellers.
priCustomerServed = 0
priCustomerWait = 0     # Stores total wait time for all priority customers.

closingTime = 3                 # Latest time customers will be helped.

stanLine = PriorityQueue()      # Stores all standard customers
priLine = PriorityQueue()       # Stores all priority customers
tellerLine = PriorityQueue()    # Stores all tellers


# Initialize Customers
# for i in range(10):
#     customerLine.put(Customer(i, 5))

priLine.put(Customer(1, 10))
priLine.put(Customer(1, 10))
priLine.put(Customer(1, 10))
priLine.put(Customer(2, 10))
priLine.put(Customer(2, 10))

stanLine.put(Customer(1, 15))
stanLine.put(Customer(1, 15))
stanLine.put(Customer(1, 15))
stanLine.put(Customer(3, 15))
stanLine.put(Customer(3, 15))

# Initialize Tellers
workRate = 10
tellerLine.put(Teller(0, workRate))
tellerLine.put(Teller(0, workRate))
tellerLine.put(Teller(0, workRate))


def bankSimulation():

    global closingTime

    global priCustomerServed
    global priCustomerWait

    global stanCustomerServed
    global stanCustomerWait

    # Begin Simulation
    while True:

        if tellerLine.empty():
            break
        else:
            teller = copy.copy(tellerLine.queue[0])

        if stanLine.empty() and priLine.empty():
            break

         # Standard line is empty.
        while not priLine.empty() and stanLine.empty():
            priCustomer = priLine.queue[0]

            if tellerLine.empty():
                break
            else:
                teller = copy.copy(tellerLine.queue[0])

           # Advance teller's time.
            while ((not tellerLine.empty()) and (teller.time < priCustomer.time)):

                tellerLine.get()

                teller.time = priCustomer.time
                if teller.time < closingTime:
                    tellerLine.put(teller)

                teller = copy.copy(tellerLine.queue[0])

            if tellerLine.empty():
                break

            # Help customer. Calculate customer's wait.
            priLine.get()
            priCustomerServed += 1
            priCustomerWait = priCustomerWait + \
                (teller.time - priCustomer.time)

            # Remove teller from queue.
            tellerLine.get()

            # Adjust teller's time.
            teller.time += (priCustomer.work / teller.workRate)

            # Add teller back to queue.
            if teller.time < closingTime:
                tellerLine.put(teller)

        # Priority line is empty.
        while priLine.empty() and not stanLine.empty():
            stanCustomer = stanLine.queue[0]

            if tellerLine.empty():
                break
            else:
                teller = copy.copy(tellerLine.queue[0])

           # Advance teller's time.
            while ((not tellerLine.empty()) and (teller.time < stanCustomer.time)):

                tellerLine.get()

                teller.time = stanCustomer.time
                if teller.time < closingTime:
                    tellerLine.put(teller)

                teller = copy.copy(tellerLine.queue[0])

            if tellerLine.empty():
                break

            # Help customer. Calculate customer's wait.
            stanLine.get()
            stanCustomerServed += 1
            stanCustomerWait = stanCustomerWait + \
                (teller.time - stanCustomer.time)

            # Remove teller from queue.
            tellerLine.get()

            # Adjust teller's time.
            teller.time += (stanCustomer.work / teller.workRate)

            # Add teller back to queue.
            if teller.time < closingTime:
                tellerLine.put(teller)

        # Priority line is not empty. Standard line is not empty.
        while not priLine.empty() and not stanLine.empty():

            stanCustomer = stanLine.queue[0]
            priCustomer = priLine.queue[0]

            if tellerLine.empty():
                break
            else:
                teller = copy.copy(tellerLine.queue[0])

            # Find which customer is next.
            if (stanCustomer.time < priCustomer.time):
                nextCustomer = stanCustomer
            else:
                nextCustomer = priCustomer

             # Advance teller's time.
            while ((not tellerLine.empty()) and (teller.time < nextCustomer.time)):

                tellerLine.get()

                teller.time = nextCustomer.time
                if teller.time < closingTime:
                    tellerLine.put(teller)

                teller = copy.copy(tellerLine.queue[0])

            # Priority customer.
            if nextCustomer.work <= priLineWorkLimit:

                # Calculate customer's wait. Remove customer from line.
                priCustomerWait += (teller.time - priCustomer.time)
                priLine.get()
                priCustomerServed += 1

                # Remove teller from queue. Adjust teller's time.
                tellerLine.get()
                teller.time += (priCustomer.work / teller.workRate)

            else:   # Standard customer.

                # Calculate customer's wait. Remove customer from line.
                stanCustomerWait = stanCustomerWait + \
                    (teller.time - stanCustomer.time)
                stanLine.get()
                stanCustomerServed += 1

                # Remove teller from queue. Adjust teller's time.
                tellerLine.get()
                teller.time += (stanCustomer.work / teller.workRate)

            # Add teller back to queue.
            if teller.time < closingTime:
                tellerLine.put(teller)

    # ADD customers wait time that were never helped
    # Consider using functions for the while loops
    # There is a logical error when both standard and priority customer are in line.
    #   To fix the error tellers must have a way to specify whether they are a priority teller or a standard teller. 

# def advanceTellerTime(teller, customer):
#     tellerLine.get()

#     teller.time = customer.time
#     if teller.time < closingTime:
#         tellerLine.put(teller)

#     teller = copy.copy(tellerLine.queue[0])


bankSimulation()
printMetrics()
