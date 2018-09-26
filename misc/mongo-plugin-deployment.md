
# Prepare
## Mongodb install and start
### ubuntu
```
sudo apt-get install mongo
sudo service mongod start
```
### macOS
```
brew install mongo
```

## Download cybex bitshares-core and build
This step can be left out if you have a compiled binary.
Better to use a debug version.

### Fetch source code
```
git clone https://github.com/NebulaCybexDEX/bitshares-core.git

```
### Build
Please follow https://github.com/NebulaCybexDEX/cybex-node-doc/blob/master/misc/how2build.md to install mongo-related dependencies.

# Run Mongo plugin


```
cd <witness_node directory>
```
start delayed node:
```
./witness_node -d data/ --plugins mongodb delayed_node --trusted-node <another witness node> --genesis-json genesis.json --max-ops-per-account 500 -m mongodb://<user>:<password>@127.0.0.1:27017/<table>  --mongodb-block-start <start blk num, general set is 1>  > witness_node.log 2>&1 &
```
for example:
```
./witness_node -d data/ --plugins mongodb delayed_node --trusted-node 47.100.231.66 --genesis-json genesis.json --max-ops-per-account 500 -m mongodb://sunqi:sunqi123@127.0.0.1:27017/cybex --resync-blockchain --replay-blockchain --mongodb-wipe > witness_node.log 2>&1

./witness_node -d data/ --plugins mongodb delayed_node --trusted-node 47.100.231.66 --genesis-json genesis.json --max-ops-per-account 500 -m mongodb://cybex:Jsh64mcy1H9a@127.0.0.1:27017/cybex  --mongodb-block-start 5504357> witness_node.log 2>&1 &
```


# check
less witness_node.log and those logs under p2p

