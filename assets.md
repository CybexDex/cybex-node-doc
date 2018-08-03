# assets


### 1. get\_assets

`Return the detail of assets corresponding to the provided IDs`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_assets","params":[["1.3.0"]],"id":1}' https://apihk.cybex.io

* Parameters:

		asset_ids: IDs of the assets to retrieve

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.3.0",
				"symbol": "CYB",
				"precision": 5,
				"issuer": "1.2.3",
				"options": {
					"max_supply": "100000000000000",
					"market_fee_percent": 0,
					"max_market_fee": "1000000000000000",
					"issuer_permissions": 0,
					"flags": 0,
					"core_exchange_rate": {
						"base": {
							"amount": 1,
							"asset_id": "1.3.0"
						},
						"quote": {
							"amount": 1,
							"asset_id": "1.3.0"
						}
					},
					"whitelist_authorities": [],
					"blacklist_authorities": [],
					"whitelist_markets": [],
					"blacklist_markets": [],
					"description": "",
					"extensions": []
				},
				"dynamic_asset_data_id": "2.3.0"
			}]
		}



### 2. list\_assets

`Return the assets found`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"list_assets","params":["CYB", 3],"id":1}' https://apihk.cybex.io

* Parameters:

		lower_bound_symbol: Lower bound of symbol names to retrieve
		limit: Maximum number of assets to fetch (must not exceed 100)

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.3.0",             
				"symbol": "CYB",           
				"precision": 5,
				"issuer": "1.2.3",
				"options": {
					"max_supply": "100000000000000",
					"market_fee_percent": 0,
					"max_market_fee": "1000000000000000",
					"issuer_permissions": 0,
					"flags": 0,
					"core_exchange_rate": {
						"base": {
							"amount": 1,
							"asset_id": "1.3.0"
						},
						"quote": {
							"amount": 1,
							"asset_id": "1.3.0"
						}
					},
					"whitelist_authorities": [],
					"blacklist_authorities": [],
					"whitelist_markets": [],
					"blacklist_markets": [],
					"description": "",
					"extensions": []
				},
				"dynamic_asset_data_id": "2.3.0"
			}, {
				"id": "1.3.503",
				"symbol": "CYBEX",
				"precision": 6,
				"issuer": "1.2.29",
				"options": {
					"max_supply": "100000000000",
					"market_fee_percent": 0,
					"max_market_fee": 0,
					"issuer_permissions": 79,
					"flags": 0,
					"core_exchange_rate": {
						"base": {
							"amount": 100000,
							"asset_id": "1.3.0"
						},
						"quote": {
							"amount": 1000000,
							"asset_id": "1.3.503"
						}
					},
					"whitelist_authorities": [],
					"blacklist_authorities": [],
					"whitelist_markets": [],
					"blacklist_markets": [],
					"description": "{\"main\":\"It's CYBEX!\",\"market\":\"\"}",
					"extensions": []
				},
				"dynamic_asset_data_id": "2.3.503"
			}, {
				"id": "1.3.1",
				"symbol": "JADE",
				"precision": 6,
				"issuer": "1.2.29",
				"options": {
					"max_supply": "1000000000000000",
					"market_fee_percent": 0,
					"max_market_fee": 0,
					"issuer_permissions": 79,
					"flags": 0,
					"core_exchange_rate": {
						"base": {
							"amount": 200000000,
							"asset_id": "1.3.0"
						},
						"quote": {
							"amount": 1000000,
							"asset_id": "1.3.1"
						}
					},
					"whitelist_authorities": [],
					"blacklist_authorities": [],
					"whitelist_markets": [],
					"blacklist_markets": [],
					"description": "{\"main\":\"It's gateway name.\",\"market\":\"\"}",
					"extensions": []
				},
				"dynamic_asset_data_id": "2.3.1"
			}]
		}


### 3. lookup\_asset\_symbols

`The assets corresponding to the provided symbols or IDs`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"lookup_asset_symbols","params":[["CYB", "JADE.ETH"]],"id":1}' https://apihk.cybex.io

* Parameters:

		asset_symbols: Symbols or stringified IDs of the assets to retrieve

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.3.0",
				"symbol": "CYB",
				"precision": 5,
				"issuer": "1.2.3",
				"options": {
					"max_supply": "100000000000000",
					"market_fee_percent": 0,
					"max_market_fee": "1000000000000000",
					"issuer_permissions": 0,
					"flags": 0,
					"core_exchange_rate": {
						"base": {
							"amount": 1,
							"asset_id": "1.3.0"
						},
						"quote": {
							"amount": 1,
							"asset_id": "1.3.0"
						}
					},
					"whitelist_authorities": [],
					"blacklist_authorities": [],
					"whitelist_markets": [],
					"blacklist_markets": [],
					"description": "",
					"extensions": []
				},
				"dynamic_asset_data_id": "2.3.0"
			}, {
				"id": "1.3.2",
				"symbol": "JADE.ETH",
				"precision": 6,
				"issuer": "1.2.29",
				"options": {
					"max_supply": "1000000000000000",
					"market_fee_percent": 0,
					"max_market_fee": 0,
					"issuer_permissions": 79,
					"flags": 0,
					"core_exchange_rate": {
						"base": {
							"amount": 100000000,
							"asset_id": "1.3.0"
						},
						"quote": {
							"amount": 1000000,
							"asset_id": "1.3.2"
						}
					},
					"whitelist_authorities": [],
					"blacklist_authorities": [],
					"whitelist_markets": [],
					"blacklist_markets": [],
					"description": "{\"main\":\"It's an ETH IOU of Jade gateway.\",\"market\":\"\"}",
					"extensions": []
				},
				"dynamic_asset_data_id": "2.3.2"
			}]
		}



