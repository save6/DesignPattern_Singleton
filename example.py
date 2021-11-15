class UserCart:
    _instance = None
    items = []

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__internal_new__()

        return cls._instance

    def add(self, item):
        print("{}がカートに追加されました".format(item))
        self.items.append(item)

    def reset(self):
        self.items = []
    
    def is_added(self, item_name: str):
        return any([('name',item_name) in item.items() for item in self.items])

    def print_items(self):
        print('カート -----------')

        if len(self.items) == 0:
            print('カートに商品がありません')
            return
        
        for item in self.items:
            print("商品名：{0},価格：{1}".format(item['name'], item['price']))
        
    def calc(self):
        return sum([item['price'] for item in self.items])

class ItemList:

    def __init__(self):
        self.init_data()

    def init_data(self):
        self.data = [
            {'name': 'hoge', 'price': 3000},
            {'name': 'fuge', 'price': 5000},
            {'name': 'hoga', 'price': 2500},
        ]
    
    def find_by(self, name: str):
        for item in self.data:
            if ('name', name) in item.items():
                return item

    def get_data(self):
        return self.data

class Purchase:

    def __init__(self):
        self.cart = UserCart.get_instance()
    
    def payment(self):
        print('商品を購入しました')
        self.cart.reset()

    def print_total_price(self):
        total_price = self.cart.calc() * 1.1
        print('購入商品の合計額は{}円です'.format(total_price))

def display_itemlist(item_list):
    print('商品リスト -----------')
    for item in item_list:
        print_str = '商品名：' + item['name'] + ', 価格：' + str(item['price'])
        if UserCart.get_instance().is_added(item['name']):
            print_str += '(カート追加済み)'
        print(print_str)

PURCHASE = Purchase()
ITEM_LIST = ItemList()
USER_CART = UserCart.get_instance()

display_itemlist(ITEM_LIST.get_data())
USER_CART.print_items()
USER_CART.add(ITEM_LIST.find_by('hoge'))
USER_CART.print_items()
USER_CART.add(ITEM_LIST.find_by('fuge'))
USER_CART.print_items()
display_itemlist(ITEM_LIST.get_data())
PURCHASE.print_total_price()
PURCHASE.payment()
USER_CART.print_items()