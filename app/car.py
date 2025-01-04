from decimal import Decimal


class Car:
    def __init__(self, brand: str, fuel_consumption: Decimal) -> None:
        self.brand = brand
        self.fuel_consumption = Decimal(fuel_consumption)

    def count_fuel_consumption(
        self, fuel_price: Decimal, length_way: Decimal
    ) -> Decimal:
        return (
            ((Decimal(length_way) / 100) * self.fuel_consumption)
            * Decimal(fuel_price)
            * 2
        )
