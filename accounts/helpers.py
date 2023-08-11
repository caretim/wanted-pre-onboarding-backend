from rest_framework.exceptions import  ValidationError
from rest_framework.fields import CharField

# 유효성 검사 클래스 정의 (Validator) password,email
class PasswordValidator:
    message = '8자 이상의 비밀번호를 작성해주세요'
    code = 'invalid'
    password_regex = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
    
    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
            
    def __call__(self, value):
        if  len(value)<8:
            raise ValidationError(self.message, code=self.code)
    
        
    def __eq__(self, other):
        return (
            isinstance(other, PasswordValidator)
            and (self.message == other.message)
            and (self.code == other.code)
        )

class EmailValidator:
    message = '유효한 이메일이 아닙니다 . @를 포함시켜주세요'
    code = 'invalid'
    password_regex = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
    
    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
            
    def __call__(self, value):
        if '@' not in value:
            raise ValidationError(self.message, code=self.code)
    
        

    def __eq__(self, other):
        return (
            isinstance(other, EmailValidator)
            and (self.message == other.message)
            and (self.code == other.code)
        )

class PasswordField(CharField):
    default_error_messages ={
        'invalid': '유효한 비밀번호가 아닙니다. 8자 이상으로 입력해주세요'
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        validator = PasswordValidator(message=self.error_messages['invalid'])
        self.validators.append(validator)


class CustomMailField(CharField):
    default_error_messages ={
        'invalid': '유효한 이메일이 아닙니다 . @를 포함시켜주세요.'
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        validator = EmailValidator(message=self.error_messages['invalid'])
        self.validators.append(validator)