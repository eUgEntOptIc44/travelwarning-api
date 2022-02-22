"""
    Auswärtiges Amt: Reisewarnungen OpenData Schnittstelle

    Reisewarnungen OpenData Schnittstelle. Dies ist die Beschreibung für die Schnittstelle zum Zugriff auf die Daten des [Auswärtigen Amtes](https://www.auswaertiges-amt.de/de/) im Rahmen der [OpenData](https://www.auswaertiges-amt.de/de/open-data-schnittstelle/736118) Initiative. ## Deaktivierung Die Schnittstelle kann deaktiviert werden, in dem Fall wird ein leeres JSON-Objekt zurückgegeben. ## Fehlerfall Im Fehlerfall wird ein leeres JSON-Objekt zurückgegeben. ## Nutzungsbedingungen Die Nutzungsbedingungen sind auf der [OpenData-Schnittstelle](https://www.auswaertiges-amt.de/de/open-data-schnittstelle/736118)  des Auswärtigen Amtes zu finden.   ## Änderungen [(offizielles Changelog)](https://www.auswaertiges-amt.de/de/-/2412916) ### version [1.2.6](https://www.auswaertiges-amt.de/de/-/2412916) - (08.12.2021) Es werden zusätzlich zu jedem Land **Ländercodes** mit jeweils **zwei Buchstaben** mit ausgegeben.  Die Länderkürzel werden bei [`/travelwarning`](#operations-default-getTravelwarning) und [`/travelwarning/{contentId}`](#operations-default-getSingleTravelwarning) in einem neuen Attribut ausgegeben z.B. in: [`/travelwarning/199124`](https://www.auswaertiges-amt.de/opendata/travelwarning/199124). ### version [1.2.5](https://www.auswaertiges-amt.de/de/-/2412916) (ursprünglich geplant für Ende September 2021) `content` (-> Details des Reise- und Sicherheitshinweis) wurde von [`/travelwarning`](#operations-default-getTravelwarning) entfernt -> bitte ab jetzt [`/travelwarning/{contentId}`](#operations-default-getSingleTravelwarning) nutzen um `content` abzufragen  `flagURL` (-> Details des Reise- und Sicherheitshinweis) wurde entfernt -> es werden keine **Flaggen** mehr angeboten  # noqa: E501

    The version of the OpenAPI document: 1.2.6
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.travelwarning.api_client import ApiClient
from deutschland.travelwarning.api_client import Endpoint as _Endpoint
from deutschland.travelwarning.model.response_address import ResponseAddress
from deutschland.travelwarning.model.response_download import ResponseDownload
from deutschland.travelwarning.model.response_warning import ResponseWarning
from deutschland.travelwarning.model.response_warnings import ResponseWarnings
from deutschland.travelwarning.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_healthcare_endpoint = _Endpoint(
            settings={
                "response_type": (ResponseDownload,),
                "auth": [],
                "endpoint_path": "/healthcare",
                "operation_id": "get_healthcare",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_representatives_country_endpoint = _Endpoint(
            settings={
                "response_type": (ResponseAddress,),
                "auth": [],
                "endpoint_path": "/representativesInCountry",
                "operation_id": "get_representatives_country",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["text/json;charset=UTF-8"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_representatives_germany_endpoint = _Endpoint(
            settings={
                "response_type": (ResponseAddress,),
                "auth": [],
                "endpoint_path": "/representativesInGermany",
                "operation_id": "get_representatives_germany",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["text/json;charset=UTF-8"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_single_travelwarning_endpoint = _Endpoint(
            settings={
                "response_type": (ResponseWarning,),
                "auth": [],
                "endpoint_path": "/travelwarning/{contentId}",
                "operation_id": "get_single_travelwarning",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "content_id",
                ],
                "required": [
                    "content_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "content_id",
                ],
            },
            root_map={
                "validations": {
                    ("content_id",): {
                        "inclusive_minimum": 1,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "content_id": (int,),
                },
                "attribute_map": {
                    "content_id": "contentId",
                },
                "location_map": {
                    "content_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["text/json;charset=UTF-8"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_state_names_endpoint = _Endpoint(
            settings={
                "response_type": (ResponseDownload,),
                "auth": [],
                "endpoint_path": "/stateNames",
                "operation_id": "get_state_names",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.get_travelwarning_endpoint = _Endpoint(
            settings={
                "response_type": (ResponseWarnings,),
                "auth": [],
                "endpoint_path": "/travelwarning",
                "operation_id": "get_travelwarning",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["text/json;charset=UTF-8"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def get_healthcare(self, **kwargs):
        """Gibt die Merkblätter des Gesundheitsdienstes zurück  # noqa: E501

        Merkblätter des Gesundheitsdienstes als Link auf ein PDF  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_healthcare(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResponseDownload
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_healthcare_endpoint.call_with_http_info(**kwargs)

    def get_representatives_country(self, **kwargs):
        """Gibt eine Liste der deutschen Vertretungen im Ausland zurück  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_representatives_country(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResponseAddress
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_representatives_country_endpoint.call_with_http_info(**kwargs)

    def get_representatives_germany(self, **kwargs):
        """Gibt eine Liste der ausländischen Vertretungen in Deutschland zurück  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_representatives_germany(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResponseAddress
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_representatives_germany_endpoint.call_with_http_info(**kwargs)

    def get_single_travelwarning(self, content_id, **kwargs):
        """Gibt einen Reise- und Sicherheitshinweis zurück  # noqa: E501

        Gibt den vollständigen Datensatz eines Reise- und Sicherheitshinweises zurück. Benötigt die jeweilige ID siehe /travelwarning  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_single_travelwarning(content_id, async_req=True)
        >>> result = thread.get()

        Args:
            content_id (int): Die ID des Reise- und Sicherheitshinweises, IDs siehe /travelwarning

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResponseWarning
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["content_id"] = content_id
        return self.get_single_travelwarning_endpoint.call_with_http_info(**kwargs)

    def get_state_names(self, **kwargs):
        """Gibt das Verzeichnis der Staatennamen zurück  # noqa: E501

        Verzeichnis der Staatennamen als Link auf eine XML- oder CSV-Datei. Eine PDF-Datei mit Nutzungshinweisen wird ebenfalls zurückgegeben.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_state_names(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResponseDownload
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_state_names_endpoint.call_with_http_info(**kwargs)

    def get_travelwarning(self, **kwargs):
        """Gibt alle Reise- und Sicherheitshinweise zurück  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_travelwarning(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ResponseWarnings
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.get_travelwarning_endpoint.call_with_http_info(**kwargs)
