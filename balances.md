# balances


### 1. get\_account\_balances

`Get an account’s balances in various assets.`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_account_balances","params":["1.2.7", []],"id":1}' https://apihk.cybex.io

* Parameters:

		id: ID of the account to get balances for
		assets: IDs of the assets to get balances of; if empty, get all assets account has a balance in

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"amount": 1225975847,
				"asset_id": "1.3.0"
			}]
		}


### 2.get\_named\_account\_balances
`Semantically equivalent to get_account_balances, but takes a name instead of an ID, return balances of the account`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_named_account_balances","params":["harley", ["1.3.0"]],"id":1}' https://apihk.cybex.io

* Parameters:

		name: account name
		asset_ids: asset ids

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"amount": 1224975115,
				"asset_id": "1.3.0"
			}]
		}



### 3. get\_vesting\_balances
`Return vesting balances`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_vesting_balances","params":["1.2.7"],"id":1}' https://apihk.cybex.io

* Parameters:

		account_id: account id

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.13.0",
				"owner": "1.2.7",
				"balance": {
					"amount": "112298566510",
					"asset_id": "1.3.0"
				},
				"policy": [1, {
					"vesting_seconds": 31536000,
					"start_claim": "1970-01-01T00:00:00",
					"coin_seconds_earned": "1045287256041805458",
					"coin_seconds_earned_last_update": "2018-08-02T19:00:00"
				}]
			}, {
				"id": "1.13.10",
				"owner": "1.2.7",
				"balance": {
					"amount": "2623960000",
					"asset_id": "1.3.0"
				},
				"policy": [1, {
					"vesting_seconds": 86400,
					"start_claim": "1970-01-01T00:00:00",
					"coin_seconds_earned": "226709280000000",
					"coin_seconds_earned_last_update": "2018-08-03T04:18:30"
				}]
			}]
		}


