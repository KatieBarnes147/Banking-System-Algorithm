import unittest
import random
import string

class Bank:
    """Class representing a Bank."""

    MAX_ACCOUNTS = 100

    def __init__(self):
        """Initialize the Bank with an empty list of accounts."""
        self.accounts = [None] * self.MAX_ACCOUNTS

    def add_account_to_bank(self, account):
        """Add a new account to the bank."""
        for i in range(self.MAX_ACCOUNTS):
            if not self.accounts[i]:
                self.accounts[i] = account
                return True
        print("No more accounts available")
        return False

    def remove_account_from_bank(self, account):
        """Remove an account from the bank."""
        for i in range(self.MAX_ACCOUNTS):
            if self.accounts[i] and self.accounts[i].account_number == account.account_number:
                self.accounts[i] = None
                print(f"Account {account.account_number} closed")
                return
        print(f"Account not found for account number: {account.account_number}")

    def find_account(self, account_number):
        """Find an account by account number."""
        for account in self.accounts:
            if account and account.account_number == account_number:
                return account
        return None


class Account:
    """Class representing an individual bank account."""

    def __init__(self, first_name, last_name, ssn):
        """Initialize an account with owner information and generate account number and PIN."""
        self.account_number = self.generate_account_number()
        self.owner_first_name = first_name
        self.owner_last_name = last_name
        self.owner_ssn = ssn
        self.pin = self.generate_pin()
        self.balance = 0

    @staticmethod
    def generate_account_number():
        """Generate a random 8-digit account number."""
        return random.randint(10000000, 99999999)

    @staticmethod
    def generate_pin():
        """Generate a random 4-digit PIN."""
        return ''.join(random.choices(string.digits, k=4))

    def deposit(self, amount):
        """Deposit funds into the account."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw funds from the account."""
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def is_valid_pin(self, pin):
        """Check if provided PIN is valid."""
        return self.pin == pin

    def __str__(self):
        """Return a string representation of the account."""
        return f"""============================================================
Account Number: {self.account_number}
Owner First Name: {self.owner_first_name}
Owner Last Name: {self.owner_last_name}
Owner SSN: XXX-XX-{self.owner_ssn[-4:]}
PIN: {self.pin}
Balance: ${self.balance / 100:.2f}
============================================================"""


class CoinCollector:
    """Class for collecting coins and parsing change."""

    @staticmethod
    def parse_change(coins):
        """Parse change represented by coins into total cents."""
        coin_values = {'P': 1, 'N': 5, 'D': 10, 'Q': 25, 'H': 50, 'W': 100}
        total_cents = 0
        for coin in coins:
            if coin in coin_values:
                total_cents += coin_values[coin]
            else:
                print(f"Invalid coin: {coin}")
        return total_cents


class BankUtility:
    """Utility class for banking operations."""

    @staticmethod
    def is_numeric(s):
        """Check if a string is numeric."""
        return s.replace('.', '', 1).isdigit()

    @staticmethod
    def prompt_user_for_string(prompt):
        """Prompt user for input string."""
        return input(prompt)

    @staticmethod
    def prompt_user_for_positive_number(prompt):
        """Prompt user for a positive number input."""
        while True:
            value = input(prompt)
            if BankUtility.is_numeric(value) and float(value) > 0:
                return float(value)
            else:
                print("Amount cannot be negative. Try again.")

    @staticmethod
    def convert_from_dollars_to_cents(amount):
        """Convert a dollar amount to cents."""
        return int(amount * 100)

    @staticmethod
    def generate_random_integer(min_val, max_val):
        """Generate a random integer within a given range."""
        return random.randint(min_val, max_val)


