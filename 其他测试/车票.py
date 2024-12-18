class TrainTicketSystem:
    def __init__(self):
        # 初始化可用票的信息，包括车次、座位数、价格、出发站和到达站
        self.available_tickets = {
            'G101': {'seats': 5, 'price': 100, 'departure': '北京', 'destination': '上海'},
            'D202': {'seats': 3, 'price': 80, 'departure': '广州', 'destination': '深圳'},
            'K303': {'seats': 10, 'price': 50, 'departure': '成都', 'destination': '重庆'}
        }

    def display_tickets(self):
        # 显示可用票的信息，包括车次、座位数、价格、出发站和到达站
        print("\nAvailable Tickets:")
        for train, info in self.available_tickets.items():
            print(f"Train {train}: Seats Available: {info['seats']}, Price: {info['price']} CNY, Departure: {info['departure']}, Destination: {info['destination']}")

    def purchase_ticket(self, train_number, quantity):
        # 检查提供的车次编号是否有效
        if train_number not in self.available_tickets:
            print("无效的车次编号，请重试。")
            return

        # 获取对应车次的信息
        train = self.available_tickets[train_number]
        # 检查是否有足够的座位可供购买
        if train['seats'] >= quantity:
            # 从可用座位中扣除购买的数量
            train['seats'] -= quantity
            # 计算购买票的总价
            total_price = train['price'] * quantity
            # 打印购买成功的信息和总价
            print(f"\n成功购买了{quantity}张{train_number}次列车的票。")
            print(f"出发站: {train['departure']}, 到达站: {train['destination']}")
            print(f"总价: {total_price} CNY")
        else:
            # 如果没有足够的座位，打印错误信息
            print("\n座位不足，请重试。")


def main():
    # 创建一个TrainTicketSystem的实例
    system = TrainTicketSystem()
    while True:
        # 向用户显示可用的票
        system.display_tickets()
        # 提示用户输入车次编号或退出
        train_number = input("\n请输入想要购买车票的车次编号（或输入'quit'退出）：")
        if train_number.lower() == 'quit':
            # 如果用户想退出，则结束循环
            print("感谢使用火车票系统，再见！")
            break

        try:
            # 提示用户输入想要购买的票数
            quantity = int(input("请输入想要购买的票数："))
            if quantity <= 0:
                # 检查输入的票数是否有效（大于0）
                print("请输入有效的票数。")
                continue
            # 尝试购买车票
            system.purchase_ticket(train_number, quantity)
        except ValueError:
            # 处理票数输入无效（非整数）的情况
            print("输入无效，请输入一个有效的数字。")


if __name__ == "__main__":
    main()