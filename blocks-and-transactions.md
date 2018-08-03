# blocks and transactions

### 1.get\_block_header

`Return the header of referenced block, or null if no matching block was found`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_block_header","params":["4427000"],"id":1}' https://apihk.cybex.io

* Parameters:

		block_num: height of the block to be returned

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"previous": "00438cf7e5e52236bf61d15740449cfee84c257b",
				"timestamp": "2018-07-30T09:49:03",
				"witness": "1.6.8",
				"transaction_merkle_root": "7a9f852c737b442ce42d3f239f723994aad82fa7",
				"extensions": []
			}
		}


### 2.get_block

`Return the referenced block, or null if no matching block was found`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_block","params":["4427000"],"id":1}' https://apihk.cybex.io

* Parameters:

		block_num: height of the block to be returned

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"previous": "00438cf7e5e52236bf61d15740449cfee84c257b",
				"timestamp": "2018-07-30T09:49:03",
				"witness": "1.6.8",
				"transaction_merkle_root": "7a9f852c737b442ce42d3f239f723994aad82fa7",
				"extensions": [],
				"witness_signature": "2037dac761871e52abf2e58669e23ad2e07732f1a808cae794e5503f11a004f29d3d8689eb922fdce556034cc3cd6b6785da3109f5ec6aa0ae21368a84e54db296",
				"transactions": [{
					"ref_block_num": 36086,
					"ref_block_prefix": 1500000766,
					"expiration": "2018-07-30T09:49:29",
					"operations": [
						[1, {
							"fee": {
								"amount": 55,
								"asset_id": "1.3.0"
							},
							"seller": "1.2.31042",
							"amount_to_sell": {
								"amount": 17977820,
								"asset_id": "1.3.27"
							},
							"min_to_receive": {
								"amount": 7340834,
								"asset_id": "1.3.0"
							},
							"expiration": "2018-07-30T09:54:59",
							"fill_or_kill": false,
							"extensions": []
						}]
					],
					"extensions": [],
					"signatures": ["1f696c3e532e163b4860a39da54f89c81c37f850a012b46767919ff6436e008fd939d992df4442894205a1582452dfd23aae8c2446d4ea0ef9e031fc0d036cfe80"],
					"operation_results": [
						[1, "1.7.61886713"]
					]
				}, {
					"ref_block_num": 36086,
					"ref_block_prefix": 1500000766,
					"expiration": "2018-07-30T09:49:29",
					"operations": [
						[1, {
							"fee": {
								"amount": 55,
								"asset_id": "1.3.0"
							},
							"seller": "1.2.31085",
							"amount_to_sell": {
								"amount": 10474665,
								"asset_id": "1.3.27"
							},
							"min_to_receive": {
								"amount": 1259669,
								"asset_id": "1.3.26"
							},
							"expiration": "2018-07-30T09:53:59",
							"fill_or_kill": false,
							"extensions": []
						}]
					],
					"extensions": [],
					"signatures": ["1f2b5b86599c7dd7e22525f18bed562cc82e21b03e2fdf26dbf4a40b37239c403a014d3086cbee64f3f114372ed36dce75b3a45e2d2b48a1b5dfcbfe825a7d9cc5"],
					"operation_results": [
						[1, "1.7.61886714"]
					]
				}, {
					"ref_block_num": 36086,
					"ref_block_prefix": 1500000766,
					"expiration": "2018-07-30T09:49:29",
					"operations": [
						[1, {
							"fee": {
								"amount": 55,
								"asset_id": "1.3.0"
							},
							"seller": "1.2.31102",
							"amount_to_sell": {
								"amount": 123926,
								"asset_id": "1.3.3"
							},
							"min_to_receive": {
								"amount": 1212338,
								"asset_id": "1.3.26"
							},
							"expiration": "2018-07-30T09:53:59",
							"fill_or_kill": false,
							"extensions": []
						}]
					],
					"extensions": [],
					"signatures": ["1f107e8f2f499566972a6d8a7d504ac30f2fe6d71d9b7ff3a4374dec6ff1907bfb4b8ef2ab06695a7c15baa386a24c4400fcd577a3b0fc54172e038755bd9d674b"],
					"operation_results": [
						[1, "1.7.61886715"]
					]
				}, {
					"ref_block_num": 36086,
					"ref_block_prefix": 1500000766,
					"expiration": "2018-07-30T09:49:29",
					"operations": [
						[1, {
							"fee": {
								"amount": 55,
								"asset_id": "1.3.0"
							},
							"seller": "1.2.10641",
							"amount_to_sell": {
								"amount": 2660695,
								"asset_id": "1.3.0"
							},
							"min_to_receive": {
								"amount": 14157,
								"asset_id": "1.3.2"
							},
							"expiration": "2018-07-30T09:53:59",
							"fill_or_kill": false,
							"extensions": []
						}]
					],
					"extensions": [],
					"signatures": ["1f041a5aa35f798776cf668c2b4bbaeefe0fb3762607bb454fe73aa8dd3cfb4e9b3a386cc2e2a2e47e575ab9f173d8931acbedf65547a244c9ee65b2f48dc7cf8b"],
					"operation_results": [
						[1, "1.7.61886716"]
					]
				},
				.....
				]
			}
		}

### 3.get_transaction

`Used to fetch an individual transaction`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_transaction","params":["4427000","2"],"id":1}' https://apihk.cybex.io

* Parameters:

		block_num: block number

		trx_in_block: subscript number of transaction in block, starting from zero

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"ref_block_num": 36086,
				"ref_block_prefix": 1500000766,
				"expiration": "2018-07-30T09:49:29",
				"operations": [
					[1, {
						"fee": {
							"amount": 55,
							"asset_id": "1.3.0"
						},
						"seller": "1.2.31102",
						"amount_to_sell": {
							"amount": 123926,
							"asset_id": "1.3.3"
						},
						"min_to_receive": {
							"amount": 1212338,
							"asset_id": "1.3.26"
						},
						"expiration": "2018-07-30T09:53:59",
						"fill_or_kill": false,
						"extensions": []
					}]
				],
				"extensions": [],
				"signatures": ["1f107e8f2f499566972a6d8a7d504ac30f2fe6d71d9b7ff3a4374dec6ff1907bfb4b8ef2ab06695a7c15baa386a24c4400fcd577a3b0fc54172e038755bd9d674b"],
				"operation_results": [
					[1, "1.7.61886715"]
				]
			}
		}



