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

class RestartPolicyAlways(object):
	"""A Class representing the RestartPolicyAlways structure used by the kubernetes API

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete RestartPolicyAlways.
		'''

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		return True

	def __str__(self):
		'''A string representation of this Kubernetes.RestartPolicyAlways instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.RestartPolicyAlways instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.RestartPolicyAlways instance.
	
		Returns:
		  A JSON string representation of this kubernetes.RestartPolicyAlways instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.RestartPolicyAlways instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.RestartPolicyAlways instance
		'''
		data = {}
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.RestartPolicyAlways instance
		'''
		return RestartPolicyAlways()

class RestartPolicyOnFailure(object):
	"""A Class representing the RestartPolicyOnFailure structure used by the kubernetes API

		TODO(dchen1107): Define what kinds of failures should restart.
		TODO(dchen1107): Decide whether to support policy knobs, and, if so, which ones.
	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete RestartPolicyOnFailure.
		'''

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		return True

	def __str__(self):
		'''A string representation of this Kubernetes.RestartPolicyOnFailure instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.RestartPolicyOnFailure instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.RestartPolicyOnFailure instance.
	
		Returns:
		  A JSON string representation of this kubernetes.RestartPolicyOnFailure instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.RestartPolicyOnFailure instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.RestartPolicyOnFailure instance
		'''
		data = {}
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.RestartPolicyOnFailure instance
		'''
		return RestartPolicyOnFailure()


