import phonenumbers
from phonenumbers import geocoder

number = 8002412468

ch_number = phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_number, 'en'))
