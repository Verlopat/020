# Testnet deployment

Deployment is intentionally parameterized. Do not commit private keys or pretend that a contract was deployed.

Install Foundry and the Chainlink contracts dependency, configure the target network RPC/private key locally, then deploy the contracts with the network-specific coordinator, subscription and key hash.

Record the resulting contract addresses, transaction hashes, gas used, and VRF request/response IDs in the experiment output. The Python pipeline remains fully runnable without a blockchain.
