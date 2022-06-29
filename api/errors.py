class Error(Exception):
    pass


class AccountNotExistError(Error):
    def __init__(self, message='존재하지 않는 계정입니다.'):
        self.message = message
        super().__init__(message)


class UserAlreadyBlockedError(Error):
    def __init__(self, message='이미 차단한 계정입니다.'):
        self.message = message
        super().__init__(message)


class BlockedUserNotExistError(Error):
    def __init__(self, message='차단하지 않은 계정입니다.'):
        self.message = message
        super().__init__(message)


class IncorrectBlockUserError(Error):
    def __init__(self, message='차단 계정이 올바르지 않습니다.'):
        self.message = message
        super().__init__(message)


class InvalidTitleError(Error):
    def __init__(self, message='제목이 비어 있습니다.'):
        self.message = message
        super().__init__(message)


class InvalidContentError(Error):
    def __init__(self, message='내용이 비어 있습니다.'):
        self.message = message
        super().__init__(message)


class PostNotExistError(Error):
    def __init__(self, message='존재하지 않는 게시물입니다.'):
        self.message = message
        super().__init__(message)