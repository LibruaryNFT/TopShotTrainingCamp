# TopShot Nexus

This repo is meant as a way to share important utilities, contracts, and tools for the NBA TopShot community. It is a work in progress and will be updated as new tools are developed.

Currently the repo contains the following projects:
- TopShot Tiers - Designed to help find the tier and badges of NBA Top Shot moments on-chain.
- TopShot Badges - Designed to help find the badges of NBA Top Shot moments on-chain.
- TopShot Emulator - Designed to help anyone with deploying TopShot locally.
- TopShot Links - An aggregated list of helpful resources.

## TopShot Tiers

### Status

Under review/testing. Will deploy to mainnet soon.

### Commands

get_tier (account, momentID)

- flow-c1 scripts execute ./tiers/scripts/getTier.cdc 0xf8d6e0586b0a20c7 1

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

## TopShot Emulator

1. Deploy TopShotLocking, TopShot, TopShotTiers, TopShotBadges

JSON looks like this:

"emulator-account": [
"TopShotLocking",
"TopShot",
"TopShotTiers",
"TopShotBadges"
]

- flow-c1 project deploy

2. (Optional) Setup second emulator user

- flow-c1 accounts create

- flow transactions send .\topshot\transactions\setupCollection.cdc --signer=justin

3. create_set (string)
  - flow-c1 transactions send ./topshot/transactions/create_set.cdc "First Set!"

4. create_plays (metadata found inside transaction)
  - flow-c1 transactions send ./topshot/transactions/create_plays.cdc

5. mint_moment(setID: UInt32, playID: UInt32, recipientAddr: Address)

-flow-c1 transactions send ./topshot/transactions/mint_moment.cdc 1 1 0xf8d6e0586b0a20c7

or mint_moments(setID: UInt32, playID: UInt32, recipientAddr: Address)

- flow-c1 transactions send ./topshot/transactions/mint_moments.cdc 1 1 5 0xf8d6e0586b0a20c7

5. send_moments (recipientAddr: Address, momentIDs: [UInt32])
 - flow transactions send .\topshot\transactions\send_moments.cdc 0x01cf0e2f2f715450 [1,2,3,4,5]

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
