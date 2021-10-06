#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program calculates the area and perimeter of a rectangle
#    with dimensions 5cm x 3cm


def main():
    # this function calculates the area and perimeter

    # input
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print(f"Area is {area} cm².")
    print(f"Perimeter is {perimeter} cm.")


if __name__ == "__main__":
    main()
