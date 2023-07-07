# Pre-steps
## Add to host machine PATH ws-infra/scripts
hung@dell-G15-5511:~/work/ws-finance$ export PATH=$PATH:$WS-infra-scripts-path' >> ~/.bashrc

## Create x-auth cookie to local file
hung@dell-G15-5511:~/work/ws-finance$ xauth-create-params.sh

## Run bash shell in docker
hung@dell-G15-5511:~/work/ws-finance$ shell-dev-python-stats.sh

## Add x-auth cookie in docker
root@dell-G15-5511:/workspace# xauth-import-params.sh x-auth-params.txt

## Test UI app
root@dell-G15-5511:/workspace# python test-env/simple_plot.py
