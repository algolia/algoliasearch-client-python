class Params:
    HEADERS = [
        'Content-type',
        'User-Agent',
        'createIfNotExists',
    ]

    QUERY_PARAMETERS = [
        'forwardToReplicas',
        'replaceExistingSynonyms',
        'clearExistingRules',
        'getVersion',
    ]

    TIMEOUTS = [
        'readTimeout',
        'writeTimeout',
        'connectTimeout',
    ]