class RestartPolicyNever(object):
	"""A Class representing the RestartPolicyNever structure used by the kubernetes API

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete RestartPolicyNever.
		'''

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		return True

	def __str__(self):
		'''A string representation of this Kubernetes.RestartPolicyNever instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.RestartPolicyNever instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.RestartPolicyNever instance.
	
		Returns:
		  A JSON string representation of this kubernetes.RestartPolicyNever instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.RestartPolicyNever instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.RestartPolicyNever instance
		'''
		data = {}
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.RestartPolicyNever instance
		'''
		return RestartPolicyNever()


class RestartPolicy(object):
	"""A Class representing the RestartPolicy structure used by the kubernetes API

	The RestartPolicy structure exposes the following properties:

	RestartPolicy.Always
	RestartPolicy.OnFailure
	RestartPolicy.Never

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete RestartPolicy.
		
		Arg:
		 
		 Always:
		 OnFailure:
		 Never:
		 	Only one of the following restart policies may be specified.
			If none of the following policies is specified, the default one
			is RestartPolicyAlways.
		 
		'''
		
		param_defaults = {
			'Always': 						None,
			'OnFailure':	 				None,
			'Never': 						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Always == other.Always and \
			self.OnFailure == other.OnFailure and \
			self.Never == other.Never
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.RestartPolicy instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.RestartPolicy instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.RestartPolicy instance.
	
		Returns:
		  A JSON string representation of this kubernetes.RestartPolicy instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.RestartPolicy instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.RestartPolicy instance
		'''
		data = {}
		if self.Always:
			data['always'] = self.Always.AsDict()
		if self.OnFailure:
			data['onFailure'] = self.OnFailure.AsDict()
		if self.Never:
			data['never'] = self.Never.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.RestartPolicy instance
		'''

		always = None
		onFailure = None
		never = None

		if 'always' in data:
			from kubernetes import RestartPolicyAlways
			always = RestartPolicyAlways.NewFromJsonDict(data['always'])

		if 'onFailure' in data:
			from kubernetes import RestartPolicyOnFailure
			onFailure = RestartPolicyOnFailure.NewFromJsonDict(data['onFailure'])

		if 'never' in data:
			from kubernetes import RestartPolicyNever
			never = RestartPolicyNever.NewFromJsonDict(data['never'])

		return RestartPolicy(
					Always=always,
					OnFailure=onFailure,
					Never=never)

class PodState(object):
	"""A Class representing the PodState structure used by the kubernetes API
	
	PodState is the state of a pod, used as either input (desired state) or output (current state).

	The PodState structure exposes the following properties:

	PodState.Manifest
	PodState.Status
	PodState.Host
	PodState.HostIP
	PodState.PodIP
	PodState.Info

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete PodState.
		
		Arg:
		 
		 Manifest:
		 Status:
		 Host:
		 HostIP:
		 PodIP
		 Info:
		 	The key of this map is the *name* of the container within the manifest; it has one
			entry per container in the manifest. The value of this map is currently the output
			of `docker inspect`. This output format is *not* final and should not be relied
			upon.
			TODO: Make real decisions about what our info should look like. Re-enable fuzz test
			when we have done this.
		 
		'''
		
		param_defaults = {
			'Manifest': 					None,
			'Status':	 					None,
			'Host': 						None,
			'HostIP': 						None,
			'PodIP': 						None,
			'Info': 						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Manifest == other.Manifest and \
			self.Status == other.Status and \
			self.Host == other.Host and \
			self.HostIP == other.HostIP and \
			self.PodIP == other.PodIP and \
			self.Info == other.Info
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.PodState instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.PodState instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.PodState instance.
	
		Returns:
		  A JSON string representation of this kubernetes.PodState instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.PodState instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.PodState instance
		'''

		data = {}
		if self.Manifest:
			data['manifest'] = self.Manifest.AsDict()
		if self.Status:
			data['status'] = self.Status
		if self.Host:
			data['host'] = self.Host
		if self.HostIP:
			data['hostIP'] = self.HostIP
		if self.PodIP:
			data['podIP'] = self.PodIP
		if self.Info:
			data['info'] = dict([(key, containerStatus.AsDict()) for (key, containerStatus) in self.Info.iteritems()])

		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.PodState instance
		'''

		manifest = None
		info = None

		if 'manifest' in data:
			from kubernetes import ContainerManifest
			manifest = ContainerManifest.NewFromJsonDict(data['manifest'])

		if 'info' in data:
			from kubernetes import ContainerStatus
			info = dict([(key, ContainerStatus.NewFromJsonDict(cs)) for (key, cs) in data['info'].iteritems()])

		return PodState(
					Manifest=manifest,
					Status=data.get('status', None),
					Host=data.get('host', None),
					HostIP=data.get('hostIP', None),
					PodIP=data.get('podIP', None),
					Info=info)


from kubernetes import TypeMeta
class PodList(TypeMeta):
	"""A Class representing the PodList structure used by the kubernetes API
	
	PodList is a list of Pods.

	The PodList structure exposes the following properties:

	PodList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete PodList.
		
		Arg:
		 
		 Items:
		 
		'''
		
		param_defaults = {
			'Items': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(PodList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(PodList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.PodList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.PodList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.PodList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.PodList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(PodList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.PodList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.PodList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [pod.AsDict() for pod in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.PodList instance
		'''

		items = None

		if 'items' in data and data['items']:
			from kubernetes import Pod
			items = [Pod.NewFromJsonDict(pod) for pod in data['items']]

		return PodList(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					Items=items)

class Pod(TypeMeta):
	"""A Class representing the Pod structure used by the kubernetes API
	
	Pod is a collection of containers, used as either input (create, update) or as output (list, get).

	The Pod structure exposes the following properties:

	Pod.Labels
	Pod.DesiredState
	Pod.CurrentState

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Pod.
		
		Arg:
		 
		 Labels:
		 DesiredState:
		 CurrentState:
		 
		'''
		
		param_defaults = {
			'Labels': 							None,
			'DesiredState': 					None,
			'CurrentState': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(Pod, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Labels == other.Labels and \
			self.DesiredState == other.DesiredState and \
			self.CurrentState == other.CurrentState and \
			super(Pod, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Pod instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Pod instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Pod instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Pod instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(PodList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Pod instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Pod instance
		'''
		data = {}
		if self.Labels:
			data['labels'] = self.Labels
		if self.DesiredState:
			data['desiredState'] = self.DesiredState.AsDict()
		if self.CurrentState:
			data['currentState'] = self.CurrentState.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Pod instance
		'''

		desiredState = None
		currentState = None

		if 'desiredState' in data:
			from kubernetes import PodState
			desiredState = PodState.NewFromJsonDict(data['desiredState'])

		if 'currentState' in data:
			from kubernetes import PodState
			currentState = PodState.NewFromJsonDict(data['currentState'])

		return Pod(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					Labels=data.get('labels', None),
					DesiredState=desiredState,
					CurrentState=currentState)


class ReplicationControllerState(object):
	"""A Class representing the ReplicationControllerState structure used by the kubernetes API
	
	ReplicationControllerState is the state of a pod, used as either input (desired state) or output (current state).

	The ReplicationControllerState structure exposes the following properties:

	ReplicationControllerState.Replicas
	ReplicationControllerState.ReplicaSelector
	ReplicationControllerState.PodTemplate

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ReplicationControllerState.
		
		Arg:
		 Replicas:
		 ReplicaSelector
		 PodTemplate:
		 	
		 
		'''
		
		param_defaults = {
			'Replicas': 						None,
			'ReplicaSelector': 					None,
			'PodTemplate': 						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Replicas == other.Replicas and \
			self.ReplicaSelector == other.ReplicaSelector and \
			self.PodTemplate == other.PodTemplate
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ReplicationControllerState instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ReplicationControllerState instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ReplicationControllerState instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ReplicationControllerState instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ReplicationControllerState instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ReplicationControllerState instance
		'''
		data = {}
		if self.Replicas:
			data['replicas'] = self.Replicas
		if self.ReplicaSelector:
			data['replicaSelector'] = self.ReplicaSelector
		if self.PodTemplate:
			data['podTemplate'] = self.PodTemplate.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ReplicationControllerState instance
		'''

		podTemplate = None
		if 'podTemplate' in data:
			from kubernetes import PodTemplate
			podTemplate = PodTemplate.NewFromJsonDict(data['podTemplate'])

		return ReplicationControllerState(
					Replicas=data.get('replicas', None),
					ReplicaSelector=data.get('replicaSelector', None),
					PodTemplate=podTemplate)


class ReplicationControllerList(TypeMeta):
	"""A Class representing the ReplicationControllerList structure used by the kubernetes API
	
	ReplicationControllerList is a collection of replication controllers.

	The ReplicationControllerList structure exposes the following properties:

	ReplicationControllerList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ReplicationControllerList.
		
		Arg:
		 
		 Items:
		 
		'''
		
		param_defaults = {
			'Items': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(ReplicationControllerList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(ReplicationControllerList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ReplicationControllerList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ReplicationControllerList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ReplicationControllerList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ReplicationControllerList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(PodList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ReplicationControllerList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ReplicationControllerList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [replicationController.AsDict() for replicationController in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ReplicationControllerList instance
		'''

		items = None

		if 'items' in data:
			from kubernetes import ReplicationController
			items = [ReplicationController.NewFromJsonDict(r) for r in data['items']]

		return ReplicationControllerList(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					Items=items)


class ReplicationController(TypeMeta):
	"""A Class representing the ReplicationController structure used by the kubernetes API
	
	ReplicationController represents the configuration of a replication controller.

	The ReplicationController structure exposes the following properties:

	ReplicationController.DesiredState
	ReplicationController.CurrentState
	ReplicationController.Labels

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ReplicationController.
		
		Arg:
		 
		 DesiredState:
		 CurrentState:
		 Labels:
		 
		'''
		
		param_defaults = {
			'DesiredState': 							None,
			'CurrentState': 							None,
			'Labels': 									None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(ReplicationController, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.DesiredState == other.DesiredState and \
			self.CurrentState == other.CurrentState and \
			self.Labels == other.Labels and \
			super(ReplicationController, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ReplicationController instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ReplicationController instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ReplicationController instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ReplicationController instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(PodList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ReplicationController instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ReplicationController instance
		'''
		data = {}
		if self.DesiredState:
			data['desiredState'] = self.DesiredState.AsDict()
		if self.CurrentState:
			data['currentState'] = self.CurrentState.AsDict()
		if self.Labels:
			data['labels'] = self.Labels
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ReplicationController instance
		'''

		desiredState = None
		currentState = None

		if 'desiredState' in data:
			from kubernetes import ReplicationControllerState
			desiredState = ReplicationControllerState.NewFromJsonDict(data['desiredState'])

		if 'currentState' in data:
			from kubernetes import ReplicationControllerState
			currentState = ReplicationControllerState.NewFromJsonDict(data['currentState'])


		return ReplicationController(
					DesiredState=desiredState,
					CurrentState=currentState,
					Labels=data.get('labels', None))

class PodTemplate(object):
	"""A Class representing the PodTemplate structure used by the kubernetes API
	
	PodTemplate holds the information used for creating pods.

	The PodTemplate structure exposes the following properties:

	PodTemplate.DesiredState
	PodTemplate.Labels

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete PodTemplate.
		
		Arg:
		 DesiredState:
		 Labels
		 	
		 
		'''
		
		param_defaults = {
			'DesiredState': 						None,
			'Labels': 								None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.DesiredState == other.DesiredState and \
			self.Labels == other.Labels
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.PodTemplate instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.PodTemplate instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.PodTemplate instance.
	
		Returns:
		  A JSON string representation of this kubernetes.PodTemplate instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.PodTemplate instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.PodTemplate instance
		'''
		data = {}
		if self.DesiredState:
			data['desiredState'] = self.DesiredState.AsDict()
		if self.Labels:
			data['labels'] = self.Labels
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.PodTemplate instance
		'''

		desiredState = None
		if 'desiredState' in data:
			from kubernetes import PodState
			desiredState = PodState.NewFromJsonDict(data['desiredState'])

		return PodTemplate(
					DesiredState=desiredState,
					Labels=data.get('labels', None))
