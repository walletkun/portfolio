#!/bin/bash


# Project routes
PROJECT_DIR="$HOME/portfolio"
VENV_PATH="$PROJECT_DIR/py3"
TMUX_SESSION_NAME="flaskapp"

# first we'll kill all tmux sessions
echo "Killing all tmux sessions.."
if tmux list-sessions &> /dev/null; then
    tmux kill-server
    echo "Tmux session killed"
else
    echo "No existing tmux session found"
fi

# now we'll navigate to the project directory
echo "Navigating to the project"
cd "$PROJECT_DIR"
echo "We're in $(pwd)"


# then we'll fetch the latest changes
echo "Fetching latest changes"
git fetch && git reset origin/main --hard
echo "Repository has updated to the latest version"

# then we'll make sure to activate the python enviornment and have up to date dependencies
echo "Activating python env and make sure the dependencies are updated"
source "$VENV_PATH/bin/activate"
pip install -r requirements.txt

# start the flask server and start a new tmux session
echo "Starting flask server and a new tmux session"
tmux new-session -d -s "$TMUX_SESSION_NAME" -c "$PROJECT_DIR" \
    "source $VENV_PATH/bin/activate && pip install -r requirements.txt && flask run --host=0.0.0.0 --port=5000"

sleep 3
echo "Deployment complete"

