# objects

### 1.get_objects


`Return the details of objects retrieved, in the order they are mentioned in ids`

* Requesst:

		curl --data '{"jsonrpc":"2.0","method":"get_objects","params":[["1.2.7", "1.3.0"]],"id":1}' https://apihk.cybex.io
* Parameters:

		ids: IDs of the objects to retrieve

* Response:
		
		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.2.7",                      // id of account
				"membership_expiration_date": "1969-12-31T23:59:59",
				"registrar": "1.2.7",
				"referrer": "1.2.7",
				"lifetime_referrer": "1.2.7",
				"network_fee_percentage": 2000,
				"lifetime_referrer_fee_percentage": 8000,
				"referrer_rewards_percentage": 0,
				"name": "harley",
				"owner": {
					"weight_threshold": 1,
					"account_auths": [],
					"key_auths": [
						["CYB8jM4e1z1xS63xxVhuperU1VvusQz8Ye8CrnTBigFUaErpigpPL", 1]
					],
					"address_auths": []
				},
				"active": {
					"weight_threshold": 1,
					"account_auths": [],
					"key_auths": [
						["CYB7UdEEgrFYAR4DfSi8svfUUzE2E2twSFqAx66LqmgxXJjk5h7LR", 1]
					],
					"address_auths": []
				},
				"options": {
					"memo_key": "CYB7UdEEgrFYAR4DfSi8svfUUzE2E2twSFqAx66LqmgxXJjk5h7LR",
					"voting_account": "1.2.5",
					"num_witness": 0,
					"num_committee": 0,
					"votes": [],
					"extensions": []
				},
				"statistics": "2.6.7",
				"whitelisting_accounts": [],
				"blacklisting_accounts": [],
				"whitelisted_accounts": [],
				"blacklisted_accounts": [],
				"cashback_vb": "1.13.0",
				"owner_special_authority": [0, {}],
				"active_special_authority": [0, {}],
				"top_n_control_flags": 0
			}, {
				"id": "1.3.0",                   // id of asset
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
		