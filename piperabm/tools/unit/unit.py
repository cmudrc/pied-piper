from datetime import datetime as Date
from datetime import timedelta as DT
from numpy import pi


all_units = {
    'weight': {
        'kg': 1,
        'g': 1000,
        'ton': 0.001,
    },
    'volume': {
        'm3': 1,
        'liter': 1000,
        'cc': 1000000,
        'ml': 1000000,
    },
    'area': {
        'm2': 1,
        'km2': 0.000001,
        'cm2': 0.0001,
    },
    'length': {
        'm': 1,
        'km': 0.001,
        'cm': 100,
        'mm': 1000,
    },
    'time': {
        'second': 24 * 3600,
        'minute': 24 * 60,
        'hour': 24,
        'day': 1,
        'week': 1/7,
    },
    'angle': {
        'rad': pi,
        'degree': 180,
    }
}

SI_units = {
    'weight': 'kg',
    'volume': 'm3',
    'area': 'm2',
    'length': 'm',
    'time': 'second',
    'angle': 'rad',
}


class Unit:
    """
    A value with physical unit, could be converted into other supported units.
    """
    
    def __init__(self, val, unit_name):
        self.unit_name = unit_name
        self.name_numerator, self.name_denominator = self.unit_name_split(unit_name)
        self.type_numerator = self.type_finder(self.name_numerator)
        self.type_denominator = self.type_finder(self.name_denominator)
        self.val = float(val)
        self.unit_name = unit_name

    def unit_name_split(self, unit_name):
        """
        Splits the unit_name into numerator and denominator.
        """

        unit_name = unit_name.split('/')
        unit_name_numerator = unit_name[0]
        try:
            unit_name_denominator = unit_name[1]
        except:
            unit_name_denominator = None
        return unit_name_numerator, unit_name_denominator

    def type_finder(self, unit_name):
        """
        Looks for the type of unit in all_units dict.
        """

        unit_type = None
        for key in all_units:
            if unit_name in all_units[key]:
                unit_type = key
        return unit_type

    def scientific_notion(self):
        """
        Returns the scientific notion of val.        
        """

        scientific_notion = "{:e}".format(self.val)
        return scientific_notion

    def conversion(self, other_unit):
        """
        Calculates the new val based on other_unit.
        """

        val = None
        unit_name = None
        other_name_numerator, other_name_denominator = self.unit_name_split(other_unit)
        other_type_numerator = self.type_finder(other_name_numerator)
        other_type_denominator = self.type_finder(other_name_denominator)
        if other_type_numerator == self.type_numerator:
            coeff_other_numerator = all_units[other_type_numerator][other_name_numerator]
            coeff_self_numerator = all_units[self.type_numerator][self.name_numerator]
            coeff_numerator = coeff_other_numerator / coeff_self_numerator
            coeff_denominator = 1
            if other_type_denominator == self.type_denominator:
                if other_type_denominator is not None and self.type_denominator is not None:
                    coeff_other_denominator = all_units[other_type_denominator][other_name_denominator]
                    coeff_self_denominator = all_units[self.type_denominator][self.name_denominator]
                    coeff_denominator = coeff_other_denominator / coeff_self_denominator
            else:
                print("unit convertion type error in denominator")
            val = self.val * coeff_numerator / coeff_denominator
            unit_name = other_unit
        else:
            print("unit convertion type error in numerator")
        return val, unit_name

    def to(self, other_unit):
        """
        Returns a new converted instance and keeps this instance untouched.
        """

        val, unit_name = self.conversion(other_unit)
        if val is not None and unit_name is not None:
            result = Unit(val, unit_name)
        else:
            result = None
        return result

    def convert(self, other_unit):
        """
        Changes the instance after conversion.
        """

        val, unit_name = self.conversion(other_unit)
        if val is not None and unit_name is not None:
            self.val = val
            self.unit_name = unit_name
            self.name_numerator, self.name_denominator = self.unit_name_split(unit_name)

    def to_SI(self, object=False):
        """
        Convert to SI units.

        Args:
            object: whether return a Unit instance or only the value
        """

        type_numerator_SI = SI_units[self.type_numerator]
        if self.type_denominator is not None:
            type_denominator_SI = SI_units[self.type_denominator]
        else:
            type_denominator_SI = None

        type_SI = type_numerator_SI
        if type_denominator_SI is not None:
            type_SI += '/' + type_denominator_SI
        result = self.to(type_SI)

        if object is True:
            return result
        else:
            return result.val

    def to_DT(self):
        """
        Convert unit of time into a DT (datetime.timedelta) object
        """
        if self.type_numerator is 'time' and \
            self.type_denominator is None:
            result = DT(seconds=self.to('second').val)
        else:
            result = None
        return result

    def copy(self):
        return Unit(self.val, self.unit_name)

    def __str__(self):
        return str(self.val) + ' ' + self.unit_name

    def __add__(self, other):
        """
        Supports unit_1 + unit_2, and also Unit(val, <time>) + date()
        """

        if isinstance(other, Unit):
            if self.type_numerator == other.type_numerator:
                if other.type_denominator == self.type_denominator:
                    other.convert(self.unit_name)
                return Unit(self.val + other.val, self.unit_name)
        elif isinstance(other, Date) and self.type_numerator == 'time' and self.type_denominator is None:
            return other + DT(seconds=self.to('second').val)
    
    def __sub__(self, other):
        """
        Supports unit_1 - unit_2, and also Unit(val, <time>) - date()
        """

        if isinstance(other, Unit):
            if self.type_numerator == other.type_numerator:
                if other.type_denominator == self.type_denominator:
                    other.convert(self.unit_name)
                return Unit(self.val - other.val, self.unit_name)
        elif isinstance(other, Date) and self.type_numerator == 'time' and self.type_denominator is None:
            return other - DT(seconds=self.to('second').val)

    def __mul__(self, other):
        """
        Only supports scalar multipication.
        """

        return Unit(self.val * other, self.unit_name)

    def __truediv__(self, other):
        """
        Only supports scalar float division.
        """
        
        return Unit(self.val / other, self.unit_name)


if __name__ == "__main__":
    v = Unit(2, 'km/hour')
    v.convert('m/minute')
    print(v)
    print(Unit(35, 'day').to_SI())
