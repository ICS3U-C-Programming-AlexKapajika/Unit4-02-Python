#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 11, 2023
#This program uses a do while loop to factor positive numbers


def main():

    #Initialize the counter and the factor
    loop_counter = 0
    factor = 1
    #Get the user number
    user_number = int(input("Enter a positive number : "))
    print("")
    #calculating the accumulation of all the numbers from 1

    while True:
        loop_counter = loop_counter + 1
        factor = factor * loop_counter
        print("Tracking {} times through loop.".format(loop_counter))
        if loop_counter >= user_number:
            break

        print("")
        print("{}! = {}".format(user_number, factor))


if __name__ == "__main__":
    main()
