import asyncio
from logger import logger

from database.queries import *
from util_functions import try_times
from destination.mqtt_client import CubaMqttClient
from destination.superset import Superset


class TaskRunner:

    def __init__(self, superset: Superset, mqtt_client: CubaMqttClient):
        self.superset: Superset = superset
        self.mqtt_client: CubaMqttClient = mqtt_client
        self.tasks_table = [
            self.fetch_filials,
            self.fetch_customers,
            self.fetch_contracts,
            self.fetch_objects,
            self.fetch_posts,
            self.fetch_security_guards,
            self.fetch_income,
            self.fetch_triggerings,
            self.fetch_shifts,
            self.fetch_fines,
            self.fetch_employees,
            self.fetch_contract_trus,
            self.fetch_legal_claims,
            self.fetch_transports,
            self.fetch_training_and_medical_services,
            self.fetch_journals,
            self.fetch_communication_facilities,
            self.fetch_providing_workwears,
        ]

    async def run_tasks(self):
        tasks = [asyncio.create_task(task()) for task in self.tasks_table]

        done_tasks, pending_tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

        for task in done_tasks:
            if exc := task.exception():
                logger.error(f"{task=} raised an exception: {exc}")

        for task in pending_tasks:
            try:
                task.cancel()
                await task
            except asyncio.CancelledError:
                logger.info(f"{task=} successfully cancelled")
            except Exception as exc:
                logger.exception(f"{task=} raised an exception: {exc}")

    @try_times(number_of_tries=3)
    async def fetch_filials(self):
        simbase_filials = FilialOrm.all()
        self.superset.consume_filials(simbase_filials)
        logger.info("Fetched filials")

    @try_times(number_of_tries=3)
    async def fetch_customers(self):
        simbase_customers = CustomerOrm.all()
        self.superset.consume_customers(simbase_customers)
        logger.info("Fetched customers")

    @try_times(number_of_tries=3)
    async def fetch_objects(self):
        simbase_objects = ObjectOrm.all()
        self.superset.consume_objects(simbase_objects)
        logger.info("Fetched objects")

    @try_times(number_of_tries=3)
    async def fetch_posts(self):
        simbase_posts = PostOrm.all()
        self.superset.consume_posts(simbase_posts)
        logger.info("Fetched posts")

    @try_times(number_of_tries=3)
    async def fetch_route_sheet(self):
        simbase_route_sheet = RouteSheetOrm.all()
        self.superset.consume_route_sheet(simbase_route_sheet)
        logger.info("Fetched route sheet")

    @try_times(number_of_tries=3)
    async def fetch_security_guards(self):
        simbase_security_guards = SecurityGuardOrm.all()
        self.superset.consume_security_guards(simbase_security_guards)
        logger.info("Fetched security guards")

    @try_times(number_of_tries=3)
    async def fetch_contracts(self):
        simbase_contracts = ContractOrm.all()
        self.superset.consume_contracts(simbase_contracts)
        logger.info("Fetched contracts")

    @try_times(number_of_tries=3)
    async def fetch_income(self):
        simbase_income = IncomeOrm.all()
        self.superset.consume_income(simbase_income)
        logger.info("Fetched income")

    @try_times(number_of_tries=3)
    async def fetch_triggerings(self):
        simbase_triggerings = TriggeringOrm.all()
        self.superset.consume_triggerings(simbase_triggerings)
        logger.info("Fetched triggerings")

    @try_times(number_of_tries=3)
    async def fetch_shifts(self):
        simbase_shifts = ShiftOrm.all()
        self.superset.consume_shifts(simbase_shifts)
        logger.info("Fetched shifts")

    @try_times(number_of_tries=3)
    async def fetch_fines(self):
        simbase_fines = FineOrm.all()
        self.superset.consume_fines(simbase_fines)
        logger.info("Fetched fines")

    @try_times(number_of_tries=3)
    async def fetch_legal_claims(self):
        simbase_legal_claims = LegalClaimsOrm.all()
        self.superset.consume_legal_claims(simbase_legal_claims)
        logger.info("Fetched legal claims")

    @try_times(number_of_tries=3)
    async def fetch_contract_trus(self):
        simbase_contract_trus = ContractTRUOrm.all()
        self.superset.consume_contract_trus(simbase_contract_trus)
        logger.info("Fetched contract TRUs")

    @try_times(number_of_tries=3)
    async def fetch_employees(self):
        simbase_employees = EmployeeOrm.all()
        self.superset.consume_employees(simbase_employees)
        logger.info("Fetched emmployees")

    @try_times(number_of_tries=3)
    async def fetch_transports(self):
        simbase_transports = TransportOrm.all()
        self.superset.consume_transports(simbase_transports)
        logger.info("Fetched transports")

    @try_times(number_of_tries=3)
    async def fetch_training_and_medical_services(self):
        simbase_training_and_medical_services = TrainingAndMedicalServiceOrm.all()
        self.superset.consume_training_and_medical_services(simbase_training_and_medical_services)
        logger.info("Fetched training and medical services")

    @try_times(number_of_tries=3)
    async def fetch_journals(self):
        simbase_journals = JournalOrm.all()
        self.superset.consume_journals(simbase_journals)
        logger.info("Fetched journals")

    @try_times(number_of_tries=3)
    async def fetch_communication_facilities(self):
        simbase_comm_facils = CommunicationFacilitiyOrm.all()
        self.superset.consume_communication_facilities(simbase_comm_facils)
        logger.info("Fetched communication facilities")

    @try_times(number_of_tries=3)
    async def fetch_providing_workwears(self):
        simbase_prov_wws = ProvidingWorkwearsOrm.all()
        self.superset.consume_providing_workwears(simbase_prov_wws)
        logger.info("Fetched providing workwears")
