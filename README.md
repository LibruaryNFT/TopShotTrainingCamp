# TopShot Nexus!

This repo is meant as a way to share important utilities, contracts, and tools for the NBA TopShot community. It is a work in progress and will be updated as new tools are developed. This is an open-source project, feel free to contribute or open issues for any suggestions or improvements.

Currently the repo contains the following projects:

- **TopShot Emulator**
  - Designed to help anyone with deploying TopShot locally and ready to mint moments. It includes the same sets and play data as found on TopShot.

- **TopShot Tiers** 
  - Designed to help find the tier and badges of NBA Top Shot moments on-chain.
  - Status: In-progress

- **TopShot Badges**
  - Designed to help find the badges of NBA Top Shot moments on-chain.
  - Status: In-progress

- **TopShot Links**
   - An aggregated list of helpful resources.

## TopShot Emulator Setup
This setup will get you started with the TopShot emulator and ready to mint moments.
### [TopShot Emulator Commands Reference](./EMULATOR.md)

1. Start the emulator
```bash
flow-c1 emulator start
```

2. Run the setup-flow.ps1 script. This will deploy contracts, setup a second emulator account(0x179b6b1cb6755e31) with a TopShot collection and create the sets.
```bash
./setup-flow.ps1
```

3. Create the plays. There are two options, Verbose or Minimal Mode. You can either create plays that do not have metadata or create plays with the exact metadata from Top Shot. Depends on your use case and creating all the metadata takes about 20 minutes compared to 4 minutes for the minimal metadata.

Create a python virtual environment
```bash
python -m venv venv
```

Activate the Virtual environment

```bash
.\venv\Scripts\activate
```

Option 1: Verbose Mode: Same Play Metadata as TopShot 

```bash
python ./topshot/tools/create_plays.py
```

Option 2: Minimal Mode: Empty Play Metadata

```bash
python ./topshot/tools/create_plays_minimal.py
```

Add plays to sets. This is the exact mapping found on TopShot. Takes about 5 minutes. The script to generate the json that is used(play_metadata.json) is found in /topshot/tools/fetch_plays.py.
  
```bash
python ./topshot/tools/add_plays_to_sets.py
```
## TopShot Tiers

### Status

Under review/testing. Will deploy to mainnet soon.

### [Tiers Commands Reference](./TIERS.md)

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

#### get_all_badges
- **Description**: Retrieves all badges associated with a specified account.
- **Input Parameters**:
  - `account: Address` - The Flow account address to query (e.g., `0xf8d6e0586b0a20c7`).
- **Example Usage**:

```bash
  flow-c1 scripts execute ./badges/scripts/get_all_badges.cdc 0xf8d6e0586b0a20c7
```

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


