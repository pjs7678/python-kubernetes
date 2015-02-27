#!/usr/bin/env python

'''Get Pods from Kubernetes'''

__author__ = 'pjs7678@pjs7678'

import requests
import urllib3
urllib3.disable_warnings()

def main():
	r = requests.get('https://10.245.1.2/api/v1beta2/pods', auth=('vagrant', 'vagrant'), verify=False)
	print r.json()

if __name__ == '__main__':
	main()