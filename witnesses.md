# witnesses


### 1. get\_witnesses

`Get a list of witnesses by ID`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_witnesses","params":[["1.6.1"]],"id":1}' https://apihk.cybex.io

* Parameters:

		witness_ids: IDs of the witnesses to retrieve
		
* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.6.1",
				"witness_account": "1.2.6",
				"last_aslot": 10605553,
				"signing_key": "CYB8iWrVHcBaq74mqA6Dd58yeN7pEgmvBLrhYB1HSQRj8UBrHec5u",
				"pay_vb": "1.13.2",
				"vote_id": "1:0",
				"total_votes": "280493540206",
				"url": "",
				"total_missed": 3096,
				"last_confirmed_block_num": 4621255
			}]
		}
		
### 2. get\_witness\_by\_account

`Return the witness object, or null if the account does not have a witness`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_witness_by_account","params":["1.2.7"],"id":1}' https://apihk.cybex.io

* Parameters:

		account: The ID of the account whose witness should be retrieved

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"id": "1.6.2",
				"witness_account": "1.2.7",
				"last_aslot": 10605630,
				"signing_key": "CYB8Vfkpqn6B35xTMCwhqUuGDHuTfdmo368zDWT4xz2MZmy368Gvh",
				"pay_vb": "1.13.10",
				"vote_id": "1:1",
				"total_votes": "280484687773",
				"url": "",
				"total_missed": 542713,
				"last_confirmed_block_num": 4621332
			}
		}


### 3. lookup\_witness\_accounts

`Get names and IDs for registered witnesses`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"lookup_witness_accounts","params":["harley", 15],"id":1}' https://apihk.cybex.io

* Parameters:

		lower_bound_name: Lower bound of the first name to return
		limit: Maximum number of results to return must not exceed 1000

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [
				["harley", "1.6.2"],
				["jupiter", "1.6.3"],
				["mars", "1.6.4"],
				["mercury", "1.6.5"],
				["moon", "1.6.6"],
				["neptune", "1.6.7"],
				["saturn", "1.6.8"],
				["sun", "1.6.9"],
				["uranus", "1.6.10"],
				["venus", "1.6.11"]
			]
		}

### 4. get\_witness\_count

`Get the total number of witnesses registered with the blockchain`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_witness_count","params":[],"id":1}' https://apihk.cybex.io

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": 11
		}


