from datetime import datetime, date, time
from typing import Any

from pydantic import BaseModel, Field


class FilialSchema(BaseModel):
    id: int | None
    id_sm: int | None
    name: str | None
    latitude: float | None = None
    longitude: float | None = None
    date_modified: datetime | None
    date_created: datetime | None


class CustomerSchema(BaseModel):
    id: int | None
    id_sm: int | None
    name: str | None
    bin: str | None
    status: str | None
    date_modified: datetime | None
    date_created: datetime | None


class ObjectSchema(BaseModel):
    id: int | None 
    id_sm: int | None 
    filial_id_sm: int | None 
    customer_id_sm: int | None 
    contract_id_sm: int | None 
    contract_name: str | None = Field(validation_alias="contract")
    name: str | None
    contract_date: date | None
    contract_number: str | None
    type: str | None
    date_modified: datetime | None
    date_created: datetime | None


class PostSchema(BaseModel):
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


class MobGroupSchema(BaseModel):
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


class SecurityGuardSchema(BaseModel):
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
    employee_photo: Any
    gender: str | None
    nationality: str | None
    labor_union: str | None
    date_modified: datetime | None
    date_created: datetime | None


class IncomeSchema(BaseModel):
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


class ContractSchema(BaseModel):
    id: int | None
    id_sm: int | None
    start_date: date | None
    warning_date: date | None
    end_date: date | None
    customer_id_sm: int | None
    name: str | None
    type: str | None
    contract_number: str | None
    date_modified: datetime | None
    date_created: datetime | None


class TriggeringSchema(BaseModel):
    id: int | None
    id_sm: int | None
    filial_id_sm: int | None
    object_id_sm: int | None
    post_id_sm: int | None
    type: str | None
    customer: str | None
    reason: str | None
    description: str | None
    place: str | None
    departure_mg: int | None
    departure_time: datetime | None
    arrival_time: datetime | None
    response_time: time | None
    mg_moment_of_actuation: str | None
    trigger_date: datetime | None
    date_modified: datetime | None
    date_created: datetime | None


class ShiftSchema(BaseModel):
    id: int | None
    id_sm: int | None
    filial_id_sm: int | None
    object_id_sm: int | None
    post_id_sm: int | None
    security_guard_id_sm: int | None
    security_guard_replaced_id_sm: int | None
    joined_posts: int | None
    shift_date: date | None
    shift_type: str | None
    date_modified: datetime | None
    date_created: datetime | None


class ContractTRUSchema(BaseModel):
    id: int | None
    id_sm: int | None
    name:int | None
    sm_state:int | None
    date_modified: int | None
    date_created: int | None


class FineSchema(BaseModel):
    id: int | None
    id_sm: int | None
    filial_id_sm: int | None
    customer_id_sm: int | None
    circumstances: str | None
    violation_type: str | None
    fine_type: str | None
    request_amount: float | None
    recognition_amount: float | None
    fine_number: str | None
    fine_date: datetime | None
    decision: str | None
    date_modified: datetime | None
    date_created: datetime | None


class LegalClaimsSchema(BaseModel):
    id: int | None
    id_sm: int | None
    sm_state: str | None
    responsible_employee_id_sm: int | None
    contract_TRU_id_sm: int | None
    conclusion_date: datetime | None
    contract_number: str | None
    applicant: str | None
    defendant: str | None
    case_classification: str | None
    property_requirements: str | None
    currency: str | None
    non_property_claims: str | None
    grounds_of_claim: str | None
    result: str | None
    dishonest_supplier: int | None
    date_modified: datetime | None
    date_created: datetime | None
