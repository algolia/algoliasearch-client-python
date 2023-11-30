import json
from typing import Any, Dict
from urllib.parse import urlencode


class QueryParametersSerializer:
    def serialize(query_parameters: Dict[str, Any]) -> str:
        for key, value in query_parameters.items():
            if isinstance(value, (list, dict)):
                value = json.dumps(value)
            elif isinstance(value, bool):
                value = "true" if value else "false"

            query_parameters[key] = value

        return urlencode(sorted(query_parameters.items(), key=lambda val: val[0]))
