#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
usage:
python csv_cleaner.py <filename>.csv
./csv_cleaner.py <filename>.csv
'''

import os.path
import sys
import csv
from datetime import datetime
from pytz import timezone

def convert_to_secs(timer):
    """
    Convert datetime-style timer to floating point seconds format
    """
    timer_split = timer.split(':')
    hour = float(timer_split[0]) * 3600
    minute = float(timer_split[1]) * 60
    sec = float(timer_split[2])
    return hour + minute + sec

def csv_writer(filename, data):
    """
    Write to csv file
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in data:
            writer.writerow(row)

def csv_reader(file_obj):
    """
    Read from csv file
    """
    reader = csv.reader(file_obj)
    results = []
    for idx, row in enumerate(reader):
        try:
            if idx == 0 and row:
                results.append(row)
                continue
            result = []
            if row[0]:
                timestamp = row[0]
                new_dt_obj = datetime.strptime(timestamp, '%m/%d/%y %H:%M:%S %p')
                eastern = timezone('US/Eastern')
                new_dt = eastern.localize(new_dt_obj)
                new_ts = new_dt.isoformat()
                result.append(new_ts)
            if row[1]:
                address = row[1]
                result.append(address)
            if row[2]:
                zip_codes = row[2]
                if len(zip_codes) < 5:
                    zip_codes = "0" * (5 - len(zip_codes)) + zip_codes
                result.append(zip_codes)
            if row[3]:
                name = row[3].upper()
                result.append(name)
            if row[4]:
                foo_dur = convert_to_secs(row[4])
                result.append(str(foo_dur))
            if row[5]:
                bar_dur = convert_to_secs(row[5])
                result.append(str(bar_dur))
            if row[6]:
                if foo_dur and bar_dur:
                    total_dur = foo_dur + bar_dur
                    result.append(str(total_dur))
            if row[7]:
                notes = row[7]
                result.append(notes)
            print(result)
            if result:
                results.append(result)
        except Exception as exc:
            print("WARNING: " + str(exc) + ", skipping row", file=sys.stderr)
            continue
    return results

if __name__ == '__main__':
    args = sys.argv[1:]
    if args and len(args) == 1:
        try:
            csv_file = args[0]
            if os.path.exists(csv_file):
                # Read as utf-8, replacing errors with Unicode Replacement Character.
                with open(args, 'r', encoding="utf-8", errors="replace") as f:
                    csv_data = csv_reader(f)
                    new_file = 'cleaned-{}'.format(csv_file)
                    csv_writer(new_file, csv_data)
            else:
                print("{} doesn't exist. Please enter one valid csv argument. (i.e. python3 csv.py sample.csv)".format(csv_file))
        except IndexError:
            print("Please enter one valid csv argument. (i.e. python3 csv.py sample.csv)")    
        except Exception as exc:
            print("ERROR: " + str(exc), file=sys.stderr)
            raise
    else:
        print("Please enter one valid csv argument. (i.e. python3 csv.py sample.csv)")

