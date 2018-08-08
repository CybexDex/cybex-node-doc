# globals


### 1. get\_chain\_properties()

`Retrieve the chain property object associated with the chain`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_chain_properties","params":[],"id":1}' https://apihk.cybex.io

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"id": "2.11.0",
				"chain_id": "90be01e82b981c8f201c9a78a3d31f655743b29ff3274727b1439b093d04aa23",
				"immutable_parameters": {
					"min_committee_member_count": 21,
					"min_witness_count": 11,
					"num_special_accounts": 0,
					"num_special_assets": 0
				}
			}
		}


### 2. get\_global\_properties()

`Retrieve the current global property object`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_global_properties","params":[],"id":1}' https://apihk.cybex.io

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"id": "2.0.0",
				"parameters": {
					"current_fees": {
						"parameters": [
							[0, {
								"fee": 1000,
								"price_per_kbyte": 555
							}],
							[1, {
								"fee": 55
							}],
							[2, {
								"fee": 5
							}],
							[3, {
								"fee": 55
							}],
							[4, {}],
							[5, {
								"basic_fee": 1000000,
								"premium_fee": "7500000000",
								"price_per_kbyte": 5000
							}],
							[6, {
								"fee": 55,
								"price_per_kbyte": 389
							}],
							[7, {
								"fee": 5555
							}],
							[8, {
								"membership_annual_fee": "60168000000000",
								"membership_lifetime_fee": 100000000
							}],
							[9, {
								"fee": 277784
							}],
							[10, {
								"symbol3": "100000000000",
								"symbol4": "100000000000",
								"long_symbol": 50000000,
								"price_per_kbyte": 100000
							}],
							[11, {
								"fee": 111114,
								"price_per_kbyte": 389
							}],
							[12, {
								"fee": 277784
							}],
							[13, {
								"fee": 277784
							}],
							[14, {
								"fee": 1000,
								"price_per_kbyte": 555
							}],
							[15, {
								"fee": 55
							}],
							[16, {
								"fee": 27778
							}],
							[17, {
								"fee": 2777
							}],
							[18, {
								"fee": 277784
							}],
							[19, {
								"fee": 5
							}],
							[20, {
								"fee": 2777844
							}],
							[21, {
								"fee": 555
							}],
							[22, {
								"fee": 8333,
								"price_per_kbyte": 2777
							}],
							[23, {
								"fee": 277,
								"price_per_kbyte": 389
							}],
							[24, {
								"fee": 0
							}],
							[25, {
								"fee": 8333
							}],
							[26, {
								"fee": 555
							}],
							[27, {
								"fee": 800,
								"price_per_kbyte": 389
							}],
							[28, {
								"fee": 0
							}],
							[29, {
								"fee": 277784
							}],
							[30, {
								"fee": 555569
							}],
							[31, {
								"fee": 0
							}],
							[32, {
								"fee": 55557
							}],
							[33, {
								"fee": 111114
							}],
							[34, {
								"fee": 2777844
							}],
							[35, {
								"fee": 555,
								"price_per_kbyte": 2777
							}],
							[36, {
								"fee": 27778
							}],
							[37, {}],
							[38, {
								"fee": 55557,
								"price_per_kbyte": 389
							}],
							[39, {
								"fee": 11667,
								"price_per_output": 3889
							}],
							[40, {
								"fee": 11667,
								"price_per_output": 3889
							}],
							[41, {
								"fee": 11667
							}],
							[42, {}],
							[43, {
								"fee": 55557
							}],
							[44, {}],
							[45, {
								"fee": 10000,
								"price_per_kbyte": 10
							}],
							[46, {
								"fee": 10000,
								"price_per_kbyte": 10
							}],
							[47, {
								"fee": 10000,
								"price_per_kbyte": 10
							}]
						],
						"scale": 10000
					},
					"block_interval": 3,
					"maintenance_interval": 86400,
					"maintenance_skip_slots": 3,
					"committee_proposal_review_period": 0,
					"maximum_transaction_size": 2048,
					"maximum_block_size": 2048000000,
					"maximum_time_until_expiration": 86400,
					"maximum_proposal_lifetime": 62208000,
					"maximum_asset_whitelist_authorities": 10,
					"maximum_asset_feed_publishers": 10,
					"maximum_witness_count": 1001,
					"maximum_committee_count": 1001,
					"maximum_authority_membership": 10,
					"reserve_percent_of_fee": 2000,
					"network_percent_of_fee": 2000,
					"lifetime_referrer_percent_of_fee": 3000,
					"cashback_vesting_period_seconds": 31536000,
					"cashback_vesting_threshold": 10000000,
					"count_non_member_votes": true,
					"allow_non_member_whitelists": false,
					"witness_pay_per_block": 10000,
					"worker_budget_per_day": "50000000000",
					"max_predicate_opcode": 1,
					"fee_liquidation_threshold": 10000000,
					"accounts_per_fee_scale": 1000,
					"account_fee_scale_bitshifts": 4,
					"max_authority_depth": 2,
					"extensions": []
				},
				"next_available_vote_id": 37,
				"active_committee_members": ["1.5.11", "1.5.3", "1.5.12", "1.5.13", "1.5.6", "1.5.1", "1.5.2", "1.5.4", "1.5.5", "1.5.7", "1.5.8", "1.5.9", "1.5.10", "1.5.14", "1.5.15", "1.5.16", "1.5.17", "1.5.18", "1.5.19", "1.5.20", "1.5.21"],
				"active_witnesses": ["1.6.1", "1.6.2", "1.6.3", "1.6.4", "1.6.5", "1.6.6", "1.6.7", "1.6.8", "1.6.9", "1.6.10", "1.6.11"]
			}
		}


