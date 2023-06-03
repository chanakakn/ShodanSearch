#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shodan
import re
import argparse
import time
import logging

class ShodanSearch:
    """Class for searching in Shodan"""
    def __init__(self, api_key):
        self.api = shodan.Shodan(api_key)

    def search(self, search):
        """Search based on the search string"""
        try:
            result = self.api.search(str(search))
            return result
        except shodan.APIError as e:
            logging.error('Shodan API Error: %s' % e)
            result = []
            return result

    def get_host_info(self, ip):
        """Get information about a host based on its IP address"""
        try:
            host = self.api.host(ip)
            return host
        except shodan.APIError as e:
            logging.error('Shodan API Error: %s' % e)
            host = []
            return host


def print_banner():
    print("""
         ____  _               _             _____      
        / ___|| |__   ___   __| | __ _ _ __
        \___ \| '_ \ / _ \ / _` |/ _` | '_ \  
         ___) | | | | (_) | (_| | (_| | | | |  
        |____/|_| |_|\___/ \__,_|\__,_|_| |_|
                                       Search
    """)


def print_search_result(result):
    if len(result) != 0:
        print('Quantity of results found: %s' % result['total'])
        for i in result['matches']:
            print('City: %s' % i.get('city', 'Unknown'))
            print('Country: %s' % i.get('country_name', 'Unknown'))
            print('IP: %s' % i.get('ip_str'))
            print('O.S: %s' % i.get('os', 'Unknown'))
            print('Port: %s' % i.get('port'))
            print('Hostnames: %s' % i.get('hostnames'))
            print('Latitude: %s' % i.get('latitude', 'Unknown'))
            print('Longitude: %s' % i.get('longitude', 'Unknown'))
            print('Updated: %s' % i.get('updated'))
            print(i['data'])
            print('')
        print(result.keys())
        if 'organizations' in result.keys():
            for key, value in result['organizations'].items():
                print(key + ":" + value)
        if 'countries' in result.keys():
            for key, value in result['countries'].items():
                print(key + ":" + value)
        if 'cities' in result.keys():
            for key, value in result['cities'].items():
                print(key + ":" + value)


def print_host_info(host):
    if len(host) != 0:
        if 'ip' in host.keys():
            print('IP: %s' % host.get('ip_str'))
        if 'country_name' in host.keys():
            print('Country: %s' % host.get('country_name', 'Unknown'))
        if 'country_code' in host.keys():
            print('Country code: %s' % host.get('country_code', 'Unknown'))
        if 'city' in host.keys():
            print('City: %s' % host.get('city', 'Unknown'))
        if 'isp' in host.keys():
            print('ISP: %s' % host.get('isp', 'Unknown'))
        if 'latitude' in host.keys():
            print('Latitude: %s' % host.get('latitude'))
        if 'longitude' in host.keys():
            print('Longitude: %s' % host.get('longitude'))
        if 'hostnames' in host.keys():
            print('Hostnames: %s' % host.get('hostnames'))
        try:
            for i in host['data']:
                print('Port: %s' % i['port'])
                print('Banner: %s' % i['banner'])
                print('')
        except Exception as e:
            pass


def parse_arguments():
    parser = argparse.ArgumentParser(description='ShodanSearch.py - A tool for searching in Shodan.')
    parser.add_argument('option', choices=['-s', '--search', '-h', '--host'], help='Specify the search option.')
    parser.add_argument('query', help='Specify the search query or IP address.')
    return parser.parse_args()


def main():
    logging.basicConfig(filename='shodan_search.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    shodan_search = ShodanSearch(API_KEY)
    args = parse_arguments()

    if args.option in ['-s', '--search']:
        print_banner()
        time.sleep(3)
        try:
            result = shodan_search.search(args.query)
            print_search_result(result)
        except Exception as e:
            logging.error('Exception: %s' % e)
            print('An error occurred while searching.')

    elif args.option in ['-h', '--host']:
        print_banner()
        time.sleep(3)
        try:
            host = shodan_search.get_host_info(args.query)
            print_host_info(host)
        except Exception as e:
            logging.error('Exception: %s' % e)
            print('An error occurred while retrieving host information.')

if __name__ == '__main__':
    main()
