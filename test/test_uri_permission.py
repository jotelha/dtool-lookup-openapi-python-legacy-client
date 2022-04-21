# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.models.uri_permission import UriPermission  # noqa: E501
from dtool_lookup_openapi_client.rest import ApiException

class TestUriPermission(unittest.TestCase):
    """UriPermission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UriPermission
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dtool_lookup_openapi_client.models.uri_permission.UriPermission()  # noqa: E501
        if include_optional :
            return UriPermission(
                users_with_register_permissions = [
                    ''
                    ], 
                users_with_search_permissions = [
                    ''
                    ], 
                base_uri = ''
            )
        else :
            return UriPermission(
        )

    def testUriPermission(self):
        """Test UriPermission"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()