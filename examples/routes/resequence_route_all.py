# -*- coding: utf-8 -*-

from route4me import Route4Me

API_KEY = "11111111111111111111111111111111"


def main():
    r4m = Route4Me(API_KEY)
    route = r4m.route
    response = route.get_routes(limit=1, offset=0)
    if isinstance(response, dict) and 'errors' in response.keys():
        print('. '.join(response['errors']))
    else:
        route_id = response[0]['route_id']
        print('Route ID: {}'.format(route_id))
        response = route.get_route(route_id=route_id)
        if isinstance(response, dict) and 'errors' in response.keys():
            print('. '.join(response['errors']))
        else:
            print('Route ID: {}'.format(route_id))
            data = {
                "disable_optimization": 0,
                "optimize": 'Distance',
                "route_id": route_id,
            }
            response = route.resequence_route_all(**data)
            print(response)


if __name__ == '__main__':
    main()
