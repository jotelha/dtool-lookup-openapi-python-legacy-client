# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from dtool_lookup_openapi_client.configuration import Configuration


class RegisterDataset(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'readme': 'object',
        'uuid': 'str',
        'annotations': 'object',
        'tags': 'list[str]',
        'uri': 'str',
        'name': 'str',
        'manifest': 'Manifest',
        'type': 'str',
        'base_uri': 'str',
        'frozen_at': 'str',
        'created_at': 'str',
        'creator_username': 'str'
    }

    attribute_map = {
        'readme': 'readme',
        'uuid': 'uuid',
        'annotations': 'annotations',
        'tags': 'tags',
        'uri': 'uri',
        'name': 'name',
        'manifest': 'manifest',
        'type': 'type',
        'base_uri': 'base_uri',
        'frozen_at': 'frozen_at',
        'created_at': 'created_at',
        'creator_username': 'creator_username'
    }

    def __init__(self, readme=None, uuid=None, annotations=None, tags=None, uri=None, name=None, manifest=None, type=None, base_uri=None, frozen_at=None, created_at=None, creator_username=None, local_vars_configuration=None):  # noqa: E501
        """RegisterDataset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._readme = None
        self._uuid = None
        self._annotations = None
        self._tags = None
        self._uri = None
        self._name = None
        self._manifest = None
        self._type = None
        self._base_uri = None
        self._frozen_at = None
        self._created_at = None
        self._creator_username = None
        self.discriminator = None

        if readme is not None:
            self.readme = readme
        if uuid is not None:
            self.uuid = uuid
        if annotations is not None:
            self.annotations = annotations
        if tags is not None:
            self.tags = tags
        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if manifest is not None:
            self.manifest = manifest
        if type is not None:
            self.type = type
        if base_uri is not None:
            self.base_uri = base_uri
        if frozen_at is not None:
            self.frozen_at = frozen_at
        if created_at is not None:
            self.created_at = created_at
        if creator_username is not None:
            self.creator_username = creator_username

    @property
    def readme(self):
        """Gets the readme of this RegisterDataset.  # noqa: E501


        :return: The readme of this RegisterDataset.  # noqa: E501
        :rtype: object
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this RegisterDataset.


        :param readme: The readme of this RegisterDataset.  # noqa: E501
        :type readme: object
        """

        self._readme = readme

    @property
    def uuid(self):
        """Gets the uuid of this RegisterDataset.  # noqa: E501


        :return: The uuid of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RegisterDataset.


        :param uuid: The uuid of this RegisterDataset.  # noqa: E501
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def annotations(self):
        """Gets the annotations of this RegisterDataset.  # noqa: E501


        :return: The annotations of this RegisterDataset.  # noqa: E501
        :rtype: object
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this RegisterDataset.


        :param annotations: The annotations of this RegisterDataset.  # noqa: E501
        :type annotations: object
        """

        self._annotations = annotations

    @property
    def tags(self):
        """Gets the tags of this RegisterDataset.  # noqa: E501


        :return: The tags of this RegisterDataset.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RegisterDataset.


        :param tags: The tags of this RegisterDataset.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def uri(self):
        """Gets the uri of this RegisterDataset.  # noqa: E501


        :return: The uri of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RegisterDataset.


        :param uri: The uri of this RegisterDataset.  # noqa: E501
        :type uri: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this RegisterDataset.  # noqa: E501


        :return: The name of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegisterDataset.


        :param name: The name of this RegisterDataset.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def manifest(self):
        """Gets the manifest of this RegisterDataset.  # noqa: E501


        :return: The manifest of this RegisterDataset.  # noqa: E501
        :rtype: Manifest
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this RegisterDataset.


        :param manifest: The manifest of this RegisterDataset.  # noqa: E501
        :type manifest: Manifest
        """

        self._manifest = manifest

    @property
    def type(self):
        """Gets the type of this RegisterDataset.  # noqa: E501


        :return: The type of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RegisterDataset.


        :param type: The type of this RegisterDataset.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def base_uri(self):
        """Gets the base_uri of this RegisterDataset.  # noqa: E501


        :return: The base_uri of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri):
        """Sets the base_uri of this RegisterDataset.


        :param base_uri: The base_uri of this RegisterDataset.  # noqa: E501
        :type base_uri: str
        """

        self._base_uri = base_uri

    @property
    def frozen_at(self):
        """Gets the frozen_at of this RegisterDataset.  # noqa: E501


        :return: The frozen_at of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._frozen_at

    @frozen_at.setter
    def frozen_at(self, frozen_at):
        """Sets the frozen_at of this RegisterDataset.


        :param frozen_at: The frozen_at of this RegisterDataset.  # noqa: E501
        :type frozen_at: str
        """

        self._frozen_at = frozen_at

    @property
    def created_at(self):
        """Gets the created_at of this RegisterDataset.  # noqa: E501


        :return: The created_at of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RegisterDataset.


        :param created_at: The created_at of this RegisterDataset.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def creator_username(self):
        """Gets the creator_username of this RegisterDataset.  # noqa: E501


        :return: The creator_username of this RegisterDataset.  # noqa: E501
        :rtype: str
        """
        return self._creator_username

    @creator_username.setter
    def creator_username(self, creator_username):
        """Sets the creator_username of this RegisterDataset.


        :param creator_username: The creator_username of this RegisterDataset.  # noqa: E501
        :type creator_username: str
        """

        self._creator_username = creator_username

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RegisterDataset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterDataset):
            return True

        return self.to_dict() != other.to_dict()
