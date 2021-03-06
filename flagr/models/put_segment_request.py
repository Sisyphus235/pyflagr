# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PutSegmentRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'rollout_percent': 'int'
    }

    attribute_map = {
        'description': 'description',
        'rollout_percent': 'rolloutPercent'
    }

    def __init__(self, description=None, rollout_percent=None):  # noqa: E501
        """PutSegmentRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._rollout_percent = None
        self.discriminator = None

        self.description = description
        self.rollout_percent = rollout_percent

    @property
    def description(self):
        """Gets the description of this PutSegmentRequest.  # noqa: E501


        :return: The description of this PutSegmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutSegmentRequest.


        :param description: The description of this PutSegmentRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def rollout_percent(self):
        """Gets the rollout_percent of this PutSegmentRequest.  # noqa: E501


        :return: The rollout_percent of this PutSegmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._rollout_percent

    @rollout_percent.setter
    def rollout_percent(self, rollout_percent):
        """Sets the rollout_percent of this PutSegmentRequest.


        :param rollout_percent: The rollout_percent of this PutSegmentRequest.  # noqa: E501
        :type: int
        """
        if rollout_percent is None:
            raise ValueError("Invalid value for `rollout_percent`, must not be `None`")  # noqa: E501
        if rollout_percent is not None and rollout_percent > 100:  # noqa: E501
            raise ValueError("Invalid value for `rollout_percent`, must be a value less than or equal to `100`")  # noqa: E501
        if rollout_percent is not None and rollout_percent < 0:  # noqa: E501
            raise ValueError("Invalid value for `rollout_percent`, must be a value greater than or equal to `0`")  # noqa: E501

        self._rollout_percent = rollout_percent

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PutSegmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
