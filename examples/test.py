#!/usr/bin/env python

'''Get Pods from Kubernetes'''

__author__ = 'pjs7678@cosmos.io'

import requests
import urllib3
urllib3.disable_warnings()

def main():
	r = requests.get('https://107.178.217.20/api/v1beta1/pods', auth=('admin', 'hdrmCA3OXuL1lq12'), verify=False)
	print r.json()

if __name__ == '__main__':
	main()