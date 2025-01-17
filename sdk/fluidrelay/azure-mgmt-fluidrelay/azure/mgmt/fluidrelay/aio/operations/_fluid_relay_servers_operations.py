# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._fluid_relay_servers_operations import build_create_or_update_request, build_delete_request, build_get_request, build_list_by_resource_group_request, build_list_by_subscription_request, build_list_keys_request, build_regenerate_key_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FluidRelayServersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.fluidrelay.aio.FluidRelayManagementClient`'s
        :attr:`fluid_relay_servers` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def get(
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        **kwargs: Any
    ) -> _models.FluidRelayServer:
        """Get a Fluid Relay server.

        Get a Fluid Relay server.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FluidRelayServer, or the result of cls(response)
        :rtype: ~azure.mgmt.fluidrelay.models.FluidRelayServer
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayServer]

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FluidRelayServer', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}"}  # type: ignore


    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        resource: _models.FluidRelayServer,
        **kwargs: Any
    ) -> _models.FluidRelayServer:
        """Create or Update a Fluid Relay server.

        Create or Update a Fluid Relay server.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :param resource: The details of the Fluid Relay server resource.
        :type resource: ~azure.mgmt.fluidrelay.models.FluidRelayServer
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FluidRelayServer, or the result of cls(response)
        :rtype: ~azure.mgmt.fluidrelay.models.FluidRelayServer
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayServer]

        _json = self._serialize.body(resource, 'FluidRelayServer')

        request = build_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FluidRelayServer', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}"}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        resource: _models.FluidRelayServerUpdate,
        **kwargs: Any
    ) -> _models.FluidRelayServer:
        """Update a Fluid Relay server.

        Update a Fluid Relay server.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :param resource: The details of the Fluid Relay server resource included in update calls.
        :type resource: ~azure.mgmt.fluidrelay.models.FluidRelayServerUpdate
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FluidRelayServer, or the result of cls(response)
        :rtype: ~azure.mgmt.fluidrelay.models.FluidRelayServer
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayServer]

        _json = self._serialize.body(resource, 'FluidRelayServerUpdate')

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FluidRelayServer', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        **kwargs: Any
    ) -> None:
        """Delete a Fluid Relay server.

        Delete a Fluid Relay server.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}"}  # type: ignore


    @distributed_trace_async
    async def regenerate_key(
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        parameters: _models.RegenerateKeyRequest,
        **kwargs: Any
    ) -> _models.FluidRelayServerKeys:
        """Regenerate the primary or secondary key for this server.

        Regenerate the primary or secondary key for this server.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :param parameters: The details of which keys to generate.
        :type parameters: ~azure.mgmt.fluidrelay.models.RegenerateKeyRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FluidRelayServerKeys, or the result of cls(response)
        :rtype: ~azure.mgmt.fluidrelay.models.FluidRelayServerKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayServerKeys]

        _json = self._serialize.body(parameters, 'RegenerateKeyRequest')

        request = build_regenerate_key_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.regenerate_key.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FluidRelayServerKeys', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regenerate_key.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/regenerateKey"}  # type: ignore


    @distributed_trace_async
    async def list_keys(
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        **kwargs: Any
    ) -> _models.FluidRelayServerKeys:
        """Get primary and secondary key for this server.

        Get primary and secondary key for this server.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FluidRelayServerKeys, or the result of cls(response)
        :rtype: ~azure.mgmt.fluidrelay.models.FluidRelayServerKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayServerKeys]

        
        request = build_list_keys_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            api_version=api_version,
            template_url=self.list_keys.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FluidRelayServerKeys', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_keys.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/listKeys"}  # type: ignore


    @distributed_trace
    def list_by_subscription(
        self,
        **kwargs: Any
    ) -> AsyncIterable[_models.FluidRelayServerList]:
        """List all Fluid Relay servers in a subscription.

        List all Fluid Relay servers in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FluidRelayServerList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.fluidrelay.models.FluidRelayServerList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayServerList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_subscription.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FluidRelayServerList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.FluidRelay/fluidRelayServers"}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.FluidRelayServerList]:
        """List all Fluid Relay servers in a resource group.

        List all Fluid Relay servers in a resource group.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FluidRelayServerList or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.fluidrelay.models.FluidRelayServerList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayServerList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group=resource_group,
                    api_version=api_version,
                    template_url=self.list_by_resource_group.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group=resource_group,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FluidRelayServerList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers"}  # type: ignore
