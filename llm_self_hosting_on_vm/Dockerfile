# Use the official lightweight Python image #
# https://hub.docker.com/_/python #
FROM python:3.12-slim

# Copy local code to the container image #
WORKDIR /llm_self_hosting_on_vm
COPY . ./

# Install linux packages # 
RUN apt update && apt install bc htop tmux tree vim wget -y

# Install python dependencies #
#RUN pip install --no-cache-dir -r requirements.txt

# Set up VIM #
RUN wget https://raw.githubusercontent.com/J-sephB-lt-n/my-vim-config/main/.vimrc  
RUN mv .vimrc ~/.vimrc 
# Set up my personal bash aliases #
RUN wget https://raw.githubusercontent.com/J-sephB-lt-n/my-personal-bashrc-zshrc/main/.bash_aliases
RUN mv .bash_aliases ~/.bash_aliases
RUN echo "source ~/.bash_aliases" >> ~/.bashrc
