weight_units_conversion = {
    'kg': 1,
    'g': 1000,
    'ton': 0.001,
}

volume_units_conversion = {
    'm3': 1,
    'liter': 1000,
    'cc': 1000000,
    'ml': 1000000,
}

area_units_conversion = {
    'm2': 1,
    'km2': 0.000001,
    'cm2': 0.0001,
}

length_units_conversion = {
    'm': 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
}

all_units = {
    'weight': weight_units_conversion,
    'volume': volume_units_conversion,
    'area': area_units_conversion,
    'length': length_units_conversion,
}


class Unit():
    def __init__(self, val, unit_name):
        self.type = self.type_finder(unit_name)
        self.val = float(val)
        self.unit_name = unit_name

    def type_finder(self, unit_name):
        type = None
        for key in all_units:
            if unit_name in all_units[key]:
                type = key
        return type

    def scientific_notion(self):
        scientific_notion = "{:e}".format(self.val)
        return scientific_notion

    def convert(self, other_unit):
        other_type = self.type_finder(other_unit)
        if other_type == self.type:
            coeff_other = all_units[other_type][other_unit]
            coeff_self = all_units[self.type][self.unit_name]
            self.val = self.val * coeff_other / coeff_self
            self.unit_name = other_unit
        else:
            print("unit convertion type error")

    def __str__(self):
        return str(self.val) + ' ' + self.unit_name

    def __add__(self, other):
        if self.type == other.type:
            other.convert(self.unit_name)
            return Unit(self.val + other.val, self.unit_name)
    
    def __sub__(self, other):
        if self.type == other.type:
            other.convert(self.unit_name)
            return Unit(self.val - other.val, self.unit_name)

    def __mul__(self, other):
        return Unit(self.val * other, self.unit_name)

    def __div__(self, other):
        return Unit(self.val / other, self.unit_name)


if __name__ == "__main__":
    u_1 = Unit(2, 'kg')
    u_2 = Unit(3, 'g')

    u = u_1 - u_2
    u.convert('g')
    print(u * 2)