from datetime import datetime, date

from pydantic import BaseModel, Field


class FilialModel(BaseModel):
    i_id: int | None
    name_filial: str | None
    id_sb_object_filial: int | None
    date: datetime | None


class CustomerModel(BaseModel):
    i_id: int | None
    name_customer: str | None
    id_sb_object_zakazchik: int | None
    bin: str | None
    date: datetime | None


class ObjectModel(BaseModel):
    i_id: int | None
    id_sb_object_filial: int | None
    id_sb_object_zakazchik: int | None
    id_sb_object_object: int | None
    name_object: str | None
    contract: str | None
    id_sb_object_dogovor: int | None
    contract_date: date | None
    contract_number: str | None
    type: str | None
    date: datetime | None


class PostModel(BaseModel):
    i_id: int | None
    id_sb_object_filial: int | None
    id_sb_object_zakazchik: int | None
    id_sb_object_object: int | None
    id_sb_object_post: int | None
    name_post: str | None
    type: str | None
    shift_mode: str | int | None
    date: datetime | None


class MobGroupModel(BaseModel):
    i_id: int | None
    id_sb_object_filial: int | None
    id_sb_object_zakazchik: int | None
    id_sb_object_object: int | None
    id_sb_object_post: int | None
    id_sb_object_mob_group: int | None
    mobile_group_name: str | None
    operating_mode: str | None
    shift_mode: str | None
    linear_part: str | None
    length_from: str | None
    length_to: str | None
    date: datetime | None


class SecurityGuardModel(BaseModel):
    i_id: int | None
    id_sb_guards: int | None
    object_name: str | None
    name: str | None
    surname: str | None
    job_title: str | None
    employee_photo: str | None
    gender: str | None
    nationality: str | None
    customer: str | None
    date: datetime | None
    id_sb_object_filial: int | None
    id_sb_object_zakazchik: int | None
    id_sb_object_object: int | None
    iin: str | None
    social_status: str | None
    status: str | None
    labor_union: str | None


class IncomeModel(BaseModel):
    i_id: int
    id_sb_object_filial: int | None
    id_sb_object_zakazchik: int | None
    id_sb_object_object: int | None
    id_sb_object_dogovor: int | None
    type_dogovor: str | None
    status_dogovor: str | None
    year: int | None
    month: str | None
    contract_amount: float | None
    additional_agreement_amount: float | None
    amount_avr: float | None
    payment_date_avr: date | None
    actual_payment: float | None
    payment_date_actual: date | None
    deviation_amount: float | None
    deviation_from_avr: float | None
    deviation_from_contract_prc: str | None
    deviation_from_avr_prc: str | None
    remainder: float | None
    comment: str | None
    additional_comment: str | None
    date: datetime | None
