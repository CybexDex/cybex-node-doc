# accounts


#### 1. get_accounts
`Get a list of accounts by ID`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_accounts","params":[["1.2.7"]],"id":1}' https://apihk.cybex.io

* Parameters:

 		account_ids: IDs of the accounts to retrieve

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.2.7",
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
			}]
		}

#### 2. get\_full\_accounts

`Map of string from names_or_ids to the corresponding account`

* Request:

			curl --data '{"jsonrpc":"2.0","method":"get_full_accounts","params":[["1.2.7"], false],"id":1}' https://apihk.cybex.io

* Parameters:

		names_or_ids: Each item must be the name or ID of an account to retrieve
		callback: Bool, function to call with updates

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [
				["1.2.7", {
					"account": {
						"id": "1.2.7",
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
					},
					"statistics": {
						"id": "2.6.7",
						"owner": "1.2.7",
						"most_recent_op": "2.9.176217607",
						"total_ops": 36289,
						"removed_ops": 35789,
						"total_core_in_orders": 0,
						"lifetime_fees_paid": "73433177259",
						"pending_fees": 0,
						"pending_vested_fees": 4002933
					},
					"registrar_name": "harley",
					"referrer_name": "harley",
					"lifetime_referrer_name": "harley",
					"votes": [],
					"cashback_balance": {
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
					},
					"balances": [{
						"id": "2.5.11",
						"owner": "1.2.7",
						"asset_type": "1.3.0",
						"balance": 1226976574
					}],
					"vesting_balances": [{
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
							"amount": "2622780000",
							"asset_id": "1.3.0"
						},
						"policy": [1, {
							"vesting_seconds": 86400,
							"start_claim": "1970-01-01T00:00:00",
							"coin_seconds_earned": "226607328000000",
							"coin_seconds_earned_last_update": "2018-08-03T03:13:54"
						}]
					}],
					"limit_orders": [],
					"call_orders": [],
					"settle_orders": [],
					"proposals": [],
					"assets": [],
					"withdraws": []
				}]
			]
		}



#### 3. get\_account\_by\_name

`Return the detail of account by name`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_account_by_name","params":["nathan"],"id":1}' https://apihk.cybex.io

* Parameters:

		name: account name

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"id": "1.2.25",
				"membership_expiration_date": "1969-12-31T23:59:59",
				"registrar": "1.2.25",
				"referrer": "1.2.25",
				"lifetime_referrer": "1.2.25",
				"network_fee_percentage": 2000,
				"lifetime_referrer_fee_percentage": 8000,
				"referrer_rewards_percentage": 0,
				"name": "nathan",
				"owner": {
					"weight_threshold": 1,
					"account_auths": [],
					"key_auths": [
						["CYB6iPuTiBpghi4Dh8phPeAUTofNa3DZK4HjugTpduA48kLXxfKZd", 1]
					],
					"address_auths": []
				},
				"active": {
					"weight_threshold": 1,
					"account_auths": [],
					"key_auths": [
						["CYB7pb9B2J3D6NXRmsaXNnBZr5AVnH5nLNtrti3ADZfgYpRn7ihQQ", 1]
					],
					"address_auths": []
				},
				"options": {
					"memo_key": "CYB7pb9B2J3D6NXRmsaXNnBZr5AVnH5nLNtrti3ADZfgYpRn7ihQQ",
					"voting_account": "1.2.5",
					"num_witness": 0,
					"num_committee": 0,
					"votes": [],
					"extensions": []
				},
				"statistics": "2.6.25",
				"whitelisting_accounts": [],
				"blacklisting_accounts": [],
				"whitelisted_accounts": [],
				"blacklisted_accounts": [],
				"cashback_vb": "1.13.1",
				"owner_special_authority": [0, {}],
				"active_special_authority": [0, {}],
				"top_n_control_flags": 0
			}
		}


#### 4. get\_account\_references

`all accounts that referr to the key or account id in their owner or active authorities`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_account_references","params":["1.2.7"],"id":1}' https://apihk.cybex.io

* Parameters:

		account_id : account id

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": ["1.2.0", "1.2.1", "1.2.2"]
		}


#### 5. lookup\_account\_names

`The accounts holding the provided names`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"lookup_account_names","params":[["nathan", "harley"]],"id":1}' https://apihk.cybex.io

* Parameters:

		account_names: Names of the accounts to retrieve

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.2.25",
				"membership_expiration_date": "1969-12-31T23:59:59",
				"registrar": "1.2.25",
				"referrer": "1.2.25",
				"lifetime_referrer": "1.2.25",
				"network_fee_percentage": 2000,
				"lifetime_referrer_fee_percentage": 8000,
				"referrer_rewards_percentage": 0,
				"name": "nathan",
				"owner": {
					"weight_threshold": 1,
					"account_auths": [],
					"key_auths": [
						["CYB6iPuTiBpghi4Dh8phPeAUTofNa3DZK4HjugTpduA48kLXxfKZd", 1]
					],
					"address_auths": []
				},
				"active": {
					"weight_threshold": 1,
					"account_auths": [],
					"key_auths": [
						["CYB7pb9B2J3D6NXRmsaXNnBZr5AVnH5nLNtrti3ADZfgYpRn7ihQQ", 1]
					],
					"address_auths": []
				},
				"options": {
					"memo_key": "CYB7pb9B2J3D6NXRmsaXNnBZr5AVnH5nLNtrti3ADZfgYpRn7ihQQ",
					"voting_account": "1.2.5",
					"num_witness": 0,
					"num_committee": 0,
					"votes": [],
					"extensions": []
				},
				"statistics": "2.6.25",
				"whitelisting_accounts": [],
				"blacklisting_accounts": [],
				"whitelisted_accounts": [],
				"blacklisted_accounts": [],
				"cashback_vb": "1.13.1",
				"owner_special_authority": [0, {}],
				"active_special_authority": [0, {}],
				"top_n_control_flags": 0
			}, {
				"id": "1.2.7",
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
			}]
		}



#### 6. lookup\_accounts

`Map of account names to corresponding IDs`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"lookup_accounts","params":["nathan", 7],"id":1}' https://apihk.cybex.io

* Parameters:

		lower_bound_name: Lower bound of the first name to return
		limit: Maximum number of results to return must not exceed 1000
		
* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [
				["nathan", "1.2.25"],
				["natu61", "1.2.10857"],
				["nau529", "1.2.13494"],
				["nauhc6", "1.2.36394"],
				["nawuh925", "1.2.27623"],
				["naya1008", "1.2.29372"],
				["nayayan12", "1.2.16352"]
			]
		}


#### 7. get\_account\_count

`Get the total number of accounts registered with the blockchain.`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_account_count","params":[],"id":1}' https://apihk.cybex.io

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": 36884
		}
