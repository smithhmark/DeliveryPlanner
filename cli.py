import argparse


def build_parser():
    parser = argparse.ArgumentParser()

    # positional parameters
    parser.add_argument('shipment_file')

    # optional flag parameters
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, dest="is_verbose",
                        help="Print the total cost and a per-driver breakdown")

    return parser


def parse_args():
    parser = build_parser()
    return parser.parse_args()
