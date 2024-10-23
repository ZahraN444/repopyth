# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mistapi.api_helper import APIHelper
from mistapi.configuration import Server
from mistapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from mistapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from mistapi.models.nac_tag import NacTag
from mistapi.exceptions.api_v_1_orgs_nactags_400_error_exception import ApiV1OrgsNactags400ErrorException
from mistapi.exceptions.api_v_1_orgs_nactags_401_error_exception import ApiV1OrgsNactags401ErrorException
from mistapi.exceptions.api_v_1_orgs_nactags_403_error_exception import ApiV1OrgsNactags403ErrorException
from mistapi.exceptions.response_http_404_exception import ResponseHttp404Exception
from mistapi.exceptions.api_v_1_orgs_nactags_429_error_exception import ApiV1OrgsNactags429ErrorException


class OrgsNACTagsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(OrgsNACTagsController, self).__init__(config)

    def get_org_nac_tag(self,
                        org_id,
                        nactag_id):
        """Does a GET request to /api/v1/orgs/{org_id}/nactags/{nactag_id}.

        Get Org NAC Tag

        Args:
            org_id (uuid|str): TODO: type description here.
            nactag_id (uuid|str): TODO: type description here.

        Returns:
            NacTag: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nactags/{nactag_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nactag_id')
                            .value(nactag_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(NacTag.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNactags400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNactags401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNactags403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNactags429ErrorException)
        ).execute()

    def list_org_nac_tags(self,
                          org_id,
                          mtype=None,
                          name=None,
                          match=None,
                          page=1,
                          limit=100):
        """Does a GET request to /api/v1/orgs/{org_id}/nactags.

        Get List of Org NAC Tags

        Args:
            org_id (uuid|str): TODO: type description here.
            mtype (str, optional): Type of NAC Tag
            name (str, optional): Name of NAC Tag
            match (str, optional): Type of NAC Tag
            page (int, optional): TODO: type description here. Example: 1
            limit (int, optional): TODO: type description here. Example: 100

        Returns:
            List[NacTag]: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nactags')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('match')
                         .value(match))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(NacTag.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNactags400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNactags401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNactags403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNactags429ErrorException)
        ).execute()

    def delete_org_nac_tag(self,
                           org_id,
                           nactag_id):
        """Does a DELETE request to /api/v1/orgs/{org_id}/nactags/{nactag_id}.

        Delete Org NAC Tag

        Args:
            org_id (uuid|str): TODO: type description here.
            nactag_id (uuid|str): TODO: type description here.

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nactags/{nactag_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nactag_id')
                            .value(nactag_id)
                            .should_encode(True))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).execute()

    def update_org_nac_tag(self,
                           org_id,
                           nactag_id,
                           body=None):
        """Does a PUT request to /api/v1/orgs/{org_id}/nactags/{nactag_id}.

        Update Org NAC Tag

        Args:
            org_id (uuid|str): TODO: type description here.
            nactag_id (uuid|str): TODO: type description here.
            body (NacTag, optional): TODO: type description here.

        Returns:
            NacTag: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nactags/{nactag_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nactag_id')
                            .value(nactag_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(NacTag.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNactags400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNactags401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNactags403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNactags429ErrorException)
        ).execute()

    def create_org_nac_tag(self,
                           org_id,
                           body=None):
        """Does a POST request to /api/v1/orgs/{org_id}/nactags.

        Create Org NAC Tag

        Args:
            org_id (uuid|str): TODO: type description here.
            body (NacTag, optional): TODO: type description here.

        Returns:
            NacTag: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nactags')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(NacTag.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNactags400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNactags401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNactags403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNactags429ErrorException)
        ).execute()
