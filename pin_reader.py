#!/usr/bin/env python3

import sys

def read_pin_list(filename='pin_list.txt'):
    """Read the pin list from file"""
    try:
        with open(filename, 'r') as f:
            pins = [line.strip() for line in f.readlines() if line.strip()]
        return pins
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        print("Please run threadTone.py first to generate the pin list.")
        sys.exit(1)

def main():
    pins = read_pin_list()
    total_pins = len(pins)
    increment = 5
    current_index = 0
    
    print("=" * 50)
    print("STRING ART PIN SEQUENCE READER")
    print("=" * 50)
    print(f"Total pins to connect: {total_pins}")
    print(f"Showing {increment} pins at a time")
    print("=" * 50)
    print()
    
    while current_index < total_pins:
        # Calculate progress
        progress = (current_index / total_pins) * 100
        
        # Get next batch of pins
        end_index = min(current_index + increment, total_pins)
        batch = pins[current_index:end_index]
        
        # Display progress bar
        bar_length = 30
        filled = int(bar_length * current_index / total_pins)
        bar = '█' * filled + '░' * (bar_length - filled)
        
        print(f"Progress: [{bar}] {progress:.1f}%")
        print(f"Pins {current_index + 1}-{end_index} of {total_pins}:")
        print()
        
        # Display the pins with arrows
        for i, pin in enumerate(batch):
            pin_num = current_index + i + 1
            if pin_num < total_pins:
                print(f"  {pin_num}. Pin {pin} →")
            else:
                print(f"  {pin_num}. Pin {pin} (FINAL)")
        
        print()
        
        # Update index
        current_index = end_index
        
        # Check if we're done
        if current_index >= total_pins:
            print("=" * 50)
            print("✓ COMPLETE! All pins displayed.")
            print("=" * 50)
            break
        
        # Wait for user input
        user_input = input("Press Enter for next 5 pins (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print(f"\nStopped at pin {current_index}/{total_pins}")
            break
        
        print()

if __name__ == "__main__":
    main()
