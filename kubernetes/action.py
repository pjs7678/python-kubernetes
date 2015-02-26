#!/usr/bin/env python
#
# Copyright 2014 Cosmos.io
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from kubernetes import simplejson

class EnvVar(object):
	"""A Class representing the EnvVar structure used by the kubernetes API
	
	EnvVar represents an environment variable present in a Container.

	The EnvVar structure exposes the following properties:

	EnvVar.Name
	EnvVar.Value

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete EnvVar.
		
		Arg:
		 Name:
		 	Required: This must be a C_IDENTIFIER.
		 Value:
		 	Optional: defaults to "".
		'''
		
		param_defaults = {
			'Name': 					None,
			'Value': 					""}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Name == other.Name and \
			self.Value == other.Value
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.EnvVar instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.EnvVar instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.EnvVar instance.
	
		Returns:
		  A JSON string representation of this kubernetes.EnvVar instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.EnvVar instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.EnvVar instance
		'''
		data = {}
		if self.Name:
			data['name'] = self.Name
		if self.Value:
			data['value'] = self.Value
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.EnvVar instance
		'''
		return EnvVar(Name=data.get('name', None),
					Value=data.get('value', ""))

class HTTPGetAction(object):
	"""A Class representing the HTTPGetAction structure used by the kubernetes API
	
	HTTPGetAction describes an action based on HTTP Get requests.

	The HTTPGetAction structure exposes the following properties:

	HTTPGetAction.Path
	HTTPGetAction.Port
	HTTPGetAction.Host

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete HTTPGetAction.
		
		Arg:
		 Path:
		 	Optional: Path to access on the HTTP server.
		 Port:
		 	Required: Name or number of the port to access on the container.
		 Host:
		 	Optional: Host name to connect to, defaults to the pod IP.
		'''
		
		param_defaults = {
			'Path': 					None,
			'Port': 					None,
			'Host': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Path == other.Path and \
			self.Port == other.Port and \
			self.Host == other.Host
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.HTTPGetAction instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.HTTPGetAction instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.HTTPGetAction instance.
	
		Returns:
		  A JSON string representation of this kubernetes.HTTPGetAction instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.HTTPGetAction instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.HTTPGetAction instance
		'''
		data = {}
		if self.Path:
			data['path'] = self.Path
		if self.Port:
			data['port'] = self.Port
		if self.Host:
			data['host'] = self.Host
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.HTTPGetAction instance
		'''
		return HTTPGetAction(Path=data.get('path', None),
					Port=data.get('port', None),
					Host=data.get('host', None))

class TCPSocketAction(object):
	"""A Class representing the TCPSocketAction structure used by the kubernetes API
	
	TCPSocketAction describes an action based on opening a socket

	The TCPSocketAction structure exposes the following properties:

	TCPSocketAction.Port

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete TCPSocketAction.
		
		Arg:
		 Port:
		 	Required: Port to connect to.
		'''
		
		param_defaults = {
			'Port': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Port == other.Port
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.TCPSocketAction instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.TCPSocketAction instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.TCPSocketAction instance.
	
		Returns:
		  A JSON string representation of this kubernetes.TCPSocketAction instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.TCPSocketAction instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.TCPSocketAction instance
		'''
		data = {}
		if self.Port:
			data['port'] = self.Port
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.TCPSocketAction instance
		'''
		return TCPSocketAction(Port=data.get('port', None))


class ExecAction(object):
	"""A Class representing the ExecAction structure used by the kubernetes API
	
	ExecAction describes a "run in container" action.

	The ExecAction structure exposes the following properties:

	ExecAction.Command

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ExecAction.
		
		Arg:
		 Command:
		 	Command is the command line to execute inside the container, the working directory for the
			command  is root ('/') in the container's filesystem.  The command is simply exec'd, it is
			not run inside a shell, so traditional shell instructions ('|', etc) won't work.  To use
			a shell, you need to explicitly call out to that shell.
		'''
		
		param_defaults = {
			'Command': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Command == other.Command
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ExecAction instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ExecAction instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ExecAction instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ExecAction instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ExecAction instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ExecAction instance
		'''
		data = {}
		if self.Command:
			data['command'] = self.Command
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ExecAction instance
		'''

		command = None
		if 'command' in data:
			command = [c for c in data['command']]

		return ExecAction(Command=command)

class LivenessProbe(object):
	"""A Class representing the LivenessProbe structure used by the kubernetes API
	
	LivenessProbe describes a liveness probe to be examined to the container.
	TODO: pass structured data to the actions, and document that data here.

	The LivenessProbe structure exposes the following properties:

	LivenessProbe.HTTPGet
	LivenessProbe.TCPSocket
	LivenessProbe.Exec
	LivenessProbe.InitialDelaySeconds

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete LivenessProbe.
		
		Arg:
		 HTTPGet:
		 	HTTPGetProbe parameters, required if Type == 'http'
		 TCPSocket:
		 	TCPSocketProbe parameter, required if Type == 'tcp'
		 Exec:
		 	ExecProbe parameter, required if Type == 'exec'
		 InitialDelaySeconds:
		 	Length of time before health checking is activated.  In seconds.
		'''
		
		param_defaults = {
			'HTTPGet': 							None,
			'TCPSocket': 						None,
			'Exec': 							None,
			'InitialDelaySeconds': 				None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.HTTPGet == other.HTTPGet and \
			self.TCPSocket == other.TCPSocket and \
			self.Exec == other.Exec and \
			self.InitialDelaySeconds == other.InitialDelaySeconds
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.LivenessProbe instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.LivenessProbe instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.LivenessProbe instance.
	
		Returns:
		  A JSON string representation of this kubernetes.LivenessProbe instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.LivenessProbe instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.LivenessProbe instance
		'''
		data = {}
		if self.HTTPGet:
			data['httpGet'] = self.HTTPGet.AsDict()
		if self.TCPSocket:
			data['tcpSocket'] = self.TCPSocket.AsDict()
		if self.Exec:
			data['exec'] = self.Exec.AsDict()
		if self.InitialDelaySeconds:
			data['initialDelaySeconds'] = self.InitialDelaySeconds
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.LivenessProbe instance
		'''

		httpGet = None
		tcpSocket = None
		Exec = None

		if 'httpGet' in data:
			from kubernetes import HttpGetAction
			httpGet = HttpGetAction.NewFromJsonDict(data['httpGet'])

		if 'tcpSocket' in data:
			from kubernetes import TCPSocketAction
			tcpSocket = TCPSocketAction.NewFromJsonDict(data['tcpSocket'])

		if 'exec' in data:
			from kubernetes import ExecAction
			Exec = ExecAction.NewFromJsonDict(data['exec'])

		return LivenessProbe(HTTPGet=httpGet,
					TCPSocket=tcpSocket,
					Exec=Exec,
					InitialDelaySeconds=data.get('initialDelaySeconds', None))
