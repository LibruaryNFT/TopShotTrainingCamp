# TopShot Nexus

This repo is meant as a way to share important utilities, contracts, and tools for the NBA TopShot community. It is a work in progress and will be updated as new tools are developed.

Currently the repo contains the following projects:
- TopShot Emulator - Designed to help anyone with deploying TopShot locally.
- TopShot Tiers(in-progress) - Designed to help find the tier and badges of NBA Top Shot moments on-chain.
- TopShot Badges(in-progress) - Designed to help find the badges of NBA Top Shot moments on-chain.
- TopShot Links - An aggregated list of helpful resources.

## TopShot Emulator Setup

1. Start the emulator
- flow-c1 emulator start

2. Run the setup-flow.ps1 script. This will deploy contracts, setup a second emulator account(0x179b6b1cb6755e31) with a TopShot collection and create the sets.

- ./setup-flow.ps1

3. Create the plays. There are two modes, you can either create plays that do not have metadata or create plays with the exact metadata from Top Shot. Depends on your use case and creating all the metadata takes about 20 minutes compared to 4 minutes for the minimal metadata.

 - .\venv\Scripts\activate

- python ./topshot/tools/create_plays.py    

- python ./topshot/tools/create_plays_minimal.py 

4. Add plays to sets. Takes about 5 minutes.

- python ./topshot/tools/add_plays_to_sets.py

## TopShot Emulator Commands

### Minting

mint_moment(setID: UInt32, playID: UInt32, recipientAddr: Address)

-flow-c1 transactions send ./topshot/transactions/mint_moment.cdc 1 1 0xf8d6e0586b0a20c7

mint_moments(setID: UInt32, playID: UInt32, quantity: UInt64, recipientAddr: Address)

- flow-c1 transactions send ./topshot/transactions/mint_moments.cdc 1 1 5 0xf8d6e0586b0a20c7

### Transfer

transfer_moment (recipientAddr: Address, momentID: UInt32)
 - flow-c1 transactions send .\topshot\transactions\transfer_moment.cdc 0x179b6b1cb6755e31 1

### Verification

get_collection_ids (account: Address)
 flow-c1 scripts execute .\topshot\scripts\get_collection_ids.cdc 0x179b6b1cb6755e31 

## TopShot Tiers

### Status

Under review/testing. Will deploy to mainnet soon.

### Commands

get_tier (account, momentID)

- flow-c1 scripts execute ./tiers/scripts/get_tier.cdc 0xf8d6e0586b0a20c7 1

(Admin) update_default_tier (setID: UInt32, tierRawValue: UInt8)

- flow-c1 transactions send ./tiers/transactions/update_default_tier.cdc 1 2

(Admin) update_mixed_tier (setID: UInt32, playID: UInt32, tierRawValue: UInt8)

- flow-c1 transactions send ./tiers/transactions/update_mixed_tier.cdc

(Admin) remove_playid.cdc (setID: UInt32, playID: UInt32)

- flow-c1 transactions send ./tiers/transactions/remove_playid.cdc 1 245

  ### [Tiers Reference](./TIERS.md)

## TopShot Badges

### Status

The following are implemented:

- Rookie Mint
- Rookie of the Year
- MVP Year
- Rookie Year
- Championship Year

The following are in-progress:

- Rookie Premiere
- Top Shot Debut
- Challenge Reward
- Crafting Challenge Reward
- Leaderboard Reward

### Commands

get_all_badges (account)
- flow-c1 scripts execute ./badges/scripts/get_all_badges.cdc 0xf8d6e0586b0a20c7



## TopShot Links

**Repos**

- [Dapper Labs NBA Smart Contracts](https://github.com/dapperlabs/nba-smart-contracts)
- [TopShot Explorer by rrrkren](https://github.com/rrrkren/topshot-explorer)

**Tools**

- [Current TopShot Wallet](https://flow-view-source.com/mainnet/account/0x0b2a3299cc857e29/contract/TopShot)
  - [Media Gateway Documentation](https://developers.nbatopshot.com/docs/Media%20Gateway/index.html)

## Flow Community

**Repos**

- [Emerald DAO](https://github.com/emerald-dao)

**Tools**

- [Flow Developer Documentation](https://developers.flow.com/)
- [Flow NFT Catalog](https://www.flow-nft-catalog.com/)
- [Graffle](https://www.graffle.io/)
- [ECDAO Documentation](https://docs.ecdao.org/)
- [ECDAO Links](https://link.ecdao.org/)
- [Dapper Labs Developer Portal](https://developers.dapperlabs.com/)

**Migration to Cadence 1.0**

- [Migration ChatGPT Bot](https://chatgpt.com/g/g-lt4a6jvfj-flow-cadence-1-0-migration-helper)
- [Contract Browser](https://contractbrowser.com/)
- [Cadence Migration Guide](https://cadence-lang.org/docs/cadence-migration-guide)
- [Previewnet Deployment](https://previewnet.flowdiver.io/account/0x31c25c145e66dbe9) - Dapper team's most recent deployment to Previewnet for C1
- [Previewnet NFT Contract](https://previewnet.flowdiver.io/contract/A.002bb351357cf238.NonFungibleToken?tab=deployments) - Most recent NFT contract on Previewnet
- [NBA-2865-upgrade-flow-sdk branch](https://github.com/dapperlabs/nba-smart-contracts/tree/judez/NBA-2865-upgrade-flow-sdk/transactions/admin)
  They are actively updating the content for C1. You can dig through some of the branches for the latest C1 code.

## Flow Ecosystem Analytics

- [FlowDiver Analytics](https://www.flowdiver.io/analytics?interval=1Y)
- [FindLabs API](https://findonflow.github.io/findlabs-api/)
- FindLabs is working on a new API, but the historical API 1.1.0 should work:
- [Flipside Crypto Flow Models](https://flipsidecrypto.github.io/flow-models/#!/overview/flow_models)

## Tokenomics

- [FLOW Token Distribution](https://flow.com/token-distribution)


