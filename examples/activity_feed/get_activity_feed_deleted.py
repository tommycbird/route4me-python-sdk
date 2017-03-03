from route4me import Route4Me

KEY = "11111111111111111111111111111111"


def main():
    route4me = Route4Me(KEY)
    activity_feed = route4me.activity_feed
    response = activity_feed.get_activity_feed_deleted(
        route_id='C9F6F9F664169DFB4042110069EBE688'
    )
    if hasattr(response, 'errors'):
        print('. '.join(response.errors))
    else:
        print('Total affected: {}'.format(response.total))
        for i, activity in enumerate(response.results):
            print('Activity #{}'.format(i + 1))
            print('\tActivity ID: {}'.format(activity.activity_id))
            print('\tActivity Type: {}'.format(activity.activity_type))

if __name__ == '__main__':
    main()
