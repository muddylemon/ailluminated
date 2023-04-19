import sys
import os
import re

def create_prompts(prefix, suffix, input_file, output_file=None):
    if output_file is None:
        words = prefix.split()[:5]
        output_file = '-'.join(words).lower() + '.txt'

    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file.readlines():
            _, content = line.strip().split(None, 1)
            wrapped_line = f"{prefix} ( {content} ), {suffix}\n"
            out_file.write(wrapped_line)

    print(f"Output written to {output_file}")

if __name__ == "__main__":
    print("Please provide the following information:")

    prefix = input("Enter the prefix: ")
    suffix = input("Enter the suffix: ")
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file (press enter to use default): ")

    if not output_file.strip():
        output_file = None

    create_prompts(prefix, suffix, input_file, output_file)
