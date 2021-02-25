
#data = "5045.56486,N,00419.98855,E".split(',')
data = "5045.56365,N,00419.98988,E".split(',')

print(data[0],data[1],data[2])

latitude = str(float(data[0][:2]) + float(data[0][2:])/60) + ' ' + data[1]
print('Latitude : ', latitude)
longitude = str(float(data[2][:3]) + float(data[2][3:])/60) + ' ' + data[3]
print('Longitude : ', longitude)
print('Formatted : ', latitude, longitude)
