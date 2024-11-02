
# Discord Bot - CODM Map Helper

This Discord bot, written using `discord.py`, provides functionalities like clearing messages, nuking a channel, ghost pinging, spamming messages, and providing Call of Duty Mobile (CODM) map intel based on the given map and game mode.

## Features

- **Moderation Commands**: Clear messages and nuke channels with admin permissions. 
- **Fun Commands**: Ghostping or spam messages with configurable limits. 
- **CODM Map Intel**: Get detailed intel about CODM maps with satellite imagery for different game modes like Domination, Hardpoint, and Search and Destroy (SnD).

## Requirements

- Python 3.8+
- `discord.py` library
- An active Discord bot token
- `keep_alive` script (hosted to keep your bot online, e.g., on Replit)

## Installation

1. Clone this repository or download the bot's code.
2. Install dependencies:
   ```bash
   pip install discord.py
   ```
3. Set up your bot's token in your environment:
   ```bash
   export SECRET_KEY='your-bot-token'
   ```
4. (Optional) Add a keep-alive script if you need your bot to stay online, e.g., if hosted on Replit or other hosting platforms.

## Commands

### General Commands

- **`Boi clear <amount>`**: Deletes the specified number of messages in a channel.
  - Requires `manage_messages` permission.
  - Example: `Boi clear 10`

- **`Boi nuke_channel`**: Deletes all messages in the channel (limit of 9999999).
  - Requires `manage_messages` permission.
  - Example: `Boi nuke_channel`

### Fun Commands

- **`Boi ghostping <user> <amount>`**: Sends ghost pings to the specified user (up to 10 times).
  - User cannot be `@LoneWolF#7895`.
  - Example: `Boi ghostping @User 5`

- **`Boi spam <message> <amount>`**: Spams a message a certain number of times (up to 10).
  - Example: `Boi spam Hello 5`

### CODM Map Commands

Use the `Boi codmap` command followed by the map name and game mode to get satellite intel on CODM maps. Supported maps and modes include:

- **Maps**: FiringRange, Summit, Nuketown, Crossfire, Raid, Standoff, Crash, Meltdown, Rust, Scrapyard, Takeoff, HeckneyYard, Highrise, Terminal, Cage, Hijacked, Killhouse 
- **Modes**: Domination, Hardpoint, SnD (Search and Destroy)

- **Command Format**: 
  ```bash
  Boi codmap <map_name> <mode>
  ```

  - Example: `Boi codmap FiringRange domination`

If no map or mode is specified, general instructions are provided.

### Example CODM Map Intel

The bot provides embedded images and descriptions of the map:
  
- **`Boi codmap Nuketown domination`**: Provides the map's satellite scan for Nuketown in Domination mode.

### Error Handling

- **Missing Arguments**: If a command is missing required arguments, the bot will notify the user and prompt them to use the help command.
  
- **Command Not Found**: If a user types an invalid command, the bot will notify that the command doesn't exist.

## Hosting

1. Add your bot token to the environment variable `SECRET_KEY`.
2. Use a service like [Replit](https://replit.com/) or a server to keep the bot running.
3. Start the bot:
   ```bash
   python BoiCode.py
   ```


Feel free to customize the bot or extend its functionality!

