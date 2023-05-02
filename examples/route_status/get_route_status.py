# -*- coding: utf-8 -*-

import argparse

from route4me import Route4Me


def main(api_key, route_id):
    r4m = Route4Me(api_key)

    route = r4m.route_status
    print('Route ID: {}'.format(route_id))
    response = route.get_route_status(route_id=route_id)
    print(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get a Route')
    parser.add_argument('--api_key', dest='api_key', help='Route4Me API KEY',
                        type=str, required=True)
    parser.add_argument('--route_id', dest='route_id', help='Route4Me Route ID',
                        type=str, required=True)
    args = parser.parse_args()
    main(args.api_key, args.route_id)
