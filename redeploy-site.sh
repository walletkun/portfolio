#!/bin/bash


# Project routes
PROJECT_DIR="$HOME/portfolio"
VENV_PATH="$PROJECT_DIR/py3"
ACTIVATE_VENV="$VENV_PATH/bin/activate"
SERVICE_NAME="myportfolio.service"

echo "Starting portfolio session via service starts..."

# First we'll stop the service if it's running
# using sudo to prevent priviledge
echo "Stopping existing portfolio service"
sudo systemctl stop "$SERVICE_NAME"
echo "Service successfully stopped"

# Navigate to the root project directory
echo "Changing into the project directory.."
cd "$PROJECT_DIR"
echo "We're in $(pwd)"

# Fetching the latest changes
echo "Fetching updated changes.."
git fetch && git reset origin/main --hard
echo "Repository updated to the latest version"

# Activate the virtual enviornment and updating the dependencies
echo "Activating the venv and updating the necessary dependencies..."
source "$ACTIVATE_VENV"
pip install -r requirements.txt
echo "Dependencies up to date.."

# Set up the proper flask enviroment variables
echo "Setting up Flask environments.."
export FLASK_APP=app.py
export FLASK_ENV=development

# Reload the systemd configuration (in case service file changed)
echo "Reloading systemd configuration files.."
sudo systemctl daemon-reload

# Start and enable the service
echo "Startting and enabling to allow auto service start when system starts..."
sudo systemctl start "$SERVICE_NAME"
sudo systemctl enable "$SERVICE_NAME"

# Delay a moment for the service to start
sleep 3

# Checking the status of the service
echo "Checking status of service.."
if sudo systemctl is-active --quiet "$SERVICE_NAME"; then
    echo "Deployment successful, Service running successfully."
    echo "Service status:" 
    sudo systemctl status "$SERVICE_NAME"

else
    echo "Service failed to start: Check logs"
    sudo journalctl -u "$SERVICE_NAME" --no-pager -l
    exit 1

fi


echo ""
echo "Deployment complete"
echo "To view logs do: sudo journalctl -u $SERVICE_NAME -f"
echo "To restart service do: sudo systemctl restart $SERVICE_NAME"
echo "TO stop service do: sudo systemctl stop $SERVICE_NAME"




