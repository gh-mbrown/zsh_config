#!/bin/python

import os

HOME = os.environ.get("HOME")
XDG_CONFIG_HOME = os.environ.get("XDG_CONFIG_HOME")
CWD = os.getcwd()

SRC_DEST = {
    f"{CWD}/.tmux": f"{HOME}/.tmux",
    f"{CWD}/.gitconfig": f"{HOME}/.gitconfig",
    f"{CWD}/.tmux.conf": f"{HOME}/.tmux.conf",
    f"{CWD}/.zshrc": f"{HOME}/.zshrc",
    f"{CWD}/.zsh_profile": f"{HOME}/.zsh_profile",
    f"{CWD}/config": f"{XDG_CONFIG_HOME}/ghostty/config",
}


def link_files():
    for src, dest in SRC_DEST.values():
        os.link(src, dest)


if __name__ == "__main__":
    link_files()
