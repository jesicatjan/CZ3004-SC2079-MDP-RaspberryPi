# # STM32 Commands - Send straight to STM32
# stm32_prefixes = ("FS", "BS", "FW", "BW", "FL", "FR", "BL",
#                   "BR", "TL", "TR", "A", "C", "DT", "STOP", "ZZ", "RS")

def formatToSTM(command):

    cmd_type = command[:2]
    value = command[2:]

    if cmd_type == "FW":  # Forward
        return f"f {value},"
    elif cmd_type == "BW":  # Backward
        return f"b {value},"
    elif cmd_type == "FR":  # Forward Right
        return f"fr 90,"
    elif cmd_type == "FL":  # Forward Left
        return f"fl 90,"
    elif cmd_type == "BR":  # Backward Right
        return f"br 90,"
    elif cmd_type == "BL":  # Backward Left
        return f"bl 90,"
    else:
        return command

formatted_result = formatToSTM("un")
print(formatted_result)

json_data = {
  "data": {
    "commands": [
      "FW90",
      "FW70",
      "BR00",
      "BW50",
      "BR00",
      "FW10",
      "SNAP1_C",
      "BW10",
      "FL00",
      "FW10",
      "FR00",
      "FW30",
      "FR00",
      "SNAP5_R",
      "FW10",
      "FL00",
      "FW20",
      "FL00",
      "SNAP2_C",
      "BW30",
      "FL00",
      "FW40",
      "SNAP7_L",
      "FIN"
    ],
    "distance": 241.0,
    "path": [
      {
        "d": 0,
        "s": -1,
        "x": 1,
        "y": 1
      },
      {
        "d": 0,
        "s": -1,
        "x": 1,
        "y": 10
      },
      {
        "d": 0,
        "s": -1,
        "x": 1,
        "y": 17
      },
      {
        "d": 6,
        "s": -1,
        "x": 2,
        "y": 14
      },
      {
        "d": 6,
        "s": -1,
        "x": 7,
        "y": 14
      },
      {
        "d": 4,
        "s": -1,
        "x": 10,
        "y": 15
      },
      {
        "d": 4,
        "s": 1,
        "x": 10,
        "y": 14
      },
      {
        "d": 4,
        "s": -1,
        "x": 10,
        "y": 15
      },
      {
        "d": 2,
        "s": -1,
        "x": 13,
        "y": 14
      },
      {
        "d": 2,
        "s": -1,
        "x": 14,
        "y": 14
      },
      {
        "d": 4,
        "s": -1,
        "x": 15,
        "y": 11
      },
      {
        "d": 4,
        "s": -1,
        "x": 15,
        "y": 8
      },
      {
        "d": 6,
        "s": 5,
        "x": 12,
        "y": 7
      },
      {
        "d": 6,
        "s": -1,
        "x": 11,
        "y": 7
      },
      {
        "d": 4,
        "s": -1,
        "x": 10,
        "y": 4
      },
      {
        "d": 4,
        "s": -1,
        "x": 10,
        "y": 2
      },
      {
        "d": 2,
        "s": 2,
        "x": 13,
        "y": 1
      },
      {
        "d": 2,
        "s": -1,
        "x": 10,
        "y": 1
      },
      {
        "d": 0,
        "s": -1,
        "x": 11,
        "y": 4
      },
      {
        "d": 0,
        "s": 7,
        "x": 11,
        "y": 8
      }
    ]
  },
  "error": None
}
