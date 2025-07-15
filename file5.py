# Ota klass
class Appliance:
    def turn_on(self):
        return "Qurilma yoqildi."

    def turn_off(self):
        return "Qurilma ochirildi."

# TV klassi
class TV(Appliance):
    def turn_on(self):
        return "TV yoqildi. Kanal korsatilmoqda."

    def turn_off(self):
        return "TV ochirildi. Ekran qora."

# Fridge klassi
class Fridge(Appliance):
    def turn_on(self):
        return "Muzlatkich yoqildi. Sovutish boshlandi."

    def turn_off(self):
        return "Muzlatkich ochirildi. Sovutish toxtadi."

# Test
devices = [TV(), Fridge()]

for device in devices:
    print(device.turn_on())
    print(device.turn_off())
    print("---")
