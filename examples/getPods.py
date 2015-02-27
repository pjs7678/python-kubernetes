#!/usr/bin/env python

'''Get Pods from Kubernetes'''

__author__ = 'pjs7678@pjs7678'

import getopt
import os
import sys
import json
import kubernetes

USAGE = '''Usage: tweet [options] message

  This script get Pods from Kubernetes.

  Options:

    -h --help : print this help
    --url : the kubernetes master host
    --user-id : the kubernetes user id
    --user-pw : the kubernetes user password
    --encoding : the character set encoding used in input strings, e.g. "utf-8". [optional]

  Documentation:

  If either of the command line flags are not present, the environment
  variables KUBERNETESUSERNAME and KUBERNETESPASSWORD will then be checked for your
  user id or user password, respectively.

  If neither the command line flags nor the environment variables are
  present, the .kubernetes_auth file, if it exists, can be used to set the
  default user_id and user_password.  The file should contain the
  following five lines, replacing *User* with your user id, and
  *Password* with your user password:

  A skeletal .kubernetes_auth file:
  {
    "User": "admin",
    "Password": "hdrmCA3OXuL1lq12",
    "CAFile": "/Users/tigmi/.kubernetes.ca.crt",
    "CertFile": "/Users/tigmi/.kubecfg.crt",
    "KeyFile": "/Users/tigmi/.kubecfg.key"
  }
'''

def PrintUsageAndExit():
  print USAGE
  sys.exit(2)

def GetUserIDKeyEnv():
  return os.environ.get("KUBERNETESUSERNAME", None)

def GetUserPasswordEnv():
  return os.environ.get("KUBERNETESPASSWORD", None)

class KubernetesRc(object):
  def __init__(self):
    pass

  def GetUserIdKey(self):
    return self._GetValue('User')

  def GetUserPasswordKey(self):
    return self._GetValue('Password')

  def _GetOption(self, option):
    try:
      return self._GetConfig().get(option)
    except:
      return None

  def _GetValue(self, key):
    if os.environ.get('KUBERNETES_PROVIDER') and os.environ.get('KUBERNETES_PROVIDER') is 'vagrant':
      path = '~/.kubernetes_vagrant_auth'
    else:
      path = '~/.kubernetes_auth'
    with open(os.path.expanduser(path)) as f:
      value = json.load(f)[key]
    return value

def main():
  try:
    shortflags = 'h'
    longflags = ['help', 'user-id=', 'user-pw=', 'url=', 'encoding=']
    opts, args = getopt.gnu_getopt(sys.argv[1:], shortflags, longflags)
  except getopt.GetoptError:
    PrintUsageAndExit()
  user_idflag = None
  user_passwordflag = None
  encoding = None
  url = None
  for o, a in opts:
    if o in ("-h", "--help"):
      PrintUsageAndExit()
    if o in ("--user-id"):
      user_idflag = a
    if o in ("--user-pw"):
      user_passwordflag = a
    if o in ("--encoding"):
      encoding = a
    if o in ("--url"):
      url = a

  if url is None:
    PrintUsageAndExit()

  rc = KubernetesRc()
  user_id = user_idflag or GetUserIDKeyEnv() or rc.GetUserIdKey()
  user_password = user_passwordflag or GetUserPasswordEnv() or rc.GetUserPasswordKey()

  print user_id
  print user_password
  
  if not user_id or not user_password:
    PrintUsageAndExit()

  api = kubernetes.Api(user_id=user_id, user_password=user_password,
                    input_encoding=encoding,
                    base_url=url,
                    debugHTTP=True)
  try:
    pod_list = api.GetPods()
  except UnicodeDecodeError:
    print "Error!! "
    sys.exit(2)
  print "GetPods: %s" % (pod_list.AsJsonString())

  try:
    pod_list = api.GetReplicationControllers()
  except UnicodeDecodeError:
    print "Error!! "
    sys.exit(2)
  print "GetReplicationControllers: %s" % (pod_list.AsJsonString())

  try:
    pod_list = api.GetServices()
  except UnicodeDecodeError:
    print "Error!! "
    sys.exit(2)
  print "GetServices: %s" % (pod_list.AsJsonString())

if __name__ == "__main__":
  main()
