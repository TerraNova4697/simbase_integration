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
    SsShiftOrm,
    SsFineOrm,
    SsLegalClaimsOrm,
    SsEmployeeOrm,
    SsContractTRUOrm,
    SsTransportOrm, 
    SsTrainingAndMedicalServiceOrm,
    SsJournalOrm,
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

    def consume_fines(self, fines: list[Fine]) -> None:
        for fine in fines:
            schema = FineSchema.model_validate(fine, from_attributes=True)
            SsFineOrm.create_from_schema(schema)

    def consume_legal_claims(self, legal_claims: list[LegalClaims]) -> None:
        for lc in legal_claims:
            schema = LegalClaimsSchema.model_validate(lc, from_attributes=True)
            SsLegalClaimsOrm.create_from_schema(schema)

    def consume_contract_trus(self, contract_trus: list[ContractTRU]) -> None:
        for contract_tru in contract_trus:
            schema = ContractTRUSchema.model_validate(contract_tru, from_attributes=True)
            SsContractTRUOrm.create_from_schema(schema)

    def consume_employees(self, employees: list[Employee]) -> None:
        for employee in employees:
            schema = EmployeeSchema.model_validate(employee, from_attributes=True)
            SsEmployeeOrm.create_from_schema(schema)

    def consume_transports(self, transports: list[Transport]) -> None:
        for transport in transports:
            schema = TransportSchema.model_validate(transport, from_attributes=True)
            SsTransportOrm.create_from_schema(schema)

    def consume_training_and_medical_services(self, training_and_medical_services: list[TrainingAndMedicalService]) -> None:
        for tans in training_and_medical_services:
            schema = TrainingAndMedicalServiceSchema.model_validate(tans, from_attributes=True)
            SsTrainingAndMedicalServiceOrm.create_from_schema(schema)

    def consume_journals(self, journals: list[Journal]) -> None:
        for journal in journals:
            schema = JournalSchema.model_validate(journal, from_attributes=True)
            SsJournalOrm.create_from_schema(schema)

    def consume_route_sheet(self, route_sheet: list[RouteSheet]) -> None:
        pass

    def consume_drivers(self, drivers: list[Driver]) -> None:
        pass
