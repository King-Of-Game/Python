:<<EOF
auto deploy
# prerequisite（前置条件）:
1. installed docker
2. installed python3.6+
3. installed docker-compose
4. installed nginx
# run this shell script
1. put project.zip into /var/www/
2. put auto_deploy.sh into /var/www/
3. chmod +x /var/www/auto_deploy.sh
4. cd /var/www/ && ./auto_deploy.sh
EOF

echo "starting deploy..."
rm -rf /var/www/tq_match_bigscreen_backend
mkdir /var/www/tq_match_bigscreen_backend
unzip tq_match_bigscreen_backend.zip -d /var/www/tq_match_bigscreen_backend/
rm -rf /usr/share/nginx/nginx*
cp /var/www/tq_match_bigscreen_backend/deploy/nginx.conf /usr/share/nginx/nginx.conf
echo "deploying python virtual environment..."
rm -rf /var/www/tq_match_bigscreen_backend/venv
python3 -m venv /var/www/tq_match_bigscreen_backend/venv
cd /var/www/tq_match_bigscreen_backend/venv/bin/
./pip install -U pip
./pip install -r /var/www/tq_match_bigscreen_backend/requirements.txt
echo "deploying database environment by docker..."
systemctl restart docker
docker-compose -f /var/www/tq_match_bigscreen_backend/deploy/docker-compose.yaml up -d --force-recreate
echo "starting up by supervisor"
rm -rf /tmp/supervisor*
./supervisord -c /var/www/tq_match_bigscreen_backend/deploy/supervisord.conf
