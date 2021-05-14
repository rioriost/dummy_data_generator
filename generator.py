#!/usr/bin/env python3

import datetime
import random
import uuid
import sys
import calendar

def main():
    with open(sys.argv[1], "w") as f:
        type = 'SensorMeasurement'
        devicetype = 'WebFleet'
        recommendedaxlepressuremin = 10
        recommendedaxlepressuremax = 10
        recommendedpressure = 10
        pressureseverity = 0
        tempseverity = 0
        createdsource = 'WebFleet'
        createdby = ''
        updatedby = ''
        lastupdatedtype = 'Measurement'
        version = 1
        for vehicle_ct in range(0, 10):
            fleetlocationid = str(uuid.uuid4())
            vehicleid = str(uuid.uuid4())
            deviceid = str(uuid.uuid4())
            sensorid = str(uuid.uuid4())
            rfid = str(uuid.uuid4())
            issensorbatterylow = 'true'
            axis_ct = random.randint(1, 4)
            tire_ct_per_axis = {}
            for axis_num in range(axis_ct):
                if axis_num == 0:
                    tire_ct_per_axis[0] = 1
                else:
                    tire_ct_per_axis[axis_num] = random.randint(1, 3)
            for month_num in range(1, 13):
                for day_num in range(1, calendar.monthrange(2021, month_num)[1] + 1):
                    for hour_num in range(0, 24):
                        for min_num in range(0, 60):
                            readingdate = datetime.datetime(2021, month_num, day_num, hour_num, min_num, 0)
                            messageid = str(uuid.uuid4())
                            correlationid = str(uuid.uuid4())
                            pressure = random.randint(5, 20)
                            coldadjustedpressure = pressure
                            temperature = random.randint(-40, 50)
                            battery = random.randint(0,  10)
                            ambienttemperature = temperature - 10
                            id = str(uuid.uuid4())
                            createddate = readingdate
                            for axis_num in range(axis_ct):
                                for tire_ct in range(tire_ct_per_axis[axis_num]):
                                    mountposition = '{0}-L{1}'.format(str(axis_num + 1), str(tire_ct + 1))
                                    f.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28}\n".format(type, fleetlocationid, vehicleid, deviceid, devicetype, sensorid, mountposition, readingdate, rfid, messageid, correlationid, recommendedaxlepressuremin, recommendedaxlepressuremax, recommendedpressure, pressureseverity, tempseverity, issensorbatterylow, pressure, coldadjustedpressure, temperature, battery, ambienttemperature, id, createddate, createdsource, createdby, updatedby, lastupdatedtype, version))
                                    mountposition = '{0}-R{1}'.format(str(axis_num + 1), str(tire_ct + 1))
                                    f.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28}\n".format(type, fleetlocationid, vehicleid, deviceid, devicetype, sensorid, mountposition, readingdate, rfid, messageid, correlationid, recommendedaxlepressuremin, recommendedaxlepressuremax, recommendedpressure, pressureseverity, tempseverity, issensorbatterylow, pressure, coldadjustedpressure, temperature, battery, ambienttemperature, id, createddate, createdsource, createdby, updatedby, lastupdatedtype, version))
                        
if __name__ == "__main__":
    main()