# IDEX Monitor
![idex monitor](https://raw.githubusercontent.com/mragicl/idex_monitor/master/img/IdexMonitor.png)

Monitor used to display data from the idex staking tier 3 (uptime, earned credits, percentage online, ...).
It will display the data in a grafana Dashboard.
Tested in Ubuntu 18.04.
You will have to install the IDEX staker:
https://github.com/idexio/IDEXd#getting-aurad

I also highly recommend running this great tool, which will restart the IDEX staker in case it crashes (which happens around once a day...):
https://github.com/Bobface/aurad-utils

## Installation
To install the IDEX monitor, clone this repository and run the installation script:
```sh
cd ~/
git clone https://github.com/mragicl/idex_monitor.git
cd idex_monitor
./install_idex_monitor.sh
```

## Running
To collect the data from IDEX staker, just run the monitor script:
```sh
cd ~/idex_monitor
./idex_monitor.sh
```

Point then your browser to:
http://localhost:3003
and click on the idex_monitoring dashboard.


ETH: 0x6c54eA14109f3E97cdfC02b0C5AbE88e190BDf18
