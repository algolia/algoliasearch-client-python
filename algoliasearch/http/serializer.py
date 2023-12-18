import json
from typing import Any, Dict


class Serializer:
    def parse_query_parameters(self, value) -> Any:
        if isinstance(value, dict):
            value = json.dumps(value)
        elif isinstance(value, list):
            serialized_value: list[str] = []

            for item in value:
                serialized_value.append(self.parse_query_parameters(item))
            value = ",".join(serialized_value)
        elif isinstance(value, bool):
            value = "true" if value else "false"
        else:
            value = str(value)
        return value

    def query_parameters(self, query_parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parses the given 'query_parameters' values of each keys into their string value.
        """

        for key, value in query_parameters.items():
            query_parameters[key] = self.parse_query_parameters(value)
        return query_parameters
