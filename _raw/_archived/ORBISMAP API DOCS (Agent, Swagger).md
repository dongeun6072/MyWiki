
{
    "openapi": "3.0.1",
    "info": {
        "title": "ORBISMAP API DOCS",
        "description": "ORBISMAP API DOCS",
        "version": "1.0"
    },
    "servers": [
        {
            "url": "[HOST]",
            "description": "Generated server url"
        }
    ],
    "security": [
        {
            "bearerAuth": []
        }
    ],
    "tags": [
        {
            "name": "TomTom",
            "description": "TomTom 관련 API"
        },
        {
            "name": "Auth",
            "description": "인증 관련 API"
        },
        {
            "name": "System",
            "description": "시스템 관련 API"
        },
        {
            "name": "Common",
            "description": "AWS LB 체크 API"
        },
        {
            "name": "Route",
            "description": "탐색 관련 API"
        }
    ],
    "paths": {
        "/api/tomtom/search/reverse-geocode": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Orbis Reverse Geocode API",
                "description": "Orbis 역지오코딩",
                "operationId": "getTomTomReverseGeocode",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomReverseGeocodeRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomReverseGeocodeResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/poi": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Orbis POI Search API",
                "description": "Orbis POI 검색 ",
                "operationId": "getTomTomPoiSearch",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSearchCommonRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSearchResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/nearby": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Orbis Nearby Search API",
                "description": "Orbis 주변 검색",
                "operationId": "getTomTomNearbySearch",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSearchCommonRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSearchResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/geocode": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Orbis Geocode API",
                "description": "Orbis 지오코딩",
                "operationId": "getTomTomGeocode",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSearchCommonRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSearchResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/genesis/reverse-geocode": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Genesis Reverse Geocode API",
                "description": "Genesis 역지오코딩",
                "operationId": "getTomTomGenesisReverseGeocode",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomReverseGeocodeRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomReverseGeocodeResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/genesis/geocode": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Genesis Geocode API",
                "description": "Genesis 지오코딩",
                "operationId": "getTomTomGenesisGeocode",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSearchCommonRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSearchResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/genesis/fuzzy": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Genesis Fuzzy Search API",
                "description": "Genesis Fuzzy 검색",
                "operationId": "getTomTomGenesisFuzzySearch",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSearchCommonRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSearchResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/fuzzy": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Orbis Fuzzy Search API",
                "description": "Orbis Fuzzy 검색",
                "operationId": "getTomTomFuzzySearch",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSearchCommonRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSearchResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/search/category": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "Orbis Category Search API",
                "description": "Orbis 카테고리 검색",
                "operationId": "getTomTomSearchCategory",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSearchCommonRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSearchResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/safety-camera/mobile": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "TomTom Mobile Safety Cameras API",
                "description": "Safety Camera Alerts - Mobile Safety Cameras",
                "operationId": "getTomTomMobileSafetyCameras",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSafetyCameraRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSafetyCameraResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/safety-camera/fixed": {
            "post": {
                "tags": [
                    "TomTom"
                ],
                "summary": "TomTom Fixed Safety Cameras API",
                "description": "Safety Camera Alerts - Fixed Safety Cameras",
                "operationId": "getTomTomFixedSafetyCameras",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TomTomSafetyCameraRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomSafetyCameraResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/serviceGate": {
            "post": {
                "tags": [
                    "System"
                ],
                "summary": "초기 구동",
                "description": "초기 구동 정보를 조회한다.",
                "operationId": "getServiceGate",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/ServiceGateRequest"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/ServiceGateResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/searchRoute": {
            "post": {
                "tags": [
                    "Route"
                ],
                "summary": "경로 탐색",
                "description": "출발지, 목적지, 경유지 요청 필드 등을 통해 출발지에서 목적지까지의 최적 경로를 반환한다.",
                "operationId": "getSearchRoute",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/SearchRouteRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/SearchRouteResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/searchRoute/multi": {
            "post": {
                "tags": [
                    "Route"
                ],
                "summary": "다중 경로 탐색",
                "description": "기본 최적 경로와 함께 최대 3 개의 경로를 반환한다. 출발지와 목적지까지 도로 상황에 따라 최적 경로 외에 대안 경로가 존재하지 않으면, 3개 미만의 경로만 반환한다.",
                "operationId": "getSearchRouteMulti",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/SearchRouteMultiRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/SearchRouteMultiResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/auth": {
            "post": {
                "tags": [
                    "Auth"
                ],
                "summary": "인증 API",
                "description": "imaps 인증 및 JWT 생성 API",
                "operationId": "getAuth",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AuthRequest"
                            }
                        }
                    },
                    "required": true
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/AuthResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/tomtom/key": {
            "get": {
                "tags": [
                    "TomTom"
                ],
                "summary": "TomTom key API",
                "description": "TomTom key를 전달해주는 전용 API",
                "operationId": "getTomTomKey",
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/TomTomKeyResponse"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        },
        "/api/health": {
            "get": {
                "tags": [
                    "Common"
                ],
                "summary": "로드벨런서 Health Check",
                "operationId": "health",
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "$ref": "#/components/schemas/Response"
                                }
                            }
                        }
                    }
                }
            },
            "parameters": [
                {
                    "name": "INAVI",
                    "in": "header",
                    "description": "Service Key",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "SYSTEMS"
                    }
                },
                {
                    "name": "country",
                    "in": "header",
                    "description": "국가 코드",
                    "required": true,
                    "schema": {
                        "type": "string",
                        "default": "TW"
                    }
                },
                {
                    "name": "osType",
                    "in": "header",
                    "description": "OS Type",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "ANDROID",
                        "enum": [
                            "ANDROID",
                            "IOS"
                        ]
                    }
                },
                {
                    "name": "osVer",
                    "in": "header",
                    "description": "Device OS Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "12.0"
                    }
                },
                {
                    "name": "appVer",
                    "in": "header",
                    "description": "App Version",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "1.0.0"
                    }
                },
                {
                    "name": "appVerCode",
                    "in": "header",
                    "description": "App Version Code",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "483"
                    }
                },
                {
                    "name": "device",
                    "in": "header",
                    "description": "Device Name",
                    "required": false,
                    "schema": {
                        "type": "string",
                        "default": "SM-S918N"
                    }
                }
            ]
        }
    },
    "components": {
        "schemas": {
            "TomTomReverseGeocodeRequest": {
                "required": [
                    "ext",
                    "key",
                    "lat",
                    "lon"
                ],
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "유효한 API 키"
                    },
                    "ext": {
                        "type": "string",
                        "description": "유효 응답 형식",
                        "example": "json"
                    },
                    "language": {
                        "type": "string",
                        "description": "검색 결과가 반환될 언어"
                    },
                    "view": {
                        "type": "string",
                        "description": "\n        지정 학적 견해. 분쟁 영토의 처리를 해결하는 데 사용되는 맥락.\n        AR, CN, IL, IN, MA, PK, RU, RS 및 TW와 함께 통합은 각각 아르헨티나, 중국, 이스라엘, 인도, 모로코, 파키스탄, 러시아, 세르비아 및 대만에 맞게 조정됩니다.\n        \n        [Default values]\n        Argentina: AR\n        China: CN\n        India: IN\n        Morocco: MA\n        Pakistan: PK\n        Russia: RU\n        Serbia: RS\n        Taiwan: TW\n        Others: Unified\n    ",
                        "example": "Unified"
                    },
                    "limit": {
                        "maximum": 100,
                        "type": "integer",
                        "description": "반환되는 응답의 최대 수",
                        "format": "int32",
                        "example": 20,
                        "default": 10
                    },
                    "lat": {
                        "type": "number",
                        "description": "WGS84 위도",
                        "format": "float",
                        "example": 25.037727
                    },
                    "lon": {
                        "type": "number",
                        "description": "WGS84 경도",
                        "format": "float",
                        "example": 121.511246
                    },
                    "radius": {
                        "type": "integer",
                        "description": "검색 반경 (미터)",
                        "format": "int32",
                        "default": 10000
                    },
                    "heading": {
                        "maximum": 360,
                        "minimum": -360,
                        "type": "integer",
                        "description": "차량 진행 방향 각도",
                        "format": "int32"
                    },
                    "number": {
                        "type": "string",
                        "description": "특정 주소 번호 검색"
                    },
                    "returnMatchType": {
                        "type": "boolean",
                        "description": "결과 매치 타입 반환 여부"
                    },
                    "allowFreeformNewline": {
                        "type": "boolean",
                        "description": "주소 개행 문자 허용 여부",
                        "default": false
                    },
                    "returnIntersectionDetails": {
                        "type": "boolean",
                        "description": "교차로 상세 정보 반환 여부"
                    },
                    "returnSpeedLimit": {
                        "type": "boolean",
                        "description": "속도 제한 정보 반환 여부"
                    },
                    "returnRoadUse": {
                        "type": "boolean",
                        "description": "도로 이용 제한 정보 반환 여부"
                    },
                    "roadUse": {
                        "type": "string",
                        "description": "특정 도로 이용 제한 타입 필터"
                    },
                    "entityType": {
                        "type": "string",
                        "description": "지리 정보에 대해 수행되는 필터링 수준을 지정"
                    },
                    "extendedPostalCodesFor": {
                        "type": "string"
                    }
                }
            },
            "Address": {
                "type": "object",
                "properties": {
                    "streetNumber": {
                        "type": "string",
                        "description": "거리 번호"
                    },
                    "streetName": {
                        "type": "string",
                        "description": "거리명"
                    },
                    "municipalitySubdivision": {
                        "type": "string",
                        "description": "하위 도시(Sub City)"
                    },
                    "municipalitySecondarySubdivision": {
                        "type": "string",
                        "description": "하위 하위 도시 (Sub Sub City)"
                    },
                    "neighbourhood": {
                        "type": "string",
                        "description": "동네/지역"
                    },
                    "municipality": {
                        "type": "string",
                        "description": "도시/마을(City / Town)"
                    },
                    "countrySecondarySubdivision": {
                        "type": "string",
                        "description": "County"
                    },
                    "countryTertiarySubdivision": {
                        "type": "string",
                        "description": "Named Area"
                    },
                    "countrySubdivision": {
                        "type": "string",
                        "description": "State or Province"
                    },
                    "postalCode": {
                        "type": "string",
                        "description": "우편번호"
                    },
                    "postalName": {
                        "type": "string",
                        "description": "단일 행정구역"
                    },
                    "extendedPostalCode": {
                        "type": "string",
                        "description": "확장 우편번호"
                    },
                    "countryCode": {
                        "type": "string",
                        "description": "국가 코드(2글자 코드)"
                    },
                    "country": {
                        "type": "string",
                        "description": "국가"
                    },
                    "countryCodeISO3": {
                        "type": "string",
                        "description": "국가 코드(3글자)"
                    },
                    "freeformAddress": {
                        "type": "string",
                        "description": "전체 주소 문자열"
                    },
                    "countrySubdivisionName": {
                        "type": "string",
                        "description": "\n        국가의 첫 번째 행정 계층의 전체 이름\n        미국, 캐나다, 영국에서만 지원\n    "
                    },
                    "countrySubdivisionCode": {
                        "type": "string",
                        "description": "countryCode와 countrySubdivisionCode를 하이픈으로 연결한 ISO 3166-2 코드",
                        "example": "TX|ON"
                    },
                    "localName": {
                        "type": "string",
                        "description": "행정 단위가 아닌 주소 지정 목적으로 여러 주소 지정 가능한 객체를 그룹화하는 지리적 영역 또는 지역의 이름을 나타내는 주소 구성요소"
                    }
                },
                "description": "주소 정보 객체"
            },
            "BoundingBox": {
                "type": "object",
                "properties": {
                    "topLeftPoint": {
                        "$ref": "#/components/schemas/LatLon"
                    },
                    "btmRightPoint": {
                        "$ref": "#/components/schemas/LatLon"
                    }
                }
            },
            "IntersectionDetail": {
                "type": "object",
                "properties": {
                    "streets": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "type": {
                        "type": "string"
                    }
                },
                "description": "교차로 정보 (returnIntersectionDetails=true 요청 시)"
            },
            "LatLon": {
                "type": "object",
                "properties": {
                    "lat": {
                        "type": "number",
                        "format": "float"
                    },
                    "lon": {
                        "type": "number",
                        "format": "float"
                    }
                }
            },
            "Mapcode": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "맵코드 유형",
                        "example": "Local|International|Alternative"
                    },
                    "fullMapcode": {
                        "type": "string",
                        "description": "지도 코드(territory + code)의 전체 형태"
                    },
                    "territory": {
                        "type": "string",
                        "description": "맵코드의 영토 요소"
                    },
                    "code": {
                        "type": "string"
                    }
                }
            },
            "QueryIntent": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "\n        쿼리 의도 유형\n        COORDINATE|NEARBY|W3W|BOOKMARK\"\n    "
                    },
                    "details": {
                        "$ref": "#/components/schemas/QueryIntentDetails"
                    }
                },
                "description": "감지된 쿼리 의도 목록"
            },
            "QueryIntentDetails": {
                "type": "object",
                "properties": {
                    "lat": {
                        "type": "number",
                        "description": "COORDINATE details",
                        "format": "float"
                    },
                    "lon": {
                        "type": "number",
                        "description": "COORDINATE details",
                        "format": "float"
                    },
                    "query": {
                        "type": "string",
                        "description": "NEARBY details"
                    },
                    "text": {
                        "type": "string",
                        "description": "NEARBY details"
                    },
                    "address": {
                        "type": "string",
                        "description": "W3W details"
                    },
                    "bookmark": {
                        "type": "string",
                        "description": "\n       BOOKMARK details\n       HOME|WORK\n    "
                    }
                }
            },
            "Result": {
                "required": [
                    "code",
                    "message"
                ],
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "\n        응답 코드\n        \n        SUCCESS - 성공\n        ROUTE_FAILED - 경로 탐색에 실패했습니다.\n        ROUTE_EXPANSION_FAILED - 경로 탐색 시 도로 확장에 실패했습니다.\n        NO_ROAD_NEAR_START - 출발지 근처에 도로가 존재하지 않습니다.\n        NO_ROAD_NEAR_DESTINATION - 목적지 근처에 도로가 존재하지 않습니다.\n        NO_ROAD_NEAR_WAYPOINT - 경유지 근처에 도로가 존재하지 않습니다.\n        NOT_SUPPORT_COUNTRY - 지원하지 않는 국가입니다.\n        SERVICE_NOT_SUPPORTED - 미지원 서비스 입니다.\n        AUTH_FAIL - 사용자 인증에 실패 하였습니다.앱 재실행 후 사용해 주세요.\n        IMAPS_FAIL - imaps API 호출 실패했습니다.\n        PERSONAL_KEY_CHECK_FAIL - 사용자 정보가 변경되었습니다. 약관 재 동의 후 사용해 주세요.\n        NO_MATCH_MEMBER - 일치하는 회원 정보가 없습니다.\n        NEED_ID_PASSWORD_CONFIRM - 아이디, 비밀번호 확인이 필요합니다.\n        NEED_EMAIL_CONFIRM - 이메일 인증이 필요합니다. 이메일 인증 후 재시도 해주시기 바랍니다.\n        ENCRYPTION_ERROR - 데이터 암호화 처리 중 오류가 발생했습니다.\n        DECRYPTION_ERROR - 데이터 복호화 처리 중 오류가 발생했습니다.\n        WEBCLIENT_ERROR - 외부 통신 처리 중 오류가 발생했습니다.\n        DATA_NOT_FOUND - 조회된 데이터가 없습니다.\n        DATA_INTEGRITY_ERROR - DB 무결성이 유효하지 않습니다.\n        INTERNAL_SERVER_ERROR - 서버 내부 오류가 발생했습니다.\n        REQUEST_ERROR - 요청하신 정보가 유효하지 않거나 올바르지 않습니다.\n        UNDEFINED_ERROR - 접속이 지연되고 있습니다. 잠시 후 다시 시도해 주세요.\n    ",
                        "example": "Success",
                        "enum": [
                            "SUCCESS",
                            "ROUTE_FAILED",
                            "ROUTE_EXPANSION_FAILED",
                            "NO_ROAD_NEAR_START",
                            "NO_ROAD_NEAR_DESTINATION",
                            "NO_ROAD_NEAR_WAYPOINT",
                            "NOT_SUPPORT_COUNTRY",
                            "NOT_SUPPORT_APP_VERSION",
                            "NOT_SUPPORT_TOMTOM",
                            "SERVICE_NOT_SUPPORTED",
                            "AUTH_FAIL",
                            "IMAPS_FAIL",
                            "APPKEY_ERROR",
                            "NOT_FOUND_MAP_INFO",
                            "NO_MATCH_MEMBER",
                            "NEED_ID_PASSWORD_CONFIRM",
                            "NEED_EMAIL_CONFIRM",
                            "PERSONAL_KEY_CHECK_FAIL",
                            "ENCRYPTION_ERROR",
                            "DECRYPTION_ERROR",
                            "WEBCLIENT_ERROR",
                            "DATA_NOT_FOUND",
                            "DATA_INTEGRITY_ERROR",
                            "INTERNAL_SERVER_ERROR",
                            "REQUEST_ERROR",
                            "UNDEFINED_ERROR",
                            "TIME_LOCK_ERROR"
                        ]
                    },
                    "message": {
                        "type": "string",
                        "description": "응답 정보",
                        "example": "성공"
                    }
                }
            },
            "ReverseGeocodeAddress": {
                "type": "object",
                "properties": {
                    "address": {
                        "$ref": "#/components/schemas/Address"
                    },
                    "position": {
                        "type": "string",
                        "description": "결과의 위치(위도, 경도)"
                    },
                    "id": {
                        "type": "string",
                        "description": "고유 ID"
                    },
                    "matchType": {
                        "type": "string",
                        "description": "매치 유형 (returnMatchType=true 요청 시)",
                        "example": "PointAddress|Street|Intersection|Geography"
                    },
                    "distance": {
                        "type": "number",
                        "format": "double"
                    },
                    "mapcodes": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Mapcode"
                        }
                    },
                    "intersection": {
                        "$ref": "#/components/schemas/IntersectionDetail"
                    },
                    "speedLimit": {
                        "type": "string",
                        "description": "속도 제한 정보 (returnSpeedLimit=true 요청 시)",
                        "example": "50 km/h"
                    },
                    "roadUse": {
                        "type": "array",
                        "description": "도로 이용 제한 정보 (returnRoadUse=true 요청 시)",
                        "example": "LimitedAccess|Tunnel",
                        "items": {
                            "type": "string",
                            "description": "도로 이용 제한 정보 (returnRoadUse=true 요청 시)",
                            "example": "LimitedAccess|Tunnel"
                        }
                    },
                    "entityType": {
                        "type": "string"
                    },
                    "boundingBox": {
                        "$ref": "#/components/schemas/BoundingBox"
                    }
                },
                "description": "Reverse Geocode Address 목록"
            },
            "Summary": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "검색 엔진이 해석한 쿼리"
                    },
                    "queryType": {
                        "type": "string",
                        "description": "\n        쿼리 타입\n        NEARBY|NON_NEAR\n    "
                    },
                    "queryTime": {
                        "type": "integer",
                        "description": "쿼리 처리에 소요된 시간",
                        "format": "int32"
                    },
                    "numResults": {
                        "type": "integer",
                        "description": "응답에 포함된 결과 수",
                        "format": "int32"
                    },
                    "offset": {
                        "type": "integer",
                        "description": "deprecated",
                        "format": "int32"
                    },
                    "totalResults": {
                        "type": "integer",
                        "description": "발견된 전체 결과 수",
                        "format": "int32"
                    },
                    "fuzzyLevel": {
                        "type": "integer",
                        "description": "deprecated",
                        "format": "int32"
                    },
                    "geoBias": {
                        "$ref": "#/components/schemas/LatLon"
                    },
                    "queryIntent": {
                        "type": "array",
                        "description": "감지된 쿼리 의도 목록",
                        "items": {
                            "$ref": "#/components/schemas/QueryIntent"
                        }
                    }
                },
                "description": "수행된 검색에 대한 요약 정보"
            },
            "TomTomReverseGeocodeDto": {
                "type": "object",
                "properties": {
                    "summary": {
                        "$ref": "#/components/schemas/Summary"
                    },
                    "addresses": {
                        "type": "array",
                        "description": "Reverse Geocode Address 목록",
                        "items": {
                            "$ref": "#/components/schemas/ReverseGeocodeAddress"
                        }
                    }
                }
            },
            "TomTomReverseGeocodeResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "tomTomSearchDto": {
                        "$ref": "#/components/schemas/TomTomReverseGeocodeDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "TomTomSearchCommonRequest": {
                "required": [
                    "ext",
                    "key",
                    "language",
                    "lat",
                    "lon",
                    "view"
                ],
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "유효한 API 키"
                    },
                    "ext": {
                        "type": "string",
                        "description": "유효 응답 형식",
                        "example": "json"
                    },
                    "language": {
                        "type": "string",
                        "description": "검색 결과가 반환될 언어"
                    },
                    "view": {
                        "type": "string",
                        "description": "\n        지정 학적 견해. 분쟁 영토의 처리를 해결하는 데 사용되는 맥락.\n        AR, CN, IL, IN, MA, PK, RU, RS 및 TW와 함께 통합은 각각 아르헨티나, 중국, 이스라엘, 인도, 모로코, 파키스탄, 러시아, 세르비아 및 대만에 맞게 조정됩니다.\n        \n        [Default values]\n        Argentina: AR\n        China: CN\n        India: IN\n        Morocco: MA\n        Pakistan: PK\n        Russia: RU\n        Serbia: RS\n        Taiwan: TW\n        Others: Unified\n    "
                    },
                    "limit": {
                        "maximum": 100,
                        "type": "integer",
                        "description": "반환되는 응답의 최대 수",
                        "format": "int32",
                        "example": 20,
                        "default": 10
                    },
                    "query": {
                        "type": "string",
                        "description": "쿼리 문자열",
                        "example": "hotel"
                    },
                    "typeahead": {
                        "type": "boolean",
                        "description": "자동 완성 플래그가 설정된 경우, 쿼리는 부분 입력으로 해석되어 예측 모드로 전환됩니다.",
                        "example": false,
                        "default": false
                    },
                    "ofs": {
                        "type": "integer",
                        "description": "전체 결과 세트 내에서 반환된 결과의 시작 오프셋",
                        "format": "int32",
                        "default": 10
                    },
                    "geobias": {
                        "type": "string"
                    },
                    "lat": {
                        "type": "number",
                        "description": "WGS84 위도",
                        "format": "float",
                        "example": 25.037727
                    },
                    "lon": {
                        "type": "number",
                        "description": "WGS84 경도",
                        "format": "float",
                        "example": 121.511246
                    },
                    "radius": {
                        "type": "integer",
                        "description": "검색 반경 (미터)",
                        "format": "int32",
                        "default": 10000
                    },
                    "topLeft": {
                        "type": "string",
                        "description": "Bounding Box 좌상단"
                    },
                    "btmRight": {
                        "type": "string",
                        "description": "Bounding Box 우하단"
                    },
                    "extendedPostalCodesFor": {
                        "type": "string",
                        "description": "결과에 확장 우편번호를 포함해야 하는 인덱스"
                    },
                    "minFuzzyLevel": {
                        "maximum": 2,
                        "type": "integer",
                        "description": "사용할 최소 퍼지 레벨",
                        "format": "int32",
                        "default": 1
                    },
                    "maxFuzzyLevel": {
                        "maximum": 2,
                        "type": "integer",
                        "description": "사용할 최대 퍼지 레벨",
                        "format": "int32",
                        "default": 2
                    },
                    "idxSet": {
                        "type": "string",
                        "description": "인덱스 필터",
                        "default": "POI,PAD,Str,Xstr,Geo,Addr"
                    },
                    "categorySet": {
                        "type": "string",
                        "description": "카테고리 필터",
                        "example": "TW"
                    },
                    "brandSet": {
                        "type": "string",
                        "description": "브랜드 필터"
                    },
                    "connectorSet": {
                        "type": "string",
                        "description": "EV 커넥터 필터"
                    },
                    "minPowerKW": {
                        "type": "number",
                        "description": "EV 최소 충전 전력",
                        "format": "double"
                    },
                    "maxPowerKW": {
                        "type": "number",
                        "description": "EV 최대 충전 전력",
                        "format": "double"
                    },
                    "fuelSet": {
                        "type": "string",
                        "description": "연료 타입 필터"
                    },
                    "vehicleTypeSet": {
                        "type": "string",
                        "description": "차량 타입 필터"
                    },
                    "openingHours": {
                        "type": "string",
                        "description": "영업 시간 필터"
                    },
                    "timeZone": {
                        "type": "string",
                        "description": "시간대 정보"
                    },
                    "mapcodes": {
                        "type": "string"
                    },
                    "relatedPois": {
                        "type": "string",
                        "description": "관련 POI 요청"
                    },
                    "entityTypeSet": {
                        "type": "string",
                        "description": "일반 검색용 엔티티 타입 필터"
                    }
                }
            },
            "AddressRanges": {
                "type": "object",
                "properties": {
                    "rangeLeft": {
                        "type": "string"
                    },
                    "rangeRight": {
                        "type": "string"
                    },
                    "from": {
                        "$ref": "#/components/schemas/LatLon"
                    },
                    "to": {
                        "$ref": "#/components/schemas/LatLon"
                    }
                },
                "description": "\n        도로 구간의 주소 범위\n        type == \"Address Range\" 일 때만\n    "
            },
            "Brand": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    }
                },
                "description": "POI 접근에 대한 차량 제약 정보(브랜드 등)"
            },
            "Category": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64"
                    }
                },
                "description": "POI 카테고리 목록"
            },
            "ChargingPark": {
                "type": "object",
                "properties": {
                    "connectors": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Connector"
                        }
                    }
                },
                "description": "\n        충전소 객체 목록\n        전기차 충전소 POI인 경우에만 존재\n    "
            },
            "Classification": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string"
                    },
                    "names": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/NameLocale"
                        }
                    }
                },
                "description": "deprecated"
            },
            "Connector": {
                "type": "object",
                "properties": {
                    "connectorType": {
                        "type": "string"
                    },
                    "ratedPowerKW": {
                        "type": "number",
                        "format": "double"
                    },
                    "currentA": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "currentType": {
                        "type": "string"
                    },
                    "voltageV": {
                        "type": "integer",
                        "format": "int32"
                    }
                }
            },
            "DataSourceInfo": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    }
                }
            },
            "DataSources": {
                "type": "object",
                "properties": {
                    "chargingAvailability": {
                        "$ref": "#/components/schemas/DataSourceInfo"
                    },
                    "parkingAvailability": {
                        "$ref": "#/components/schemas/DataSourceInfo"
                    },
                    "fuelPrice": {
                        "$ref": "#/components/schemas/DataSourceInfo"
                    },
                    "geometry": {
                        "$ref": "#/components/schemas/GeometryInfo"
                    }
                },
                "description": "추가 데이터 서비스에 사용할 참조 ID"
            },
            "EntryPoint": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "functions": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "position": {
                        "$ref": "#/components/schemas/LatLon"
                    }
                },
                "description": "POI/PAD/EPP의 진입점 목록"
            },
            "GeometryInfo": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "sourceName": {
                        "type": "string"
                    }
                }
            },
            "NameLocale": {
                "type": "object",
                "properties": {
                    "nameLocale": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    }
                }
            },
            "OpeningHours": {
                "type": "object",
                "properties": {
                    "mode": {
                        "type": "string"
                    },
                    "timeRanges": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/TimeRange"
                        }
                    }
                }
            },
            "Poi": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "POI 명칭"
                    },
                    "phone": {
                        "type": "string",
                        "description": "전화번호"
                    },
                    "brands": {
                        "type": "array",
                        "description": "POI 브렌드 목록",
                        "items": {
                            "$ref": "#/components/schemas/Brand"
                        }
                    },
                    "categorySet": {
                        "type": "array",
                        "description": "POI 카테고리 목록",
                        "items": {
                            "$ref": "#/components/schemas/Category"
                        }
                    },
                    "url": {
                        "type": "string",
                        "description": "URL"
                    },
                    "categories": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "openingHours": {
                        "$ref": "#/components/schemas/OpeningHours"
                    },
                    "classifications": {
                        "type": "array",
                        "description": "deprecated",
                        "items": {
                            "$ref": "#/components/schemas/Classification"
                        }
                    },
                    "timeZone": {
                        "$ref": "#/components/schemas/TimeZoneInfo"
                    }
                },
                "description": "type == POI 일 때만 존재"
            },
            "RelatedPoi": {
                "type": "object",
                "properties": {
                    "relationType": {
                        "type": "string",
                        "description": "관계 유형: child(자식), parent(부모)"
                    },
                    "id": {
                        "type": "string",
                        "description": "Place by ID 서비스에 entityId로 전달하여 해당 POI의 추가 데이터를 가져올 때 사용하는 식별자"
                    }
                },
                "description": "관련 POI 목록"
            },
            "SearchCommonDto": {
                "type": "object",
                "properties": {
                    "summary": {
                        "$ref": "#/components/schemas/Summary"
                    },
                    "results": {
                        "type": "array",
                        "description": "Score에 따라 내림차순으로 정렬된 결과 목록",
                        "items": {
                            "$ref": "#/components/schemas/SearchResult"
                        }
                    }
                }
            },
            "SearchResult": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "POI|Street|Geography|Point Address|Address Range|Cross Street"
                    },
                    "id": {
                        "type": "string",
                        "description": "POI 인덱스의 안정적인 고유 ID"
                    },
                    "score": {
                        "type": "number",
                        "description": "결과의 점수, 점수가 높을수록 쿼리 기준을 만족할 확률이 높음",
                        "format": "double"
                    },
                    "dist": {
                        "type": "number",
                        "description": "geoBias가 제공된 경우 객체까지의 거리(미터)",
                        "format": "double"
                    },
                    "info": {
                        "type": "string",
                        "description": "deprecated"
                    },
                    "entityType": {
                        "type": "string",
                        "description": "\n       선택적 섹션\n       type == Geography인 경우에만 존재 \n    "
                    },
                    "poi": {
                        "$ref": "#/components/schemas/Poi"
                    },
                    "relatedPois": {
                        "type": "array",
                        "description": "관련 POI 목록",
                        "items": {
                            "$ref": "#/components/schemas/RelatedPoi"
                        }
                    },
                    "address": {
                        "$ref": "#/components/schemas/Address"
                    },
                    "position": {
                        "$ref": "#/components/schemas/LatLon"
                    },
                    "mapcodes": {
                        "type": "array",
                        "description": "맵코드 객체 목록",
                        "items": {
                            "$ref": "#/components/schemas/Mapcode"
                        }
                    },
                    "viewport": {
                        "$ref": "#/components/schemas/Viewport"
                    },
                    "boundingBox": {
                        "$ref": "#/components/schemas/BoundingBox"
                    },
                    "entryPoints": {
                        "type": "array",
                        "description": "POI/PAD/EPP의 진입점 목록",
                        "items": {
                            "$ref": "#/components/schemas/EntryPoint"
                        }
                    },
                    "addressRanges": {
                        "$ref": "#/components/schemas/AddressRanges"
                    },
                    "chargingPark": {
                        "$ref": "#/components/schemas/ChargingPark"
                    },
                    "vehicleConstraint": {
                        "type": "array",
                        "description": "POI 접근에 대한 차량 제약 정보(브랜드 등)",
                        "items": {
                            "$ref": "#/components/schemas/Brand"
                        }
                    },
                    "dataSources": {
                        "$ref": "#/components/schemas/DataSources"
                    },
                    "fuelTypes": {
                        "type": "array",
                        "description": "\n        주유소가 제공하는 연료 유형 목록  \n        주유소 POI인 경우에만 존재\n    ",
                        "items": {
                            "type": "string",
                            "description": "\n        주유소가 제공하는 연료 유형 목록  \n        주유소 POI인 경우에만 존재\n    "
                        }
                    },
                    "vehicleTypes": {
                        "type": "array",
                        "description": "\n        주유소가 지원하는 차량 유형 목록 (Car, Truck)\n        주유소 POI인 경우에만 존재\n    ",
                        "items": {
                            "type": "string",
                            "description": "\n        주유소가 지원하는 차량 유형 목록 (Car, Truck)\n        주유소 POI인 경우에만 존재\n    "
                        }
                    }
                },
                "description": "Score에 따라 내림차순으로 정렬된 결과 목록"
            },
            "TimePoint": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string"
                    },
                    "hour": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "minute": {
                        "type": "integer",
                        "format": "int32"
                    }
                }
            },
            "TimeRange": {
                "type": "object",
                "properties": {
                    "startTime": {
                        "$ref": "#/components/schemas/TimePoint"
                    },
                    "endTime": {
                        "$ref": "#/components/schemas/TimePoint"
                    }
                }
            },
            "TimeZoneInfo": {
                "type": "object",
                "properties": {
                    "ianaId": {
                        "type": "string",
                        "description": "\n       IANA 표준 시간대 데이터베이스의 ID\n       https://www.iana.org/time-zones \n    "
                    }
                },
                "description": "POI의 시간대 정보"
            },
            "TomTomSearchResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "tomTomSearchDto": {
                        "$ref": "#/components/schemas/SearchCommonDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "Viewport": {
                "type": "object",
                "properties": {
                    "topLeftPoint": {
                        "$ref": "#/components/schemas/LatLon"
                    },
                    "btmRightPoint": {
                        "$ref": "#/components/schemas/LatLon"
                    }
                },
                "description": "지도에 결과를 표시하는 데 사용할 수 있는 뷰포트"
            },
            "TomTomSafetyCameraRequest": {
                "required": [
                    "key"
                ],
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "유효한 API 키"
                    }
                }
            },
            "Coordinates": {
                "required": [
                    "bearing",
                    "latitude",
                    "longitude"
                ],
                "type": "object",
                "properties": {
                    "latitude": {
                        "type": "number",
                        "description": "WGS84 위도",
                        "format": "double",
                        "example": 25.037727
                    },
                    "longitude": {
                        "type": "number",
                        "description": "WGS84 경도",
                        "format": "double",
                        "example": 121.511246
                    },
                    "bearing": {
                        "type": "integer",
                        "description": "\n       카메라가 확인하고 있는 차량의 방향(도 단위, 0은 북쪽, 90은 동쪽 등)\n       방위는 카메라의 깜빡이는 방향이 아닌 대상 차량의 주행 방향을 표시\n    ",
                        "format": "int32"
                    }
                }
            },
            "CoordinatesRepresentation": {
                "required": [
                    "coordinates"
                ],
                "type": "object",
                "properties": {
                    "coordinates": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Coordinates"
                        }
                    }
                }
            },
            "Reliability": {
                "required": [
                    "lastObservation",
                    "numberOfObservations",
                    "score"
                ],
                "type": "object",
                "properties": {
                    "lastObservation": {
                        "type": "string"
                    },
                    "numberOfObservations": {
                        "type": "integer",
                        "format": "int32"
                    },
                    "score": {
                        "type": "number",
                        "format": "double"
                    }
                }
            },
            "Spot": {
                "required": [
                    "countryCode",
                    "expiryDate",
                    "id",
                    "lastUpdate",
                    "spotLocation",
                    "spotType"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "lastUpdate": {
                        "type": "string"
                    },
                    "expiryDate": {
                        "type": "string"
                    },
                    "speedLimit": {
                        "type": "integer",
                        "description": "허용되는 최대 속도(km/h)",
                        "format": "int32"
                    },
                    "countryCode": {
                        "type": "string",
                        "description": "해당 지점 또는 구역이 위치한 국가의 ISO 3166-1 alpha-3 코드"
                    },
                    "reliability": {
                        "$ref": "#/components/schemas/Reliability"
                    },
                    "spotLocation": {
                        "$ref": "#/components/schemas/SpotLocation"
                    },
                    "spotType": {
                        "type": "string",
                        "description": "Spot 유형",
                        "example": "FIXED_SPEED_CAM|RED_LIGHT_CAM|RED_LIGHT_SPEED_CAM|RESTRICTION_CAM"
                    }
                }
            },
            "SpotLocation": {
                "required": [
                    "coordinates",
                    "openLR"
                ],
                "type": "object",
                "properties": {
                    "coordinates": {
                        "$ref": "#/components/schemas/Coordinates"
                    },
                    "openLR": {
                        "type": "string",
                        "description": "해당 Spot 또는 Zone 위치의 이진 OpenLR 표현"
                    }
                }
            },
            "Spots": {
                "required": [
                    "spot"
                ],
                "type": "object",
                "properties": {
                    "spot": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Spot"
                        }
                    }
                },
                "description": "Spot Type 속도 카메라 목록"
            },
            "TomTomSafetyCameraDto": {
                "required": [
                    "creationDate"
                ],
                "type": "object",
                "properties": {
                    "schemaVersion": {
                        "type": "string"
                    },
                    "creationDate": {
                        "type": "string",
                        "description": "이 속도캠 세트의 타임스탬프(UTC 시간대)"
                    },
                    "spots": {
                        "$ref": "#/components/schemas/Spots"
                    },
                    "zones": {
                        "$ref": "#/components/schemas/Zones"
                    }
                }
            },
            "TomTomSafetyCameraResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "tomSafetyCameraDto": {
                        "$ref": "#/components/schemas/TomTomSafetyCameraDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "Zone": {
                "required": [
                    "countryCode",
                    "expiryDate",
                    "id",
                    "lastUpdate",
                    "zoneLength",
                    "zoneLocation",
                    "zoneType"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64"
                    },
                    "lastUpdate": {
                        "type": "string"
                    },
                    "expiryDate": {
                        "type": "string"
                    },
                    "speedLimit": {
                        "type": "integer",
                        "description": "허용되는 최대 속도(km/h)",
                        "format": "int32"
                    },
                    "countryCode": {
                        "type": "string",
                        "description": "해당 지점 또는 구역이 위치한 국가의 ISO 3166-1 alpha-3 코드"
                    },
                    "zoneLocation": {
                        "$ref": "#/components/schemas/ZoneLocation"
                    },
                    "zoneLength": {
                        "type": "integer",
                        "description": "구역의 길이(미터)",
                        "format": "int32"
                    },
                    "zoneType": {
                        "type": "string",
                        "description": "Zone 유형",
                        "example": "AVERAGE_SPEED_ZONE|SPEED_ENFORCEMENT_ZONE|DANGER_ZONE|LIKELY_MOBILE_ZONE|ACCIDENT_BLACKSPOT_ZONE"
                    }
                }
            },
            "ZoneBoundingBox": {
                "required": [
                    "maxLatitude",
                    "maxLongitude",
                    "minLatitude",
                    "minLongitude"
                ],
                "type": "object",
                "properties": {
                    "minLatitude": {
                        "type": "number",
                        "format": "double"
                    },
                    "minLongitude": {
                        "type": "number",
                        "format": "double"
                    },
                    "maxLatitude": {
                        "type": "number",
                        "format": "double"
                    },
                    "maxLongitude": {
                        "type": "number",
                        "format": "double"
                    }
                },
                "description": "영역 주변의 가장 작은 사각형의 좌표, 이는 공간 검색에 사용될 수 있음"
            },
            "ZoneLocation": {
                "required": [
                    "boundingBox",
                    "coordinatesRepresentation",
                    "openLR"
                ],
                "type": "object",
                "properties": {
                    "boundingBox": {
                        "$ref": "#/components/schemas/ZoneBoundingBox"
                    },
                    "openLR": {
                        "type": "string",
                        "description": "해당 Spot 또는 Zone 위치의 이진 OpenLR 표현"
                    },
                    "coordinatesRepresentation": {
                        "$ref": "#/components/schemas/CoordinatesRepresentation"
                    }
                }
            },
            "Zones": {
                "required": [
                    "zone"
                ],
                "type": "object",
                "properties": {
                    "zone": {
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/Zone"
                        }
                    }
                },
                "description": "Zone Type 속도 카메라 목록"
            },
            "ServiceGateRequest": {
                "type": "object",
                "properties": {
                    "reg_id": {
                        "type": "string",
                        "description": "push id (Android) or device token (iOS)"
                    },
                    "app_ver": {
                        "type": "string",
                        "description": "App Version",
                        "example": "1.0.0"
                    },
                    "smr_ver": {
                        "type": "string",
                        "description": "SMR Version (Map Version)",
                        "example": "21.10a"
                    },
                    "smdc_ver": {
                        "type": "string",
                        "description": "SMDC Version"
                    },
                    "gp_ver": {
                        "type": "string",
                        "description": "안전운행 Version",
                        "example": "21.09(T29)"
                    },
                    "clause_ver": {
                        "type": "string",
                        "description": "약관 Version",
                        "example": "210226"
                    },
                    "channel": {
                        "type": "string",
                        "description": "유입 경로 NOR:정상실행",
                        "example": "NOR"
                    },
                    "opt": {
                        "type": "string",
                        "description": "opt",
                        "example": "ON"
                    }
                }
            },
            "MapInfoDto": {
                "type": "object",
                "properties": {
                    "mapVer": {
                        "type": "string",
                        "description": "맵 버전",
                        "example": "1_0_0_1"
                    },
                    "mapUrl": {
                        "type": "string",
                        "description": "지도 데이터 CDN URL",
                        "example": "https://inavi.com/orbis_stream_data/KR/1_0_0_1/OrbisRouteData.zip"
                    },
                    "country": {
                        "type": "string",
                        "description": "국가 코드",
                        "example": "KR"
                    }
                },
                "description": "지도 버전 정보"
            },
            "ServiceGateDto": {
                "required": [
                    "searchType"
                ],
                "type": "object",
                "properties": {
                    "mapInfo": {
                        "$ref": "#/components/schemas/MapInfoDto"
                    },
                    "searchType": {
                        "type": "integer",
                        "description": "\n       TomTom 검색 타입\n       0: Genesis 검색 타입 사용\n       1: Orbis 검색 타입 사용\n    ",
                        "format": "int32",
                        "enum": [
                            0,
                            1
                        ]
                    }
                }
            },
            "ServiceGateResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "serviceGateDto": {
                        "$ref": "#/components/schemas/ServiceGateDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "SearchRouteRequest": {
                "required": [
                    "endX",
                    "endY",
                    "startX",
                    "startY",
                    "traffic"
                ],
                "type": "object",
                "properties": {
                    "startX": {
                        "type": "number",
                        "description": "출발지 X 좌표(WGS84)",
                        "format": "double",
                        "example": 127.1536160755102
                    },
                    "startY": {
                        "type": "number",
                        "description": "출발지 Y 좌표(WGS84)",
                        "format": "double",
                        "example": 37.12754480671075
                    },
                    "endX": {
                        "type": "number",
                        "description": "목적지 X 좌표(WGS84)",
                        "format": "double",
                        "example": 127.1102523803711
                    },
                    "endY": {
                        "type": "number",
                        "description": "목적지 Y 좌표(WGS84)",
                        "format": "double",
                        "example": 37.40242004394531
                    },
                    "viaList": {
                        "type": "array",
                        "description": "경유지 좌표(WGS84)",
                        "example": [
                            [
                                127.153409,
                                37.135123
                            ],
                            [
                                127.15005,
                                37.138312
                            ]
                        ],
                        "items": {
                            "type": "array",
                            "description": "경유지 좌표(WGS84)",
                            "example": [
                                [
                                    127.153409,
                                    37.135123
                                ],
                                [
                                    127.15005,
                                    37.138312
                                ]
                            ],
                            "items": {
                                "type": "number",
                                "description": "경유지 좌표(WGS84)",
                                "format": "double"
                            }
                        }
                    },
                    "option": {
                        "type": "integer",
                        "description": "\n        경로 탐색 옵션\n        1 : 최적 경로(Default)(현재 최적 경로만 지원)\n    ",
                        "format": "int32",
                        "example": 1
                    },
                    "traffic": {
                        "type": "integer",
                        "description": "\n        교통정보 적용 탐색 옵션  \n        0 : 교통정보 미 적용(Default)  \n        1 : 교통정보 적용\n    ",
                        "format": "int32",
                        "example": 0
                    },
                    "directionangle": {
                        "type": "integer",
                        "description": "\n        출발지 방향성 탐색 옵션  \n        -1 : 출발지 방향성 미 적용(Default)  \n        0 ~ 360 : 정북 기준 차량 진행 방향 각도 (시계 방향, 동쪽 90)\n        sideroadstart 옵션과 동시 적용 불가\n    ",
                        "format": "int32",
                        "example": -1
                    },
                    "sideroadstart": {
                        "type": "integer",
                        "description": "\n        출발지 좌표 기준 도로 방향성 탐색 옵션\n        0 : 도로 방향성 옵션 미 적용(Default)\n        1 : 도로 방향성 옵션 적용\n        directionangle 옵션과 동시 적용 불가\n    ",
                        "format": "int32"
                    },
                    "sideroadend": {
                        "type": "integer",
                        "description": "\n        목적지 좌표 기준 도로 방향성 탐색 옵션\n        0 : 도로 방향성 옵션 미 적용(Default)\n        1 : 도로 방향성 옵션 적용\n    ",
                        "format": "int32"
                    },
                    "weight": {
                        "type": "number",
                        "description": "\n        차량 제원 옵션\n        차량의 총 중량 (화물 포함)\n        단위 : Ton (톤)\n        옵션 입력 여부에 따라 통행 불가 도로 회피 탐색\n    ",
                        "format": "double"
                    },
                    "height": {
                        "type": "number",
                        "description": "\n        차량 제원 옵션\n        차량의 최대 높이\n        단위 : Meter (미터)\n        옵션 입력 여부에 따라 통행 불가 도로 회피 탐색\n    ",
                        "format": "double"
                    },
                    "length": {
                        "type": "number",
                        "description": "\n        차량 제원 옵션\n        차량 전체 길이 (전장)\n        단위 : Meter (미터)\n        옵션 입력 여부에 따라 통행 불가 도로 회피 탐색\n    ",
                        "format": "double"
                    }
                }
            },
            "CoordinateDto": {
                "required": [
                    "x",
                    "y"
                ],
                "type": "object",
                "properties": {
                    "x": {
                        "type": "number",
                        "description": "X 좌표(WGS84)",
                        "format": "double",
                        "example": 121.563667
                    },
                    "y": {
                        "type": "number",
                        "description": "Y 좌표(WGS84)",
                        "format": "double",
                        "example": 25.061677
                    }
                },
                "description": "좌표 정보(WGS84)",
                "example": {
                    "x": 121.111111,
                    "y": 25.222222
                }
            },
            "LinksDto": {
                "required": [
                    "direction",
                    "distance",
                    "highway",
                    "id",
                    "id_index",
                    "maneuver",
                    "name_id",
                    "node_id",
                    "speed",
                    "time",
                    "vertex_offset"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "링크 ID - 원본 LINK 데이터의 ID",
                        "example": "3230761691"
                    },
                    "id_index": {
                        "type": "string",
                        "description": "링크 ID Index - 네트워크 변환기를 통해 변환된 Link 데이터의 ID Index",
                        "example": "675061484748975"
                    },
                    "osm_id": {
                        "type": "string",
                        "description": "링크 OSM ID (OpenStreetMap ID)",
                        "example": "189494283"
                    },
                    "highway": {
                        "type": "integer",
                        "description": "\n        링크 도로 종별 코드  \n        0 : Motorway (고속도로)\n        1 : Motorway Link (고속도로 연결 링크)\n        2 : Trunk Road (간선도로)\n        3 : Trunk Link (간선도로 연결 링크)\n        4 : Primary Road (주요도로)\n        5 : Primary Link (주요도로 연결 링크)\n        6 : Secondary Road (2차[보조]도로)\n        7 : Secondary Link (2차[보조]도로 연결 링크)\n        8 : Tertiary Road (3차[일반]도로)\n        9 : Tertiary Link (3차[일반]도로 연결 링크)\n        10 : Residential Road (주거용 도로)\n        11 : Living Street (생활도로)\n        12 : Unclassified Road (미분류 도로)\n        13 : Unknown Road (알 수 없는 도로)\n        14 : Service Road (시설 연결 도로)\n        15 : Track Road (농로·임로)\n    ",
                        "format": "int32",
                        "example": 14
                    },
                    "speed": {
                        "type": "integer",
                        "description": "속도(Km/h). 실시간 데이터 없으면 통계 속도, 없으면 0",
                        "format": "int32",
                        "example": 0
                    },
                    "distance": {
                        "type": "number",
                        "description": "남은 거리(m) - 목적지까지 남은 거리",
                        "format": "double",
                        "example": 3360.54
                    },
                    "time": {
                        "type": "integer",
                        "description": "남은 시간(초) - 목적지까지 남은 시간",
                        "format": "int32",
                        "example": 565
                    },
                    "node_id": {
                        "type": "string",
                        "description": "노드 ID - 원본 Node 데이터의 ID",
                        "example": "3914315761"
                    },
                    "vertex_offset": {
                        "type": "integer",
                        "description": "Vertex 시작 Index (전체 좌표 리스트 중)",
                        "format": "int32",
                        "example": 0
                    },
                    "maneuver": {
                        "type": "integer",
                        "description": "\n        TBT(Turn-by-Turn) 유형 - 현재 링크와 다음 링크 간 방향 전환\n        0 : STRAIGHT\n        1 : SLIGHT RIGHT\n        2 : SLIGHT LEFT\n        3 : TURN RIGHT\n        4 : TURN LEFT\n        5 : SHARP RIGHT\n        6 : SHARP LEFT\n        7 : U-TURN\n        11 : ROUNDABOUT_EXIT_CLOCK_1\n        12 : ROUNDABOUT_EXIT_CLOCK_2\n        13 : ROUNDABOUT_EXIT_CLOCK_3\n        14 : ROUNDABOUT_EXIT_CLOCK_4\n        15 : ROUNDABOUT_EXIT_CLOCK_5\n        16 : ROUNDABOUT_EXIT_CLOCK_6\n        17 : ROUNDABOUT_EXIT_CLOCK_7\n        18 : ROUNDABOUT_EXIT_CLOCK_8\n        19 : ROUNDABOUT_EXIT_CLOCK_9\n        20 : ROUNDABOUT_EXIT_CLOCK_10\n        21 : ROUNDABOUT_EXIT_CLOCK_11\n        22 : ROUNDABOUT_EXIT_CLOCK_12\n        -1 : UNSPECIFIED\n    ",
                        "format": "int32",
                        "example": 0
                    },
                    "name_id": {
                        "type": "integer",
                        "description": "링크 도로명 ID (연결된 도로명 없으면 0)",
                        "format": "int32",
                        "example": 93709
                    },
                    "direction": {
                        "type": "integer",
                        "description": "\n        링크 진행 방향\n        0: 정방향\n        1: 역방향\n    \"",
                        "format": "int32",
                        "example": 0
                    }
                },
                "description": "링크 정보"
            },
            "RoutesDto": {
                "required": [
                    "distance",
                    "fuel_consumption",
                    "spend_time"
                ],
                "type": "object",
                "properties": {
                    "distance": {
                        "type": "number",
                        "description": "전체 거리(m)",
                        "format": "double",
                        "example": 3360.54
                    },
                    "spend_time": {
                        "type": "integer",
                        "description": "소요 시간(초)",
                        "format": "int32",
                        "example": 565
                    },
                    "fuel_consumption": {
                        "type": "number",
                        "description": "연료 소모량(L)",
                        "format": "double",
                        "example": 0.42
                    }
                },
                "description": "경로 정보"
            },
            "SearchRouteDto": {
                "type": "object",
                "properties": {
                    "resultCode": {
                        "type": "integer",
                        "description": "탐색 엔진 결과 코드",
                        "format": "int32"
                    },
                    "user_info": {
                        "$ref": "#/components/schemas/UserInfoDto"
                    },
                    "routes": {
                        "$ref": "#/components/schemas/RoutesDto"
                    },
                    "links": {
                        "type": "array",
                        "description": "링크 정보",
                        "items": {
                            "$ref": "#/components/schemas/LinksDto"
                        }
                    },
                    "type": {
                        "type": "string",
                        "description": "LineString"
                    },
                    "coordinates": {
                        "type": "array",
                        "description": "경로 탐색 결과 Vertex X 좌표(WGS84), Vertex Y 좌표(WGS84)",
                        "example": [
                            [
                                121.123456,
                                25.123456
                            ],
                            [
                                121.123456,
                                25.123456
                            ]
                        ],
                        "items": {
                            "type": "array",
                            "description": "경로 탐색 결과 Vertex X 좌표(WGS84), Vertex Y 좌표(WGS84)",
                            "example": [
                                [
                                    121.123456,
                                    25.123456
                                ],
                                [
                                    121.123456,
                                    25.123456
                                ]
                            ],
                            "items": {
                                "type": "number",
                                "description": "경로 탐색 결과 Vertex X 좌표(WGS84), Vertex Y 좌표(WGS84)",
                                "format": "double"
                            }
                        }
                    }
                }
            },
            "SearchRouteResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "searchRouteDto": {
                        "$ref": "#/components/schemas/SearchRouteDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "UserInfoDto": {
                "required": [
                    "end",
                    "start"
                ],
                "type": "object",
                "properties": {
                    "start": {
                        "$ref": "#/components/schemas/CoordinateDto"
                    },
                    "end": {
                        "$ref": "#/components/schemas/CoordinateDto"
                    },
                    "viaList": {
                        "type": "array",
                        "description": "경유지 좌표(WGS84)",
                        "example": [
                            [
                                121.555555,
                                25.666666
                            ],
                            [
                                121.777777,
                                25.888888
                            ]
                        ],
                        "items": {
                            "type": "array",
                            "description": "경유지 좌표(WGS84)",
                            "example": [
                                [
                                    121.555555,
                                    25.666666
                                ],
                                [
                                    121.777777,
                                    25.888888
                                ]
                            ],
                            "items": {
                                "type": "number",
                                "description": "경유지 좌표(WGS84)",
                                "format": "double"
                            }
                        }
                    },
                    "option": {
                        "type": "integer",
                        "description": "경로 탐색 옵션 - 경로 요청 시 전달한 경로 탐색 옵션 (사용 안함 : 1 고정)",
                        "format": "int32"
                    },
                    "traffic": {
                        "type": "integer",
                        "description": "교통정보 적용 탐색 옵션 - 경로 요청 시 전달한 교통정보 옵션",
                        "format": "int32"
                    },
                    "directionangle": {
                        "type": "integer",
                        "description": "출발지 방향성 탐색 옵션 - 경로 요청 시 전달한 출발지 방향 각도 값",
                        "format": "int32"
                    },
                    "sideroadstart": {
                        "type": "integer",
                        "description": "출발지 좌표 기준 도로 방향성 탐색 옵션 - 경로 요청 시 전달한 옵션 값",
                        "format": "int32"
                    },
                    "sideroadend": {
                        "type": "integer",
                        "description": "목적지 좌표 기준 도로 방향성 탐색 옵션 - 경로 요청 시 전달한 옵션 값",
                        "format": "int32"
                    },
                    "routecount": {
                        "type": "integer",
                        "description": "경로 탐색 요청 개수 - 경로 요청 시 전달한 경로 개수 옵션",
                        "format": "int32"
                    },
                    "weight": {
                        "type": "number",
                        "description": "차량 총 중량 옵션 - 경로 요청 시 전달한 옵션 값",
                        "format": "double"
                    },
                    "height": {
                        "type": "number",
                        "description": "차량 최대 높이 옵션 - 경로 요청 시 전달한 옵션 값",
                        "format": "double"
                    },
                    "length": {
                        "type": "number",
                        "description": "차량 전체 길이 옵션 - 경로 요청 시 전달한 옵션 값",
                        "format": "double"
                    }
                },
                "description": "사용자 경로 탐색 요청 정보"
            },
            "SearchRouteMultiRequest": {
                "required": [
                    "endX",
                    "endY",
                    "startX",
                    "startY"
                ],
                "type": "object",
                "properties": {
                    "startX": {
                        "type": "number",
                        "description": "출발지 X 좌표(WGS84)",
                        "format": "double",
                        "example": 127.1536160755102
                    },
                    "startY": {
                        "type": "number",
                        "description": "출발지 Y 좌표(WGS84)",
                        "format": "double",
                        "example": 37.12754480671075
                    },
                    "endX": {
                        "type": "number",
                        "description": "목적지 X 좌표(WGS84)",
                        "format": "double",
                        "example": 127.1102523803711
                    },
                    "endY": {
                        "type": "number",
                        "description": "목적지 Y 좌표(WGS84)",
                        "format": "double",
                        "example": 37.40242004394531
                    },
                    "viaList": {
                        "type": "array",
                        "description": "경유지 좌표(WGS84)",
                        "example": [
                            [
                                127.153409,
                                37.135123
                            ],
                            [
                                127.15005,
                                37.138312
                            ]
                        ],
                        "items": {
                            "type": "array",
                            "description": "경유지 좌표(WGS84)",
                            "example": [
                                [
                                    127.153409,
                                    37.135123
                                ],
                                [
                                    127.15005,
                                    37.138312
                                ]
                            ],
                            "items": {
                                "type": "number",
                                "description": "경유지 좌표(WGS84)",
                                "format": "double"
                            }
                        }
                    },
                    "traffic": {
                        "type": "integer",
                        "description": "\n        교통정보 적용 탐색 옵션  \n        0 : 교통정보 미 적용(Default)  \n        1 : 교통정보 적용\n    ",
                        "format": "int32",
                        "example": 0
                    },
                    "directionangle": {
                        "maximum": 360,
                        "minimum": -1,
                        "type": "integer",
                        "description": "\n        출발지 방향성 탐색 옵션  \n        -1 : 출발지 방향성 미 적용(Default)  \n        0 ~ 360 : 정북 기준 차량 진행 방향 각도 (시계 방향, 동쪽 90)\n        sideroadstart 옵션과 동시 적용 불가\n    ",
                        "format": "int32",
                        "default": -1
                    },
                    "sideroadstart": {
                        "type": "integer",
                        "description": "\n        출발지 좌표 기준 도로 방향성 탐색 옵션\n        0 : 도로 방향성 옵션 미 적용(Default)\n        1 : 도로 방향성 옵션 적용\n        directionangle 옵션과 동시 적용 불가\n    ",
                        "format": "int32"
                    },
                    "sideroadend": {
                        "type": "integer",
                        "description": "\n        목적지 좌표 기준 도로 방향성 탐색 옵션\n        0 : 도로 방향성 옵션 미 적용(Default)\n        1 : 도로 방향성 옵션 적용\n    ",
                        "format": "int32"
                    },
                    "routecount": {
                        "type": "integer",
                        "description": "경로 결과 요청 개수",
                        "format": "int32",
                        "default": 1,
                        "enum": [
                            1,
                            2,
                            3
                        ]
                    },
                    "weight": {
                        "type": "number",
                        "description": "\n        차량 제원 옵션\n        차량의 총 중량 (화물 포함)\n        단위 : Ton (톤)\n        옵션 입력 여부에 따라 통행 불가 도로 회피 탐색\n    ",
                        "format": "double"
                    },
                    "height": {
                        "type": "number",
                        "description": "\n        차량 제원 옵션\n        차량의 최대 높이\n        단위 : Meter (미터)\n        옵션 입력 여부에 따라 통행 불가 도로 회피 탐색\n    ",
                        "format": "double"
                    },
                    "length": {
                        "type": "number",
                        "description": "\n        차량 제원 옵션\n        차량 전체 길이 (전장)\n        단위 : Meter (미터)\n        옵션 입력 여부에 따라 통행 불가 도로 회피 탐색\n    ",
                        "format": "double"
                    }
                }
            },
            "FeaturesDto": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "geometry": {
                        "$ref": "#/components/schemas/GeometryDto"
                    },
                    "properties": {
                        "$ref": "#/components/schemas/PropertiesDto"
                    }
                },
                "description": "각 경로 탐색 결과, GeoJSON Feature 형식"
            },
            "GeometryDto": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "LineString"
                    },
                    "coordinates": {
                        "type": "array",
                        "description": "경로 탐색 결과 Vertex X 좌표(WGS84), Vertex Y 좌표(WGS84)",
                        "example": [
                            [
                                121.123456,
                                25.123456
                            ],
                            [
                                121.123456,
                                25.123456
                            ]
                        ],
                        "items": {
                            "type": "array",
                            "description": "경로 탐색 결과 Vertex X 좌표(WGS84), Vertex Y 좌표(WGS84)",
                            "example": [
                                [
                                    121.123456,
                                    25.123456
                                ],
                                [
                                    121.123456,
                                    25.123456
                                ]
                            ],
                            "items": {
                                "type": "number",
                                "description": "경로 탐색 결과 Vertex X 좌표(WGS84), Vertex Y 좌표(WGS84)",
                                "format": "double"
                            }
                        }
                    }
                }
            },
            "PropertiesDto": {
                "type": "object",
                "properties": {
                    "routes": {
                        "$ref": "#/components/schemas/RoutesDto"
                    },
                    "links": {
                        "type": "array",
                        "description": "링크 정보",
                        "items": {
                            "$ref": "#/components/schemas/LinksDto"
                        }
                    }
                }
            },
            "SearchRouteMultiDto": {
                "required": [
                    "resultCount"
                ],
                "type": "object",
                "properties": {
                    "resultCode": {
                        "type": "integer",
                        "description": "탐색 엔진 결과 코드",
                        "format": "int32"
                    },
                    "resultCount": {
                        "type": "integer",
                        "description": "경로 탐색 결과 개수",
                        "format": "int32"
                    },
                    "user_info": {
                        "$ref": "#/components/schemas/UserInfoDto"
                    },
                    "type": {
                        "type": "string",
                        "description": "LineString"
                    },
                    "features": {
                        "type": "array",
                        "description": "각 경로 탐색 결과, GeoJSON Feature 형식",
                        "items": {
                            "$ref": "#/components/schemas/FeaturesDto"
                        }
                    }
                }
            },
            "SearchRouteMultiResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "searchRouteMultiDto": {
                        "$ref": "#/components/schemas/SearchRouteMultiDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "AuthRequest": {
                "required": [
                    "appKey",
                    "pkgName",
                    "uniqueKey"
                ],
                "type": "object",
                "properties": {
                    "appKey": {
                        "type": "string",
                        "description": "고유 인증 key"
                    },
                    "pkgName": {
                        "type": "string",
                        "description": "패키지 명"
                    },
                    "uniqueKey": {
                        "type": "string",
                        "description": "고유키"
                    }
                }
            },
            "AuthDto": {
                "required": [
                    "accessToken"
                ],
                "type": "object",
                "properties": {
                    "imaps": {
                        "$ref": "#/components/schemas/ImapsResult"
                    },
                    "accessToken": {
                        "type": "string",
                        "description": "인증 토큰 정보"
                    }
                }
            },
            "AuthResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "authDto": {
                        "$ref": "#/components/schemas/AuthDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "ImapsResult": {
                "type": "object",
                "properties": {
                    "result": {
                        "type": "string",
                        "description": "light style json url"
                    },
                    "resultDark": {
                        "type": "string",
                        "description": "dark style json url"
                    }
                },
                "description": "Style JSON URL"
            },
            "TomTomKeyDto": {
                "required": [
                    "firstApiKey",
                    "searchApiKey",
                    "speedCameraApiKey"
                ],
                "type": "object",
                "properties": {
                    "searchApiKey": {
                        "type": "string",
                        "description": "TomTom Orbis 검색 API Key"
                    },
                    "genesisKey": {
                        "type": "string",
                        "description": "TomTom Genesis 검색 API key"
                    },
                    "firstApiKey": {
                        "type": "string",
                        "description": "TomTom first API Key"
                    },
                    "speedCameraApiKey": {
                        "type": "string",
                        "description": "speed camera API Key",
                        "example": "KR"
                    }
                }
            },
            "TomTomKeyResponse": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "tomKeyDto": {
                        "$ref": "#/components/schemas/TomTomKeyDto"
                    },
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            },
            "Response": {
                "required": [
                    "result"
                ],
                "type": "object",
                "properties": {
                    "result": {
                        "$ref": "#/components/schemas/Result"
                    }
                }
            }
        },
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    }
}