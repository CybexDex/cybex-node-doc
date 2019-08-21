import cybex
import time

name = "cybex-jadegateway"

instance = cybex.Cybex('wss://hongkong.cybex.io')

account = cybex.Account(name, cybex_instance = instance)

current_history_id = "1.11.0"

while True:
    # get current last irreversible block number(lib)
    # only operations packed in a block earlier than lib is 100% confirmed by chain
    lib_num = instance.info()['last_irreversible_block_num']

    # call history api to fetch account history operations
    # params:
    # @account_id: operation related account
    # @op_code: 0=transfer,1=limit_order_create,2=...
    # @start_id: start history id, "1.11.0" for latest history object id
    # @end_id: end history id, "1.11.0" for earliest history object id
    # @count: maximum operations to fetch
    # @api: api name
    result = instance.rpc.get_account_history_operations(account['id'], 0, '1.11.0', current_history_id, 10, api = 'history')
    for r in result[::-1]:
        if r['block_num'] > lib_num: # op not confirmed
            break

        current_history_id = r['id']
        op_code, op_body = r['op']
        assert op_code == 0 # ensure this is a transfer operation
        assert len(op_body['extensions']) == 0 # ensure no extensions in transfer op, to avoid vesting transfer

        # fetch a bunch of objects in one call
        from_, to, asset = instance.rpc.get_objects([op_body['from'], op_body['to'], op_body['amount']['asset_id']])

        print('Got transfer from {} to {}, asset {}, amount {}'.format(
                from_['name'], to['name'], asset['symbol'], int(op_body['amount']['amount']) / 10 ** asset['precision']
            ))

    time.sleep(3)
