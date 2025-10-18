lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_in_centimetres = lenght * width * height
volume_in_liters = volume_in_centimetres/1000

liters_without_tor = percent/100 * volume_in_liters

all_volume = volume_in_liters - liters_without_tor

print(all_volume)



