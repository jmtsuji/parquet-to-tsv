#!/usr/bin/env python
"""
parquet-to-tsv.py
Converts parquet files to TSV format
Jackson M. Tsuji, 2025
"""

import pandas as pd
import os
import sys
import logging
import argparse

VERSION = '0.1.0'


def main():
    """
    Collects input arguments and performs the parquet load and save
    """
    parser = parse_cli()
    args = parser.parse_args()

    # Initialize the logger
    logger = logging.getLogger()
    formatter = logging.Formatter('[ %(asctime)s ]: %(levelname)s: %(filename)s: %(funcName)s: %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if (hasattr(args, 'verbose')) and (args.verbose is True):
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logger.debug(f'Opening parquet file: {args.input_parquet}.')
    data_table = pd.read_parquet(args.input_parquet)

    logger.debug(f'Writing to output file: {args.output_tsv}.')
    data_table.to_csv(args.output_tsv, sep='\t', index=False)

    logger.debug(f'{os.path.basename(sys.argv[0])}: done.')


def parse_cli():
    """
    Parses the CLI arguments.
    :return: An argparse parser object.
    """
    cli_title = (f'parquet-to-tsv: simple command-line utility to convert parquet files to TSV format.\n'
                 f'Copyright Jackson M. Tsuji, 2025.\n'
                 f'Version: {VERSION}')
    parser = argparse.ArgumentParser(description=cli_title)

    parser.add_argument('-i', '--input_parquet', required=True, type=str,
                        help='Path to the input .parquet file')
    parser.add_argument('-o', '--output_tsv', required=True, type=str,
                        help='Path to the output .tsv file')
    parser.add_argument('-v', '--verbose', required=False, action='store_true',
                              help='Enable verbose logging')

    return parser


if __name__ == '__main__':
    main()
