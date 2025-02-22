#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import typing as _typing

import apache.thrift.metadata.thrift_types as _fbthrift_metadata
import folly.iobuf as _fbthrift_iobuf
from thrift.python.client import (
    AsyncClient as _fbthrift_python_AsyncClient,
    SyncClient as _fbthrift_python_SyncClient,
    Client as _fbthrift_python_Client,
)
from thrift.python.client.omni_client import InteractionMethodPosition as _fbthrift_InteractionMethodPosition, FunctionQualifier as _fbthrift_FunctionQualifier
from thrift.python.common import RpcOptions
import thrift.python.exceptions as _fbthrift_python_exceptions
import thrift.python.types as _fbthrift_python_types
import meta.example.thrift.service.thrift_types as _fbthrift__meta__example__thrift__service__thrift_types
import meta.example.thrift.service.thrift_metadata

class EchoService(_fbthrift_python_Client["EchoService.Async", "EchoService.Sync"]):
    @staticmethod
    def __get_thrift_name__() -> str:
        return "service.EchoService"
    
    @staticmethod
    def __get_thrift_uri__() -> _typing.Optional[str]:
        return None
    
    @staticmethod
    def __get_thrift_unstructured_annotations_DEPRECATED__() -> _typing.Mapping[str, str]:
        return {
        }
    
    @staticmethod
    def __get_metadata__() -> _fbthrift_metadata.ThriftMetadata:
        return meta.example.thrift.service.thrift_metadata.gen_metadata_service_EchoService()
    
    class Async(_fbthrift_python_AsyncClient):
        @staticmethod
        def __get_thrift_name__() -> str:
            return "service.EchoService"
    
        @staticmethod
        def __get_thrift_uri__() -> _typing.Optional[str]:
            return None
    
        @staticmethod
        def __get_metadata__() -> _fbthrift_metadata.ThriftMetadata:
            return meta.example.thrift.service.thrift_metadata.gen_metadata_service_EchoService()
    
        async def echo(
            self,
            request: _fbthrift__meta__example__thrift__service__thrift_types.EchoRequest,
            *,
            rpc_options: _typing.Optional[RpcOptions] = None,
        ) -> _fbthrift__meta__example__thrift__service__thrift_types.EchoResponse:
            _fbthrift_resp = await self._send_request(
                "EchoService",
                "echo",
                _fbthrift__meta__example__thrift__service__thrift_types._fbthrift_EchoService_echo_args(
                    request=request,),
                _fbthrift__meta__example__thrift__service__thrift_types._fbthrift_EchoService_echo_result,
                qualifier = _fbthrift_FunctionQualifier.Unspecified,
                uri_or_name="EchoService",
                rpc_options=rpc_options,
            )
            # shortcut to success path for non-void returns
            if _fbthrift_resp.success is not None:
                return _fbthrift_resp.success
            if _fbthrift_resp.ex is not None:
                raise _fbthrift_resp.ex
            raise _fbthrift_python_exceptions.ApplicationError(
                _fbthrift_python_exceptions.ApplicationErrorType.MISSING_RESULT,
                "Empty Response",
            )
    
    
    # pyre-ignore[4]: Missing annotation.
    echo = Async.echo
    
    class Sync(_fbthrift_python_SyncClient):
        @staticmethod
        def __get_thrift_name__() -> str:
            return "service.EchoService"
    
        @staticmethod
        def __get_thrift_uri__() -> _typing.Optional[str]:
            return None
    
        @staticmethod
        def __get_metadata__() -> _fbthrift_metadata.ThriftMetadata:
            return meta.example.thrift.service.thrift_metadata.gen_metadata_service_EchoService()
    
        def echo(
            self,
            request: _fbthrift__meta__example__thrift__service__thrift_types.EchoRequest,
            *,
            rpc_options: _typing.Optional[RpcOptions] = None,
        ) -> _fbthrift__meta__example__thrift__service__thrift_types.EchoResponse:
            _fbthrift_resp = self._send_request(
                "EchoService",
                "echo",
                _fbthrift__meta__example__thrift__service__thrift_types._fbthrift_EchoService_echo_args(
                    request=request,),
                _fbthrift__meta__example__thrift__service__thrift_types._fbthrift_EchoService_echo_result,
                uri_or_name="EchoService",
                rpc_options=rpc_options,
            )
            # shortcut to success path for non-void returns
            if _fbthrift_resp.success is not None:
                return _fbthrift_resp.success
            if _fbthrift_resp.ex is not None:
                raise _fbthrift_resp.ex
            raise _fbthrift_python_exceptions.ApplicationError(
                _fbthrift_python_exceptions.ApplicationErrorType.MISSING_RESULT,
                "Empty Response",
            )

