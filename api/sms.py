import requests
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
def send_recommendation(farmer_name, last_name, phone_number):
    """Function to send a recommendation message via SMS using the Leopard SMS API"""
    logger.debug(f"SMS_LEOPARD_ACCESS_TOKEN: {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', 'Not Found')}")
    logger.debug(f"SMS_LEOPARD_API_URL: {getattr(settings, 'SMS_LEOPARD_API_URL', 'Not Found')}")
    headers = {
        "Authorization": f"Basic {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', '')}",
        "Content-Type": "application/json",
    }
    payload = {
        "source": "AkiraChix",
        "message": f"Hello {farmer_name}, your coffee leaves are affected by leaf miner. To prevent the spread of this pests to other leaves, please avoid intercropping and prune the overcrowed branches of coffee leaves",
        "destination": [{"number": phone_number}],
    }
    try:
        response = requests.post(
            getattr(settings, 'SMS_LEOPARD_API_URL', 'https://api.smsleopard.com/v1/sms/send'),
            json=payload, headers=headers
        )
        if response.status_code == 200:
            logger.info(f"Successfully sent SMS to {farmer_name} at {phone_number}")
            return response.json()
        else:
            logger.error(
                f"Failed to send recommendation: {response.status_code} - {response.text}"
            )
            return None
    except requests.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
def send_recommendation(farmer_name, last_name, phone_number):
    """Function to send a recommendation message via SMS using the Leopard SMS API"""
    logger.debug(f"SMS_LEOPARD_ACCESS_TOKEN: {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', 'Not Found')}")
    logger.debug(f"SMS_LEOPARD_API_URL: {getattr(settings, 'SMS_LEOPARD_API_URL', 'Not Found')}")
    headers = {
        "Authorization": f"Basic {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', '')}",
        "Content-Type": "application/json",
    }
    payload = {
        "source": "AkiraChix",
        "message": f"Hello {farmer_name}, your coffee leaves are affected by leaf miner. To prevent the spread of this pests to other leaves, please avoid intercropping and prune the overcrowed branches of coffee leaves",
        "destination": [{"number": phone_number}],
    }
    try:
        response = requests.post(
            getattr(settings, 'SMS_LEOPARD_API_URL', 'https://api.smsleopard.com/v1/sms/send'),
            json=payload, headers=headers
        )
        if response.status_code == 200:
            logger.info(f"Successfully sent SMS to {farmer_name} at {phone_number}")
            return response.json()
        else:
            logger.error(
                f"Failed to send recommendation: {response.status_code} - {response.text}"
            )
            return None
    except requests.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
def send_recommendation(farmer_name, last_name, phone_number):
    """Function to send a recommendation message via SMS using the Leopard SMS API"""
    logger.debug(f"SMS_LEOPARD_ACCESS_TOKEN: {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', 'Not Found')}")
    logger.debug(f"SMS_LEOPARD_API_URL: {getattr(settings, 'SMS_LEOPARD_API_URL', 'Not Found')}")
    headers = {
        "Authorization": f"Basic {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', '')}",
        "Content-Type": "application/json",
    }
    payload = {
        "source": "AkiraChix",
        "message": f"Hello {farmer_name}, your coffee leaves are affected by leaf miner. To prevent the spread of this pests to other leaves, please avoid intercropping and prune the overcrowed branches of coffee leaves",
        "destination": [{"number": phone_number}],
    }
    try:
        response = requests.post(
            getattr(settings, 'SMS_LEOPARD_API_URL', 'https://api.smsleopard.com/v1/sms/send'),
            json=payload, headers=headers
        )
        if response.status_code == 200:
            logger.info(f"Successfully sent SMS to {farmer_name} at {phone_number}")
            return response.json()
        else:
            logger.error(
                f"Failed to send recommendation: {response.status_code} - {response.text}"
            )
            return None
    except requests.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        # return Noneimport requests
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
def send_recommendation(farmer_name, last_name, phone_number):
    """Function to send a recommendation message via SMS using the Leopard SMS API"""
    logger.debug(f"SMS_LEOPARD_ACCESS_TOKEN: {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', 'Not Found')}")
    logger.debug(f"SMS_LEOPARD_API_URL: {getattr(settings, 'SMS_LEOPARD_API_URL', 'Not Found')}")
    headers = {
        "Authorization": f"Basic {getattr(settings, 'SMS_LEOPARD_ACCESS_TOKEN', '')}",
        "Content-Type": "application/json",
    }
    payload = {
        "source": "AkiraChix",
        "message": f"Hello {farmer_name}, your coffee leaves are affected by leaf miner. To prevent the spread of this pests to other leaves, please avoid intercropping and prune the overcrowed branches of coffee leaves",
        "destination": [{"number": phone_number}],
    }
    try:
        response = requests.post(
            getattr(settings, 'SMS_LEOPARD_API_URL', 'https://api.smsleopard.com/v1/sms/send'),
            json=payload, headers=headers
        )
        if response.status_code == 200:
            logger.info(f"Successfully sent SMS to {farmer_name} at {phone_number}")
            return response.json()
        else:
            logger.error(
                f"Failed to send recommendation: {response.status_code} - {response.text}"
            )
            return None
    except requests.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return None