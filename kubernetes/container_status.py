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

class TypeMeta(object):
	'''A Class representing the TypeMeta structure used by the kubernetes API
	
	TypeMeta is shared by all objects sent to, or returned from the client.

	The TypeMeta structure exposes the following properties:

	TypeMeta.Kind
	TypeMeta.ID
	TypeMeta.UID
	TypeMeta.CreationTimestamp
	TypeMeta.SelfLink
	TypeMeta.ResourceVersion
	TypeMeta.APIVersion
	TypeMeta.Namespace
	TypeMeta.Annotations

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes TypeMeta.

		Args:
		  Kind:
		  ID:
		  UID:
		  CreationTimestamp:
		  SelfLink:
		  ResourceVersion:
		  APIVersion:
		  Namespace:
		  Annotations:
			Annotations are unstructured key value data stored with a resource that may be set by
			external tooling. They are not queryable and should be preserved when modifying
			objects.
		'''

		param_defaults = {
			'Kind': 						None,
			'ID':							None,
			'UID':							None,
			'CreationTimestamp':			None,
			'SelfLink':						None,
			'ResourceVersion':				None,
			'APIVersion':					None,
			'Namespace':					None,
			'Annotations':					None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.Kind == other.Kind and \
					self.ID == other.ID and \
					self.UID == other.UID and \
					self.CreationTimestamp == other.CreationTimestamp and \
					self.SelfLink == other.SelfLink and \
					self.ResourceVersion == other.ResourceVersion and \
					self.APIVersion == other.APIVersion and \
					self.Namespace == other.Namespace and \
					self.Annotations == other.Annotations
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this kubernetes.TypeMeta instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.TypeMeta instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.TypeMeta instance.
	
		Returns:
		  A JSON string representation of this kubernetes.TypeMeta instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.TypeMeta instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.TypeMeta instance
		'''
		data = {}
		if self.Kind:
			data['kind'] = self.Kind
		if self.ID:
			data['id'] = self.ID
		if self.UID:
			data['uid'] = self.UID
		if self.CreationTimestamp:
			data['creationTimestamp'] = self.CreationTimestamp
		if self.SelfLink:
			data['selfLink'] = self.SelfLink
		if self.ResourceVersion:
			data['resourceVersion'] = self.ResourceVersion
		if self.APIVersion:
			data['apiVersion'] = self.APIVersion
		if self.Namespace:
			data['namespace'] = self.Namespace
		if self.Annotations:
			data['annotations'] = self.Annotations
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.TypeMeta instance
		'''
		return TypeMeta(kind=data.get('kind', None),
			id=data.get('id', None),
			uid=data.get('uid', None),
			creationTimestamp=data.get('creationTimestamp', None),
			selfLink=data.get('selfLink', None),
			resourceVersion=data.get('resourceVersion', None),
			apiVersion=data.get('apiVersion', None),
			namespace=data.get('namespace', None),
			annotations=data.get('annotations', None))


class PodStatus(object):
	"""PodStatus represents a status of a pod.
	"""
	
	'''PodWaiting means that we're waiting for the pod to begin running.
	'''
	PodWaiting = "Waiting"

	'''PodRunning means that the pod is up and running.
	'''
	PodRunning = "Running"

	'''PodTerminated means that the pod has stopped.
	'''
	PodTerminated = "Terminated"
		

class ContainerStateWaiting(object):
	'''A Class representing the ContainerStateWaiting structure used by the kubernetes API

	The ContainerStateWaiting structure exposes the following properties:

	ContainerStateWaiting.Reason

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes ContainerStateWaiting.

		Args:
		  reason:
			Reason could be pulling image,
		'''

		param_defaults = {
			'Reason': 						None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.reason == other.reason
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this kubernetes.ContainerStateWaiting instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.ContainerStateWaiting instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ContainerStateWaiting instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ContainerStateWaiting instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ContainerStateWaiting instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ContainerStateWaiting instance
		'''
		data = {}
		if self.Reason:
			data['reason'] = self.Reason
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.ContainerStateWaiting instance
		'''
		return ContainerStateWaiting(Reason=data.get('reason', None))


class ContainerStateRunning(object):
	'''A Class representing the ContainerStateRunning structure used by the kubernetes API

	The ContainerStateRunning structure exposes the following properties:

	ContainerStateRunning.StartedAt

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes ContainerStateRunning.

		Args:
		  StartedAt:
		'''

		param_defaults = {
			'StartedAt': 						None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.StartedAt == other.StartedAt
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this kubernetes.ContainerStateRunning instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.ContainerStateRunning instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ContainerStateRunning instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ContainerStateRunning instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ContainerStateRunning instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ContainerStateRunning instance
		'''
		data = {}
		if self.StartedAt:
			data['startedAt'] = self.StartedAt
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.ContainerStateRunning instance
		'''
		return ContainerStateRunning(StartedAt=data.get('startedAt', None))


class ContainerStateTerminated(object):
	'''A Class representing the ContainerStateTerminated structure used by the kubernetes API
	
	ContainerStateTerminated is shared by all objects sent to, or returned from the client.

	The ContainerStateTerminated structure exposes the following properties:

	ContainerStateTerminated.ExitCode
	ContainerStateTerminated.Signal
	ContainerStateTerminated.Reason
	ContainerStateTerminated.StartedAt
	ContainerStateTerminated.FinishedAt

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes ContainerStateTerminated.

		Args:
		  ExitCode:
		  Signal:
		  Reason:
		  StartedAt:
		  FinishedAt:
		'''

		param_defaults = {
			'ExitCode': 						None,
			'Signal':							None,
			'Reason':							None,
			'StartedAt':						None,
			'FinishedAt':						None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.ExitCode == other.ExitCode and \
					self.Signal == other.Signal and \
					self.Reason == other.Reason and \
					self.StartedAt == other.StartedAt and \
					self.FinishedAt == other.FinishedAt
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this kubernetes.ContainerStateTerminated instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.ContainerStateTerminated instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ContainerStateTerminated instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ContainerStateTerminated instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ContainerStateTerminated instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ContainerStateTerminated instance
		'''
		data = {}
		if self.ExitCode:
			data['exitCode'] = self.ExitCode
		if self.Signal:
			data['signal'] = self.Signal
		if self.Reason:
			data['reason'] = self.Reason
		if self.StartedAt:
			data['startedAt'] = self.StartedAt
		if self.FinishedAt:
			data['finishedAt'] = self.FinishedAt
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.ContainerStateTerminated instance
		'''
		return ContainerStateTerminated(ExitCode=data.get('exitCode', None),
			Signal=data.get('signal', None),
			Reason=data.get('reason', None),
			StartedAt=data.get('startedAt', None),
			FinishedAt=data.get('finishedAt', None))


class ContainerState(object):
	"""A Class representing the ContainerState structure used by the kubernetes API

	The ContainerState structure exposes the following properties:

	ContainerState.Waiting
	ContainerState.Running
	ContainerState.Termination

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ContainerState.
		
		Arg:
		 	Only one of the following ContainerState may be specified.
			If none of them is specified, the default one is ContainerStateWaiting.
		 Waiting:
		 Running:
		 Termination:
		 
		'''

		param_defaults = {
			'Waiting': 							None,
			'Running':	 						None,
			'Termination': 						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Waiting == other.Waiting and \
			self.Running == other.Running and \
			self.Termination == other.Termination
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ContainerState instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ContainerState instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ContainerState instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ContainerState instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ContainerState instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ContainerState instance
		'''
		data = {}
		if self.Waiting:
			data['waiting'] = self.Waiting.AsDict()
		if self.Running:
			data['running'] = self.Running.AsDict()
		if self.Termination:
			data['termination'] = self.Termination.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ContainerState instance
		'''

		waiting = None
		running = None
		termination = None

		if 'waiting' in data:
			from kubernetes import ContainerStateWaiting
			waiting = ContainerStateWaiting.NewFromJsonDict(data['waiting'])

		if 'running' in data:
			from kubernetes import ContainerStateRunning
			running = ContainerStateRunning.NewFromJsonDict(data['running'])

		if 'termination' in data:
			from kubernetes import ContainerStateTerminated
			termination = ContainerStateTerminated.NewFromJsonDict(data['termination'])

		return ContainerState(
					Waiting=waiting,
					Running=running,
					Termination=termination)


class ContainerStatus(object):
	"""A Class representing the ContainerStatus structure used by the kubernetes API

	The ContainerStatus structure exposes the following properties:

	ContainerStatus.State
	ContainerStatus.RestartCount
	ContainerStatus.PodIP
	ContainerStatus.Image

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ContainerStatus.
		
		Arg:
		 
		 State:
		 	TODO(dchen1107): Should we rename PodStatus to a more generic name or have a separate states
			defined for container?
		 RestartCount:
		 PodIP:
		 	TODO(dchen1107): Deprecated this soon once we pull entire PodStatus from node,
			not just PodInfo. Now we need this to remove docker.Container from API
		 Image:
		 	TODO(dchen1107): Once we have done with integration with cadvisor, resource
			usage should be included.
		'''

		param_defaults = {
			'State': 							None,
			'RestartCount':	 					None,
			'PodIP': 							None,
			'Image':							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.State == other.State and \
			self.RestartCount == other.RestartCount and \
			self.PodIP == other.PodIP and \
			self.Image == other.Image
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ContainerStatus instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ContainerStatus instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ContainerStatus instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ContainerStatus instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ContainerStatus instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ContainerStatus instance
		'''
		data = {}
		if self.State:
			data['state'] = self.State.AsDict()
		if self.RestartCount:
			data['restartCount'] = self.RestartCount
		if self.PodIP:
			data['podIP'] = self.PodIP
		if self.Image:
			data['image'] = self.Image
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ContainerStatus instance
		'''

		state = None

		if 'state' in data:
			from kubernetes import ContainerState
			state = ContainerState.NewFromJsonDict(data['state'])

		return ContainerStatus(
					State=state,
					RestartCount=data.get('restartCount', None),
					PodIP=data.get('podIP', None),
					Image=data.get('image', None))
