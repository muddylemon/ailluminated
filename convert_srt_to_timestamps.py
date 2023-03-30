import sys
import re

def convert_srt_to_timestamps(srt_file, output_file):
    with open(srt_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        for line in lines:
            match = re.match(r'(\d\d:\d\d:\d\d),\d\d\d -->', line)
            if match:
                timestamp = match.group(1)
                mm, ss = timestamp.split(':')[1:]
                outfile.write(f'[{mm}:{ss}] ')
            elif line.strip() and not line.strip().isdigit():
                outfile.write(f'{line.strip()}\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python srt_to_timestamps.py <input_srt_file> <output_timestamps_file>')
        sys.exit(1)

    srt_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_srt_to_timestamps(srt_file, output_file)
