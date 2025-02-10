from datetime import datetime, date

from pydantic import BaseModel, Field


class FilialModel(BaseModel):
    id: int | None
    id_sm: int | None
    name: str | None
    latitude: float | None
    longitude: float | None
    date_modified: datetime | None
    date_created: datetime | None


class CustomerModel(BaseModel):
    id: int | None
    id_sm: int | None
    name: str | None
    bin: str | None
    status: str | None
    date_modified: datetime | None
    date_created: datetime | None


class ObjectModel(BaseModel):
    id: int | None 
    id_sm: int | None 
    filial_id_sm: int | None 
    customer_id_sm: int | None 
    contract_id_sm: int | None 
    contract: str | None
    name: str | None
    contract_date: date | None
    contract_number: str | None
    type: str | None
    date_modified: datetime | None
    date_created: datetime | None


class PostModel(BaseModel):
    id: int | None
    id_sm: int | None
    filial_id_sm: int | None
    customer_id_sm: int | None
    object_id_sm: int | None
    name: str | None
    type: str | None
    shift_mode: str | None
    operating_mode: int | None
    linear_part: str | None
    length_from: float | None
    length_to: float | None
    date_modified: datetime | None
    date_created: datetime | None


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
    id: int | None
    id_sm: int | None
    filial_id_sm: int | None
    customer_id_sm: int | None
    object_id_sm: int | None
    name: str | None
    surname: str | None
    iin: str | None
    social_status: str | None
    status: str | None
    job_title: str | None
    employee_photo: str | None
    gender: str | None
    nationality: str | None
    labor_union: str | None
    date_modified: datetime | None
    date_created: datetime | None


class IncomeModel(BaseModel):
    id: int | None
    filial_id_sm: int | None
    contract_id_sm: int | None
    type: str | None
    status: str | None
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
    date_modified: datetime | None
    date_created: datetime | None
