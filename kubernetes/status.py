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

from kubernetes import TypeMeta
class Status(TypeMeta):
	"""A Class representing the Status structure used by the kubernetes API
	
	Status is a return value for calls that don't return other objects.
	TODO: this could go in apiserver, but I'm including it here so clients needn't
	import both.

	The Status structure exposes the following properties:

	Status.Status
	Status.Message
	Status.Reason
	Status.Details
	Status.Code

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Status.
		
		Arg:
		 
		 Status:
		 	One of: "Success", "Failure", "Working" (for operations not yet completed)
		 Message:
		 	A human-readable description of the status of this operation.
		 Reason:
		 	A machine-readable description of why this operation is in the
			"Failure" or "Working" status. If this value is empty there
			is no information available. A Reason clarifies an HTTP status
			code but does not override it.
		Details:
			Extended data associated with the reason.  Each reason may define its
			own extended details. This field is optional and the data returned
			is not guaranteed to conform to any schema except that defined by
			the reason type.
		Code:
			Suggested HTTP return code for this status, 0 if not set.
		 
		'''
		
		param_defaults = {
			'Status': 					None,
			'Message': 					None,
			'Reason': 					None,
			'Details': 					None,
			'Code':						None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

		super(Status, self).__init__(**kwargs)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Status == other.Status and \
			self.Message == other.Message and \
			self.Reason == other.Reason and \
			self.Details == other.Details and \
			self.Code == other.Code and \
			super(Status, self).__eq__(other)
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Status instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Status instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Status instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Status instance.
		'''
		return simplejson.dumps(dict(self.AsDict().items()+super(Status, self).AsDict().items()), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Status instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Status instance
		'''
		data = {}
		if self.Status:
			data['status'] = self.Status
		if self.Message:
			data['message'] = self.Message
		if self.Reason:
			data['reason'] = self.Reason
		if self.Details:
			data['details'] = self.Details.AsDict()
		if self.Code:
			data['code'] = self.Code
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Status instance
		'''

		details = None

		if 'details' in data:
			from kubernetes import StatusDetails
			details = StatusDetails.NewFromJsonDict(data['details'])

		return Status(
					Kind=data.get('kind', None),
					ID=data.get('id', None),
					UID=data.get('uid', None),
					CreationTimestamp=data.get('creationTimestamp', None),
					SelfLink=data.get('selfLink', None),
					ResourceVersion=data.get('resourceVersion', None),
					APIVersion=data.get('apiVersion', None),
					Namespace=data.get('namespace', None),
					Annotations=data.get('annotations', None),

					Status=data.get('status', None),
					Message=data.get('message', None),
					Reason=data.get('reason', None),
					Details=details,
					Code=data.get('code', None))


class StatusDetails(object):
	"""A Class representing the StatusDetails structure used by the kubernetes API
	
	StatusDetails is a set of additional properties that MAY be set by the
	server to provide additional information about a response. The Reason
	field of a Status object defines what attributes will be set. Clients
	must ignore fields that do not match the defined type of each attribute,
	and should assume that any attribute may be empty, invalid, or under
	defined.

	The StatusDetails structure exposes the following properties:

	StatusDetails.ID
	StatusDetails.Kind
	StatusDetails.Causes

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete StatusDetails.
		
		Arg:
		 ID:
		 	The ID attribute of the resource associated with the status StatusReason
			(when there is a single ID which can be described).
		 Kind:
		 	The kind attribute of the resource associated with the status StatusReason.
			On some operations may differ from the requested resource Kind.
		 Causes:
		 	The Causes array includes more details associated with the StatusReason
			failure. Not all StatusReasons may provide detailed causes.
		'''
		
		param_defaults = {
			'ID': 								None,
			'Kind': 							None,
			'Causes': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.ID == other.ID and \
			self.Kind == other.Kind and \
			self.Causes == other.Causes
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.StatusDetails instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.StatusDetails instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.StatusDetails instance.
	
		Returns:
		  A JSON string representation of this kubernetes.StatusDetails instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.StatusDetails instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.StatusDetails instance
		'''
		data = {}
		if self.ID:
			data['id'] = self.ID
		if self.Kind:
			data['kind'] = self.Kind
		if self.Causes:
			data['causes'] = [cause.AsDict() for cause in self.Causes]
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.StatusDetails instance
		'''

		causes = None

		if 'causes' in data:
			from kubernetes import StatusCause
			causes = [StatusCause.NewFromJsonDict(cause) for cause in data['causes']]

		return StatusDetails(
					ID=data.get('id', None),
					Kind=data.get('kind', None),
					Causes=causes)

class StatusReason(object):
	"""
	StatusReason is an enumeration of possible failure causes.  Each StatusReason
	must map to a single HTTP status code, but multiple reasons may map
	to the same HTTP status code.
	TODO: move to apiserver
	"""
		
	'''
	StatusReasonUnknown means the server has declined to indicate a specific reason.
	The details field may contain other information about this error.
	Status code 500.
	'''
	StatusReasonUnknown = ""

	'''
	StatusReasonWorking means the server is processing this request and will complete
	at a future time.
	Details (optional):
	  "kind" string - the name of the resource being referenced ("operation" today)
	  "id"   string - the identifier of the Operation resource where updates
	                  will be returned
	Headers (optional):
	  "Location" - HTTP header populated with a URL that can retrieved the final
	               status of this operation.
	Status code 202
	'''
	StatusReasonWorking = "StatusReasonWorking"

	'''
	StatusReasonNotFound means one or more resources required for this operation
	could not be found.
	Details (optional):
	  "kind" string - the kind attribute of the missing resource
	                  on some operations may differ from the requested
	                  resource.
	  "id"   string - the identifier of the missing resource
	Status code 404
	'''
	StatusReasonNotFound = "NotFound"

	'''
	StatusReasonAlreadyExists means the resource you are creating already exists.
	Details (optional):
	  "kind" string - the kind attribute of the conflicting resource
	  "id"   string - the identifier of the conflicting resource
	Status code 409
	'''
	StatusReasonAlreadyExists = "AlreadyExists"

	'''
	StatusReasonConflict means the requested update operation cannot be completed
	due to a conflict in the operation. The client may need to alter the request.
	Each resource may define custom details that indicate the nature of the
	conflict.
	Status code 409
	'''
	StatusReasonConflict = "Conflict"

	'''
	StatusReasonInvalid means the requested create or update operation cannot be
	completed due to invalid data provided as part of the request. The client may
	need to alter the request. When set, the client may use the StatusDetails
	message field as a summary of the issues encountered.
	Details (optional):
	  "kind" string - the kind attribute of the invalid resource
	  "id"   string - the identifier of the invalid resource
	  "causes"      - one or more StatusCause entries indicating the data in the
	                  provided resource that was invalid.  The code, message, and
	                  field attributes will be set.
	Status code 422
	'''
	StatusReasonInvalid = "Invalid"


class StatusCause(object):
	"""A Class representing the StatusCause structure used by the kubernetes API
	
	StatusCause provides more information about an api.Status failure, including
	cases when multiple errors are encountered.

	The StatusCause structure exposes the following properties:

	StatusCause.Type
	StatusCause.Message
	StatusCause.Field

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete StatusCause.
		
		Arg:
		 Type:
		 	A machine-readable description of the cause of the error. If this value is
			empty there is no information available.
		 Message:
		 	A human-readable description of the cause of the error.  This field may be
			presented as-is to a reader.
		 Field:
		 	The field of the resource that has caused this error, as named by its JSON
			serialization. May include dot and postfix notation for nested attributes.
			Arrays are zero-indexed.  Fields may appear more than once in an array of
			causes due to fields having multiple errors.
			Optional.
			
			Examples:
			"name" - the field "name" on the current resource
			"items[0].name" - the field "name" on the first array entry in "items"
		'''
		
		param_defaults = {
			'Type': 							None,
			'Message': 							None,
			'Field': 							None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Type == other.Type and \
			self.Message == other.Message and \
			self.Field == other.Field
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.StatusCause instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.StatusCause instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.StatusCause instance.
	
		Returns:
		  A JSON string representation of this kubernetes.StatusCause instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.StatusCause instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.StatusCause instance
		'''
		data = {}
		if self.Type:
			data['reason'] = self.Type
		if self.Message:
			data['message'] = self.Message
		if self.Field:
			data['field'] = self.Field
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.StatusCause instance
		'''

		return StatusCause(Type=data.get('reason', None),
					Message=data.get('message', None),
					Field=data.get('field', None))

class CauseType(object):
	"""CauseType is a machine readable value providing more detail about what
	occured in a status response. An operation may have multiple causes for a
	status (whether Failure, Success, or Working).
	"""
	
	'''
	CauseTypeFieldValueNotFound is used to report failure to find a requested value
	(e.g. looking up an ID).
	'''
	CauseTypeFieldValueNotFound = "FieldValueNotFound"

	'''
	CauseTypeFieldValueInvalid is used to report required values that are not
	provided (e.g. empty strings, null values, or empty arrays).
	'''
	CauseTypeFieldValueRequired = "FieldValueRequired"

	'''
	CauseTypeFieldValueDuplicate is used to report collisions of values that must be
	// unique (e.g. unique IDs).
	'''
	CauseTypeFieldValueDuplicate = "FieldValueDuplicate"

	'''
	CauseTypeFieldValueInvalid is used to report malformed values (e.g. failed regex
	match).
	'''
	CauseTypeFieldValueInvalid = "FieldValueInvalid"

	'''
	CauseTypeFieldValueNotSupported is used to report valid (as per formatting rules)
	values that can not be handled (e.g. an enumerated string).
	'''
	CauseTypeFieldValueNotSupported = "FieldValueNotSupported"
