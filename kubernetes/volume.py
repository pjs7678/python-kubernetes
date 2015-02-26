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

class Volume(object):
	'''A Class representing the Volume structure used by the kubernetes API
	
	Volume represents a named volume in a pod that may be accessed by any containers in the pod.

	The Volume structure exposes the following properties:

	Volume.Name
	Volume.Source

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes Volume.

		This class is normally instantiated by the kubernetes.Api class and
		returned in a sequence

		Arg:
		 Name:
		 	Required: This must be a DNS_LABEL.  Each volume in a pod must have
		 	a unique name.
		 Source:
			Source represents the location and type of a volume to mount.
			This is optional for now. If not specified, the Volume is implied to be an EmptyDir.
			This implied behavior is deprecated and will be removed in a future version.
		'''

		param_defaults = {
			'Name': 				None,
			'Source':				None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.Name == other.Name and \
					self.Source == other.Source
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this kubernetes.Volume instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.Volume instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Volume instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Volume instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Volume instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Volume instance
		'''
		data = {}
		if self.Name:
			data['name'] = self.Name
		if self.source:
			data['source'] = self.Source.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.Volume instance
		'''

		if 'source' in data:
			from kubernetes import VolumeSource
			source = VolumeSource.NewFromJsonDict(data['source'])
		else:
			source = None
		return Volume(Name=data.get('name', None),
			Source=source)


class VolumeSource(object):
	'''A Class representing the VolumeSource structure used by the kubernetes API
	
	VolumeSource represents a named volumeSource in a pod that may be accessed by any containers in the pod.

	The VolumeSource structure exposes the following properties:

	VolumeSource.HostDir
	VolumeSource.EmptyDir
	VolumeSource.PersistentDisk

	'''
	def __init__(self, **kwargs):
		'''An object to hold a Kubernetes VolumeSource.

		This class is normally instantiated by the kubernetes.Api class and
		returned in a sequence

		Arg:
		 HostDir:
		 	Only one of the following sources may be specified
			HostDir represents a pre-existing directory on the host machine that is directly
			exposed to the container. This is generally used for system agents or other privileged
			things that are allowed to see the host machine. Most containers will NOT need this.
			TODO(jonesdl) We need to restrict who can use host directory mounts and
			who can/can not mount host directories as read/write.
		 EmptyDir:
			EmptyDir represents a temporary directory that shares a pod's lifetime.
		 PersistentDisk:
		 	A persistent disk that is mounted to the
			kubelet's host machine and then exposed to the pod.
		'''

		param_defaults = {
			'HostDir': 						None,
			'EmptyDir':						None,
			'PersistentDisk':				None}
		
		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
					self.HostDir == other.HostDir and \
					self.EmptyDir == other.EmptyDir and \
					self.PersistentDisk == other.PersistentDisk
		except AttributeError: 
			return False

	def __str__(self):
		'''A string representation of this kubernetes.VolumeSource instance.
	
		The return value is the same as the JSON string representation.

		Returns:
		  A string representation of this kubernetes.VolumeSource instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.VolumeSource instance.
	
		Returns:
		  A JSON string representation of this kubernetes.VolumeSource instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.VolumeSource instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.VolumeSource instance
		'''
		data = {}
		if self.HostDir:
			data['hostDir'] = self.HostDir.AsDict()
		if self.EmptyDir:
			data['emptyDir'] = self.EmptyDir.AsDict()
		if self.PersistentDisk:
			data['persistentDisk'] = self.PersistentDisk.AsDict()
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict

		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API

		Returns:
		  A kubernetes.VolumeSource instance
		'''

		if 'hostDir' in data:
			from kubernetes import HostDir
			hostDir = HostDir.NewFromJsonDict(data['hostDir'])
		else:
			hostDir = None

		if 'emptyDir' in data:
			from kubernetes import EmptyDir
			emptyDir = EmptyDir.NewFromJsonDict(data['emptyDir'])
		else:
			emptyDir = None

		if 'persistentDisk' in data:
			from kubernetes import PersistentDisk
			persistentDisk = PersistentDisk.NewFromJsonDict(data['persistentDisk'])
		else:
			persistentDisk = None

		return VolumeSource(
			HostDir=hostDir,
			EmptyDir=emptyDir,
			PersistentDisk=persistentDisk)


class HostDir(object):
	"""A Class representing the HostDir structure used by the kubernetes API
	
	HostDir represents bare host directory volume.

	The HostDir structure exposes the following properties:

	Hostdir.Path

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete HostDir.
		
		Arg:
		 Path:
		 	The path of this HostDir
		'''
		
		param_defaults = {
			'Path': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Path == other.Path
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.HostDir instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.HostDir instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.HostDir instance.
	
		Returns:
		  A JSON string representation of this kubernetes.HostDir instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.HostDir instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.HostDir instance
		'''
		data = {}
		if self.Path:
			data['path'] = self.Path
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.HostDir instance
		'''
		return HostDir(Path=data.get('path', None))


class EmptyDir(object):
	"""A Class representing the EmptyDir structure used by the kubernetes API

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete EmptyDir.
		'''

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		return True

	def __str__(self):
		'''A string representation of this Kubernetes.EmptyDir instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.EmptyDir instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.EmptyDir instance.
	
		Returns:
		  A JSON string representation of this kubernetes.EmptyDir instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.EmptyDir instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.EmptyDir instance
		'''
		data = {}
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.EmptyDir instance
		'''
		return EmptyDir()

class Protocol(object):
	'''Protocol defines network protocols supported for things like conatiner ports.
	'''

	'''ProtocolTCP is the TCP protocol.'''
	ProtocolTCP = "TCP"

	'''ProtocolUDP is the UDP protocol.'''
	ProtocolUDP = "UDP"

class Port(object):
	"""A Class representing the Port structure used by the kubernetes API
	
	Port represents a network port in a single container.

	The Port structure exposes the following properties:

	Port.Name
	Port.HostPort
	Port.ContainerPort
	Port.Protocol
	Port.HostIP

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete Port.
		
		Arg:
		 Name:
		 	Optional: If specified, this must be a DNS_LABEL.  Each named port
			in a pod must have a unique name.
		 HostPort:
		 	Optional: If specified, this must be a valid port number, 0 < x < 65536.
		 ContainerPort:
		 	Required: This must be a valid port number, 0 < x < 65536.
		 Protocol:
		 	Optional: Defaults to "TCP".
		 HostIP:
		 	Optional: What host IP to bind the external port to.
		'''
		
		param_defaults = {
			'Name': 					None,
			'HostPort': 				None,
			'ContainerPort': 			None,
			'Protocol': 				Protocol.ProtocolTCP,
			'HostIP': 					None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Name == other.Name and \
			self.HostPort == other.HostPort and \
			self.ContainerPort == other.ContainerPort and \
			self.Protocol == other.Protocol and \
			self.HostIP == other.HostIP
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.Port instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.Port instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.Port instance.
	
		Returns:
		  A JSON string representation of this kubernetes.Port instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.Port instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.Port instance
		'''
		data = {}
		if self.Name:
			data['name'] = self.Name
		if self.HostPort:
			data['hostPort'] = self.HostPort
		if self.ContainerPort:
			data['containerPort'] = self.ContainerPort
		if self.Protocol:
			data['protocol'] = self.Protocol
		if self.HostIP:
			data['hostIP'] = self.HostIP
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.Port instance
		'''
		return Port(Name=data.get('name', None),
					HostPort=data.get('hostPort', None),
					ContainerPort=data.get('containerPort', None),
					Protocol=data.get('protocol', Protocol.ProtocolTCP),
					HostIP=data.get('hostIP', None))

class GCEPersistentDisk(object):
	"""A Class representing the GCEPersistentDisk structure used by the kubernetes API
	
	GCEPersistent Disk resource.
	A GCE PD must exist before mounting to a container. The disk must
	also be in the same GCE project and zone as the kubelet.
	A GCE PD can only be mounted as read/write once.

	The GCEPersistentDisk structure exposes the following properties:

	GCEPersistentDisk.PDName
	GCEPersistentDisk.FSType
	GCEPersistentDisk.Partition
	GCEPersistentDisk.Readonly

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete GCEPersistentDisk.
		
		Arg:
		 PDName:
		 	Unique name of the PD resource. Used to identify the disk in GCE
		 FSType:
		 	Required: Filesystem type to mount.
			Must be a filesystem type supported by the host operating system.
			Ex. "ext4", "xfs", "ntfs"
			TODO: how do we prevent errors in the filesystem from compromising the machine
		 Partition:
		 	Optional: Partition on the disk to mount.
			If omitted, kubelet will attempt to mount the device name.
			Ex. For /dev/sda1, this field is "1", for /dev/sda, this field 0 or empty.
		 Readonly:
		 	Optional: Defaults to false (read/write). ReadOnly here will force
			the ReadOnly setting in VolumeMounts.
		'''
		
		param_defaults = {
			'PDName': 					None,
			'FSType': 					None,
			'Partition': 				None,
			'Readonly': 				None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.PDName == other.PDName and \
			self.FSType == other.FSType and \
			self.Partition == other.Partition and \
			self.Readonly == other.Readonly
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.GCEPersistentDisk instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.GCEPersistentDisk instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.GCEPersistentDisk instance.
	
		Returns:
		  A JSON string representation of this kubernetes.GCEPersistentDisk instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.GCEPersistentDisk instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.GCEPersistentDisk instance
		'''
		data = {}
		if self.PDName:
			data['pdName'] = self.PDName
		if self.FSType:
			data['fsType'] = self.FSType
		if self.Partition:
			data['partition'] = self.Partition
		if self.Readonly:
			data['readonly'] = self.Readonly
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.GCEPersistentDisk instance
		'''
		return GCEPersistentDisk(PDName=data.get('pdName', None),
					FSType=data.get('fsType', None),
					Partition=data.get('partition', None),
					Readonly=data.get('readonly', None))


class VolumeMount(object):
	"""A Class representing the VolumeMount structure used by the kubernetes API
	
	VolumeMount describes a mounting of a Volume within a container.

	The VolumeMount structure exposes the following properties:

	VolumeMount.Name
	VolumeMount.Readonly
	VolumeMount.MountPath

	"""
	def __init__(self, **kwargs):
		'''An object to hold a Kubernete VolumeMount.
		
		Arg:
		 Name:
		 	Required: This must match the Name of a Volume [above].
		 Readonly:
		 	Optional: Defaults to false (read-write).
	 	 MountPath:
		 	Required.
		'''
		
		param_defaults = {
			'Name': 					None,
			'Readonly': 				False,
			'MountPath': 				None}

		for (param, default) in param_defaults.iteritems():
			setattr(self, param, kwargs.get(param, default))

	def __ne__(self, other):
		return not self.__eq__(other)

	def __eq__(self, other):
		try:
			return other and \
			self.Name == other.Name and \
			self.Readonly == other.Readonly and \
			self.MountPath == other.MountPath
		except AttributeError:
			return False

	def __str__(self):
		'''A string representation of this Kubernetes.VolumeMount instance.

		The return value is the same as the JSON string representation.

		Returns:
		 A string representation of this kubernetes.VolumeMount instance.
		'''
		return self.AsJsonString()

	def AsJsonString(self):
		'''A JSON string representation of this kubernetes.VolumeMount instance.
	
		Returns:
		  A JSON string representation of this kubernetes.VolumeMount instance.
		'''
		return simplejson.dumps(self.AsDict(), sort_keys=True)

	def AsDict(self):
		''' A dic representation of this kubernetes.VolumeMount instance.

		The return values uses the same key names as the JSON representation.

		Returns:
		  A dict representing this kubernetes.VolumeMount instance
		'''
		data = {}
		if self.Name:
			data['name'] = self.Name
		if self.Readonly:
			data['readonly'] = self.Readonly
		if self.MountPath:
			data['mountPath'] = self.MountPath
		return data

	@staticmethod
	def NewFromJsonDict(data):
		'''Create a new instance base on a JSON dict
		Args:
		  data: A JSON dict, as converted from the JSON in the kubernetes API
		Returns:
		  A kubernetes.VolumeMount instance
		'''
		return VolumeMount(Name=data.get('name', None),
					Readonly=data.get('readonly', False),
					MountPath=data.get('mountPath', None))
