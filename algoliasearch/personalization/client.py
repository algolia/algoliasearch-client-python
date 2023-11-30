# coding: utf-8

"""
Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.
"""
import json
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from algoliasearch.http.api_response import ApiResponse
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb
from algoliasearch.personalization.config import Config
from algoliasearch.personalization.models.delete_user_profile_response import (
    DeleteUserProfileResponse,
)
from algoliasearch.personalization.models.get_user_token_response import (
    GetUserTokenResponse,
)
from algoliasearch.personalization.models.personalization_strategy_params import (
    PersonalizationStrategyParams,
)
from algoliasearch.personalization.models.set_personalization_strategy_response import (
    SetPersonalizationStrategyResponse,
)

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class PersonalizationClient:
    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
        "object": object,
    }

    def app_id(self) -> str:
        return self._config.app_id

    def __init__(self, transporter: Transporter, config: Config) -> None:
        self._transporter = transporter
        self._config = config

    def create_with_config(config: Config) -> Self:
        transporter = Transporter(config)

        return PersonalizationClient(transporter, config)

    def create(app_id: Optional[str] = None, api_key: Optional[str] = None) -> Self:
        return PersonalizationClient.create_with_config(Config(app_id, api_key))

    async def close(self) -> None:
        return await self._transporter.close()

    def __deserialize(self, data: Optional[dict], klass: any = None) -> dict:
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith("List["):
                sub_kls = re.match(r"List\[(.*)]", klass).group(1)
                return [self.__deserialize(sub_data, sub_kls) for sub_data in data]

            if klass.startswith("Dict["):
                sub_kls = re.match(r"Dict\[([^,]*), (.*)]", klass).group(2)
                return {k: self.__deserialize(v, sub_kls) for k, v in data.items()}

            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]

        if klass in self.PRIMITIVE_TYPES:
            try:
                return klass(data)
            except UnicodeEncodeError:
                return str(data)
            except TypeError:
                return data
        elif klass == object:
            return data
        else:
            return klass.from_dict(data)

    async def call_del_with_http_info(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> ApiResponse[str]:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        if path is not None:
            _path_params["path"] = path

        if parameters is not None:
            _query_params.append(("parameters", parameters))

        _param = self._transporter.param_serialize(
            path="/1{path}",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.DELETE,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def call_del(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> object:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'object' result object.
        """

        response = await self.call_del_with_http_info(path, parameters, request_options)

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, object)

    async def delete_user_profile_with_http_info(
        self,
        user_token: Annotated[
            StrictStr,
            Field(
                description="userToken representing the user for which to fetch the Personalization profile."
            ),
        ],
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> ApiResponse[str]:
        """
        Delete a user profile.

        Delete the user profile and all its associated data.  Returns, as part of the response, a date until which the data can safely be considered as deleted for the given user. This means if you send events for the given user before this date, they will be ignored. Any data received after the deletedUntil date will start building a new user profile.  It might take a couple hours for the deletion request to be fully processed.

        :param user_token: userToken representing the user for which to fetch the Personalization profile. (required)
        :type user_token: str
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        if user_token is not None:
            _path_params["userToken"] = user_token

        _param = self._transporter.param_serialize(
            path="/1/profiles/{userToken}",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.DELETE,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def delete_user_profile(
        self,
        user_token: Annotated[
            StrictStr,
            Field(
                description="userToken representing the user for which to fetch the Personalization profile."
            ),
        ],
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> DeleteUserProfileResponse:
        """
        Delete a user profile.

        Delete the user profile and all its associated data.  Returns, as part of the response, a date until which the data can safely be considered as deleted for the given user. This means if you send events for the given user before this date, they will be ignored. Any data received after the deletedUntil date will start building a new user profile.  It might take a couple hours for the deletion request to be fully processed.

        :param user_token: userToken representing the user for which to fetch the Personalization profile. (required)
        :type user_token: str
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'DeleteUserProfileResponse' result object.
        """

        response = await self.delete_user_profile_with_http_info(
            user_token, request_options
        )

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, DeleteUserProfileResponse)

    async def get_with_http_info(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> ApiResponse[str]:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        if path is not None:
            _path_params["path"] = path

        if parameters is not None:
            _query_params.append(("parameters", parameters))

        _param = self._transporter.param_serialize(
            path="/1{path}",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.GET,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def get(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> object:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'object' result object.
        """

        response = await self.get_with_http_info(path, parameters, request_options)

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, object)

    async def get_personalization_strategy_with_http_info(
        self, request_options: Optional[Union[dict, RequestOptions]] = None
    ) -> ApiResponse[str]:
        """
        Get the current strategy.

        The strategy contains information on the events and facets that impact user profiles and personalized search results.

        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        _param = self._transporter.param_serialize(
            path="/1/strategies/personalization",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.GET,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def get_personalization_strategy(
        self, request_options: Optional[Union[dict, RequestOptions]] = None
    ) -> PersonalizationStrategyParams:
        """
        Get the current strategy.

        The strategy contains information on the events and facets that impact user profiles and personalized search results.

        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'PersonalizationStrategyParams' result object.
        """

        response = await self.get_personalization_strategy_with_http_info(
            request_options
        )

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, PersonalizationStrategyParams)

    async def get_user_token_profile_with_http_info(
        self,
        user_token: Annotated[
            StrictStr,
            Field(
                description="userToken representing the user for which to fetch the Personalization profile."
            ),
        ],
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> ApiResponse[str]:
        """
        Get a user profile.

        Get the user profile built from Personalization strategy.  The profile is structured by facet name used in the strategy. Each facet value is mapped to its score. Each score represents the user affinity for a specific facet value given the userToken past events and the Personalization strategy defined. Scores are bounded to 20. The last processed event timestamp is provided using the ISO 8601 format for debugging purposes.

        :param user_token: userToken representing the user for which to fetch the Personalization profile. (required)
        :type user_token: str
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        if user_token is not None:
            _path_params["userToken"] = user_token

        _param = self._transporter.param_serialize(
            path="/1/profiles/personalization/{userToken}",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.GET,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def get_user_token_profile(
        self,
        user_token: Annotated[
            StrictStr,
            Field(
                description="userToken representing the user for which to fetch the Personalization profile."
            ),
        ],
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> GetUserTokenResponse:
        """
        Get a user profile.

        Get the user profile built from Personalization strategy.  The profile is structured by facet name used in the strategy. Each facet value is mapped to its score. Each score represents the user affinity for a specific facet value given the userToken past events and the Personalization strategy defined. Scores are bounded to 20. The last processed event timestamp is provided using the ISO 8601 format for debugging purposes.

        :param user_token: userToken representing the user for which to fetch the Personalization profile. (required)
        :type user_token: str
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'GetUserTokenResponse' result object.
        """

        response = await self.get_user_token_profile_with_http_info(
            user_token, request_options
        )

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, GetUserTokenResponse)

    async def post_with_http_info(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        body: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Parameters to send with the custom request."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> ApiResponse[str]:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param body: Parameters to send with the custom request.
        :type body: object
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        if path is not None:
            _path_params["path"] = path

        if parameters is not None:
            _query_params.append(("parameters", parameters))

        if body is not None:
            _body_params = body

        _param = self._transporter.param_serialize(
            path="/1{path}",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.POST,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def post(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        body: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Parameters to send with the custom request."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> object:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param body: Parameters to send with the custom request.
        :type body: object
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'object' result object.
        """

        response = await self.post_with_http_info(
            path, parameters, body, request_options
        )

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, object)

    async def put_with_http_info(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        body: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Parameters to send with the custom request."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> ApiResponse[str]:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param body: Parameters to send with the custom request.
        :type body: object
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        if path is not None:
            _path_params["path"] = path

        if parameters is not None:
            _query_params.append(("parameters", parameters))

        if body is not None:
            _body_params = body

        _param = self._transporter.param_serialize(
            path="/1{path}",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.PUT,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def put(
        self,
        path: Annotated[
            StrictStr,
            Field(
                description='Path of the endpoint, anything after "/1" must be specified.'
            ),
        ],
        parameters: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Query parameters to apply to the current query."),
        ] = None,
        body: Annotated[
            Optional[Dict[str, Any]],
            Field(description="Parameters to send with the custom request."),
        ] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> object:
        """
        Send requests to the Algolia REST API.

        This method allow you to send requests to the Algolia REST API.

        :param path: Path of the endpoint, anything after \"/1\" must be specified. (required)
        :type path: str
        :param parameters: Query parameters to apply to the current query.
        :type parameters: Dict[str, object]
        :param body: Parameters to send with the custom request.
        :type body: object
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'object' result object.
        """

        response = await self.put_with_http_info(
            path, parameters, body, request_options
        )

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, object)

    async def set_personalization_strategy_with_http_info(
        self,
        personalization_strategy_params: PersonalizationStrategyParams,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> ApiResponse[str]:
        """
        Set a new strategy.

        A strategy defines the events and facets that impact user profiles and personalized search results.

        :param personalization_strategy_params: (required)
        :type personalization_strategy_params: PersonalizationStrategyParams
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the raw algoliasearch 'APIResponse' object.
        """

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _body_params: Optional[bytes] = None

        if personalization_strategy_params is not None:
            _body_params = personalization_strategy_params

        _param = self._transporter.param_serialize(
            path="/1/strategies/personalization",
            path_params=_path_params,
            query_params=_query_params,
            body=_body_params,
            request_options=request_options,
        )

        response = await self._transporter.request(
            verb=Verb.POST,
            path=_param[0],
            data=_param[1],
            request_options=_param[2],
            use_read_transporter=True,
        )

        response.data = response.raw_data

        return response

    async def set_personalization_strategy(
        self,
        personalization_strategy_params: PersonalizationStrategyParams,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> SetPersonalizationStrategyResponse:
        """
        Set a new strategy.

        A strategy defines the events and facets that impact user profiles and personalized search results.

        :param personalization_strategy_params: (required)
        :type personalization_strategy_params: PersonalizationStrategyParams
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: Returns the deserialized response in a 'SetPersonalizationStrategyResponse' result object.
        """

        response = await self.set_personalization_strategy_with_http_info(
            personalization_strategy_params, request_options
        )

        try:
            data = json.loads(response.raw_data)
        except ValueError:
            data = response.raw_data

        return self.__deserialize(data, SetPersonalizationStrategyResponse)
