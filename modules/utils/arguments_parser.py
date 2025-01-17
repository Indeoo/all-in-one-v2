import argparse
import os


def parse_arguments(default_password, default_wallets_file):
    parser = argparse.ArgumentParser(description='Process arguments.')

    parser.add_argument('--private_keys', type=str, required=False,
                        default=os.environ.get('PRIVATE_KEYS', default_wallets_file),
                        help='a string to be processed')
    parser.add_argument('--password', type=str, required=False, default=os.environ.get('PASSWORD', default_password),
                        help='a string to be processed')

    return parser.parse_args()
