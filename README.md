# pyPlexUtils

A Python package which includes useful command-line tools for managing media files for use with Plex Media Server.

## Table of Contents

  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)

## Getting Started

### Prerequisites

The command-line tool, `clear-mkvchptnames`, included with this pyPlexUtils Python package requires the [Matroska tools](https://mkvtoolnix.download/) to be installed on your system.  The Matroska tools includes a set of command-line tools which should be accessible from the shell PATH upon installation.

> On macOS, the Matroska tools can be installed using the [Homebrew](https://brew.sh/) package manager.  From the terminal, type `brew install mkvtoolnix` and press Enter.


### Installation

> It is recommended to perform the install using pipx.  Pipx allows you to execute binaries from Python packages in isolated environments.  This is generally good housekeeping and helps to maintain a tidy global python environment on your system.  Here's how to install pipx:
>    ```sh
>    $ python3 -m pip install pipx
>    $ python3 -m userpath append ~/.local/bin
>    ```
>The last command updates your path if your system is configured to use the bash shell.  However, if your system is configured to use zsh instead of bash, you will need to edit the ~./zshrc to include `export PATH="$PATH:/Users/<your_user_name>/.local/bin"` where <your_user_name> is your specific user name.

Here's how to install pyPlexUtils:

```sh
$ pipx install --spec git+https://git@github.com/JoeArauzo/pyPlexUtils.git pyPlexUtils
```