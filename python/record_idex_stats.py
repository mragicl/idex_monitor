#!/usr/bin/env python
from influxdb import InfluxDBClient
import subprocess
import time


def write_data_to_influxdb(client, measurement, value):
    json_body = [
        {
            "measurement": measurement,
            "fields": {
                "value": value
            }
    }
    ]
    client.write_points(json_body)


def write_measurement_to_influxdb(client,measurement, fields):
    json_body = [
        {
            "measurement": measurement,
            "fields": fields
        }
    ]
    client.write_points(json_body)
    
def get_period_credits():
    mpc,tpc,online,staked_idex,total_staked_idex = -1,-1, False,0,0
    result = subprocess.run(['idex', 'status'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    for line in output.splitlines():
        #print(line)
        if line.find("My Period Credits") >=0:
            sline = line.split(' ')
            my_period_credits = float(sline[5])
            tot_period_credits = float(sline[7])
            mpc,tpc =  my_period_credits, tot_period_credits
        if line.find("Staking") >= 0:
            
           
            sline = line.split(' ')
            if sline[1].find('online') >= 0:
                online = True
        if line.find("Staked IDEX") >= 0 and line.find("Total") <0:
            sline = line.split(' ')
            staked_idex = float(sline[2])
        if line.find("Staked IDEX") >= 0 and line.find("Total") >=0:
            sline = line.split(' ')
            total_staked_idex = float(sline[3])

    return mpc,tpc,online,staked_idex,total_staked_idex

if __name__ == "__main__":
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'idexmonitor')
    client.create_database('idexmonitor')
    while True:
        mpc,tpc,online,staked_idex,total_staked_idex = get_period_credits()
        fields = {'my_period_credits':mpc,
                  'total_period_credits':tpc,
                  'online':int(online),
                  'staked_idex':staked_idex,
                  'total_staked_idex':total_staked_idex
                  }
        measurement = 'staking_parameters'
        write_measurement_to_influxdb(client,measurement, fields)
        print(mpc,tpc,online,staked_idex,total_staked_idex)
        time.sleep(60)
        
