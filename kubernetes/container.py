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

class PulllPolicy(object):
	'''PullPolicy describes a policy for if/when to pull a container image
	'''

	'''Always attempt to pull the latest image.  Container will fail If the pull fails.
	'''
	PullAlways = "PullAlways"

	'''Never pull an image, only use a local image.  Container will fail if the image isn't present
	'''
	PullNever = "PullNever"

	'''Pull if the image isn't present on disk. Container will fail if the image isn't present and the pull fails.
	'''
	PullIfNotPresent = "PullIfNotPresent"

class Container(object):
	"""A Class representing the Container structure used by the kubernetes API
	
	Container represents a single container that is expected to be run on the host.

	The Container structure exposes the following properties:

	Container.Name
	Container.Image
	Container.Command
	Container.WorkingDir
	Container.Ports
	Container.Env
	Container.Memory
	Container.CPU
	Container.VolumeMounts
	Container.LivenessProb
	Container.Lifecycle
	Container.Privileged
	Container.ImagePullPolicy

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Container.
		
		Arg:
		 Name:
		 	Required: This must be a DNS_LABEL.  Each container in a pod must have a unique name.
		 Image:
		 	Required.
		 Command:
		 	Optional: Defaults to whatever is defined in the image.
		 WorkingDir:
		 	Optional: Defaults to Docker's default.
		 Ports:
		 Env:
		 Memory:
		 	Optional: Defaults to unlimited.
		 CPU:
		 	Optional: Defaults to unlimited.
		 VolumeMounts:
		 LivenessProb:
		 Lifecycle:
		 Privileged:
		 	Optional: Default to false.
		 ImagePullPolicy:
		 	Optional: Policy for pulling images for this container
		'''
		
		param_defaults = {
			'Name': 							None,
			'Image': 							None,
			'Command': 							None,
			'WorkingDir': 						None,
			'Ports': 							None,
			'Env':	 							None,
			'Memory': 							None,
			'CPU': 								None,
			'VolumeMounts': 					None,
			'LivenessProb': 					None,
			'Lifecycle':	 					None,
			'Privileged':	 					None,
			'ImagePullPolicy':					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Name == other.Name and \
			self.Image == other.Image and \
			self.Command == other.Command and \
			self.WorkingDir == other.WorkingDir and \
			self.Ports == other.Ports and \
			self.Env == other.Env and \
			self.Memory == other.Memory and \
			self.CPU == other.CPU and \
			self.VolumeMounts == other.VolumeMounts and \
			self.LivenessProb == other.LivenessProb and \
			self.Lifecycle == other.Lifecycle and \
			self.Privileged == other.Privileged and \
			self.ImagePullPolicy == other.ImagePullPolicy
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Container instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Container instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Container instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Container instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Container instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Container instance
		'''
		data = {}
		if self.Name:
			data['name'] = self.Name
		if self.Image:
			data['image'] = self.Image
		if self.Command:
			data['command'] = self.Command
		if self.WorkingDir:
			data['workingDir'] = self.WorkingDir
		if self.Ports:
			data['ports'] = [port.AsDict() for port in self.Ports]
		if self.Env:
			data['env'] = [env.AsDict() for env in self.Env]
		if self.Memory:
			data['memory'] = self.Memory
		if self.CPU:
			data['cpu'] = self.CPU
		if self.VolumeMounts:
			data['volumeMounts'] = [volumeMount.AsDict() for volumeMount in self.VolumeMounts]
		if self.LivenessProb:
			data['livenessProb'] = self.LivenessProb
		if self.Lifecycle:
			data['lifecycle'] = self.Lifecycle
		if self.Privileged:
			data['privileged'] = self.Privileged
		if self.ImagePullPolicy:
			data['imagePullPolicy'] = self.ImagePullPolicy
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Container instance
		'''

		command = None
		ports = None
		env = None
		volumeMounts = None
		livenessProb = None
		lifecyle = None

		if 'command' in data:
			command = [c for c in data['command']]

		if 'ports' in data:
			from kubernetes import Port
			ports = [Port.NewFromJsonDict(port) for port in data['ports']]

		if 'env' in data:
			from kubernetes import EnvVar
			env = [EnvVar.NewFromJsonDict(e) for e in data['env']]

		if 'volumeMounts' in data:
			from kubernetes import VolumeMount
			volumeMounts = [VolumeMount.NewFromJsonDict(volumeMount) for volumeMount in data['volumeMount']]

		if 'livenessProb' in data:
			from kubernetes import LivenessProb
			livenessProb = LivenessProb.NewFromJsonDict(data['livenessProb'])
	
		if 'lifecyle' in data:
			from kubernetes import Lifecyle
			lifecyle = Lifecyle.NewFromJsonDict(data['lifecyle'])

		return Container(Name=data.get('name', None),
					Image=data.get('image', None),
					Command=command,
					WorkingDir=data.get('workingDir', None),
					Ports=ports,
					Env=env,
					Memory=data.get('memory', None),
					CPU=data.get('cpu', None),
					VolumeMounts=volumeMounts,
					LivenessProb=livenessProb,
					Lifecyle=lifecyle,
					Privileged=data.get('privileged', False),
					ImagePullPolicy=data.get('imagePullPolicy', None))

class Handler(object):
	'''A Class representing the Handler structure used by the kubernetes API
	
	Handler defines a specific action that should be taken
	TODO: pass structured data to these actions, and document that data here.

	The Handler structure exposes the following properties:

	Handler.Exec
	Handler.HTTPGet

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes Handler.

		One and only one of the following should be specified.
		Arg:
		 Exec:
			Exec specifies the action to take.
		 HTTPGet:
			HTTPGet specifies the http request to perform.
		'''

		param_defaults = {
			'Exec': 				None,
			'HTTPGet':				None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.Exec == other.Exec and \
					self.HTTPGet == other.HTTPGet
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this kubernetes.Handler instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.Handler instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Handler instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Handler instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Handler instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Handler instance
		'''
		data = {}
		if self.Exec:
			data['exec'] = self.Exec.AsDict()
		if self.HTTPGet:
			data['httpGet'] = self.HTTPGet.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.Handler instance
		'''

		Exec = None
		httpGet = None

		if 'exec' in data:
			from kubernetes import ExecAction
			Exec = ExecAction.NewFromJsonDict(data['exec'])

		if 'httpGet' in data:
			from kubernetes import HTTPGetAction
			httpGet = HTTPGetAction.NewFromJsonDict(data['httpGet'])

		return Handler(Exec=Exec,
			HTTPGet=httpGet)


class Lifecyle(object):
	'''A Class representing the Lifecyle structure used by the kubernetes API
	
	Lifecycle describes actions that the management system should take in response to container lifecycle
	events.  For the PostStart and PreStop lifecycle handlers, management of the container blocks
	until the action is complete, unless the container process fails, in which case the handler is aborted.

	The Lifecyle structure exposes the following properties:

	Lifecyle.PostStart
	Lifecyle.PreStop

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes Lifecyle.

		Arg:
		 PostStart:
		 	PostStart is called immediately after a container is created.  If the handler fails, the container
			is terminated and restarted.
		 PreStop:
			PreStop is called immediately before a container is terminated.  The reason for termination is
			passed to the handler.  Regardless of the outcome of the handler, the container is eventually terminated.
		'''

		param_defaults = {
			'PostStart': 			None,
			'PreStop':				None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.PostStart == other.PostStart and \
					self.PreStop == other.PreStop
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this kubernetes.Lifecyle instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.Lifecyle instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Lifecyle instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Lifecyle instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Lifecyle instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Lifecyle instance
		'''
		data = {}
		if self.PostStart:
			data['postStart'] = self.PostStart.AsDict()
		if self.PreStop:
			data['preStop'] = self.PreStop.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.Lifecyle instance
		'''

		postStart = None
		preStop = None

		if 'postStart' in data:
			from kubernetes import Handler
			postStart = Handler.NewFromJsonDict(data['postStart'])

		if 'preStop' in data:
			from kubernetes import Handler
			preStop = Handler.NewFromJsonDict(data['preStop'])

		return Lifecyle(PostStart=postStart,
			PreStop=preStop)
