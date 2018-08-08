# markets / feeds


### 1. get\_order\_book

`Returns the order book for the market base:quote`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_order_book","params":["CYB", "JADE.ETH", 3],"id":1}' https://apihk.cybex.io

* Parameters:

		base: String name of the first asset
		quote: String name of the second asset
		depth: of the order book. Up to depth of each asks and bids, capped at 50. Prioritizes most moderate of each

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"base": "CYB",
				"quote": "JADE.ETH",
				"bids": [{
					"price": "2003.106324701195219123",
					"quote": "0.016065",
					"base": "32.17991"
				}, {
					"price": "2000",
					"quote": "0.973636",
					"base": "1947.27200"
				}, {
					"price": "1983.700198370019837001",
					"quote": "0.083682",
					"base": "166"
				}],
				"asks": [{
					"price": "2008.716065865598575878",
					"quote": "0.000001",
					"base": "0.00200"
				}, {
					"price": "2173.865785526401599965",
					"quote": "0.460010",
					"base": "1000"
				}, {
					"price": "2173.913043478260869565",
					"quote": "0.920000",
					"base": "2000"
				}]
			}
		}


### 2. get\_limit\_orders

`Get limit orders in a given market`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_limit_orders","params":["1.3.0", "1.3.2", 1],"id":1}' https://apihk.cybex.io

* Parameters:

		a: ID of asset being sold
		b: ID of asset being purchased
		limit: Maximum number of orders to retrieve

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.7.66979388",
				"expiration": "2023-08-03T10:38:43",
				"seller": "1.2.5132",
				"for_sale": 493347144,
				"sell_price": {
					"base": {
						"amount": 500000000,
						"asset_id": "1.3.0"
					},
					"quote": {
						"amount": 2450000,
						"asset_id": "1.3.2"
					}
				},
				"deferred_fee": 0
			}, {
				"id": "1.7.66983772",
				"expiration": "2023-08-03T10:48:20",
				"seller": "1.2.19408",
				"for_sale": 1912008,
				"sell_price": {
					"base": {
						"amount": 1913687,
						"asset_id": "1.3.2"
					},
					"quote": {
						"amount": 414200000,
						"asset_id": "1.3.0"
					}
				},
				"deferred_fee": 0
			}]
		}	


### 4. get\_ticker

`Return the market ticker for the past 24 hours`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_ticker","params":["JADE.ETH", "CYB"],"id":1}' https://apihk.cybex.io

* Parameters:

		a: String name of the first asset
		b: String name of the second asset

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"time": "2018-08-06T03:08:16",
				"base": "JADE.ETH",
				"quote": "CYB",
				"latest": "0.000487188654353562",
				"lowest_ask": "0.000487188654353562",
				"highest_bid": "0.00048",
				"percent_change": "1.49",
				"base_volume": "225.62666",
				"quote_volume": "460960.32089"
			}
		}

### 5. get\_24\_volume

`The market volume over the past 24 hours`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_24_volume","params":["CYB", "JADE.ETH"],"id":1}' https://apihk.cybex.io

* Parameters:

		a: String name of the first asset
		b: String name of the second asset
* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"time": "2018-08-06T02:56:44",
				"base": "CYB",
				"quote": "JADE.ETH",
				"base_volume": "462814.14025",
				"quote_volume": "226.514174"
			}
		}

### 6. get\_trade\_history
`Return recent transactions in the market`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_trade_history","params":["CYB", "JADE.ETH", "2018-08-05T00:00:00", "2018-08-04T00:00:00", 3],"id":1}' https://apihk.cybex.io

* Parameters:

		a: String name of the first asset
		b: String name of the second asset
		stop: Stop time as a UNIX timestamp
		limit: Number of trasactions to retrieve, capped at 100
		start: Start time as a UNIX timestamp

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"sequence": 7757291,
				"date": "2018-08-04T23:47:42",
				"price": "2012.072434607645875251",
				"amount": "0.019422",
				"value": "39.07847",
				"side1_account_id": "1.2.34536",
				"side2_account_id": "1.2.34016"
			}, {
				"sequence": 7757289,
				"date": "2018-08-04T23:46:48",
				"price": "2012.072434607645875251",
				"amount": "0.009148",
				"value": "18.40643",
				"side1_account_id": "1.2.34536",
				"side2_account_id": "1.2.34007"
			}, {
				"sequence": 7757287,
				"date": "2018-08-04T23:46:36",
				"price": "2012.072434607645875251",
				"amount": "0.004692",
				"value": "9.44064",
				"side1_account_id": "1.2.34536",
				"side2_account_id": "1.2.8307"
			}]
		}
