# initialPositions = "OBS,1,5,4,NORTH|OBS,2,5,4,NORTH|OBS,3,5,4,NORTH|OBS,4,5,4,NORTH|OBS,5,5,4,NORTH"

"""
{
"cat": "obstacles",
"value": {
    "obstacles": [{"x": 5, "y": 10, "id": 1, "d": 2}],
    "mode": "0"
}
}
"""

def formatToAlgo(initialPositions):
    obstacles = []
    lines = initialPositions.split("|")
    
    for line in lines:
        if line.startswith("OBS"):
            parts = line.split(",")
            if len(parts) == 5:  # Make sure we have all the components
                obstacle_id = int(parts[1])
                x = int(parts[2])
                y = int(parts[3])
                direction = parts[4]

                # Map directions to integers as per requirements
                direction_mapping = {"NORTH": 0, "EAST": 2, "SOUTH": 4, "WEST": 6}
                d = direction_mapping.get(direction, 0)  # Default to NORTH if not found
                
                # Assuming we modify x and y as well to match the new format
                obstacles.append({
                    "x": x,      # or map to new coordinates here if needed
                    "y": y,      # same as above, or directly modify if the input requires it
                    "id": obstacle_id,
                    "d": d       # mapped direction
                })
    
    # Return the new JSON format
    formatted_algo = {
        "cat": "obstacles",
        "value": {
            "obstacles": obstacles,
            "mode": "0"
        }
    }

    return formatted_algo

# # Example usage:

# message = "OBS,1,5,4,NORTH|OBS,2,5,4,NORTH|OBS,3,5,4,NORTH|OBS,4,5,4,NORTH|OBS,5,5,4,NORTH"
# formatted_result = formatToAlgo(message)
# print(formatted_result)
