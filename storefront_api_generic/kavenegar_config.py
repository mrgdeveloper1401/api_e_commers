from kavenegar import KavenegarAPI, APIException, HTTPException
import os

api_key = os.environ.get('API_KEY')


def send_sms(code, receptor):
    text = f'کد تایید شما برابر است با {code}'
    try:
        api = KavenegarAPI('4755754B6A505230624D575A396531366B6E4269397952356C6345786843766477444338586F454C354E6B3D')
        params = {
            'sender': '',  # optional
            'receptor': receptor,  # multiple mobile number, split by comma
            'message': text,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
