# TopShot Training Camp

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

## TopShot Emulator Setup

This guide will help you set up the TopShot emulator, allowing you to start minting moments quickly.

You can choose from three setup options, depending on your needs and the level of detail you require:

- Express Setup: A quick start with only 18 plays and 1 set. This setup takes just a minute to complete, providing the fastest way to get started with the TopShot emulator.
- Basic Setup: A more detailed setup with 5511 empty plays data and 160 sets data. This setup is a closer representation of the Mainnet TopShot contract and takes about 4 minutes to complete.
- Full Setup: The most comprehensive setup, including 5511 full plays data and 160 full sets data. This setup is the most accurate representation of the Mainnet TopShot contract and takes around 15 minutes to complete.

### [TopShot Emulator Commands Reference](./EMULATOR.md)

After completing your setup, refer to the **TopShot Emulator Commands Reference** for detailed instructions on how to mint moments, transfer them, and execute other commands using the emulator. This document will guide you through all the necessary commands to manage and interact with your TopShot moments effectively.

### Python Setup

If you are running the Basic or Full Setup, you will need a Python Virtual Environment

Create a python virtual environment

```bash
python -m venv venv
```

Activate the Virtual environment

```bash
.\venv\Scripts\activate
```

### Express Setup

```bash

flow-c1 emulator start
./setup-flow.ps1
flow-c1 transactions send ./topshot/transactions/create_custom_plays.cdc
flow-c1 transactions send ./topshot/transactions/add_plays_to_sets.cdc 1 [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

flow-c1 transactions send ./topshot/transactions/mint_moments.cdc 1 1 5 0xf8d6e0586b0a20c7
flow-c1 transactions send .\topshot\transactions\transfer_moment.cdc 0x179b6b1cb6755e31 1
flow-c1 transactions send .\topshot\transactions\verify_entitlements.cdc 0x179b6b1cb6755e31
flow-c1 scripts execute .\topshot\scripts\verify_collection.cdc 0x179b6b1cb6755e31
```

### Basic Setup

```bash
flow-c1 emulator start
./setup-flow.ps1
python ./topshot/tools/create_plays_minimal.py
python ./topshot/tools/add_plays_to_sets.py
```

### Full Setup

```bash
flow-c1 emulator start
./setup-flow.ps1
python ./topshot/tools/create_plays.py
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
