# Samson Discord Bot

## Description
Samson is a versatile Discord bot designed to enhance your server with a variety of fun and administrative features. Whether you want to roll some dice, play music, or manage idle members, Samson has you covered.

## Features
- **Fun Commands**: Dice rolling, rating things, and more.
- **Music Playback**: Play, pause, resume, and stop music directly in your voice channels.
- **Idle Check**: Identify inactive members who haven't posted in a while.
- **Admin Tools**: Includes a killswitch for safe bot shutdown.

## Getting Started

### Prerequisites
- Python 3.8+
- `discord.py` library (v2.0 or later)
- Other dependencies listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/samson-discord-bot.git
   cd samson-discord-bot

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

### Configuration
1. Rename `data/config.example.json` to `config.json` and add your bot token and other configuration details:
```json
{
    "token": "YOUR_BOT_TOKEN_HERE",
    "prefix": "!",
    "admin_roles": ["Server Admin"]
}
```
2. Customize the configuration as needed.

### Running the Bot
1. Run the bot locally:
```bash
python main.py
```
2. The bot should now be online and responding to commands in your Discord server!

## Commands
Here are some of the key commands Samson supports:

- Fun Commands:
    - `!roll 2d6+3`: Roll a dice using standard dice notation.
    - `!rate [thing]`: Samson rates the thing out of 10.

- Music Commands:
    - `!play [song_url]`: Play music from a URL.
    - `!pause`: Pause the currently playing music.
    - `!resume`: Resume paused music.
    - `!stop`: Stop the music and disconnect.

- Admin Commands:
    - `!kill`: Shut down the bot safely (requires admin role).
    - `!idle`: Check which members have been inactive. (Recommended to only use in small servers.)

## Folder Structure
```
samson_2.0/
│
├── cogs/                    # Command modules
│   ├── dice_roll.py         # Dice roll command
│   ├── idle_check.py        # Idle check command
│   ├── kill_command.py      # Kill command
│   ├── music_commands.py    # Music commands
│   ├── rating.py            # Rating command
│   └── voice_commands.py    # Voice commands
│
├── utils/                   # Utility scripts
├── config.json              # Configuration
├── keep_alive.py            # Keep the bot alive script
├── LICENCE                  # Licence file
├── main.py                  # Main bot script
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .gitignore               # Git ignore file
```

## Contributing
At this time, contributions are not being accepted. This repository is intended for educational and personal use only. Please feel free to fork the project for your own purposes.

## Licence
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact Information
If you have any questions or suggestions, feel free to reach out:
- GitHub: Axiomaa
- Email: axiomatechlab@gmail.com
