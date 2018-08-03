# 0. rpc protocol
### http header

	Host: YOUR_RPC_ENDPOINT:PORT
	Accept: */*
	Content-Type: application/json
	
`available endpoints: tokyo-01.cybex.io; singapore-01.cybex.io; korea-01.cybex.io; hongkong.cybex.io`
### post data

	{“jsonrpc": "2.0", "method": "get_ticker", "params": ["JADE.ETH", "CYB"], "id": 1}
	
---

# 1. get_ticker
`Returns the ticker for the market assetA:assetB`

* Request :


		curl --data '{"jsonrpc":"2.0","method":"get_ticker","params":["JADE.ETH","CYB"],"id":1}' https://apihk.cybex.io

* parameters

		param1: string name(or id) of the first asset
		param2: string name(or id) of the second asset

* Response:


		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"time": "2018-08-03T06:12:03",
				"base": "JADE.ETH",
				"quote": "CYB",
				"latest": "0.0004490000000009878",           // the price of the last trade
				"lowest_ask": "0.00046012883806963589",      // ask1 price
				"highest_bid": "0.0004490000000009878",      // bid1 price
				"percent_change": "-10.28",                  // the percent of price change from 24h before to now
				"base_volume": "434.199501",                 // volume of base asset traded in last 24h
				"quote_volume": "881651.40044"               // volume of quote asset trade in last 24h
			}
		}

		
# 2. get\_24\_volume
`Returns the 24 hour volume for the market assetA:assetB`

* Request:


		curl --data '{"jsonrpc": "2.0", "method": "get_24_volume", "params": ["JADE.ETH","CYB"], "id": 1}'  https://apihk.cybex.io

* parameters:

		param1: string name(or id) of the first asset
		param2: string name(or id) of the second asset

* Response:

		
		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"time": "2018-08-03T06:15:10",
				"base": "JADE.ETH",               // symbol of base asset to be queried
				"quote": "CYB",                   // symbol of quote asset to be queried
				"base_volume": "434.201498",      // volume of base asset traded in last 24h
				"quote_volume": "881661.69757"    // volume of quote asset traded in last 24h
			}
		}

		
# 3. get\_trade\_history
`Returns recent trades for the market assetA:assetB`
`Note: Currently, timezone offsets are not supported. The time must be UTC`

* Request:


		curl --data '{"jsonrpc": "2.0", "method": "get_trade_history", "params": ["JADE.ETH","CYB","2018-07-03T09:00:00","2018-07-01T12:00:00",3], "id": 1}'  https://apihk.cybex.io
		
* parameters:


		param1: string name(or id) of the first asset
		
		param2: string name(or id) of the second asset
		
		param3: start time as a UNIX timestamp
		
		param4: stop time as a UNIX timestamp
		
		param5: number of trasactions to retrieve, capped at 100
		
**Attention：**

	The start time in get_trade_history method is closest to now, at the same, the stop time is far away from now. 

* Response:

		
		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"sequence": 3404167,                  // the sequence number of trade
				"date": "2018-07-03T09:00:00",        // the datetime of the trade
				"price": "0.0004813418275013076",     // the price of the trade
				"amount": "85.25504",                 // the amount of quote asset received in the trade
				"value": "0.041036",                  // the amount of base asset paid in the trade
				"side1_account_id": "1.2.10630",      // account id
				"side2_account_id": "1.2.10635"       // account id
			}, {
				"sequence": 3404165,
				"date": "2018-07-03T09:00:00",
				"price": "0.00048136729117731226",
				"amount": "89.77967",
				"value": "0.043217",
				"side1_account_id": "1.2.10628",
				"side2_account_id": "1.2.10635"
			}, {
				"sequence": 3404163,
				"date": "2018-07-03T09:00:00",
				"price": "0.00048136729117731226",
				"amount": "47.09738",
				"value": "0.022671",
				"side1_account_id": "1.2.10628",
				"side2_account_id": "1.2.10612"
			}]
		}

 
			
# 4. get\_trade\_history\_by\_sequence

`Returns recent trades for the market by sequence`

* Request:


		curl --data '{"jsonrpc": "2.0", "method": "get_trade_history_by_sequence", "params": ["JADE.ETH","CYB",3404168,"2018-07-01T12:00:00",3], "id": 1}'  https://apihk.cybex.io
		
* parameters:


		param1: string name(or id) of the first asset
		
		param2: string name(or id) of the second asset
		
		param3: start sequence
		
		param4: stop time as a UNIX timestamp
		
		param5: number of trasactions to retrieve, capped at 100
		
* Response:


		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"sequence": 3404167,                // the sequence number of trade 
				"date": "2018-07-03T09:00:00",      // the datetime of the trade
				"price": "0.0004813418275013076",   // the price of the trade
				"amount": "85.25504",               // the amount of quote asset received in the trade
				"value": "0.041036",                // the amount of base asset paid in the trade
				"side1_account_id": "1.2.10630",    // account id
				"side2_account_id": "1.2.10635"     // account id
			}, {
				"sequence": 3404165,
				"date": "2018-07-03T09:00:00",
				"price": "0.00048136729117731226",
				"amount": "89.77967",
				"value": "0.043217",
				"side1_account_id": "1.2.10628",
				"side2_account_id": "1.2.10635"
			}, {
				"sequence": 3404163,
				"date": "2018-07-03T09:00:00",
				"price": "0.00048136729117731226",
				"amount": "47.09738",
				"value": "0.022671",
				"side1_account_id": "1.2.10628",
				"side2_account_id": "1.2.10612"
			}]
		}

**Attention**

	The sequence is an odd number. All the sequence number returned in the method is smaller than requested, for example, when request 3404168, the biggest sequence number is 3404167.


# 5. get\_order\_book
`Returns the order book for the market base:quote`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_order_book","params":["JADE.ETH","CYB",3],"id":1}' https://apihk.cybex.io

* parameters:


		param1: string name(or id) of the first asset
		param2: string name(or id) of the second asset
		param3: depth of the order book. Up to depth of each asks and bids, acpped at 50. Prioritizes most moderate of each

* Response:

		{
		    "id": 1,
		    "jsonrpc": "2.0",
		    "result": {
		        "base": "JADE.ETH",
		        "quote": "CYB",
		        "bids": [
		            {
		                "price": "0.00063350488291374",    // the highest price in bids list
		                "quote": "36.67058999999999713",   // the minimum amount of quote asset to received in the trade
		                "base": "0.02323100000000000"      // the amount of base asset to be paid in the trade
		            },
		            {
		                "price": "0.00063328990790083",
		                "quote": "295.44130999999998721",
		                "base": "0.18709999999999999"
		            },
		            {
		                "price": "0.00063221055979644",
		                "quote": "1572.00000000000000000",
		                "base": "0.99383500000000002"
		            }
		        ],
		        "asks": [
		            {
		                "price": "0.00063441096472366",     // the lowest price in asks list
		                "quote": "48.86422999999999917",    // the amount of quote asset to be paid in the trade
		                "base": "0.03100000000000000"       // the minimum amount of base asset to received in the trade
		            },
		            {
		                "price": "0.00063593908980416",
		                "quote": "358.68214999999997872",
		                "base": "0.22810000000000000"
		            },
		            {
		                "price": "0.00063734254503984",
		                "quote": "300.62326999999999089",
		                "base": "0.19159999999999999"
		            }
		        ]
		    }
		}


# 5. list\_assets


You can get all the trading pairs in CYBEX by [https://app.cybex.io/lab/exchange/asset](https://app.cybex.io/lab/exchange/asset). Each base asset is followed by a list of quote assets.
The assets displayed in webpage is issued by Jadepool which provided by CYBEX core team. Please use the name listed to get more information about assets, and remove the 'JADE.' prefix when displayed in your webpages. 
		                
		                
		                
# remarks


#### json-rpc

Protocol used in API is JSON-RPC 2.0, here is some specification about JSON-RPC 2.0. For more information please refer to [JSON-RPC 2.0 Specification](http://www.jsonrpc.org/specification)

A rpc call is represented by sending a Request object to a Server. The Request object has the following members:

* jsonrpc


	A String specifying the version of the JSON-RPC protocol. MUST be exactly "2.0".

* method


	A String containing the name of the method to be invoked. Method names that begin with the word rpc followed by a period character (U+002E or ASCII 46) are reserved for rpc-internal methods and extensions and MUST NOT be used for anything else.

* params


	A Structured value that holds the parameter values to be used during the invocation of the method. This member MAY be omitted.

* id


	An identifier established by the Client that MUST contain a String, Number, or NULL value if included. If it is not included it is assumed to be a notification. The value SHOULD normally not be Null [1] and Numbers SHOULD NOT contain fractional parts [2]
The Server MUST reply with the same value in the Response object if included. This member is used to correlate the context between the two objects.

	[1] The use of Null as a value for the id member in a Request object is discouraged, because this specification uses a value of Null for Responses with an unknown id. Also, because JSON-RPC 1.0 uses an id value of Null for Notifications this could cause confusion in handling.

	[2] Fractional parts may be problematic, since many decimal fractions cannot be represented exactly as binary fractions. 