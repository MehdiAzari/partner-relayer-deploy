Aurora Relayer & Near Core on mainnet
=====================================
Source repo: https://github.com/aurora-is-near/partner-relayer-deploy
Requirements: docker, docker-compose, curl. x64-64 architecture.
This project is customized for Valoura 
At this stage we are not using Nginx for load balancing endpoints thus the docker compose file is would not start web server container. 

the setup script is customized to copy the generated configs. After generating configs the script will run a container which downloads and syncs block data from S3 buckets to mounted path (`./near/data/`)

After downloading the script will 

  1. Run `$ ./setup.sh`. Wait until it finishes with "Setup Complete". This can take hours due to the volume of data to download.
  2. Enjoy
  # Config

### Near Wallet
  in order to create relayer.json config file which provides access to NEAR account we use near CLI to login and generate file.
  `$ near login` (consider bypassing sanctions)
then copy the file to `config` directory as relayer.json

### Light mode
open the `./near/config.json` change `"tracked_shards": [0]` to empty array  -> `"tracked_shards": []`
  
# Changes
```
	modified:   README.md
	modified:   contrib/docker-compose.yaml-testnet
	modified:   contrib/docker/config.json
	modified:   contrib/nginx/testnet/endpoint.conf
	modified:   contrib/setup.sh
	modified:   contrib/start.sh

```
# Testing
use `while true; do python3 monitor.py ; sleep 1;done` use this to compare last block from your endpoint to public endpoint.
 
Testnet
=======

Run `$ ./setup.sh testnet` to install a testnet instead of mainnet release.

Starting & Stopping
===================

When running `./setup.sh` you should end up with a running node that is catching up with the network.
You can always stop and start the node by executing the `./stop.sh` or `./start.sh` command.


Write transactions & custom signers
===================================

The default installation does not support write transactions. Instead it disables writing and sets up a placeholder key.

To enable write transactions, you need to:

  - Create an account on testnet/mainnet and load some NEAR on it.
  - Export the account's keypair and name into config/relayer.json (check the original file for format).
  - Change the `signer` entry in the config/testnet.yaml or config/mainnet.yaml to the account's name.
  - Set writable:true in config/testnet.yaml or config/mainnet.yaml.
  - Restart the endpoint container.

Updates
=======

The software in this installation is updated automatically. Whenever Aurora releases a new image, it will be
downloaded, and the component restarted.

This is however not true for the included database and chain files. These are only downloaded initially when
running `./setup.sh`. Keep your node running to prevent going out of sync.


Good to know
============

  - You can change the setup of the nginx reverse proxy by editing the contrib/nginx/<network>/endpoint.conf files. Restart the node afterwards.
  - You can prevent listening on the public IP by modifying the docker-compose.yaml file. See embedded comments.


Changes
=======

v2.0

  - Change naming scheme for docker images to make reuse easier.
  - Add scaling of endpoints for better performance.
  - Add reverse proxy for easier deployment and more stable operations.
  - Add automatic update functionality.

