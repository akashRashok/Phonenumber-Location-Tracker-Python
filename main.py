import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number=input("Enter phone number with country code:")

ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,'en'))

service_number=phonenumbers.parse(number,"R0")
print(carrier.name_for_number(service_number,'en'))
