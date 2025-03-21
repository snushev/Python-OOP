from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list[BaseLoan] = []
        self.clients:list[BaseClient] = []

    def add_loan(self, loan_type: str):
        valid_type = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
        if loan_type not in valid_type:
            raise Exception("Invalid loan type!")
        self.loans.append(valid_type[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        valid_type = {"Student": Student, "Adult": Adult}
        if client_type not in valid_type:
            raise Exception("Invalid client type!")
        if self.capacity <= 0:
            return "Not enough bank capacity."
        self.clients.append(valid_type[client_type](client_name, client_id, income))
        self.capacity -= 1
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        loan = next((l for l in self.loans if l.__class__.__name__ == loan_type), None) #TODO maybe check if both exist ?

        mapper = {
            "Student": "StudentLoan",
            "Adult": "MortgageLoan",
        }

        if mapper[client.__class__.__name__] == loan_type:
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        return "Inappropriate loan type!"

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        self.capacity += 1
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)
        loans_count_granted_to_clients = sum(len(client.loans) for client in self.clients)
        granted_sum = sum(loan.amount for client in self.clients for loan in client.loans)
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)
        avg_client_interest_rate = (
            sum(client.interest for client in self.clients) / total_clients_count
            if total_clients_count > 0 else 0.0
        )

        result = [
            f"Active Clients: {total_clients_count}",
            f"Total Income: {total_clients_income:.2f}",
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
            f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}",
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        ]

        return '\n'.join(result)
