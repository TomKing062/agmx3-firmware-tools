import argparse
import os
from packer import Packer
from unpacker import Unpacker

parser = argparse.ArgumentParser(description='A packing/unpacking tool')
parser.add_argument(
    'mode', type=str,
    help='select operation mode: "pack" or "unpack" or "list"'
)
parser.add_argument(
    'input_path', type=str,
    help='input file or directory path'
)
parser.add_argument(
    '--nocrc', dest='crc_check', action='store_false',
    help='skip CRC check when unpacking'
)

args = parser.parse_args()

if args.mode == 'pack':
    if os.path.isdir(args.input_path):
        output_file = os.path.join(os.path.dirname(args.input_path), os.path.basename(args.input_path) + '.bin')
        p = Packer(args.input_path)
        p.export(output_file)
    else:
        print('Invalid input: not a directory')
elif args.mode == 'unpack':
    if os.path.isfile(args.input_path):
        output_path = os.path.splitext(args.input_path)[0]
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        unp = Unpacker(args.input_path)
        unp.export(output_path, unpack_files=True, crc_check=args.crc_check)
        print(unp)
    else:
        print('Invalid input: not a file')
elif args.mode == 'list':
    if os.path.isfile(args.input_path):
        output_path = os.path.splitext(args.input_path)[0]
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        unp = Unpacker(args.input_path)
        unp.export(output_path, unpack_files=False, crc_check=False)
        print(unp)
        os.rmdir(output_path)
    else:
        print('Invalid input: not a file')
else:
    print('Invalid mode:', args.mode)
