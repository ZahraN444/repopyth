# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mistapi.api_helper import APIHelper
from mistapi.configuration import Server
from mistapi.utilities.file_wrapper import FileWrapper
from mistapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from mistapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from mistapi.models.nac_portal import NacPortal
from mistapi.models.response_sso_failure_search import ResponseSsoFailureSearch
from mistapi.exceptions.api_v_1_orgs_nacportals_400_error_exception import ApiV1OrgsNacportals400ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_401_error_exception import ApiV1OrgsNacportals401ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_403_error_exception import ApiV1OrgsNacportals403ErrorException
from mistapi.exceptions.response_http_404_exception import ResponseHttp404Exception
from mistapi.exceptions.api_v_1_orgs_nacportals_429_error_exception import ApiV1OrgsNacportals429ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_failures_400_error_exception import ApiV1OrgsNacportalsFailures400ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_failures_401_error_exception import ApiV1OrgsNacportalsFailures401ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_failures_403_error_exception import ApiV1OrgsNacportalsFailures403ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_failures_429_error_exception import ApiV1OrgsNacportalsFailures429ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_template_400_error_exception import ApiV1OrgsNacportalsPortalTemplate400ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_template_401_error_exception import ApiV1OrgsNacportalsPortalTemplate401ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_template_403_error_exception import ApiV1OrgsNacportalsPortalTemplate403ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_template_429_error_exception import ApiV1OrgsNacportalsPortalTemplate429ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_image_400_error_exception import ApiV1OrgsNacportalsPortalImage400ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_image_401_error_exception import ApiV1OrgsNacportalsPortalImage401ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_image_403_error_exception import ApiV1OrgsNacportalsPortalImage403ErrorException
from mistapi.exceptions.api_v_1_orgs_nacportals_portal_image_429_error_exception import ApiV1OrgsNacportalsPortalImage429ErrorException


class OrgsNACPortalsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(OrgsNACPortalsController, self).__init__(config)

    def list_org_nac_portals(self,
                             org_id,
                             page=1,
                             limit=100):
        """Does a GET request to /api/v1/orgs/{org_id}/nacportals.

        List Org NAC Portals

        Args:
            org_id (uuid|str): TODO: type description here.
            page (int, optional): TODO: type description here. Example: 1
            limit (int, optional): TODO: type description here. Example: 100

        Returns:
            List[NacPortal]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nacportals')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
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
            .deserialize_into(NacPortal.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNacportals400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNacportals401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNacportals403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNacportals429ErrorException)
        ).execute()

    def get_org_nac_portal(self,
                           org_id,
                           nacportal_id):
        """Does a GET request to /api/v1/orgs/{org_id}/nacportals/{nacportal_id}.

        Get Org NAC Portal

        Args:
            org_id (uuid|str): TODO: type description here.
            nacportal_id (uuid|str): TODO: type description here.

        Returns:
            NacPortal: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nacportals/{nacportal_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nacportal_id')
                            .value(nacportal_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(NacPortal.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNacportals400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNacportals401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNacportals403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNacportals429ErrorException)
        ).execute()

    def update_org_nac_portal(self,
                              org_id,
                              nacportal_id,
                              body=None):
        """Does a PUT request to /api/v1/orgs/{org_id}/nacportals/{nacportal_id}.

        Update Org NAC Portal

        Args:
            org_id (uuid|str): TODO: type description here.
            nacportal_id (uuid|str): TODO: type description here.
            body (NacPortal, optional): TODO: type description here.

        Returns:
            NacPortal: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nacportals/{nacportal_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nacportal_id')
                            .value(nacportal_id)
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
            .deserialize_into(NacPortal.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNacportals400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNacportals401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNacportals403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNacportals429ErrorException)
        ).execute()

    def create_org_nac_portal(self,
                              org_id,
                              body=None):
        """Does a POST request to /api/v1/orgs/{org_id}/nacportals.

        Create Org NAC Portal

        Args:
            org_id (uuid|str): TODO: type description here.
            body (NacPortal, optional): TODO: type description here.

        Returns:
            NacPortal: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nacportals')
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
            .deserialize_into(NacPortal.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNacportals400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNacportals401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNacportals403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNacportals429ErrorException)
        ).execute()

    def delete_org_nac_portal(self,
                              org_id,
                              nacportal_id):
        """Does a DELETE request to /api/v1/orgs/{org_id}/nacportals/{nacportal_id}.

        Delete Org NAC Portal

        Args:
            org_id (uuid|str): TODO: type description here.
            nacportal_id (uuid|str): TODO: type description here.

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
            .path('/api/v1/orgs/{org_id}/nacportals/{nacportal_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nacportal_id')
                            .value(nacportal_id)
                            .should_encode(True))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).execute()

    def list_org_nac_portal_sso_latest_failures(self,
                                                org_id,
                                                nacportal_id,
                                                page=1,
                                                limit=100,
                                                start=None,
                                                end=None,
                                                duration='1d'):
        """Does a GET request to /api/v1/orgs/{org_id}/nacportals/{nacportal_id}/failures.

        Get List of Org NAC Portal SSO Latest Failures

        Args:
            org_id (uuid|str): TODO: type description here.
            nacportal_id (uuid|str): TODO: type description here.
            page (int, optional): TODO: type description here. Example: 1
            limit (int, optional): TODO: type description here. Example: 100
            start (int, optional): start datetime, can be epoch or relative
                time like -1d, -1w; -1d if not specified
            end (int, optional): end datetime, can be epoch or relative time
                like -1d, -2h; now if not specified
            duration (str, optional): duration like 7d, 2w

        Returns:
            ResponseSsoFailureSearch: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/failures')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nacportal_id')
                            .value(nacportal_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('start')
                         .value(start))
            .query_param(Parameter()
                         .key('end')
                         .value(end))
            .query_param(Parameter()
                         .key('duration')
                         .value(duration))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ResponseSsoFailureSearch.from_dictionary)
            .local_error('400', 'Bad Syntax', ApiV1OrgsNacportalsFailures400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1OrgsNacportalsFailures401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1OrgsNacportalsFailures403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist', ResponseHttp404Exception)
            .local_error('429', 'Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold', ApiV1OrgsNacportalsFailures429ErrorException)
        ).execute()

    def update_org_nac_portal_tempalte(self,
                                       org_id,
                                       nacportal_id,
                                       body=None):
        """Does a PUT request to /api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_template.

        Update Org NAC Portal Template

        Args:
            org_id (uuid|str): TODO: type description here.
            nacportal_id (uuid|str): TODO: type description here.
            body (NacPortalTemplate, optional): TODO: type description here.

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
            .path('/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_template')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nacportal_id')
                            .value(nacportal_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).execute()

    def upload_org_nac_portal_image(self,
                                    org_id,
                                    nacportal_id,
                                    file=None,
                                    json=None):
        """Does a POST request to /api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_image.

        Upload background image for NAC Portal

        Args:
            org_id (uuid|str): TODO: type description here.
            nacportal_id (uuid|str): TODO: type description here.
            file (typing.BinaryIO, optional): Binary file
            json (str, optional): JSON string describing the upload

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
            .path('/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_image')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nacportal_id')
                            .value(nacportal_id)
                            .should_encode(True))
            .multipart_param(Parameter()
                             .key('file')
                             .value(file)
                             .default_content_type('application/octet-stream'))
            .form_param(Parameter()
                        .key('json')
                        .value(json))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).execute()

    def delete_org_nac_portal_image(self,
                                    org_id,
                                    nacportal_id):
        """Does a DELETE request to /api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_image.

        Delete background image for NAC Portal
        If image is not uploaded or is deleted, NAC Portal will use default
        image.

        Args:
            org_id (uuid|str): TODO: type description here.
            nacportal_id (uuid|str): TODO: type description here.

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
            .path('/api/v1/orgs/{org_id}/nacportals/{nacportal_id}/portal_image')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('org_id')
                            .value(org_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('nacportal_id')
                            .value(nacportal_id)
                            .should_encode(True))
            .auth(Or(Single('apiToken'), Single('basicAuth'), And(Single('basicAuth'), Single('csrfToken'))))
        ).execute()
