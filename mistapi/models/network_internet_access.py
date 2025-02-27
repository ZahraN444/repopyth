# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.network_destination_nat_property import NetworkDestinationNatProperty
from mistapi.models.network_static_nat_property import NetworkStaticNatProperty


class NetworkInternetAccess(object):

    """Implementation of the 'network_internet_access' model.

    whether this network has direct internet access

    Attributes:
        create_simple_service_policy (bool): TODO: type description here.
        destination_nat (Dict[str, NetworkDestinationNatProperty]): Property
            key may be an IP/Port (i.e. "63.16.0.3:443"), or a port (i.e.
            ":2222")
        enabled (bool): TODO: type description here.
        restricted (bool): by default, all access is allowed, to only allow
            certain traffic, make `restricted`=`true` and define
            service_policies
        static_nat (Dict[str, NetworkStaticNatProperty]): Property key may be
            an IP Address (i.e. "172.16.0.1"), and IP Address and Port (i.e.
            "172.16.0.1:8443") or a CIDR (i.e. "172.16.0.12/20")

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "create_simple_service_policy": 'create_simple_service_policy',
        "destination_nat": 'destination_nat',
        "enabled": 'enabled',
        "restricted": 'restricted',
        "static_nat": 'static_nat'
    }

    _optionals = [
        'create_simple_service_policy',
        'destination_nat',
        'enabled',
        'restricted',
        'static_nat',
    ]

    def __init__(self,
                 create_simple_service_policy=False,
                 destination_nat=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 restricted=False,
                 static_nat=APIHelper.SKIP):
        """Constructor for the NetworkInternetAccess class"""

        # Initialize members of the class
        self.create_simple_service_policy = create_simple_service_policy 
        if destination_nat is not APIHelper.SKIP:
            self.destination_nat = destination_nat 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        self.restricted = restricted 
        if static_nat is not APIHelper.SKIP:
            self.static_nat = static_nat 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        create_simple_service_policy = dictionary.get("create_simple_service_policy") if dictionary.get("create_simple_service_policy") else False
        destination_nat = NetworkDestinationNatProperty.from_dictionary(dictionary.get('destination_nat')) if 'destination_nat' in dictionary.keys() else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        restricted = dictionary.get("restricted") if dictionary.get("restricted") else False
        static_nat = NetworkStaticNatProperty.from_dictionary(dictionary.get('static_nat')) if 'static_nat' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(create_simple_service_policy,
                   destination_nat,
                   enabled,
                   restricted,
                   static_nat)
