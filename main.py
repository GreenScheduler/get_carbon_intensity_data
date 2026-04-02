import time
from pathlib import Path

import cats
import pandas as pd

def download_data(location='OX1', out_path=Path('.')):
    """
    Download data and save in to csv
    """
    # Use cats to get the data (and stick in into a dataframe)
    interface = cats.CI_api_interface.API_interfaces["carbonintensity.org.uk"]
    result = cats.CI_api_query.get_CI_forecast(location, interface)
    result_frame = pd.DataFrame(data=result)
    # Build the output filename
    timestamp = result_frame['datetime'].iloc[0].isoformat()
    filename = location + "_" + timestamp + ".csv"
    # Write out (without an index col or extra set of timestamps)
    result_frame.index = result_frame.datetime
    result_frame.to_csv(path_or_buf=out_path/filename, columns=('value',))

def main():
    """
    Download data and save in to csv
    """
    location_names = ['North Scotland', 'South Scotland', 'North East England',
                      'North West England', 'East England', 'North Wales & Merseyside',
                      'South West England', 'London', 'South England', 'South East England',
                      'Yorkshire', 'West Midlands', 'East Midlands', 'South Wales'] 
    location_postcodes = ['IV1', 'EH1', 'NE1', 'M1', 'CB1', 'L1', 'BS1',
                          'WC1E', 'OX1', 'BN1', 'LS1', 'B1', 'NG1', 'CF1'] 
     
    for name, postcode in zip(location_names, location_postcodes):
        name = name.replace(' ', '_')
        name = name.replace('&', 'and')
        data_path = Path('./'+name)
        data_path.mkdir(exist_ok=True)
        download_data(location=postcode, out_path=data_path)
        time.sleep(5)


if __name__ == "__main__":
    main()
