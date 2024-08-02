import requests
import json
import logging
from typing import Dict, List

class PiNetworkAPI:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def get_blockchain_data(self) -> Dict:
        """
        Retrieves blockchain data from the Pi Network API.

        Returns:
            Dict: Blockchain data
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(self.api_url + '/blockchain/data', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Failed to retrieve blockchain data: {response.text}')
            return {}

    def send_transaction(self, transaction_data: Dict) -> Dict:
        """
        Sends a transaction to the Pi Network API.

        Args:
            transaction_data (Dict): Transaction data

        Returns:
            Dict: Transaction response
        """
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        response = requests.post(self.api_url + '/transactions', headers=headers, json=transaction_data)
        if response.status_code == 201:
            return response.json()
        else:
            self.logger.error(f'Failed to send transaction: {response.text}')
            return {}

    def get_transaction_status(self, transaction_id: str) -> Dict:
        """
        Retrieves the status of a transaction from the Pi Network API.

        Args:
            transaction_id (str): Transaction ID

        Returns:
            Dict: Transaction status
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(self.api_url + f'/transactions/{transaction_id}', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Failed to retrieve transaction status: {response.text}')
            return {}

    def get_account_balance(self, account_id: str) -> Dict:
        """
        Retrieves the balance of an account from the Pi Network API.

        Args:
            account_id (str): Account ID

        Returns:
            Dict: Account balance
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(self.api_url + f'/accounts/{account_id}/balance', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Failed to retrieve account balance: {response.text}')
            return {}

    def get_account_transactions(self, account_id: str, limit: int = 10, offset: int = 0) -> List[Dict]:
        """
        Retrieves a list of transactions for an account from the Pi Network API.

        Args:
            account_id (str): Account ID
            limit (int, optional): Number of transactions to retrieve. Defaults to 10.
            offset (int, optional): Offset for pagination. Defaults to 0.

        Returns:
            List[Dict]: List of transactions
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        params = {'limit': limit, 'offset': offset}
        response = requests.get(self.api_url + f'/accounts/{account_id}/transactions', headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Failed to retrieve account transactions: {response.text}')
            return []

    def get_block_height(self) -> int:
        """
        Retrieves the current block height from the Pi Network API.

        Returns:
            int: Block height
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(self.api_url + '/blockchain/height', headers=headers)
        if response.status_code == 200:
            return response.json()['height']
        else:
            self.logger.error(f'Failed to retrieve block height: {response.text}')
            return 0

    def get_block(self, block_height: int) -> Dict:
        """
        Retrieves a block from the Pi Network API.

        Args:
            block_height (int): Block height

        Returns:
            Dict: Block data
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(self.api_url + f'/blockchain/blocks/{block_height}', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Failed to retrieve block: {response.text}')
            return {}
