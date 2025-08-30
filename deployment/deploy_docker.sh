#!/bin/bash
# Stop script if any command fails
set -e

# Turn on debugging mode
set -x

# Step 0: Install required packages
REQUIRED_PACKAGES="nginx
    python3
    python3-pip
    python3-venv"

apt update

DEBIAN_FRONTEND=noninteractive apt install -y $REQUIRED_PACKAGES
echo "All required packages installed!"

# Step 1: Set up and activation virtual environment
CURRENT_DIR=`pwd`
python3 -m venv venv
source venv/bin/activate
echo "Virtual environment activated."

# Step 2: Install requirements
pip install -r requirements.txt
echo "Dependencies installed successfully."

# Step 3: Run Django migrations
echo "Navigating to the project directory..."
echo "Running migrations"
python3 manage.py migrate

# Step 4: Configure Nginx
rm -fv /etc/nginx/sites-enabled/default
cp -v deployment/templates/etc/nginx/site-enabled/german_app.conf /etc/nginx/sites-enabled/german_app.conf


# Step 5: Configure Nginx
cat > /docker-entrypoint.sh << EOF
#!/bin/bash
echo 'Enable virtenv'
cd $CURRENT_DIR
source venv/bin/activate
echo 'Run nginx'
nginx -g "daemon on;"
echo 'Run django'
python3 manage.py runserver
EOF

chmod 755 /docker-entrypoint.sh
