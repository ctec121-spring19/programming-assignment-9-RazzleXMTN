#!/usr/bin/env python3
# Module 6 - Problem Set No. 9 - Problem 1
#MAtthew Russell
"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Write a program that gets a string containing the person's first, middle and 
last names using input(), and then displays their first, middle and last 
initials. For example, the user enters "Bruce Lawrence Elgort", the program 
should display B.L.E. It must display exactly like this with the .'s after 
each letter with no spaces.

IPO
==========
INPUTS: 
PROCESSES: 
OUTPUTS: 

"""

def main():
    name = input("Enter First, Middle, and Last name: ")
    nlet = str()
    for l in name.split():
        nlet = nlet + l[0] + "."
    nlet = nlet.upper()
    print("Initials: ", nlet)
main()