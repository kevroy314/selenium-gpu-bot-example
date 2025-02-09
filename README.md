# selenium-gpu-bot-example

## Setup

This assumes you're in an environment that can handle these packages - I'm in Ubuntu 22.04 in WSL. See Optional Setup if you'd like to copy this. You need Anaconda installed as well:

https://docs.anaconda.com/anaconda/install/

```
conda create -n gpubot python==3.11 --yes
conda activate gpubot
pip install -r requirements.txt
```

## Run

`python bot.py`

## Optional Setup

Ubuntu on WSL: https://learn.microsoft.com/en-us/windows/wsl/install

## Troubleshooting

If you have trouble getting the firefox instance to open, it means firefox.exe isn't in your path. On Ubuntu (including WSL) you can do this by:

`sudo apt-get install firefox-geckodriver`