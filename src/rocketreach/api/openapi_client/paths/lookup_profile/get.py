# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

from openapi_client.model.profile_api import ProfileAPI

from . import path

# Query params
IdSchema = schemas.IntSchema


class NameSchema(
    schemas.StrSchema
):


    class MetaOapg:
        min_length = 1


class CurrentEmployerSchema(
    schemas.StrSchema
):


    class MetaOapg:
        min_length = 1


class TitleSchema(
    schemas.StrSchema
):


    class MetaOapg:
        min_length = 1


class LinkedinExtUrlSchema(
    schemas.StrSchema
):


    class MetaOapg:
        min_length = 1
        regex=[{
            'pattern': r'',  # noqa: E501
        }]


class LinkedinUrlSchema(
    schemas.StrSchema
):


    class MetaOapg:
        min_length = 1
        regex=[{
            'pattern': r'',  # noqa: E501
        }]


class EmailSchema(
    schemas.StrSchema
):


    class MetaOapg:
        format = 'email'
        min_length = 1


class LookupTypeSchema(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        enum_value_to_name = {
            "standard": "STANDARD",
            "premium": "PREMIUM",
            "premium (feeds disabled)": "PREMIUM_FEEDS_DISABLED",
            "bulk": "BULK",
            "phone": "PHONE",
            "enrich": "ENRICH",
        }
    
    @schemas.classproperty
    def STANDARD(cls):
        return cls("standard")
    
    @schemas.classproperty
    def PREMIUM(cls):
        return cls("premium")
    
    @schemas.classproperty
    def PREMIUM_FEEDS_DISABLED(cls):
        return cls("premium (feeds disabled)")
    
    @schemas.classproperty
    def BULK(cls):
        return cls("bulk")
    
    @schemas.classproperty
    def PHONE(cls):
        return cls("phone")
    
    @schemas.classproperty
    def ENRICH(cls):
        return cls("enrich")


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LookupTypeSchema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'id': typing.Union[IdSchema, decimal.Decimal, int, ],
        'name': typing.Union[NameSchema, str, ],
        'current_employer': typing.Union[CurrentEmployerSchema, str, ],
        'title': typing.Union[TitleSchema, str, ],
        'linkedin_ext_url': typing.Union[LinkedinExtUrlSchema, str, ],
        'linkedin_url': typing.Union[LinkedinUrlSchema, str, ],
        'email': typing.Union[EmailSchema, str, ],
        'lookup_type': typing.Union[LookupTypeSchema, None, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    explode=True,
)
request_query_current_employer = api_client.QueryParameter(
    name="current_employer",
    style=api_client.ParameterStyle.FORM,
    schema=CurrentEmployerSchema,
    explode=True,
)
request_query_title = api_client.QueryParameter(
    name="title",
    style=api_client.ParameterStyle.FORM,
    schema=TitleSchema,
    explode=True,
)
request_query_linkedin_ext_url = api_client.QueryParameter(
    name="linkedin_ext_url",
    style=api_client.ParameterStyle.FORM,
    schema=LinkedinExtUrlSchema,
    explode=True,
)
request_query_linkedin_url = api_client.QueryParameter(
    name="linkedin_url",
    style=api_client.ParameterStyle.FORM,
    schema=LinkedinUrlSchema,
    explode=True,
)
request_query_email = api_client.QueryParameter(
    name="email",
    style=api_client.ParameterStyle.FORM,
    schema=EmailSchema,
    explode=True,
)
request_query_lookup_type = api_client.QueryParameter(
    name="lookup_type",
    style=api_client.ParameterStyle.FORM,
    schema=LookupTypeSchema,
    explode=True,
)
_auth = [
    'RocketReach API Key',
]
RRRequestIDSchema = schemas.UUIDSchema
rr_request_id_parameter = api_client.HeaderParameter(
    name="RR-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RRRequestIDSchema,
)
SchemaFor200ResponseBodyApplicationJson = ProfileAPI
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'RR-Request-ID': RRRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor200


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        rr_request_id_parameter,
    ]
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _lookup_profile_read_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _lookup_profile_read_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _lookup_profile_read_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _lookup_profile_read_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Lookup Person
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_id,
            request_query_name,
            request_query_current_employer,
            request_query_title,
            request_query_linkedin_ext_url,
            request_query_linkedin_url,
            request_query_email,
            request_query_lookup_type,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class LookupProfileRead(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def lookup_profile_read(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def lookup_profile_read(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def lookup_profile_read(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def lookup_profile_read(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._lookup_profile_read_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._lookup_profile_read_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


