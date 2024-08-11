import json
import subprocess

# Load the set-play mapping from JSON file
with open('set_play_mapping.json', 'r', encoding='utf-8') as f:
    set_play_mapping = json.load(f)

# Iterate over the set-play mapping and execute transactions to add each play to its set
for set_id, play_ids in set_play_mapping.items():
    for play_id in play_ids:
        # Prepare arguments for the transaction
        args_json = json.dumps([
            {"type": "UInt32", "value": str(set_id)},
            {"type": "UInt32", "value": str(play_id)}
        ])

        # Execute the Flow transaction
        result = subprocess.run([
            'flow-c1', 'transactions', 'send', './topshot/transactions/add_play_to_set.cdc',
            '--args-json', args_json,
            '--network', 'emulator'  # Replace 'emulator' with 'mainnet' or 'testnet' as appropriate
        ], capture_output=True, text=True)

        # Print the transaction result
        print(f"Adding play {play_id} to set {set_id}")
        print("Transaction Output:\n", result.stdout)
        print("Transaction Errors:\n", result.stderr)
