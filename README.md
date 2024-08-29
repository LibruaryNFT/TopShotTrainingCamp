# TopShot Training Camp

## Drill 1: Setting up Development Environment for Cadence

### Step 1: Install Flow CLI ▲

The Flow CLI is a command-line tool that lets you interact with the Flow blockchain, including running the emulator, submitting transactions, and more. The installation process varies slightly depending on your operating system.

macOS
Open the Terminal application (you can find it in Applications > Utilities). Run the following command to install the Flow CLI using Homebrew. Make sure you have Homebrew installed.

$ brew install flow-cli
Linux
Open your terminal and run the following command. This script will download and install the appropriate binary for your system.

sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"
Windows
Open PowerShell as an Administrator (right-click on PowerShell and select "Run as administrator"). Then, run the following command to install the Flow CLI:

iex "& { $(irm 'https://raw.githubusercontent.com/onflow/flow-cli/master/install.ps1') }"

### Step 2: Install Python ▲

Python is often used in blockchain development for scripting, automation, and data analysis. The installation process varies by operating system.

macOS
Python 3 comes pre-installed on macOS. You can verify this by opening the Terminal application (Applications > Utilities) and typing:

$ python3 --version
If Python is not installed, you can install it using Homebrew:

$ brew install python
Linux
Most Linux distributions come with Python pre-installed. You can check the version by opening your terminal and typing:

$ python3 --version
If Python is not installed, you can install it using your package manager. For example, on Ubuntu:

$ sudo apt-get install python3
Windows
Download the latest version of Python from the official Python website. During installation, make sure to check the box that says "Add Python to PATH" to ensure Python can be accessed from the command line.

After installation, open Command Prompt (you can search for "cmd" in the Start menu), and type:

python --version
If the version number is displayed, Python is installed correctly. If not, you may need to restart your computer for the changes to take effect.

### Step 3: Install Git ▲

Git is a version control system that lets you manage and keep track of your source code history.

macOS
Git can be installed using Homebrew. Open Terminal (Applications > Utilities) and run:

$ brew install git
Alternatively, you can install Git by downloading it from the official Git website.

Linux
Most Linux distributions include Git by default. You can verify its installation by typing:

$ git --version
If Git is not installed, you can install it using your package manager. For example, on Ubuntu:

$ sudo apt-get install git
Windows
Download Git from the official Git website. Run the installer and follow the prompts. During installation, make sure the option "Git from the command line and also from 3rd-party software" is selected.

After installation, open Command Prompt (search for "cmd" in the Start menu), and type:

git --version
If the version number is displayed, Git is installed correctly.

### Step 4: Choose an IDE (Visual Studio Code Recommended) ▲

An Integrated Development Environment (IDE) is a software application that provides comprehensive tools for software development. While there are many IDEs to choose from, we recommend using Visual Studio Code (VS Code) because it offers a powerful extension specifically designed for Cadence, the resource-oriented smart contract programming language of Flow.

Why VS Code?

Cadence VS Code Extension: This extension integrates Cadence into VS Code, providing features like syntax highlighting, type checking, code completion, and more.
Language Server Support: The extension includes a language server that offers advanced features such as diagnostics, code completion, and debugging for Cadence smart contracts.
Seamless Integration: The Cadence extension helps you install and manage dependencies like the Flow CLI, making it easier to set up and develop on the Flow blockchain.
Here are links to download some of the popular IDEs:

Visual Studio Code (VS Code)
IntelliJ IDEA
WebStorm

### Step 5: Install the Cadence Extension (For Visual Studio Code) ▲

If you're using Visual Studio Code, you can install the Cadence extension to get features like syntax highlighting, code completion, and debugging for Cadence smart contracts.

To install the Cadence extension through the Visual Studio Code UI:

Open Visual Studio Code.
Click on the Extensions view icon on the Sidebar (or press Ctrl+Shift+X).
In the search box at the top, type "Cadence".
Find the Cadence extension in the list and click "Install".
Once installed, the extension will guide you through installing any additional dependencies, like the Flow CLI, if they aren't already set up.

## Drill 2: Deploying Locally

### Step 1: Clone the Repository

First, clone the repository to your local machine:

$ git clone https://github.com/LibruaryNFT/TopShotTrainingCamp.git

### Step 2: Run the Setup Script

Depending on your operating system, follow the appropriate instructions below:

Windows
Navigate to the root directory and run the provided PowerShell script to set up your environment. This script will handle the deployment and account setup automatically:

$ ./setup-flow.ps1
This script performs the following actions:

Deploys the project using flow-c1 project deploy.
Generates keys and saves the private key to a file.
Creates a new account with the generated public key.
Sends transactions to set up and verify collections.
Funds the emulator accounts and verifies their balances.
Sends transactions to create sets.
macOS/Linux
For macOS or Linux users, manually execute the commands found in the setup-flow.ps1 script using your terminal. This includes deploying the project, generating keys, creating accounts, and sending transactions.

### Step 3: Python Setup

If you are running the Basic or Full Setup, you will need a Python Virtual Environment.

python -m venv venv
Activate the Virtual environment:

.\venv\Scripts\activate
Step 4: Choose Your Setup Option
You can choose from three setup options, depending on your needs and the level of detail you require:

Express Setup
A quick start with only 18 plays and 1 set. This setup takes just a minute to complete, providing the fastest way to get started with the TopShot emulator.

flow-c1 emulator start
./setup-flow.ps1
flow-c1 transactions send ./topshot/transactions/create_custom_plays.cdc
flow-c1 transactions send ./topshot/transactions/add_plays_to_sets.cdc 1 [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
Basic Setup
A more detailed setup with 5511 empty plays data and 160 sets data. This setup is a closer representation of the Mainnet TopShot contract and takes about 4 minutes to complete.

flow-c1 emulator start
./setup-flow.ps1
python ./topshot/tools/create_plays_minimal.py
python ./topshot/tools/add_plays_to_sets.py
Full Setup
The most comprehensive setup, including 5511 full plays data and 160 full sets data. This setup is the most accurate representation of the Mainnet TopShot contract and takes around 15 minutes to complete.

flow-c1 emulator start
./setup-flow.ps1
python ./topshot/tools/create_plays.py
python ./topshot/tools/add_plays_to_sets.py
Step 5: Verify the Setup
After completing the setup, verify that everything has been configured correctly:

Check the output of each command to ensure there are no errors.
Ensure that the emulator accounts have been funded and check their balances using the provided scripts.
If any issues arise, refer to the setup logs or consult the repository documentation for troubleshooting steps.

## Drill 3: Minting Locally

### Step 1: Mint an NFT

Use the following script to mint an NFT:

flow transactions send ./transactions/mint_nft.cdc

### Step 2: Mint and Transfer Moments

Mint a moment using the following command:

flow-c1 transactions send ./topshot/transactions/mint_moments.cdc 1 1 5 0xf8d6e0586b0a20c7
In this command:
1: Set ID
1: Play ID
5: Quantity of moments to mint
0xf8d6e0586b0a20c7: Recipient address

Transfer a moment to another account using the following command:

flow-c1 transactions send .\topshot\transactions\transfer_moment.cdc 0x179b6b1cb6755e31 1
In this command:
0x179b6b1cb6755e31: Recipient address
1: NFT ID to transfer

### [TopShot Emulator Commands Reference](./EMULATOR.md)

After completing your setup, refer to the **TopShot Emulator Commands Reference** for detailed instructions on how to mint moments, transfer them, and execute other commands using the emulator. This document will guide you through all the necessary commands to manage and interact with your TopShot moments effectively.