class BankManager:
    """Class for managing bank operations and user interactions."""

    def __init__(self):
        """Initialize the Bank Manager with a bank instance."""
        self.bank = Bank()

    def main(self):
        """Main program loop for user interactions and operations."""
        while True:
            print("============================================================")
            print("What do you want to do?")
            print("1. Open an account")
            print("2. Get account information and balance")
            print("3. Change PIN")
            print("4. Deposit money in account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from account")
            print("7. ATM withdrawal")
            print("8. Deposit change")
            print("9. Close an account")
            print("10. Add monthly interest to all accounts")
            print("11. End Program")
            print("============================================================")

            choice = BankUtility.prompt_user_for_string("Enter your choice: ")

            if choice == '1':
                self.open_account()
            elif choice == '2':
                self.get_account_info_and_balance()
            elif choice == '3':
                self.change_pin()
            elif choice == '4':
                self.deposit_money()
            elif choice == '5':
                self.transfer_money()
            elif choice == '6':
                self.withdraw_money()
            elif choice == '7':
                self.atm_withdrawal()
            elif choice == '8':
                self.deposit_change()
            elif choice == '9':
                self.close_account()
            elif choice == '10':
                self.add_monthly_interest()
            elif choice == '11':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice")

    def open_account(self):
        """Open a new bank account."""
        print("OPEN ACCOUNT")
        first_name = BankUtility.prompt_user_for_string("Enter Account Owner's First Name: ")
        last_name = BankUtility.prompt_user_for_string("Enter Account Owner's Last Name: ")
        ssn = BankUtility.prompt_user_for_string("Enter Account Owner's SSN (9 digits): ")
        while len(ssn) != 9 or not ssn.isdigit():
            print("Social Security Number must be 9 digits")
            ssn = BankUtility.prompt_user_for_string("Enter Account Owner's SSN (9 digits): ")

        account = Account(first_name, last_name, ssn)
        self.bank.add_account_to_bank(account)
        print(account)

    def get_account_info_and_balance(self):
        """Display account information and balance."""
        print("Get Account Information and Balance")
        account_number = BankUtility.prompt_user_for_string("Enter Account Number: ")
        pin = BankUtility.prompt_user_for_string("Enter PIN: ")

        account = self.bank.find_account(int(account_number))
        if account and account.is_valid_pin(pin):
            print(account)
        else:
            print("Invalid Account Number or PIN")

    def change_pin(self):
        """Change PIN for an account."""
        print("Change PIN")
        account_number = BankUtility.prompt_user_for_string("Enter Account Number: ")
        pin = BankUtility.prompt_user_for_string("Enter PIN: ")

        account = self.bank.find_account(int(account_number))
        if account and account.is_valid_pin(pin):
            new_pin = BankUtility.prompt_user_for_string("Enter new PIN: ")
            if len(new_pin) != 4 or not new_pin.isdigit():
                print("PIN must be 4 digits, try again.")
            else:
                confirm_pin = BankUtility.prompt_user_for_string("Enter new PIN again to confirm: ")
                if new_pin == confirm_pin:
                    account.pin = new_pin
                    print("PIN updated")
                else:
                    print("PINs do not match, try again.")
        else:
            print("Invalid Account Number or PIN")

    def deposit_money(self):
        """Deposit money into an account."""
        print("Deposit Money into Account")
        account_number = BankUtility.prompt_user_for_string("Enter Account Number: ")
        pin = BankUtility.prompt_user_for_string("Enter PIN: ")

        account = self.bank.find_account(int(account_number))
        if account and account.is_valid_pin(pin):
            amount = BankUtility.prompt_user_for_positive_number("Enter amount to deposit in dollars and cents (e.g. 2.57): ")
            amount = BankUtility.convert_from_dollars_to_cents(amount)
            new_balance = account.deposit(amount)
            print(f"New balance: ${new_balance / 100:.2f}")
        else:
            print("Invalid Account Number or PIN")

    def transfer_money(self):
        """Transfer money between accounts."""
        print("Transfer Money Between Accounts")
        from_account_number = BankUtility.prompt_user_for_string("Enter Account Number to Transfer From: ")
        from_pin = BankUtility.prompt_user_for_string("Enter PIN: ")

        from_account = self.bank.find_account(int(from_account_number))
        if from_account and from_account.is_valid_pin(from_pin):
            to_account_number = BankUtility.prompt_user_for_string("Enter Account Number to Transfer To: ")
            to_pin = BankUtility.prompt_user_for_string("Enter PIN: ")

            to_account = self.bank.find_account(int(to_account_number))
            if to_account and to_account.is_valid_pin(to_pin):
                amount = BankUtility.prompt_user_for_positive_number("Enter amount to transfer in dollars and cents (e.g. 2.57): ")
                amount = BankUtility.convert_from_dollars_to_cents(amount)

                withdrawal_result = from_account.withdraw(amount)
                if isinstance(withdrawal_result, str):
                    print(withdrawal_result)
                else:
                    to_account.deposit(amount)
                    print(f"Transfer Complete")
                    print(f"New balance in account {from_account.account_number} is: ${(withdrawal_result / 100):.2f}")
                    print(f"New balance in account {to_account.account_number} is: ${(to_account.balance / 100):.2f}")
            else:
                print("Invalid Account Number or PIN for Account to Transfer To")
        else:
            print("Invalid Account Number or PIN for Account to Transfer From")

    def withdraw_money(self):
        """Withdraw money from an account."""
        print("Withdraw Money from Account")
        account_number = BankUtility.prompt_user_for_string("Enter Account Number: ")
        pin = BankUtility.prompt_user_for_string("Enter PIN: ")

        account = self.bank.find_account(int(account_number))
        if account and account.is_valid_pin(pin):
            amount = BankUtility.prompt_user_for_positive_number("Enter amount to withdraw in dollars and cents (e.g. 2.57): ")
            amount = BankUtility.convert_from_dollars_to_cents(amount)
            withdrawal_result = account.withdraw(amount)
            if isinstance(withdrawal_result, str):
                print(withdrawal_result)
            else:
                print(f"New balance: ${(withdrawal_result / 100):.2f}")
        else:
            print("Invalid Account Number or PIN")

    def atm_withdrawal(self):
        """Make an ATM withdrawal from an account."""
        print("Make an ATM withdrawal from Account")
        try:
            account_number = input("Enter Account Number: ")
            pin = input("Enter PIN: ")

            account = self.bank.find_account(int(account_number))
            if account and account.is_valid_pin(pin):
                amount = input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): ")
                while True:
                    try:
                        amount = float(amount)
                        if amount < 5 or amount > 1000 or amount % 5 != 0:
                            raise ValueError
                        break  # Exit the loop if input is valid
                    except ValueError:
                        print("Invalid amount. Amount must be a multiple of $5 between $5 and $1000.")
                        amount = input("Enter amount to withdraw: ")

                amount = int(amount)
                twenty_dollar_bills = amount // 20
                amount %= 20
                ten_dollar_bills = amount // 10
                amount %= 10
                five_dollar_bills = amount // 5
                amount %= 5

                new_balance = account.withdraw(BankUtility.convert_from_dollars_to_cents(amount))
                print(f"Number of 20-dollar bills: {twenty_dollar_bills}")
                print(f"Number of 10-dollar bills: {ten_dollar_bills}")
                print(f"Number of 5-dollar bills: {five_dollar_bills}")
                print(f"New balance: ${(new_balance / 100):.2f}")
            else:
                print("Invalid Account Number or PIN")
        except KeyboardInterrupt:
            print("\nATM withdrawal operation interrupted.")

    def deposit_change(self):
        """Deposit change into an account."""
        print("Deposit Change into Account")
        account_number = BankUtility.prompt_user_for_string("Enter Account Number: ")
        pin = BankUtility.prompt_user_for_string("Enter PIN: ")

        account = self.bank.find_account(int(account_number))
        if account and account.is_valid_pin(pin):
            coins = BankUtility.prompt_user_for_string("Deposit coins: ").upper()
            amount = CoinCollector.parse_change(coins)
            new_balance = account.deposit(amount)
            print(f"${amount / 100:.2f} in coins deposited into account")
            print(f"New balance: ${(new_balance / 100):.2f}")
        else:
            print("Invalid Account Number or PIN")

    def close_account(self):
        """Close an account."""
        print("Close an Account")
        account_number = BankUtility.prompt_user_for_string("Enter Account Number: ")
        pin = BankUtility.prompt_user_for_string("Enter PIN: ")

        account = self.bank.find_account(int(account_number))
        if account and account.is_valid_pin(pin):
            self.bank.remove_account_from_bank(account)
        else:
            print("Invalid Account Number or PIN")

    def add_monthly_interest(self):
        """Add monthly interest to all accounts."""
        print("Add Monthly Interest to All Accounts")
        annual_interest_rate = BankUtility.prompt_user_for_positive_number("Enter annual interest rate percentage (e.g. 2.75 for 2.75%): ")

        for acc in self.bank.accounts:
            if acc:
                monthly_interest = annual_interest_rate / 12 / 100 * acc.balance
                acc.deposit(monthly_interest)
                print(f"Deposited interest: ${(monthly_interest / 100):.2f} into account number:{acc.account_number}, new balance:${(acc.balance / 100):.2f}")


