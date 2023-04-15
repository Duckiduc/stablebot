# Discord Stable Diffusion Bot

This is a Discord bot that generates images using the Stable Diffusion Pipeline. The bot takes a prompt and generates an image based on the prompt using the Stable Diffusion Pipeline. The generated image is then sent back to the Discord chat.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- PyTorch 1.6 or higher
- Discord.py
- Diffusers
- dotenv

### Installation

1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Create a Discord bot and get its token
4. Create a `.env` file and add the Discord token as `DISCORD_TOKEN=your_discord_token_here`

### Usage

1. Run `python bot.py` to start the bot.
2. Use the command `/generate` followed by a prompt inside "" to generate an image.
   Example: `/generate "A beautiful sunset over the ocean"`
   > To change the resolution or the number of iterations
   > `/generate "[YOUR_PROMPT]" [WIDTH] [HEIGHT] [ITERATION]`
   > Example: `/generate "A beautiful sunset over the ocean" 1920 1080 100`

## Built With

- Python 3.6+
- PyTorch
- Discord.py
- Diffusers
- dotenv
