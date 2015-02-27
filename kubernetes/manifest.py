#!/usr/bin/env python
#
# Copyright 2014 tigmi
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

class ContainerManifest(object):
	"""A Class representing the ContainerManifest structure used by the kubernetes API
	
	ContainerManifest corresponds to the Container Manifest format, documented at:
	https://developers.google.com/compute/docs/containers/container_vms#container_manifest
	This is used as the representation of Kubernetes workloads.
	DEPRECATED: Replaced with BoundPod

	The ContainerManifest structure exposes the following properties:

	ContainerManifest.Version
	ContainerManifest.ID
	ContainerManifest.UUID
	ContainerManifest.Volumes
	ContainerManifest.Containers
	ContainerManifest.RestartPolicy

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ContainerManifest.
		
		Arg:
		 Version:
		 	Required: This must be a supported version string, such as "v1beta1".
		 ID:
		 	Required: This must be a DNS_SUBDOMAIN.
			TODO: ID on Manifest is deprecated and will be removed in the future.
		 UUID:
		 	TODO: UUID on Manifest is deprecated in the future once we are done
			with the API refactoring. It is required for now to determine the instance
			of a Pod.
		 Volumes:
		 Containers:
		 RestartPolicy:
		'''
		
		param_defaults = {
			'Version': 							None,
			'ID': 								None,
			'UUID': 							None,
			'Volumes': 							None,
			'Containers': 						None,
			'RestartPolicy': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Version == other.Version and \
			self.ID == other.ID and \
			self.UUID == other.UUID and \
			self.Volumes == other.Volumes and \
			self.Containers == other.Containers and \
			self.RestartPolicy == other.RestartPolicy
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ContainerManifest instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ContainerManifest instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ContainerManifest instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ContainerManifest instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ContainerManifest instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ContainerManifest instance
		'''
		data = {}
		if self.Version:
			data['version'] = self.Version
		if self.ID:
			data['id'] = self.ID
		if self.UUID:
			data['uuid'] = self.UUID
		if self.Volumes:
			data['volumes'] = [volume.AsDict() for volume in self.Volumes]
		if self.Containers:
			data['containers'] = [container.AsDict() for container in self.Containers]
		if self.RestartPolicy:
			data['restartPolicy'] = self.RestartPolicy.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ContainerManifest instance
		'''

		volumes = None
		containers = None
		restartPolicy = None

		if 'volumes' in data and data['volumes']:
			from kubernetes import Volume
			volumes = [Volume.NewFromJsonDict(volume) for volume in data['volumes']]

		if 'containers' in data and data['containers']:
			from kubernetes import Container
			containers = [Container.NewFromJsonDict(container) for container in data['containers']]

		if 'restartPolicy' in data:
			from kubernetes import RestartPolicy
			restartPolicy = RestartPolicy.NewFromJsonDict(data['restartPolicy'])

		return ContainerManifest(Version=data.get('version', None),
					ID=data.get('id', None),
					UUID=data.get('uuid', None),
					Volumes=volumes,
					Containers=containers,
					RestartPolicy=restartPolicy)


from kubernetes import TypeMeta
class ContainerManifestList(TypeMeta):
	"""A Class representing the ContainerManifestList structure used by the kubernetes API
	
	ContainerManifestList is used to communicate container manifests to kubelet.
	DEPRECATED: Replaced with BoundPods

	The ContainerManifestList structure exposes the following properties:

	ContainerManifestList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ContainerManifestList.
		
		Arg:
		 Items:
		'''
		
		param_defaults = {
			'Items': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(ContainerManifestList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(ContainerManifestList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ContainerManifestList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ContainerManifestList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ContainerManifestList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ContainerManifestList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(ContainerManifestList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ContainerManifestList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ContainerManifestList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [containerManifest.AsDict() for containerManifest in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ContainerManifestList instance
		'''

		items = None

		if 'items' in data:
			from kubernetes import ContainerManifest
			items = [ContainerManifest.NewFromJsonDict(containerManifest) for containerManifest in data['items']]

		return ContainerManifestList(
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

'''Backported from v1beta3 to replace ContainerManifest'''

class PodSpec(object):
	"""A Class representing the PodSpec structure used by the kubernetes API
	
	PodSpec is a description of a pod

	The PodSpec structure exposes the following properties:

	PodSpec.Volumes
	PodSpec.Containers
	PodSpec.RestartPolicy

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete PodSpec.
		
		Arg:
		 Volumes:
		 Containers:
		 RestartPolicy:
		'''
		
		param_defaults = {
			'Volumes': 							None,
			'Containers': 						None,
			'RestartPolicy': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Volumes == other.Volumes and \
			self.Containers == other.Containers and \
			self.RestartPolicy == other.RestartPolicy
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.PodSpec instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.PodSpec instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.PodSpec instance.
	
		Returns:
		  A JSON string representation of this kubernetes.PodSpec instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.PodSpec instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.PodSpec instance
		'''
		data = {}
		if self.Volumes:
			data['volumes'] = [volume.AsDict() for volume in self.Volumes]
		if self.Containers:
			data['containers'] = [container.AsDict for container in self.Containers]
		if self.RestartPolicy:
			data['restartPolicy'] = self.RestartPolicy.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.PodSpec instance
		'''

		volumes = None
		containers = None
		restartPolicy = None

		if 'volumes' in data:
			from kubernetes import Volume
			volumes = [Volume.NewFromJsonDict(volume) for volume in data['volumes']]

		if 'containers' in data:
			from kubernetes import Container
			containers = [Container.NewFromJsonDict(container) for container in data['containers']]

		if 'restartPolicy' in data:
			from kubernetes import RestartPolicy
			restartPolicy = RestartPolicy.NewFromJsonDict(data['restartPolicy'])

		return PodSpec(
					Volumes=volumes,
					Containers=containers,
					RestartPolicy=restartPolicy)


class BoundPod(TypeMeta):
	"""A Class representing the BoundPod structure used by the kubernetes API
	
	BoundPod is a collection of containers that should be run on a host. A BoundPod
	defines how a Pod may change after a Binding is created. A Pod is a request to
	execute a pod, whereas a BoundPod is the specification that would be run on a server.

	The BoundPod structure exposes the following properties:

	BoundPod.Spec

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete BoundPod.
		
		Arg:
		 Spec:
		 	Spec defines the behavior of a pod.
		'''
		
		param_defaults = {
			'Spec': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(BoundPod, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Spec == other.Spec and \
			super(BoundPod, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.BoundPod instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.BoundPod instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.BoundPod instance.
	
		Returns:
		  A JSON string representation of this kubernetes.BoundPod instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(BoundPod, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.BoundPod instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.BoundPod instance
		'''
		data = {}
		if self.Spec:
			data['spec'] = self.Spec.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.BoundPod instance
		'''

		spec = None

		if 'spec' in data:
			from kubernetes import PodSpec
			spec = PodSpec.NewFromJsonDict(data['spec'])

		return BoundPod(
			Kind=data.get('kind', None),
			ID=data.get('id', None),
			UID=data.get('uid', None),
			CreationTimestamp=data.get('creationTimestamp', None),
			SelfLink=data.get('selfLink', None),
			ResourceVersion=data.get('resourceVersion', None),
			APIVersion=data.get('apiVersion', None),
			Namespace=data.get('namespace', None),
			Annotations=data.get('annotations', None),

			Spec=spec)


class BoundPods(TypeMeta):
	"""A Class representing the BoundPods structure used by the kubernetes API
	
	BoundPods is a list of Pods bound to a common server. The resource version of
	the pod list is guaranteed to only change when the list of bound pods changes.

	The BoundPods structure exposes the following properties:

	boundPods.Host
	boundPods.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete BoundPods.
		
		Arg:
		 Host:
		 	Host is the name of a node that these pods were bound to.
		 Items:
		 	Items is the list of all pods bound to a given host.
		'''
		
		param_defaults = {
			'Host': 							None,
			'Items': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(BoundPods, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Host == other.Host and \
			self.Items == other.Items and \
			super(BoundPods, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.BoundPods instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.BoundPods instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.BoundPods instance.
	
		Returns:
		  A JSON string representation of this kubernetes.BoundPods instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(BoundPods, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.BoundPods instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.BoundPods instance
		'''
		data = {}
		if self.Host:
			data['host'] = self.Host
		if self.Items:
			data['items'] = [boundPod.AsDict() for boundPod in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.BoundPods instance
		'''

		items = None

		if 'items' in data:
			from kubernetes import BoundPod
			items = [BoundPod.NewFromJsonDict(boundPod) for boundPod in data['items']]

		return BoundPods(
			Kind=data.get('kind', None),
			ID=data.get('id', None),
			UID=data.get('uid', None),
			CreationTimestamp=data.get('creationTimestamp', None),
			SelfLink=data.get('selfLink', None),
			ResourceVersion=data.get('resourceVersion', None),
			APIVersion=data.get('apiVersion', None),
			Namespace=data.get('namespace', None),
			Annotations=data.get('annotations', None),

			Host=data.get('host', None),
			Items=items)