### 3. get\_config

`Retrieve the current global property object`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_config","params":[],"id":1}' https://apihk.cybex.io

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"GRAPHENE_SYMBOL": "CYB",
				"GRAPHENE_ADDRESS_PREFIX": "CYB",
				"GRAPHENE_MIN_ACCOUNT_NAME_LENGTH": 1,
				"GRAPHENE_MAX_ACCOUNT_NAME_LENGTH": 63,
				"GRAPHENE_MIN_ASSET_SYMBOL_LENGTH": 3,
				"GRAPHENE_MAX_ASSET_SYMBOL_LENGTH": 16,
				"GRAPHENE_MAX_SHARE_SUPPLY": "1000000000000000",
				"GRAPHENE_MAX_PAY_RATE": 10000,
				"GRAPHENE_MAX_SIG_CHECK_DEPTH": 2,
				"GRAPHENE_MIN_TRANSACTION_SIZE_LIMIT": 1024,
				"GRAPHENE_MIN_BLOCK_INTERVAL": 1,
				"GRAPHENE_MAX_BLOCK_INTERVAL": 30,
				"GRAPHENE_DEFAULT_BLOCK_INTERVAL": 5,
				"GRAPHENE_DEFAULT_MAX_TRANSACTION_SIZE": 2048,
				"GRAPHENE_DEFAULT_MAX_BLOCK_SIZE": 2000000,
				"GRAPHENE_DEFAULT_MAX_TIME_UNTIL_EXPIRATION": 86400,
				"GRAPHENE_DEFAULT_MAINTENANCE_INTERVAL": 86400,
				"GRAPHENE_DEFAULT_MAINTENANCE_SKIP_SLOTS": 3,
				"GRAPHENE_MIN_UNDO_HISTORY": 10,
				"GRAPHENE_MAX_UNDO_HISTORY": 10000,
				"GRAPHENE_MIN_BLOCK_SIZE_LIMIT": 5120,
				"GRAPHENE_MIN_TRANSACTION_EXPIRATION_LIMIT": 150,
				"GRAPHENE_BLOCKCHAIN_PRECISION": 100000,
				"GRAPHENE_BLOCKCHAIN_PRECISION_DIGITS": 5,
				"GRAPHENE_DEFAULT_TRANSFER_FEE": 100000,
				"GRAPHENE_MAX_INSTANCE_ID": "281474976710655",
				"GRAPHENE_100_PERCENT": 10000,
				"GRAPHENE_1_PERCENT": 100,
				"GRAPHENE_MAX_MARKET_FEE_PERCENT": 10000,
				"GRAPHENE_DEFAULT_FORCE_SETTLEMENT_DELAY": 86400,
				"GRAPHENE_DEFAULT_FORCE_SETTLEMENT_OFFSET": 0,
				"GRAPHENE_DEFAULT_FORCE_SETTLEMENT_MAX_VOLUME": 2000,
				"GRAPHENE_DEFAULT_PRICE_FEED_LIFETIME": 86400,
				"GRAPHENE_MAX_FEED_PRODUCERS": 200,
				"GRAPHENE_DEFAULT_MAX_AUTHORITY_MEMBERSHIP": 10,
				"GRAPHENE_DEFAULT_MAX_ASSET_WHITELIST_AUTHORITIES": 10,
				"GRAPHENE_DEFAULT_MAX_ASSET_FEED_PUBLISHERS": 10,
				"GRAPHENE_COLLATERAL_RATIO_DENOM": 1000,
				"GRAPHENE_MIN_COLLATERAL_RATIO": 1001,
				"GRAPHENE_MAX_COLLATERAL_RATIO": 32000,
				"GRAPHENE_DEFAULT_MAINTENANCE_COLLATERAL_RATIO": 1750,
				"GRAPHENE_DEFAULT_MAX_SHORT_SQUEEZE_RATIO": 1500,
				"GRAPHENE_DEFAULT_MARGIN_PERIOD_SEC": 2592000,
				"GRAPHENE_DEFAULT_MAX_WITNESSES": 1001,
				"GRAPHENE_DEFAULT_MAX_COMMITTEE": 1001,
				"GRAPHENE_DEFAULT_MAX_PROPOSAL_LIFETIME_SEC": 2419200,
				"GRAPHENE_DEFAULT_COMMITTEE_PROPOSAL_REVIEW_PERIOD_SEC": 1209600,
				"GRAPHENE_DEFAULT_NETWORK_PERCENT_OF_FEE": 2000,
				"GRAPHENE_DEFAULT_LIFETIME_REFERRER_PERCENT_OF_FEE": 3000,
				"GRAPHENE_DEFAULT_MAX_BULK_DISCOUNT_PERCENT": 5000,
				"GRAPHENE_DEFAULT_BULK_DISCOUNT_THRESHOLD_MIN": 100000000,
				"GRAPHENE_DEFAULT_BULK_DISCOUNT_THRESHOLD_MAX": "10000000000",
				"GRAPHENE_DEFAULT_CASHBACK_VESTING_PERIOD_SEC": 31536000,
				"GRAPHENE_DEFAULT_CASHBACK_VESTING_THRESHOLD": 10000000,
				"GRAPHENE_DEFAULT_BURN_PERCENT_OF_FEE": 2000,
				"GRAPHENE_WITNESS_PAY_PERCENT_PRECISION": 1000000000,
				"GRAPHENE_DEFAULT_MAX_ASSERT_OPCODE": 1,
				"GRAPHENE_DEFAULT_FEE_LIQUIDATION_THRESHOLD": 10000000,
				"GRAPHENE_DEFAULT_ACCOUNTS_PER_FEE_SCALE": 1000,
				"GRAPHENE_DEFAULT_ACCOUNT_FEE_SCALE_BITSHIFTS": 4,
				"GRAPHENE_MAX_WORKER_NAME_LENGTH": 63,
				"GRAPHENE_MAX_URL_LENGTH": 127,
				"GRAPHENE_NEAR_SCHEDULE_CTR_IV": "7640891576956012808",
				"GRAPHENE_FAR_SCHEDULE_CTR_IV": "13503953896175478587",
				"GRAPHENE_CORE_ASSET_CYCLE_RATE": 17,
				"GRAPHENE_CORE_ASSET_CYCLE_RATE_BITS": 32,
				"GRAPHENE_DEFAULT_WITNESS_PAY_PER_BLOCK": 1000000,
				"GRAPHENE_DEFAULT_WITNESS_PAY_VESTING_SECONDS": 86400,
				"GRAPHENE_DEFAULT_WORKER_BUDGET_PER_DAY": "50000000000",
				"GRAPHENE_MAX_INTEREST_APR": 10000,
				"GRAPHENE_COMMITTEE_ACCOUNT": "1.2.0",
				"GRAPHENE_WITNESS_ACCOUNT": "1.2.1",
				"GRAPHENE_RELAXED_COMMITTEE_ACCOUNT": "1.2.2",
				"GRAPHENE_NULL_ACCOUNT": "1.2.3",
				"GRAPHENE_TEMP_ACCOUNT": "1.2.4"
			}
		}


### 4. get\_chain\_id

`Get the chain ID`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_chain_id","params":[],"id":1}' https://apihk.cybex.io

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": "90be01e82b981c8f201c9a78a3d31f655743b29ff3274727b1439b093d04aa23"
		}

### 5. get\_dynamic\_global\_properties

`Retrieve the current dynamic global property object`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_dynamic_global_properties","params":[],"id":1}' https://apihk.cybex.io

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"id": "2.1.0",
				"head_block_number": 4514733,
				"head_block_id": "0044e3ad4f9edb64dfad7dfd42a000edac77ce9e",
				"time": "2018-08-02T10:56:33",
				"current_witness": "1.6.6",
				"next_maintenance_time": "2018-08-02T19:00:00",
				"last_budget_time": "2018-08-01T19:00:03",
				"witness_budget": 96720000,
				"accounts_registered_this_interval": 70,
				"recently_missed_count": 0,
				"current_aslot": 10499027,
				"recent_slots_filled": "340282366920938463463374607431768211455",
				"dynamic_flags": 0,
				"last_irreversible_block_num": 4514724
			}
		}