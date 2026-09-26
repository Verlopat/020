# Deployment

The repository provides local simulation and contract tests without paid services. For a real EVM testnet, configure an RPC endpoint, deployer key, OpenZeppelin dependencies, and Chainlink VRF coordinator/subscription parameters locally.

After deployment, record contract addresses, transaction hashes, gas used, VRF request IDs/responses and allocation outputs in the experiment metadata. Never commit private keys or fabricate deployment records.

The testnet deployment requirement is therefore implemented as reproducible tooling/documentation; an actual network deployment requires a funded wallet and network credentials supplied by the operator.
