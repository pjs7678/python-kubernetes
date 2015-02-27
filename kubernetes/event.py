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
class ServerOp(TypeMeta):
	"""A Class representing the ServerOp structure used by the kubernetes API
	
	ServerOp is an operation delivered to API clients.

	The ServerOp structure exposes the following properties:


	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ServerOp.
		
		Arg:
		 
		'''

		super(ServerOp, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			super(ServerOp, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ServerOp instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ServerOp instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ServerOp instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ServerOp instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(ServerOp, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ServerOp instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ServerOp instance
		'''
		data = {}
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ServerOp instance
		'''

		return ServerOp(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None))

class ServerOpList(TypeMeta):
	"""A Class representing the ServerOpList structure used by the kubernetes API
	
	ServerOpList is a list of operations, as delivered to API clients.

	The ServerOpList structure exposes the following properties:

	ServerOpList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ServerOpList.
		
		Arg:
		 
		 Items:
		 
		'''
		
		param_defaults = {
			'Items': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(ServerOpList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(ServerOpList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ServerOpList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ServerOpList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ServerOpList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ServerOpList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(ServerOpList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ServerOpList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ServerOpList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [serverOp.AsDict() for serverOp in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ServerOpList instance
		'''

		items = None

		if 'items' in data:
			from kubernetes import ServerOp
			items = [ServerOp.NewFromJsonDict(serverop) for serverop in data['items']]

		return ServerOpList(
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


class ObjectReference(object):
	"""A Class representing the ObjectReference structure used by the kubernetes API
	
	ObjectReference contains enough information to let you inspect or modify the referred object.

	The ObjectReference structure exposes the following properties:

	ObjectReference.Kind
	ObjectReference.Namespace
	ObjectReference.Name
	ObjectReference.UID
	ObjectReference.APIVersion
	ObjectReference.ResourceVersion
	ObjectReference.FieldPath

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete ObjectReference.
		
		Arg:
		 Kind:
		 Namespace:
		 Name:
		 UID:
		 APIVersion:
		 ResourceVersion:
		 FieldPath:
		 	Optional. If referring to a piece of an object instead of an entire object, this string
			should contain a valid field access statement. For example,
			if the object reference is to a container within a pod, this would take on a value like:
			"desiredState.manifest.containers[2]". Such statements are valid language constructs in
			both go and JavaScript. This is syntax is chosen only to have some well-defined way of
			referencing a part of an object.
			TODO: this design is not final and this field is subject to change in the future.
		'''
		
		param_defaults = {
			'Kind': 								None,
			'Namespace': 							None,
			'Name':		 							None,
			'UID':		 							None,
			'APIVersion':		 					None,
			'ResourceVersion':		 				None,
			'FieldPath':			 				None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Kind == other.Kind and \
			self.Namespace == other.Namespace and \
			self.Name == other.Name and \
			self.UID == other.UID and \
			self.APIVersion == other.APIVersion and \
			self.ResourceVersion == other.ResourceVersion and \
			self.FieldPath == other.FieldPath
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.ObjectReference instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.ObjectReference instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.ObjectReference instance.
	
		Returns:
		  A JSON string representation of this kubernetes.ObjectReference instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.ObjectReference instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.ObjectReference instance
		'''
		data = {}
		if self.Kind:
			data['kind'] = self.Kind
		if self.Namespace:
			data['namespace'] = self.Namespace
		if self.Name:
			data['name'] = self.Name
		if self.UID:
			data['uid'] = self.UID
		if self.APIVersion:
			data['apiVersion'] = self.APIVersion
		if self.ResourceVersion:
			data['resourceVersion'] = self.ResourceVersion
		if self.FieldPath:
			data['fieldPath'] = self.FieldPath
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.ObjectReference instance
		'''

		return ObjectReference(
					Kind=data.get('kind', None),
					Namespace=data.get('namespace', None),
					Name=data.get('name', None),
					UID=data.get('uid', None),
					APIVersion=data.get('apiVersion', None),
					ResourceVersion=data.get('resourceVersion', None),
					FieldPath=data.get('fieldPath', None))


class Event(TypeMeta):
	"""A Class representing the Event structure used by the kubernetes API
	
	Event is a report of an event somewhere in the cluster.
	TODO: Decide whether to store these separately or with the object they apply to.

	The Event structure exposes the following properties:

	Event.InvolvedObject
	Event.Status
	Event.Reason
	Event.Message
	Event.Source

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Event.
		
		Arg:
		 
		 InvolvedObject:
		 	Required. The object that this event is about.
		 Status:
		 	Should be a short, machine understandable string that describes the current status
			of the referred object. This should not give the reason for being in this state.
			Examples: "running", "cantStart", "cantSchedule", "deleted".
			It's OK for components to make up statuses to report here, but the same string should
			always be used for the same status.
			TODO: define a way of making sure these are consistent and don't collide.
			TODO: provide exact specification for format.
		 Reason:
		 	Optional; this should be a short, machine understandable string that gives the reason
			for the transition into the object's current status. For example, if ObjectStatus is
			"cantStart", StatusReason might be "imageNotFound".
			TODO: provide exact specification for format.
		 Message:
		 	Optional. A human-readable description of the status of this operation.
			TODO: decide on maximum length.
		 Source:
		 	Optional. The component reporting this event. Should be a short machine understandable string.
			TODO: provide exact specification for format.
		 
		'''
		
		param_defaults = {
			'InvolvedObject': 					None,
			'Status': 							None,
			'Reason': 							None,
			'Message':		 					None,
			'Source': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(Event, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.InvolvedObject == other.InvolvedObject and \
			self.Status == other.Status and \
			self.Reason == other.Reason and \
			self.Message == other.Message and \
			self.Source == other.Source and \
			super(Event, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Event instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Event instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Event instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Event instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(Event, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Event instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Event instance
		'''
		data = {}
		if self.InvolvedObject:
			data['involvedObject'] = self.InvolvedObject.AsDict()
		if self.Status:
			data['status'] = self.Status
		if self.Reason:
			data['reason'] = self.Reason
		if self.Message:
			data['message'] = self.Message
		if self.Source:
			data['source'] = self.Source
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Event instance
		'''

		involvedObject = None

		if 'involvedObject' in data:
			from kubernetes import ObjectReference
			involvedObject = ObjectReference.NewFromJsonDict(data['involvedObject'])

		return Event(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					InvolvedObject=involvedObject,
					Status=data.get('status', None),
					Reason=data.get('reason', None),
					Message=data.get('message', None),
					Source=data.get('source', None))


class EventList(TypeMeta):
	"""A Class representing the EventList structure used by the kubernetes API
	
	EventList is a list of events.

	The EventList structure exposes the following properties:

	EventList.Items

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete EventList.
		
		Arg:
		 
		 Items:
		 
		'''
		
		param_defaults = {
			'Items': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(EventList, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Items == other.Items and \
			super(EventList, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.EventList instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.EventList instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.EventList instance.
	
		Returns:
		  A JSON string representation of this kubernetes.EventList instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(EventList, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.EventList instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.EventList instance
		'''
		data = {}
		if self.Items:
			data['items'] = [event.AsDict() for event in self.Items]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.EventList instance
		'''

		items = None

		if 'items' in data:
			from kubernetes import Event
			items = [Event.NewFromJsonDict(event) for event in data['items']]

		return EventList(
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
