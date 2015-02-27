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

class NodeResources(object):
	"""A Class representing the NodeResources structure used by the kubernetes API

	NodeResources represents resources on a Kubernetes system node
	see https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/resources.md for more details.

	NodeResources.Capacity

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete NodeResources.
		
		Arg:
		 
		 Capacity:
		 
		'''
		
		param_defaults = {
			'Capacity': 						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Capacity == other.Capacity
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.NodeResources instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.NodeResources instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.NodeResources instance.
	
		Returns:
		  A JSON string representation of this kubernetes.NodeResources instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.NodeResources instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.NodeResources instance
		'''
		data = {}
		if self.Capacity:
			data['capacity'] = self.Capacity
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.NodeResources instance
		'''

		return NodeResources(
					Capacity=data.get('capacity', None))


from kubernetes import TypeMeta
class Minion(TypeMeta):
	"""A Class representing the Minion structure used by the kubernetes API
	
	Minion is a worker node in Kubernetenes.
	The name of the minion according to etcd is in TypeMeta.ID.

	The Minion structure exposes the following properties:

	Minion.HostIP
	Minion.Resources

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Minion.
		
		Arg:
		 
		 HostIP:
		 	Queried from cloud provider, if available.
		 Resources:
		 	Resources available on the node
		 
		'''
		
		param_defaults = {
			'HostIP': 						None,
			'Resources': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(Minion, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.HostIP == other.HostIP and \
			self.Resources == other.Resources and \
			super(Minion, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Minion instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Minion instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Minion instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Minion instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(Minion, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Minion instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Minion instance
		'''
		data = {}
		if self.HostIP:
			data['hostIP'] = self.HostIP
		if self.Resources:
			data['resources'] = self.Resources.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Minion instance
		'''

		resources = None

		if 'resources' in data:
			from kubernetes import NodeResources
			resources = NodeResources.NewFromJsonDict(data['resources'])

		return Minion(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					HostIP=data.get('hostIP', None),
					Resources=resources)


class MinionList(TypeMeta):
	"""A Class representing the MinionList structure used by the kubernetes API
	
	MinionList is a list of minions.

	The MinionList structure exposes the following properties:

	minionList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete MinionList.
		
		Arg:
		 
		 Items:
		 
		'''
		
		param_defaults = {
			'Items': 						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(MinionList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(MinionList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.MinionList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.MinionList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.MinionList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.MinionList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(MinionList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.MinionList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.MinionList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [minion.AsDict() for minion in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.MinionList instance
		'''

		items = None

		if 'items' in data:
			from kubernetes import Minion
			items = [Minion.NewFromJsonDict(minion) for minion in data['items']]

		return MinionList(
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


class Binding(TypeMeta):
	"""A Class representing the Binding structure used by the kubernetes API
	
	Binding is written by a scheduler to cause a pod to be bound to a host.

	The Binding structure exposes the following properties:

	Binding.PodID
	Binding.Host

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Binding.
		
		Arg:
		 
		 PostID:
		 Host:
		 
		'''
		
		param_defaults = {
			'PostID': 						None,
			'Host': 						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(Binding, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.PostID == other.PostID and \
			self.Host == other.Host and \
			super(Binding, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Binding instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Binding instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Binding instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Binding instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(Binding, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Binding instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Binding instance
		'''
		data = {}
		if self.PostID:
			data['postID'] = self.PostID
		if self.Host:
			data['host'] = self.Host
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Binding instance
		'''

		return Binding(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					PostID=data.get('postID', None),
					Host=data.get('host', None))
