# operations by websocket 


### start websocket

##### login
	{"id": 1, "method": "call", "params": [1, "login", ["",""]]}
	
	{"id":1,"jsonrpc":"2.0","result":true}

##### register
	{"id": 2, "method": "call", "params": [1, "history", []]}
	
	{"id":2,"jsonrpc":"2.0","result":2}

`register the operation for api id`


### 1. get\_account_history

`A list of operations performed by account, ordered from most recent to oldest`

* Request:

		{"id": 3, "method": "call", "params": [2, "get_account_history", ["1.2.25", "1.11.0", 3, "1.11.0"]]}


* Parameters:

		account: The account whose history should be queried
		stop: ID of the earliest operation to retrieve
		limit: Maximum number of operations to retrieve (must not exceed 100)
		start: ID of the most recent operation to retrieve

`The operation code is 1.11.X; if start = stop = 1.11.0, return these operations recently`

* Response:

		{
			"id": 3,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.11.23481",
				"op": [0, {
					"fee": {
						"amount": 2000,
						"asset_id": "1.3.0"
					},
					"from": "1.2.25",
					"to": "1.2.19",
					"amount": {
						"amount": 1000000,
						"asset_id": "1.3.0"
					},
					"extensions": []
				}],
				"result": [0, {}],
				"block_num": 859366,
				"trx_in_block": 0,
				"op_in_trx": 0,
				"virtual_op": 52221
			}, {
				"id": "1.11.23480",
				"op": [0, {
					"fee": {
						"amount": 2000,
						"asset_id": "1.3.0"
					},
					"from": "1.2.25",
					"to": "1.2.26",
					"amount": {
						"amount": 1000000,
						"asset_id": "1.3.0"
					},
					"extensions": []
				}],
				"result": [0, {}],
				"block_num": 859345,
				"trx_in_block": 0,
				"op_in_trx": 0,
				"virtual_op": 52219
			}, {
				"id": "1.11.23479",
				"op": [6, {
					"fee": {
						"amount": 2000,
						"asset_id": "1.3.0"
					},
					"account": "1.2.25",
					"active": {
						"weight_threshold": 2,
						"account_auths": [
							["1.2.19", 1],
							["1.2.26", 1]
						],
						"key_auths": [],
						"address_auths": []
					},
					"extensions": {}
				}],
				"result": [0, {}],
				"block_num": 859339,
				"trx_in_block": 0,
				"op_in_trx": 0,
				"virtual_op": 52216
			}]
		}
		
		
### 2. get\_fill\_order\_history

* Request:

		{"id": 4, "method": "call", "params": [2, "get_fill_order_history", ["1.3.0", "1.3.2", 2]]}

* Parameters:

		asset_id_type_a: asset id
		asset_id_type_b: asset id
		limit: maximum number of operations to retrieve

* Response:

		{
			"id": 4,
			"jsonrpc": "2.0",
			"result": [{
				"id": "5.0.97429638",
				"key": {
					"base": "1.3.0",
					"quote": "1.3.2",
					"sequence": -7819491
				},
				"time": "2018-08-09T02:41:21",
				"op": {
					"fee": {
						"amount": 0,
						"asset_id": "1.3.0"
					},
					"order_id": "1.7.77233765",
					"account_id": "1.2.9765",
					"pays": {
						"amount": 1,
						"asset_id": "1.3.2"
					},
					"receives": {
						"amount": 300,
						"asset_id": "1.3.0"
					},
					"fill_price": {
						"base": {
							"amount": 1150261,
							"asset_id": "1.3.2"
						},
						"quote": {
							"amount": 265643056,
							"asset_id": "1.3.0"
						}
					},
					"is_maker": true
				}
			}, {
				"id": "5.0.97429637",
				"key": {
					"base": "1.3.0",
					"quote": "1.3.2",
					"sequence": -7819490
				},
				"time": "2018-08-09T02:41:21",
				"op": {
					"fee": {
						"amount": 0,
						"asset_id": "1.3.2"
					},
					"order_id": "1.7.77348599",
					"account_id": "1.2.19408",
					"pays": {
						"amount": 300,
						"asset_id": "1.3.0"
					},
					"receives": {
						"amount": 1,
						"asset_id": "1.3.2"
					},
					"fill_price": {
						"base": {
							"amount": 1150261,
							"asset_id": "1.3.2"
						},
						"quote": {
							"amount": 265643056,
							"asset_id": "1.3.0"
						}
					},
					"is_maker": false
				}
			}]
		}

		
		
### 3. get\_market\_history

`K line`

* Request:

		{"id": 5, "method": "call", "params": [2, "get_market_history", ["1.3.0", "1.3.2", 3600, "2018-08-08T00:00:00", "2018-08-08T02:00:00"]]}
		
* Parameters:

		asset_id_type_a: asset id
		asset_id_type_b: asset id
		bucket_seconds: bucket size
		start: start time
		end: end time

* Response:

		{
			"id": 5,
			"jsonrpc": "2.0",
			"result": [{
				"id": "5.1.11161845",
				"key": {
					"base": "1.3.0",
					"quote": "1.3.2",
					"seconds": 3600,
					"open": "2018-08-08T00:00:00"
				},
				"high_base": 2038748863,
				"high_quote": 9197000,
				"low_base": 509700000,
				"low_quote": 2371175,
				"open_base": 509700000,
				"open_quote": 2371175,
				"close_base": 2038748863,
				"close_quote": 9197000,
				"base_volume": 29533955,
				"quote_volume": 134091
			}, {
				"id": "5.1.11168859",
				"key": {
					"base": "1.3.0",
					"quote": "1.3.2",
					"seconds": 3600,
					"open": "2018-08-08T01:00:00"
				},
				"high_base": 673728209,
				"high_quote": 3031774,
				"low_base": 450000000,
				"low_quote": 2070000,
				"open_base": 450000000,
				"open_quote": 2070000,
				"close_base": 450000000,
				"close_quote": 2070000,
				"base_volume": "6693864279",
				"quote_volume": 30170097
			}, {
				"id": "5.1.11171475",
				"key": {
					"base": "1.3.0",
					"quote": "1.3.2",
					"seconds": 3600,
					"open": "2018-08-08T02:00:00"
				},
				"high_base": 113122171,
				"high_quote": 500000,
				"low_base": 450000000,
				"low_quote": 2070000,
				"open_base": 109899769,
				"open_quote": 494548,
				"close_base": 136363636,
				"close_quote": 616364,
				"base_volume": 293106406,
				"quote_volume": 1321394
			}]
		}
		
		
### 4. get\_market\_history\_buckets

* Request:

		{"id": 6, "method": "call", "params": [2, "get_market_history_buckets", []]}


* Response:

		{
			"id": 6,
			"jsonrpc": "2.0",
			"result": [15, 60, 300, 3600, 86400]
		}
