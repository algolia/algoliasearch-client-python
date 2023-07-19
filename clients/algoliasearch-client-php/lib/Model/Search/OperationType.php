<?php

// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

namespace Algolia\AlgoliaSearch\Model\Search;

/**
 * OperationType Class Doc Comment
 *
 * @category Class
 *
 * @description Operation to perform (_move_ or _copy_).
 *
 * @package Algolia\AlgoliaSearch
 */
class OperationType
{
    /**
     * Possible values of this enum
     */
    const MOVE = 'move';

    const COPY = 'copy';

    /**
     * Gets allowable values of the enum
     *
     * @return string[]
     */
    public static function getAllowableEnumValues()
    {
        return [
            self::MOVE,
            self::COPY,
        ];
    }
}

