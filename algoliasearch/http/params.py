class Params:
    HEADERS = [
        'Content-type',
        'User-Agent',
    ]

    QUERY_PARAMETERS = [
        'createIfNotExists',
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
