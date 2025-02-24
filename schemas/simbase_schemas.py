from datetime import datetime, date, time
from typing import Any

from pydantic import BaseModel, Field, field_validator


class FilialSchema(BaseModel):
    id: int | None
    id_sm: int | None
    name: str | None
    latitude: float | None = None
    longitude: float | None = None
    sm_state: str | None
    date_modified: datetime | None
    date_created: datetime | None


class CustomerSchema(BaseModel):
    id: int | None
    id_sm: int | None
    name: str | None
    bin: str | None
    status: str | None
    sm_state: str | None
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
    sm_state: str | None
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
    operating_mode: str | None
    linear_part: str | None
    length_from: float | None
    length_to: float | None
    sm_state: str | None
    date_modified: datetime | None
    date_created: datetime | None

    @field_validator("type", mode="before")
    @classmethod
    def rename_type(cls, value):
        if value == "Группа быстрого реагирования":
            return "Мобильная группа"
        return value


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
    sm_state: str | None
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
    sm_state: str | None
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
    sm_state: str | None
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
    sm_state: str | None
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
    sm_state: str | None
    date_modified: datetime | None
    date_created: datetime | None


class ContractTRUSchema(BaseModel):
    id: int | None
    id_sm: int | None
    name: str | None
    sm_state: str | None
    date_modified: datetime | None
    date_created: datetime | None


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
    fine_date: date | None
    decision: str | None
    sm_state: str | None
    date_modified: datetime | None
    date_created: datetime | None


class LegalClaimsSchema(BaseModel):
    id: int | None
    id_sm: int | None
    sm_state: str | None
    responsible_employee_id_sm: int | None
    contract_tru_id_sm: int | None = Field(validation_alias="contract_TRU_id_sm")
    conclusion_date: date | None
    contract_number: str | None
    applicant: str | None
    defendant: str | None
    case_classification: str | None
    property_requirements: str | None
    currency: str | None
    non_property_claims: str | None
    grounds_of_claim: str | None
    result: str | None
    dishonest_supplier: bool | None
    date_modified: datetime | None
    date_created: datetime | None


class EmployeeSchema(BaseModel):
    id: int | None
    id_sm: int | None
    employee: str | None
    name: str | None
    second_name: str | None
    middle_name: str | None
    filial_id_sm: int | None
    job_title: str | None
    job_type: str | None
    subdivision: str | None
    iin: str | None
    personnel_number: str | None
    gender: str | None
    nationality: str | None
    birth_date: date | None
    place_of_birth: str | None
    social_status: str | None
    employee_type: str | None
    type: str | None
    position_level: str | None
    reserved: bool | None
    labor_union: str | None
    nomenclature_CEO: bool | None
    nomenclature_CA: bool | None
    retiree: bool | None
    member_collective_agreement: bool | None
    wage_rate: bool | None
    salary: bool | None
    rating: bool | None
    sm_state: str | None
    date_modified: datetime | None
    date_created: datetime | None


class TransportSchema(BaseModel):
    id: int
    sm_state: str | None
    filial_id_sm: int | None
    customer_id_sm: int | None
    post_id_sm: int | None
    transport_quantity: int | None
    additional_necessary_transport_quantity: int | None
    GPS: int | None
    date_modified: datetime | None
    date_created: datetime | None


class TrainingAndMedicalServiceSchema(BaseModel):
    id: int | None
    sm_state: str | None
    filial_id_sm: int | None
    customer_id_sm: int | None
    post_id_sm: int | None
    annual_retraining_of_security_guards_quantity: int | None
    anti_terrorism_training_quantity: int | None
    annual_medical_examination_quantity: int | None
    annual_medical_examination_quantity: int | None
    pre_shift_medical_examination_quantity: int | None
    date_modified: datetime | None
    date_created: datetime | None


class JournalSchema(BaseModel):
    id: int | None
    sm_state: str | None
    filial_id_sm: int | None
    customer_id_sm: int | None
    post_id_sm: int | None
    journal_transfer_of_weapons_and_ammunition: bool | None
    journal_finery: bool | None
    journal_aboard: bool | None
    journal_list_of_way: bool | None
    journal_information_and_recording: bool | None
    journal_transfers_of_inventory_items: bool | None
    journal_acceptance_log_for_premises_delivery: bool | None
    journal_visitors: bool | None
    journal_vehicle_registration: bool | None
    date_modified: datetime | None
    date_created: datetime | None