class TestBank(unittest.TestCase):
    """Class for unit tests of banking functionalities."""

    def test_generate_account_number(self):
        """Test if the generated account number is within the correct range."""
        account_number = Account.generate_account_number()
        self.assertTrue(10000000 <= account_number <= 99999999)

    def test_generate_pin(self):
        """Test if the generated PIN has 4 digits."""
        pin = Account.generate_pin()
        self.assertEqual(len(pin), 4)

    def test_parse_change(self):
        """Test parsing change."""
        coins = 'PNDQHW'
        total_cents = CoinCollector.parse_change(coins)
        self.assertEqual(total_cents, 191)

    def test_is_numeric(self):
        """Test if the function correctly identifies numeric strings."""
        self.assertTrue(BankUtility.is_numeric("123"))
        self.assertTrue(BankUtility.is_numeric("3.14"))
        self.assertFalse(BankUtility.is_numeric("abc"))

    def test_convert_from_dollars_to_cents(self):
        """Test conversion from dollars to cents."""
        self.assertEqual(BankUtility.convert_from_dollars_to_cents(10.50), 1050)


def execute_main_program():
    """Execute the main program loop."""
    bank_manager = BankManager()
    bank_manager.main()

def run_tests():
    """Run unit tests."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBank)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
    execute_main_program()
