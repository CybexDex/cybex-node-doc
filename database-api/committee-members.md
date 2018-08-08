# committee members


### 1. get\_committee\_member\_by\_account

`Get the committee_member owned by a given account`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_committee_member_by_account","params":["1.2.7"],"id":1}' https://apihk.cybex.io

* Parameters:

		account: The ID of the account whose committee_member should be retrieved

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": {
				"id": "1.5.12",
				"committee_member_account": "1.2.7",
				"vote_id": "0:23",
				"total_votes": "280482493905",
				"url": ""
			}
		}


### 2. lookup\_committee\_member\_accounts

`Get names and IDs for registered committee_members`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"lookup_committee_member_accounts","params":["1.2.7", 6],"id":1}' https://apihk.cybex.io

* Parameters:
		
		lower_bound_name: Lower bound of the first name to return
		limit: Maximum number of results to return must not exceed 1000

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [
				["april", "1.5.1"],
				["avir", "1.5.2"],
				["bigerjoe", "1.5.3"],
				["bigjoe", "1.5.4"],
				["celtics-tatum", "1.5.5"],
				["earth", "1.5.11"]
			]
		}

