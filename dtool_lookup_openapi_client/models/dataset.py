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


class Dataset(object):
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
        'uuid': 'str',
        'uri': 'str',
        'name': 'str',
        'base_uri': 'object',
        'frozen_at': 'datetime',
        'created_at': 'datetime',
        'creator_username': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'uri': 'uri',
        'name': 'name',
        'base_uri': 'base_uri',
        'frozen_at': 'frozen_at',
        'created_at': 'created_at',
        'creator_username': 'creator_username'
    }

    def __init__(self, uuid=None, uri=None, name=None, base_uri=None, frozen_at=None, created_at=None, creator_username=None, local_vars_configuration=None):  # noqa: E501
        """Dataset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._uri = None
        self._name = None
        self._base_uri = None
        self._frozen_at = None
        self._created_at = None
        self._creator_username = None
        self.discriminator = None

        self.uuid = uuid
        self.uri = uri
        self.name = name
        self.base_uri = base_uri
        self.frozen_at = frozen_at
        self.created_at = created_at
        self.creator_username = creator_username

    @property
    def uuid(self):
        """Gets the uuid of this Dataset.  # noqa: E501


        :return: The uuid of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Dataset.


        :param uuid: The uuid of this Dataset.  # noqa: E501
        :type uuid: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uuid is not None and len(uuid) > 36):
            raise ValueError("Invalid value for `uuid`, length must be less than or equal to `36`")  # noqa: E501

        self._uuid = uuid

    @property
    def uri(self):
        """Gets the uri of this Dataset.  # noqa: E501


        :return: The uri of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Dataset.


        :param uri: The uri of this Dataset.  # noqa: E501
        :type uri: str
        """
        if self.local_vars_configuration.client_side_validation and uri is None:  # noqa: E501
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                uri is not None and len(uri) > 255):
            raise ValueError("Invalid value for `uri`, length must be less than or equal to `255`")  # noqa: E501

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this Dataset.  # noqa: E501


        :return: The name of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dataset.


        :param name: The name of this Dataset.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 80):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `80`")  # noqa: E501

        self._name = name

    @property
    def base_uri(self):
        """Gets the base_uri of this Dataset.  # noqa: E501


        :return: The base_uri of this Dataset.  # noqa: E501
        :rtype: object
        """
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri):
        """Sets the base_uri of this Dataset.


        :param base_uri: The base_uri of this Dataset.  # noqa: E501
        :type base_uri: object
        """

        self._base_uri = base_uri

    @property
    def frozen_at(self):
        """Gets the frozen_at of this Dataset.  # noqa: E501


        :return: The frozen_at of this Dataset.  # noqa: E501
        :rtype: datetime
        """
        return self._frozen_at

    @frozen_at.setter
    def frozen_at(self, frozen_at):
        """Sets the frozen_at of this Dataset.


        :param frozen_at: The frozen_at of this Dataset.  # noqa: E501
        :type frozen_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and frozen_at is None:  # noqa: E501
            raise ValueError("Invalid value for `frozen_at`, must not be `None`")  # noqa: E501

        self._frozen_at = frozen_at

    @property
    def created_at(self):
        """Gets the created_at of this Dataset.  # noqa: E501


        :return: The created_at of this Dataset.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Dataset.


        :param created_at: The created_at of this Dataset.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def creator_username(self):
        """Gets the creator_username of this Dataset.  # noqa: E501


        :return: The creator_username of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._creator_username

    @creator_username.setter
    def creator_username(self, creator_username):
        """Sets the creator_username of this Dataset.


        :param creator_username: The creator_username of this Dataset.  # noqa: E501
        :type creator_username: str
        """
        if self.local_vars_configuration.client_side_validation and creator_username is None:  # noqa: E501
            raise ValueError("Invalid value for `creator_username`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                creator_username is not None and len(creator_username) > 255):
            raise ValueError("Invalid value for `creator_username`, length must be less than or equal to `255`")  # noqa: E501

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
        if not isinstance(other, Dataset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dataset):
            return True

        return self.to_dict() != other.to_dict()