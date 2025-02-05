from database.models import *
from database.queries import (
    SsFilialOrm,
    SsCustomerOrm,
    SsObjectOrm,
    SsPostOrm,
    SsMobGroupOrm,
    SsSecurityGuardOrm,
    SsIncomeOrm
)


class Superset:

    def __init__(self):
        pass

    def consume_filials(self, filials: list[Filial]) -> None:
        for filial in filials:
            SsFilialOrm.create(
                id_sm=filial.id_sb_object_filial,
                name=filial.name_filial,
                date=filial.date,
                model=filial
            )

    def consume_customers(self, customers: list[Customer]) -> None:
        for customer in customers:
            SsCustomerOrm.create(
                id_sm=customer.id_sb_object_zakazchik,
                name=customer.name_customer,
                bin=customer.bin,
                date=customer.date,
                model=customer
            )


    def consume_objects(self, objects: list[Object]) -> None:
        for object in objects:
            SsObjectOrm.create(
                id_sm=object.id_sb_object_object,
                filial_id_sm=object.id_sb_object_filial,
                customer_id_sm=object.id_sb_object_zakazchik,
                contract=object.contract,
                name=object.name_object,
                contract_date=object.contract_date,
                contract_number=object.contract_number,
                type=object.type,
                date=object.date,
                model=object
            )

    def consume_posts(self, posts: list[Post]) -> None:
        for post in posts:
            SsPostOrm.create(
                id_sm=post.id_sb_object_post,
                filial_id_sm=post.id_sb_object_filial,
                customer_id_sm=post.id_sb_object_zakazchik,
                object_id_sm=post.id_sb_object_object,
                name=post.name_post,
                type=post.type,
                shift_mode=post.shift_mode,
                date=post.date,
                model=post
            )

    def consume_mobile_groups(self, mob_groups: list[MobileGroup]) -> None:
        for mob_group in mob_groups:
            SsMobGroupOrm.create(
                id_sm=mob_group.id_sb_object_mob_group,
                filial_id_sm=mob_group.id_sb_object_filial,
                customer_id_sm=mob_group.id_sb_object_zakazchik,
                object_id_sm=mob_group.id_sb_object_object,
                name=mob_group.mobile_group_name,
                operating_mode=mob_group.operating_mode,
                linear_part=mob_group.linear_part,
                length_from=float(mob_group.length_from),
                length_to=float(mob_group.length_to),
                date=mob_group.date,
                model=mob_group
            )

    def consume_security_guards(self, guards: list[SecurityGuard]) -> None:
        for guard in guards:
            SsSecurityGuardOrm.create(
                id_sm=guard.id_sb_guards,
                filial_id_sm=guard.id_sb_object_filial,
                customer_id_sm=guard.id_sb_object_zakazchik,
                object_id_sm=guard.id_sb_object_object,
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
                date=guard.date,
                model=guard
            )

    def consume_income(self, income: list[Income]) -> None:
        for inc in income:
            SsIncomeOrm.create(
                id_sm=inc.id_sb_object_dogovor,
                filial_id_sm=inc.id_sb_object_filial,
                customer_id_sm=inc.id_sb_object_zakazchik,
                object_id_sm=inc.id_sb_object_object,
                contract_id_sm=None,
                type=inc.type_dogovor,
                status=inc.status_dogovor,
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
                date_modified=inc.date,
                date_created=inc.date,
                model=inc
            )

    def consume_route_sheet(self, route_sheet: list[RouteSheet]) -> None:
        pass

    def consume_drivers(self, drivers: list[Driver]) -> None:
        pass
