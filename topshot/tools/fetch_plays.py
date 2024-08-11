import subprocess
import json
import re

# Function to clean up invalid Unicode escape sequences in the JSON string
def clean_json_string(json_str):
    # Remove invalid Unicode sequences (e.g., \u{XXXX}) and replace with a placeholder
    json_str = re.sub(r'\\u\{[0-9a-fA-F]+\}', '', json_str)
    return json_str

# Function to run the Flow script and retrieve the metadata for a single playID
def get_play_metadata(playID):
    # Execute the Flow CLI command
    result = subprocess.run([
        'flow-c1', 'scripts', 'execute', './topshot/scripts/get_play_metadata.cdc', 
        '--args-json', f'[{{"type": "UInt32", "value": "{playID}"}}]',
        '--network', 'mainnet'
    ], capture_output=True, text=True)

    # Check for errors in execution
    if result.returncode != 0:
        print(f"Error executing the Flow script for playID {playID}")
        print("Raw output:\n", result.stdout)
        return None

    # Extract the JSON from the output
    try:
        # Remove "Result:" prefix and clean the JSON string
        output_str = result.stdout.strip()
        json_str = output_str.replace("Result: ", "").strip()
        cleaned_json_str = clean_json_string(json_str)
        
        # Parse the cleaned JSON string
        output = json.loads(cleaned_json_str)
        return output
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON for playID {playID}: {str(e)}")
        print("Raw output:\n", result.stdout)
        return None

# Define the range of playIDs to retrieve
start_id = 1
end_id = 5511

# Retrieve metadata for each playID and store it in a dictionary
all_metadata = {}
for play_id in range(start_id, end_id + 1):
    metadata = get_play_metadata(play_id)
    if metadata:
        all_metadata[play_id] = metadata

# Save to a file
with open('play_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(all_metadata, f, ensure_ascii=False, indent=2)

print("Metadata has been saved to play_metadata.json")
