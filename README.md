# AIGameHackathon

## Running Instructions
1. Try using the executable uploaded [here](https://drive.google.com/file/d/15W3kX29P7DZNeomIBC216fOOsXp3HNqw/view?usp=share_link) (ChatRPG_MacOS or ChatRPG_Windows). This should have our API keys bundled inside and hopefully work without a hitch
   1. If you get any error messages, see if you can resolve them (you may need to brew/chocolately install a dependency or two, but hopefully not)
3. If this does not work, you will need to follow all of the instructions below to run it from this repo (set up your computer, add your own API keys, etc.)

## Computer Setup

Depending how much coding you've done before, you may need to install some things on your computer to get started. Here we'll install homebrew, python3, git, vscode, and the vscode extensions we'll be using.

1. Install homebrew (mac) or chocolatey (windows)
   1. homebrew: https://brew.sh
   1. chocolately: go get a mac
2. Install python3
   1. `brew install python3`
3. Install and set up git
   1. `brew install git` or `choco install git`
   1. `brew install gh` or `choco install gh`
   1. `git config --global user.name "Your Name"`
   1. `gh auth login` and follow the prompts to login with your github account
   1. `git clone <repo url>` (run this in the dir you want the repo to be in)
4. Install vscode (from browser). Then inside vscode:
   1. Install the python extension for vscode
   1. Install the copilot extension for vscode
   1. You can open your repo folder in vscode by running `code .` in the repo folder top level directory

## Repo Setup

These are the steps to get the repo set up on your local machine. Things like python packages and environment variables are intentionally excluded from git via the .gitignore file, so we will set them up locally here.

1. Set up the virtual environment
   1. `python3 -m venv .venv` (this will create a virtual environment in the .venv folder in the repo. Virtual environments are used to keep the python packages for this project separate from other projects on your computer)
   1. `source .venv/bin/activate` (this will activate the virtual environment. You will need to do this every time you open a new terminal window to work on this project)
   1. `pip install -r requirements.txt` (this will install all the python packages needed for the project)
   1. Set the .venv in vscode to make linting work (bottom right of screen, point it to your local venv)
2. Set up the .env file
   1. Copy the .env.example file to a new file called .env
   1. Fill in the values in the .env file (get this from the team or your own API key on OpenAI.com)

## Reminders

- Always activate the virtual environment after first opening the terminal and entering your repo
  `source .venv/bin/activate`
- If you ever change repos, you will need to deactivate the current virtual environment (`deactivate`) and activate the new one. You also need to change the .venv in vscode to point to the new virtual environment, otherwise linting won't work.
- `isort <filename>` will automatically sort your imports

## Getting Started

Inside the src folder you will find a few Demo folders. These should give you enough boiler plate to get started with some basic functionality.

### BasicChatDemo

This is a simple chat bot that calls the ChatGpt API. It should be similar to using the ChatGpt UI but via your command line.
It's a lot more bare bones than the UI. In order to keep context of the conversation, you actually need to pass in the previous messages as well as the current message. This is because the model is stateless and doesn't know what has been said before. This will lead to a hard limit once you reach the max token limit of the model (4k tokens or about 2.8k workds)

### ImageGenDemo

All this does is take a prompt, call the Dalle3 API to generate an image, and open the image in your default browser. This is a good starting point for generating images.
Please read the costs [here](https://openai.com/api/pricing). Of all the tools this one can be the most expensive, so stick to dalle3+standard and 1024x1024 for most calls (4 cents per image at the time of writing this)

### VectorDbDemo

This is the most complicated of the demos. One file will load any documents and automatically convert them into vectors for a vector db. The other file will load manually defined nodes into the vector db. We should be using the latter primarily, as we ultimately will want to be able to control and update the contents of each node as we go.
