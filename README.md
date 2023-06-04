# Discord Stable Diffusion Bot

This is a Discord bot that generates images using the Stable Diffusion Pipeline. The bot takes a prompt and generates an image based on the prompt using the Stable Diffusion Pipeline. The generated image is then sent back to the Discord chat.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- PyTorch 1.6 or higher
- Discord.py
- Diffusers
- dotenv
- Install CUDA

### Installation

To set up the Discord Stable Diffusion Bot, follow the steps below:

1. Clone the repository

   ```bash
   git clone <repository_url>
   ```

2. Install the dependencies with

   ```bash
   pip install -r requirements.txt
   ```

3. Install [CUDA for Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html) (except if you are using WSL - in that case go to the WSL section)

4. Create a Discord bot and get its token

- Go to the [Discord Developer Portal](https://discord.com/developers/applications)
- Create a new application
- Under the "Token" section, click on "Copy" to copy the token

   > For more informations go the Discord documentation and search for Bot Creation 

5. Create a `.env.config` file and add the Discord token

   ```bash
   DISCORD_TOKEN=<your_discord_token_here>
   ```

### Usage

1. Run the bot

   ```bash
   python3 stablebot.py
   ```

2. Use the /generate command followed by a prompt enclosed in double quotes to generate an image. For example:
   
   ```bash
   /generate "A beautiful sunset over the ocean"
   ```

   To customize the resolution and the number of iterations, you can provide additional arguments:

   ```bash
   /generate "[YOUR_PROMPT]" [WIDTH] [HEIGHT] [ITERATION]
   ```

   Example:

   ```bash
   /generate "A beautiful sunset over the ocean" 1920 1080 100
   ```

### WSL (Windows Subsystem for Linux) Setup

If you are using WSL to run the Discord Stable Diffusion Bot, follow these additional steps:

1. Install WSL on your Windows machine. You can find detailed instructions on the official Microsoft documentation: [WSL Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install).

2. Install [CUDA](https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl) for WSL: [https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl](https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl)

3. Open the WSL terminal and navigate to the project directory.

4. Create a Python virtual environment (recommended but optional)

- If you are running WSL with Ubuntu or Debian, install python venv

   ```bash
   apt install python3.10-venv
   ```

- Create the virtual environment

   ```bash
   python3 -m venv .env
   ```

- Use the created environment

   ```bash
   source .env/bin/activate
   ```

5. Install Python and other dependencies in the WSL environment. Follow the same installation steps mentioned above in the "Installation" section.

#### Possible errors

- Error: `Could not load library libcudnn_cnn_infer.so.8. Error: libcuda.so: cannot open shared object file: No such file or directory
Please make sure libcudnn_cnn_infer.so.8 is in your library path!`, `libcuda.so not found`  
Solution: add `export LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH` to your `.bashrc` file

### Running with GPU 

To run the Discord Stable Diffusion Bot with GPU, ensure that you have the following prerequisites:

- A compatible NVIDIA GPU
- CUDA Toolkit installed (refer to the CUDA installation guide for instructions)

Follow these steps to run the bot with GPU:

1. Ensure that the correct CUDA device is specified in the cuda parameter of the StableDiffusionGenerator class within the stablebot.py file. For example:

   ```python
   cuda = "cuda:0"
   ```
   > Adjust the device identifier (cuda:0, cuda:1, etc.) as needed based on your GPU configuration. The bot will utilize the GPU for generating images.

### Running with CPU 

If you want to run the Discord Stable Diffusion Bot using CPU instead of GPU, follow these steps:

1. Modify the cuda parameter in the StableDiffusionGenerator class within the stablebot.py file. Change it to:

   ```python
   cuda = "cpu"
   ```
   You can uncomment the line and comment the one with `cuda = "cuda:0"`.
   > The bot will now use CPU for generating images.

### Changing the model

It is as simple as commenting/keeping the model you want to use:

```python
# model="prompthero/openjourney",  # "andite/anything-v4.0",
# model="dreamlike-art/dreamlike-photoreal-2.0",
# model="prompthero/openjourney-v4",
model="MirageML/lowpoly-world",
```

If you want to select another model, chose one from [Hugging Face](https://huggingface.co/models?pipeline_tag=text-to-image&library=diffusers&sort=downloads) and copy its name like so `model=<model_name>`

> When running the bot your selected model will be downloaded automatically.
