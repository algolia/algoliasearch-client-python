<?php

// Code generated by OpenAPI Generator (https://openapi-generator.tech), manual changes will be lost - read more on https://github.com/algolia/api-clients-automation. DO NOT EDIT.

namespace Algolia\AlgoliaSearch\Model\Abtesting;

/**
 * AddABTestsRequest Class Doc Comment
 *
 * @category Class
 * @package Algolia\AlgoliaSearch
 */
class AddABTestsRequest extends \Algolia\AlgoliaSearch\Model\AbstractModel implements ModelInterface, \ArrayAccess, \JsonSerializable
{
    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $modelTypes = [
        'name' => 'string',
        'variants' => '\Algolia\AlgoliaSearch\Model\Abtesting\AddABTestsVariant[]',
        'endAt' => 'string',
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $modelFormats = [
        'name' => null,
        'variants' => null,
        'endAt' => null,
    ];

    /**
      * Array of attributes where the key is the local name,
      * and the value is the original name
      *
      * @var string[]
    */
    protected static $attributeMap = [
        'name' => 'name',
        'variants' => 'variants',
        'endAt' => 'endAt',
    ];

    /**
      * Array of attributes where the key is the local name,
      * and the value is the original name
      *
      * @return array
      */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function modelTypes()
    {
        return self::$modelTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function modelFormats()
    {
        return self::$modelFormats;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'name' => 'setName',
        'variants' => 'setVariants',
        'endAt' => 'setEndAt',
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'name' => 'getName',
        'variants' => 'getVariants',
        'endAt' => 'getEndAt',
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     */
    public function __construct(array $data = null)
    {
        if (isset($data['name'])) {
            $this->container['name'] = $data['name'];
        }
        if (isset($data['variants'])) {
            $this->container['variants'] = $data['variants'];
        }
        if (isset($data['endAt'])) {
            $this->container['endAt'] = $data['endAt'];
        }
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if (!isset($this->container['name']) || $this->container['name'] === null) {
            $invalidProperties[] = "'name' can't be null";
        }
        if (!isset($this->container['variants']) || $this->container['variants'] === null) {
            $invalidProperties[] = "'variants' can't be null";
        }
        if ((count($this->container['variants']) > 2)) {
            $invalidProperties[] = "invalid value for 'variants', number of items must be less than or equal to 2.";
        }

        if ((count($this->container['variants']) < 2)) {
            $invalidProperties[] = "invalid value for 'variants', number of items must be greater than or equal to 2.";
        }

        if (!isset($this->container['endAt']) || $this->container['endAt'] === null) {
            $invalidProperties[] = "'endAt' can't be null";
        }

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }

    /**
     * Gets name
     *
     * @return string
     */
    public function getName()
    {
        return $this->container['name'] ?? null;
    }

    /**
     * Sets name
     *
     * @param string $name A/B test name
     *
     * @return self
     */
    public function setName($name)
    {
        $this->container['name'] = $name;

        return $this;
    }

    /**
     * Gets variants
     *
     * @return \Algolia\AlgoliaSearch\Model\Abtesting\AddABTestsVariant[]
     */
    public function getVariants()
    {
        return $this->container['variants'] ?? null;
    }

    /**
     * Sets variants
     *
     * @param \Algolia\AlgoliaSearch\Model\Abtesting\AddABTestsVariant[] $variants A/B test variants
     *
     * @return self
     */
    public function setVariants($variants)
    {

        if ((count($variants) > 2)) {
            throw new \InvalidArgumentException('invalid value for $variants when calling AddABTestsRequest., number of items must be less than or equal to 2.');
        }
        if ((count($variants) < 2)) {
            throw new \InvalidArgumentException('invalid length for $variants when calling AddABTestsRequest., number of items must be greater than or equal to 2.');
        }
        $this->container['variants'] = $variants;

        return $this;
    }

    /**
     * Gets endAt
     *
     * @return string
     */
    public function getEndAt()
    {
        return $this->container['endAt'] ?? null;
    }

    /**
     * Sets endAt
     *
     * @param string $endAt End date timestamp in [ISO-8601](https://wikipedia.org/wiki/ISO_8601) format.
     *
     * @return self
     */
    public function setEndAt($endAt)
    {
        $this->container['endAt'] = $endAt;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param int $offset Offset
     *
     * @return bool
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param int $offset Offset
     *
     * @return mixed|null
     */
    public function offsetGet($offset)
    {
        return $this->container[$offset] ?? null;
    }

    /**
     * Sets value based on offset.
     *
     * @param int|null $offset Offset
     * @param mixed    $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param int $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }
}

