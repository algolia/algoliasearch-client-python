<?php

// This file is generated, manual changes will be lost - read more on https://github.com/algolia/api-clients-automation.

namespace Algolia\AlgoliaSearch\Model\Recommend;

/**
 * AlternativesAsExact Class Doc Comment
 *
 * @category Class
 * @package Algolia\AlgoliaSearch
 */
class AlternativesAsExact
{
    /**
     * Possible values of this enum
     */
    const IGNORE_PLURALS = 'ignorePlurals';

    const SINGLE_WORD_SYNONYM = 'singleWordSynonym';

    const MULTI_WORDS_SYNONYM = 'multiWordsSynonym';

    /**
     * Gets allowable values of the enum
     *
     * @return string[]
     */
    public static function getAllowableEnumValues()
    {
        return [
            self::IGNORE_PLURALS,
            self::SINGLE_WORD_SYNONYM,
            self::MULTI_WORDS_SYNONYM,
        ];
    }
}