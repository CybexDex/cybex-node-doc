# committee members

### 1. get\_committee\_members

`Get a list of committee_members by ID`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"get_committee_members","params":[["1.5.1"]],"id":1}' https://apihk.cybex.io

* Parameters:

		committee_member_ids: IDs of the committee_members to retrieve

* Response:

		{
			"id": 1,
			"jsonrpc": "2.0",
			"result": [{
				"id": "1.5.1",
				"committee_member_account": "1.2.17",
				"vote_id": "0:12",
				"total_votes": "241189234794",
				"url": ""
			}]
		}


### 2. get\_committee\_member\_by\_account

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


### 3. lookup\_committee\_member\_accounts

`Get names and IDs for registered committee_members`

* Request:

		curl --data '{"jsonrpc":"2.0","method":"lookup_committee_member_accounts","params":["1.5.1", 22],"id":1}' https://apihk.cybex.io

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
				["earth", "1.5.11"],
				["fairystar", "1.5.6"],
				["harley", "1.5.12"],
				["jupiter", "1.5.13"],
				["kvir", "1.5.7"],
				["lucifer", "1.5.8"],
				["mars", "1.5.14"],
				["mercury", "1.5.15"],
				["moon", "1.5.16"],
				["nathan", "1.5.0"],
				["neptune", "1.5.17"],
				["processon", "1.5.9"],
				["saturn", "1.5.18"],
				["sun", "1.5.19"],
				["tina", "1.5.10"],
				["uranus", "1.5.20"],
				["venus", "1.5.21"]
			]
		}
