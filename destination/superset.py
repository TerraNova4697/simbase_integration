from database.models import *
from database.queries import (
    SsFilialOrm,
    SsCustomerOrm,
    SsObjectOrm,
    SsPostOrm,
    SsSecurityGuardOrm,
    SsIncomeOrm,
    SsContractOrm,
    SsTriggeringOrm,
    SsShiftOrm
)
from schemas.simbase_schemas import *


class Superset:

    def __init__(self):
        pass

    def consume_filials(self, filials: list[Filial]) -> None:
        for filial in filials:
            schema = FilialSchema.model_validate(filial, from_attributes=True)
            SsFilialOrm.create_from_schema(schema)

    def consume_customers(self, customers: list[Customer]) -> None:
        for customer in customers:
            schema = CustomerSchema.model_validate(customer, from_attributes=True)
            SsCustomerOrm.create_from_schema(schema)

    def consume_objects(self, objects: list[Object]) -> None:
        for object in objects:
            schema = ObjectSchema.model_validate(object, from_attributes=True)
            SsObjectOrm.create_from_schema(schema)

    def consume_posts(self, posts: list[Post]) -> None:
        for post in posts:
            schema = PostSchema.model_validate(post, from_attributes=True)
            SsPostOrm.create_from_schema(schema)

    def consume_security_guards(self, guards: list[SecurityGuard]) -> None:
        for guard in guards:
            schema = SecurityGuardSchema.model_validate(guard, from_attributes=True)
            SsSecurityGuardOrm.create_from_schema(schema)

    def consume_income(self, income: list[Income]) -> None:
        for inc in income:
            schema = IncomeSchema.model_validate(inc, from_attributes=True)
            SsIncomeOrm.create_from_schema(schema)

    def consume_contracts(self, contracts: list[Contract]) -> None:
        for contract in contracts:
            schema = ContractSchema.model_validate(contract, from_attributes=True)
            SsContractOrm.create_from_schema(schema)

    def consume_triggerings(self, triggerings: list[Triggering]) -> None:
        for triggering in triggerings:
            schema = TriggeringSchema.model_validate(triggering, from_attributes=True)
            SsTriggeringOrm.create_from_schema(schema)

    def consume_shifts(self, shifts: list[Shift]) -> None:
        for shift in shifts:
            schema = ShiftSchema.model_validate(shift, from_attributes=True)
            SsShiftOrm.create_from_schema(schema)

    def consume_route_sheet(self, route_sheet: list[RouteSheet]) -> None:
        pass

    def consume_drivers(self, drivers: list[Driver]) -> None:
        pass
