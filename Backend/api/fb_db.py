import firebase_admin
from firebase_admin import db

data = {
    "type": "service_account",
    "project_id": "sih-sc500",
    "private_key_id": "9eff8dd0b6c09c1684ebcd0d55f26495d81971c0",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCzqUwxsMjbPUJ5\nSTp2QNV0Xc/kGGecrBuGD6u51Ty9HFN1iNKVNv8pIOtdIGnVvevJpc2kXyt6zX1e\nBP/9I/1ES0eSn8j7DjXMqO7Eb7/+G/pSEXU1IwsVcxURMOfHvGE+RQWXw4ZtzsJ7\nOlOE4+5Iy6gO7V56/8TdBMWEgs4DtRLubtlXsSfneh3fG0k4/1ReSp/aiXvg0VpI\nWCcW13jujSGrcDqsV1pmQH7f7VLxMrlrRU3FyNzRBFmGMXNBB1cP2v38+DyaoHbk\nK9wEFYyHsN3yxYBTa+c4C1+ajwNSLWA7M0GqKGasberSLPHukXvYTGJ/GN4ISDKh\ny2tgf131AgMBAAECggEAPMdqUmknGhw4T8W5NGYskChoexbSfosu6ISGqOB9otBh\nX6LA8t/fJG/Rj/i2NSwCB37C+feEQxAfeF4ip+Wz+ZWqCe1qVZxyEOGZnPTdM78N\nSRRE3YwUZNZA60brMoQFNcat5LCt2poW6w9JT+y4IQJcwWgGDYBXfhnuJC0IOvJF\nEGrO3kqOT7hygzblZd0ZtuolMcIhLuS8ym1EJqnRWXd8Qow2wQmK/u7QPW5Jcc04\nmgXo7Z1VpRsAVGW4ItqhIflalpgTsGzqmZEsCp5H0KLH79pN9UWjIpcjkxA4nSix\nb0FBo7KDbcrr506FYkkhTD6GMl4ETYnYGh9v8b2UZQKBgQD73DDps/ElgqwWTItu\ncHxFbZctzGL8TI+55s4h4oYywzsaztkLZE9XzByyC9uFcEwd5tNnOoOAFDiaASmc\nu3ZYZWzhy2wEp1Q/oaYb1P15Oev77jog09jD+MH5JCm3+HqvLBHhns8fcYsJ6DWv\nTWbWbgRnxg9ExhSJszhjVnfMqwKBgQC2nUyevi/XyJfrYSwek4HZ0GgdOTFCrphY\nX9pJJTzq0hcPt7GTpzfY77m+EaomdSZ0oxhkSsqnRAukXnPrcAXqfKFwnIfudkCf\nbYZSLok9IGg29XkqjOpv2zttS7XQBzSYgvg2dDadJRUKYwEOLO6zcKJE0ZVIKQo/\nD7fsDFI/3wKBgQDq4q+7RNXg5b0YDsr6dG1xUoNrcvHd2okwFtCnSVtefDTjC4Xf\n2e0lNHaOlgBkshZKzLrbyvZYvIMNHYhxY2M7jVu+OLjEnkk0Ds2bp0e9hwdOLR6I\n/wlputUsRU2jBVllhPQoNrNz37CLzMREeSsvT+tL3KrguNrukPZFrp6LgQKBgDVu\nCqf7j3X8O+7jjIwZrolzP7MlM7OF8A8TZIO4QH2YIKU5otxHtcBkS50//9+msSy5\nN37In0iXUSyzcgk1ypVUB8wyEFeGA9xhqEZNVVwsKjHCWsRHXKSDqXyOBVEreokQ\n8NzF3eDWo7RZSUrDfMfFscSe6aWmVFglGjQXWs1TAoGAQhZpSvULeg8y1q+2EoaG\n+jBzz0EEHLTTnuH63pOpr+FZYjEZeytXFM1p/nH8UWT0FaV95baLDBfAv5culC9x\nb3hRkqtxsQ9i/QCAe2mZ6fV53uEKL6ChItKcqEQYqe7RekHVOoLO5SPszp003smL\nuJrChnfboyVLreqX+9TdTFk=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-8edsl@sih-sc500.iam.gserviceaccount.com",
    "client_id": "115175824248259915805",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8edsl%40sih-sc500.iam.gserviceaccount.com"
}
cred_obj = firebase_admin.credentials.Certificate(data)
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://sih-sc500-default-rtdb.firebaseio.com/'
	})


ref = db.reference('/Users/1234')
# ref = db.reference('/Users/' + user_id)
print(ref.child('user_type').get())
res = str(ref.child('user_type').get())
print(res)