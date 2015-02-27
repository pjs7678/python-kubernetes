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

from kubernetes import TypeMeta
class ServiceList(TypeMeta):
	"""A Class representing the ServiceList structure used by the kubernetes API
	
	ServiceList holds a list of services.

	The ServiceList structure exposes the following properties:

	ServiceList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ServiceList.
		
		Arg:
		 
		 Items:
		 
		'''
		
		param_defaults = {
			'Items': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(ServiceList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(ServiceList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ServiceList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ServiceList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ServiceList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ServiceList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(ServiceList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ServiceList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ServiceList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [service.AsDict() for service in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ServiceList instance
		'''

		items = None

		if 'items' in data and data['items']:
			from kubernetes import Service
			items = [Service.NewFromJsonDict(service) for service in data['items']]

		return ServiceList(
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

class Service(TypeMeta):
	"""A Class representing the Service structure used by the kubernetes API
	
	Service is a named abstraction of software service (for example, mysql) consisting of local port
	(for example 3306) that the proxy listens on, and the selector that determines which pods
	will answer requests sent through the proxy.

	The Service structure exposes the following properties:

	Service.Port
	Service.Protocol
	Service.Labels
	Service.Selector
	Service.CreateExternalLoadBalancer
	Service.ContainerPort
	Service.PortalIP
	Service.ProxyPort

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Service.
		
		Arg:
		 
		 Port:
		 	Required.
		 Protocol:
		 	Optional: Defaults to "TCP".
		 Labels:
			This service's labels.
		 Selector:
		 	This service will route traffic to pods having labels matching this selector.
		 CreateExternalLoadBalancer:
		 ContainerPort:
		 	ContainerPort is the name of the port on the container to direct traffic to.
			Optional, if unspecified use the first port on the container.
		 PortalIP:
		 	PortalIP is assigned by the master.  If specified by the user it will be ignored.
		 ProxyPort:
		 	ProxyPort is assigned by the master.  If specified by the user it will be ignored.
		 
		'''
		
		param_defaults = {
			'Port': 								None,
			'Protocol': 							None,
			'Labels': 								None,
			'Selector': 							None,
			'CreateExternalLoadBalancer': 			None,
			'ContainerPort': 						None,
			'PortalIP': 							None,
			'ProxyPort': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(Service, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Port == other.Port and \
			self.Protocol == other.Protocol and \
			self.Labels == other.Labels and \
			self.Selector == other.Selector and \
			self.CreateExternalLoadBalancer == other.CreateExternalLoadBalancer and \
			self.ContainerPort == other.ContainerPort and \
			self.PortalIP == other.PortalIP and \
			self.ProxyPort == other.ProxyPort and \
			super(Service, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Service instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Service instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Service instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Service instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(Service, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Service instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Service instance
		'''
		data = {}
		if self.Port:
			data['port'] = self.Port
		if self.Protocol:
			data['protocol'] = self.Protocol
		if self.Labels:
			data['labels'] = self.Labels
		if self.Selector:
			data['selector'] = self.Selector
		if self.CreateExternalLoadBalancer:
			data['createExternalLoadBalancer'] = self.CreateExternalLoadBalancer
		if self.ContainerPort:
			data['containerPort'] = self.ContainerPort
		if self.PortalIP:
			data['portalIP'] = self.PortalIP
		if self.ProxyPort:
			data['proxyPort'] = self.ProxyPort
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Service instance
		'''

		return Service(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					Port=data.get('port', None),
					Protocol=data.get('protocol', None),
					Labels=data.get('labels', None),
					Selector=data.get('selector', None),
					CreateExternalLoadBalancer=data.get('createExternalLoadBalancer', None),
					ContainerPort=data.get('containerPort', None),
					PortalIP=data.get('portalIP', None),
					ProxyPort=data.get('proxyPort', None))


class Endpoints(TypeMeta):
	"""A Class representing the Endpoints structure used by the kubernetes API
	
	Endpoints is a collection of endpoints that implement the actual service, for example:
	Name: "mysql", Endpoints: ["10.10.1.1:1909", "10.10.2.2:8834"]

	The Endpoints structure exposes the following properties:

	Endpoints.Endpoints

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Endpoints.
		
		Arg:
		 
		 Endpoints:
		 
		'''
		
		param_defaults = {
			'Endpoints': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(Endpoints, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Endpoints == other.Endpoints and \
			super(Endpoints, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Endpoints instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Endpoints instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Endpoints instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Endpoints instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(Endpoints, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Endpoints instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Endpoints instance
		'''
		data = {}
		if self.Endpoints:
			data['endpoints'] = [endpoint.AsDict() for endpoint in self.Endpoints]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Endpoints instance
		'''

		return Endpoints(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					Endpoints=data.get('endpoints', None))

class EndpointsList(TypeMeta):
	"""A Class representing the EndpointsList structure used by the kubernetes API
	
	EndpointsList is a list of endpoints.

	The EndpointsList structure exposes the following properties:

	EndpointsList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete EndpointsList.
		
		Arg:
		 
		 Items:
		 
		'''
		
		param_defaults = {
			'Items': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(EndpointsList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(EndpointsList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.EndpointsList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.EndpointsList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.EndpointsList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.EndpointsList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(EndpointsList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.EndpointsList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.EndpointsList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [endPoints.AsDict() for endPoints in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.EndpointsList instance
		'''

		items = None

		if 'items' in data:
			from kubernetes import Endpoints
			items = [Endpoints.NewFromJsonDict(endpoint) for endpoint in data['items']]

		return EndpointsList(
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
