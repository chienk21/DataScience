import numpy as np

fp = 'WeatherAnalysis//WeatherDataSet.txt'
data = np.genfromtxt(fp, skip_header=1, usecols=(0, 1, 2, 3))
print(data)
date = data[:,0]
print(data)
temp_avg = data[:,1]
temp_max = data[:,2]
temp_min = data[:,3]


print(date.min())
print(date.max())


#finding the number of days 
date_mask = np.isfinite(date)
print("Number of days:", np.count_nonzero(date_mask))

#finding the number of missing days in the data
missing_date_mask = ~np.isfinite(date)
print("Number of missing days:", np.count_nonzero(missing_date_mask))

#finding average temperature days
tavg_mask = np.isfinite(temp_avg)
print("Number of average temps:", np.count_nonzero(tavg_mask))

#checking for missing data
missing_tmax_mask = ~np.isfinite(temp_max)
print("Number of missing tmax values:", np.count_nonzero(missing_tmax_mask))

#Make a mask array, then remove bad values using the mask.
tmax_mask = np.isfinite(temp_max)
tmax_clean = temp_max[tmax_mask]

#We can also remove the corresponding dates by using the same mask (tmax_mask) on our date array.
date_clean = date[tmax_mask]

#average annual temperature, use a range of dates to find the average maximum temperature for one year
tmax_total = tmax_clean[(date_clean >= 1973) & (date_clean <= 2021)]
print(tmax_total.mean())









