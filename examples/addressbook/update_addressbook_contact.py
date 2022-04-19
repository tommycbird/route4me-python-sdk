# -*- coding: utf-8 -*-
import argparse

from route4me import Route4Me


def main(api_key):
    route4me = Route4Me(api_key)

    address_book = route4me.address_book
    response = address_book.get_addressbook_contacts(limit=10, offset=5)
    if 'errors' in response.keys():
        print('. '.join(response['errors']))
    else:
        address_id = "'{}'".format(response['results'][0]['address_id'])
        response = address_book.get_addressbook_contact(address_id=address_id)
        if 'errors' in response.keys():
            print('. '.join(response['errors']))
        else:
            contact = response['results'][0]
            contact['first_name'] = '{} Updated'.format(contact['first_name'])
            response = address_book.update_contact(**contact)
            if 'errors' in response.keys():
                print('. '.join(response['errors']))
            else:
                print('Address ID: {0}'.format(response['address_id']))
                print('First Name: {0}'.format(response['first_name']))
                print('Last Name: {0}'.format(response['last_name']))
                print('Address: {0}'.format(response['address_1']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update Address Book Contact')
    parser.add_argument('--api_key', dest='api_key', help='Route4Me API KEY',
                        type=str, required=True)
    args = parser.parse_args()
    main(args.api_key)
