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


class Error(object):
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
        'errors': 'object',
        'code': 'int',
        'message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'errors': 'errors',
        'code': 'code',
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, errors=None, code=None, message=None, status=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self._code = None
        self._message = None
        self._status = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def errors(self):
        """Gets the errors of this Error.  # noqa: E501

        Errors  # noqa: E501

        :return: The errors of this Error.  # noqa: E501
        :rtype: object
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Error.

        Errors  # noqa: E501

        :param errors: The errors of this Error.  # noqa: E501
        :type errors: object
        """

        self._errors = errors

    @property
    def code(self):
        """Gets the code of this Error.  # noqa: E501

        Error code  # noqa: E501

        :return: The code of this Error.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.

        Error code  # noqa: E501

        :param code: The code of this Error.  # noqa: E501
        :type code: int
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        Error message  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        Error message  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this Error.  # noqa: E501

        Error name  # noqa: E501

        :return: The status of this Error.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Error.

        Error name  # noqa: E501

        :param status: The status of this Error.  # noqa: E501
        :type status: str
        """

        self._status = status

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
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
