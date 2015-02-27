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

'''A library that provides a Python interface to the Kubetnete API'''

__author__ = 'pjs7678@pjs7678'
__version__ = '0.1'

import json as simplejson

try:
	from hashlib import md5
except ImportError:
	from md5 import md5

from _file_cache import _FileCache
from error import KubernetesError

from action import EnvVar, HTTPGetAction, TCPSocketAction, ExecAction, LivenessProbe
from volume import Port, Volume, HostDir, EmptyDir, GCEPersistentDisk, VolumeMount
from container import Handler, Lifecyle, Container
from container_status import TypeMeta, ContainerState, ContainerStatus, ContainerStateWaiting, ContainerStateRunning, ContainerStateTerminated
from manifest import ContainerManifest, PodSpec, BoundPod, BoundPods, ContainerManifestList
from pod import RestartPolicy, PodState, PodTemplate, RestartPolicyAlways, RestartPolicyNever, Pod, ReplicationControllerState, RestartPolicyOnFailure, PodList, ReplicationController, ReplicationControllerList
from service import Service, Endpoints, ServiceList, EndpointsList
from minion import NodeResources, Minion, Binding, MinionList
from status import StatusDetails, StatusCause, Status
from event import ObjectReference, Event, ServerOp, EventList, ServerOpList

from api import Api
