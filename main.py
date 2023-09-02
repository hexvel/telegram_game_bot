from User.user import User
from Chat.chat import Chat
from Games.marry import Marry
from Games.roles import RolePlay


class Main(User, Chat, Marry):
    def __init__(self):
        super().__init__()
        self.user: User = User()
        self.chat: Chat = Chat()
        self.marry: Marry = Marry()
        self.rp: RolePlay = RolePlay()
