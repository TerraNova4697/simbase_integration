from database.models import *
from database.queries import (
    SsFilialOrm,
    SsCustomerOrm,
    SsObjectOrm,
    SsPostOrm,
    SsSecurityGuardOrm,
    SsIncomeOrm,
    SsContractOrm,
)


class Superset:

    def __init__(self):
        pass

    def consume_filials(self, filials: list[Filial]) -> None:
        for filial in filials:
            SsFilialOrm.create(
                id_sm=filial.id_sm,
                name=filial.name,
                date_modified=filial.date_modified,
                date_created=filial.date_created,
                model=filial
            )

    def consume_customers(self, customers: list[Customer]) -> None:
        for customer in customers:
            SsCustomerOrm.create(
                id_sm=customer.id_sm,
                name=customer.name,
                bin=customer.bin,
                status=customer.status,
                date_modified=customer.date_modified,
                date_created=customer.date_created,
                model=customer
            )


    def consume_objects(self, objects: list[Object]) -> None:
        for object in objects:
            SsObjectOrm.create(
                id_sm=object.id_sm,
                filial_id_sm=object.filial_id_sm,
                customer_id_sm=object.customer_id_sm,
                contract_id_sm=object.contract_id_sm,
                contract_name=object.contract,
                name=object.name,
                contract_date=object.contract_date,
                contract_number=object.contract_number,
                type=object.type,
                date_modified=object.date_modified,
                date_created=object.date_created,
                model=object
            )

    def consume_posts(self, posts: list[Post]) -> None:
        for post in posts:
            SsPostOrm.create(
                id_sm=post.id_sm,
                filial_id_sm=post.filial_id_sm,
                customer_id_sm=post.customer_id_sm,
                object_id_sm=post.object_id_sm,
                name=post.name,
                type=post.type,
                shift_mode=post.shift_mode,
                operating_mode=post.operating_mode,
                linear_part=post.linear_part,
                length_from=post.length_from,
                length_to=post.length_to,
                date_modified=post.date_modified,
                date_created=post.date_created,
                model=post
            )

    def consume_security_guards(self, guards: list[SecurityGuard]) -> None:
        for guard in guards:
            SsSecurityGuardOrm.create(
                id_sm=guard.id_sm,
                filial_id_sm=guard.filial_id_sm,
                customer_id_sm=guard.customer_id_sm,
                object_id_sm=guard.object_id_sm,
                name=guard.name,
                surname=guard.surname,
                iin=guard.iin,
                social_status=guard.social_status,
                status=guard.status,
                job_title=guard.job_title,
                employee_photo=guard.employee_photo,
                gender=guard.gender,
                nationality=guard.nationality,
                labor_union=guard.labor_union,
                date_modified=guard.date_modified,
                date_created=guard.date_created,
                model=guard
            )

    def consume_income(self, income: list[Income]) -> None:
        for inc in income:
            SsIncomeOrm.create(
                filial_id_sm=inc.filial_id_sm,
                contract_id_sm=inc.contract_id_sm,
                type=inc.type,
                status=inc.status,
                year=inc.year,
                month=inc.month,
                contract_amount=inc.contract_amount,
                additional_agreement_amount=inc.additional_agreement_amount,
                amount_avr=inc.amount_avr,
                payment_date_avr=inc.payment_date_avr,
                actual_payment=inc.actual_payment,
                payment_date_actual=inc.payment_date_actual,
                deviation_amount=inc.deviation_amount,
                deviation_from_avr=inc.deviation_from_avr,
                deviation_from_contract_prc=inc.deviation_from_contract_prc,
                deviation_from_avr_prc=inc.deviation_from_avr_prc,
                remainder=inc.remainder,
                comment=inc.comment,
                additional_comment=inc.additional_comment,
                date_modified=inc.date_modified,
                date_created=inc.date_created,
                model=inc
            )

    def consume_contracts(self, contracts: list[Contract]) -> None:
        for contract in contracts:
            SsContractOrm.create(
                id_sm=contract.id_sm,
                start_date=contract.start_date,
                warning_date=contract.warning_date,
                end_date=contract.end_date,
                customer_id_sm=contract.customer_id_sm,
                name=contract.name,
                type=contract.type,
                contract_number=contract.contract_number,
                date_modified=contract.date_modified,
                date_created=contract.date_created,
                model=contract,
            )


    def consume_route_sheet(self, route_sheet: list[RouteSheet]) -> None:
        pass

    def consume_drivers(self, drivers: list[Driver]) -> None:
        pass
